"""Static contract checks only; no ESPHome compile, secrets resolution or hardware I/O."""

from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET

try:
    import yaml
except ImportError:
    raise SystemExit("PyYAML is required: install it in your Python environment; no checks ran.")


PROJECT = Path(__file__).resolve().parents[1]
ROOT = PROJECT.parents[1]


class SecretRef(str):
    """Keep the reference name, never read its value or secrets.yaml."""


class ConfigLoader(yaml.SafeLoader):
    pass


ConfigLoader.add_constructor(
    "!secret", lambda loader, node: SecretRef(loader.construct_scalar(node))
)


class ConfigurationContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = yaml.load(
            (PROJECT / "esphome/casita-smart-dc-switches.yaml").read_text(),
            Loader=ConfigLoader,
        )

    def test_hardware_mapping(self):
        c = self.config
        self.assertEqual(c["esp32"]["variant"], "esp32s3")
        self.assertEqual(c["esp32"]["flash_size"], "16MB")
        self.assertEqual(c["i2c"]["sda"], "GPIO42")
        self.assertEqual(c["i2c"]["scl"], "GPIO41")
        self.assertEqual(c["pca9554"], [
            {"id": "relay_hub", "i2c_id": c["i2c"]["id"], "address": 0x20},
        ])
        self.assertEqual(len(c["switch"]), 4)
        for index, output in enumerate(c["switch"]):
            self.assertEqual(output["id"], f"load_{index + 1}")
            self.assertEqual(output["platform"], "gpio")
            self.assertEqual(output["restore_mode"], "ALWAYS_OFF")
            self.assertEqual(output["pin"], {
                "pca9554": "relay_hub", "number": index,
                "mode": "OUTPUT", "inverted": False,
            })

    def test_local_idempotent_press_actions_only(self):
        inputs = self.config["binary_sensor"]
        self.assertEqual(len(inputs), 8)
        for index, sensor in enumerate(inputs):
            load = f"load_{index // 2 + 1}"
            # As installed 2026-10-23: odd inputs (even index) are DOWN, even inputs are UP.
            direction = "down" if index % 2 == 0 else "up"
            action = "switch.turn_on" if direction == "up" else "switch.turn_off"
            self.assertEqual(set(sensor), {
                "platform", "id", "internal", "pin", "filters", "on_press",
            })  # Reject release/state/click actions as well as hidden dependencies.
            self.assertEqual(sensor["platform"], "gpio")
            self.assertEqual(sensor["id"], f"{load}_{direction}")
            self.assertIs(sensor["internal"], True)
            self.assertEqual(sensor["pin"], {
                "number": f"GPIO{4 + index}", "mode": "INPUT_PULLUP", "inverted": True,
            })
            self.assertEqual(sensor["filters"], [{"delayed_on_off": "25ms"}])
            self.assertEqual(sensor["on_press"], [{action: load}])

    def test_offline_and_secrets_contract(self):
        c = self.config
        self.assertEqual(set(c), {
            "esphome", "esp32", "logger", "api", "ota", "wifi", "captive_portal",
            "i2c", "pca9554", "switch", "binary_sensor",
        })
        self.assertEqual(c["wifi"]["reboot_timeout"], "0s")
        self.assertEqual(c["api"]["reboot_timeout"], "0s")
        self.assertEqual(len(c["ota"]), 1)
        self.assertEqual(c["ota"][0]["platform"], "esphome")
        # Trailer network first, home network as backup; fallback hotspot last.
        networks = c["wifi"]["networks"]
        self.assertEqual(len(networks), 2)
        self.assertEqual(c["wifi"]["ap"]["ssid"], "Casita Smart DC Fallback")
        refs = {
            "smart_dc_api_encryption_key": c["api"]["encryption"]["key"],
            "ota_password": c["ota"][0]["password"],
            "wifi_ssid": networks[0]["ssid"],
            "wifi_password": networks[0]["password"],
            "wifi_backup_ssid": networks[1]["ssid"],
            "wifi_backup_password": networks[1]["password"],
            "fallback_ap_password": c["wifi"]["ap"]["password"],
        }
        for name, value in refs.items():
            self.assertIsInstance(value, SecretRef)
            self.assertEqual(value, name)
        examples = yaml.safe_load((PROJECT / "esphome/secrets.example.yaml").read_text())
        self.assertEqual(set(examples), set(refs))
        self.assertTrue(all("REPLACE" in value for value in examples.values()))
        forbidden = {"switch.toggle", "homeassistant.service", "homeassistant.action", "lambda"}

        def visit(value):
            if isinstance(value, dict):
                self.assertFalse(forbidden.intersection(value))
                self.assertNotEqual(value.get("platform"), "homeassistant")
                for child in value.values():
                    visit(child)
            elif isinstance(value, list):
                for child in value:
                    visit(child)

        visit(c)

    def test_relative_links_and_diagram(self):
        files = list(PROJECT.rglob("*.md")) + [
            ROOT / "README.md", ROOT / "modifications/README.md",
            ROOT / "docs/trailer.md", ROOT / "docs/smart-dc-switch-research.md",
        ]
        for file in files:
            for target in re.findall(r"\]\(([^)]+)\)", file.read_text()):
                if re.match(r"[a-z]+:", target) or target.startswith("#"):
                    continue
                relative = target.split("#", 1)[0]
                with self.subTest(file=file.relative_to(ROOT), target=target):
                    self.assertTrue((file.parent / relative).exists())
        svg = ET.parse(PROJECT / "images/control-overview.svg").getroot()
        ns = "{http://www.w3.org/2000/svg}"
        for tag in ("title", "desc"):
            self.assertTrue(svg.findtext(ns + tag))

    def test_project_whitespace(self):
        # Explicit source paths: never inspect a private secrets.yaml or build tree.
        paths = [
            "README.md", "TESTS.md", "components.md", ".gitignore", "tests/test_config.py",
            "esphome/casita-smart-dc-switches.yaml", "esphome/secrets.example.yaml",
            "images/control-overview.svg",
        ]
        for path in paths:
            text = (PROJECT / path).read_text()
            self.assertTrue(text.endswith("\n"), path)
            for number, line in enumerate(text.splitlines(), 1):
                with self.subTest(path=path, line=number):
                    self.assertEqual(line, line.rstrip())
                    self.assertNotIn("\t", line)


if __name__ == "__main__":
    print("Static checks only: no ESPHome compile, credential provisioning or device access.")
    unittest.main(verbosity=2)
