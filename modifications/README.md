# Modifications

Each modification has its own folder with instructions, diagrams, parts, and a status line. Number new folders in order; 09 is retired and not reused, so the next free number is 13.

| # | Modification | Status | Summary |
| --- | --- | --- | --- |
| 01 | [Second battery](01-second-battery/README.md) | Done | Second Renogy 300 Ah battery in parallel for a 600 Ah bank, each battery individually fused to a common busbar |
| 02 | [A/C soft start](02-ac-soft-start/README.md) | Done | Spartan Power SpartanStart on the Coleman Mach 8 so the inverter can start the compressor; start capacitor and PTCR removed |
| 03 | [Whole-panel inverter](03-whole-panel-inverter/README.md) | Done | Go Power TS-30 so the whole WFCO panel, including the A/C, runs from the inverter when unplugged, with the converter and water heater element on a shore-only breaker box |
| 04 | [Battery monitor to Home Assistant](04-battery-monitor-esp32/README.md) | Installed and calibrated | XIAO ESP32-S3 and INA228 inside the Renogy display housing; publishes state of charge, power and a charging indicator to the trailer's Home Assistant, mirrored to the home one over Tailscale |
| 05 | [Starlink Mini on 12 V](05-starlink-12v-power/README.md) | Installed; fuse to add | Starlink Mini powered from the battery bank through a 12-36 V adapter and Casita's exterior Starlink port |
| 06 | [Four smart DC switches](06-smart-dc-switches/README.md) | Installed 2026-10-23; cover pending | Four BANDC momentary rockers in the Nilight panel, Waveshare ESP32-S3-POE-ETH-8DI-8RO in the adjacent cabinet; two LED light circuits on CH1/CH2, two spare channels; local UP ON / DOWN OFF plus Home Assistant |
| 07 | [Tank monitor to Home Assistant (propane, fresh and grey)](07-tank-monitor/README.md) | Propane device reading both cylinders (uncalibrated); fresh live via Garnet; grey Mopeka mounted, no echo yet | Propane: one XIAO ESP32-S3 (`casita-tank-monitor`) on trailer 12 V reads two DYP L06 ultrasonic sensors in magnetic collars under the 20 lb cylinders. Fresh: a Garnet SeeLeveL 710-ES3 sender read by a Garnet 709-BTP7 Bluetooth display (replaced the planned ESPHome fresh device, 2026-10-28). Grey: a Mopeka Pro Check Universal under the belly tank, Bluetooth to the trailer's Home Assistant (replaced a wired DYP L02 that never worked, 2026-10-27). Propane %, pounds, and water % in Home Assistant. Combines the former mods 07 and 09 (2026-10-27) |
| 08 | [E-ink dashboard](08-eink-dashboard/README.md) | Running since 2026-10-20; real tank entities and a Power page since 2026-10-28 | TRMNL 7.5" e-paper kit running ESPHome, mounted in the trailer, showing battery, propane and water levels from the trailer's Home Assistant |
| 09 | Retired: merged into [07, tank monitor](07-tank-monitor/README.md) | — | Number not reused |
| 10 | [AC voltage and power meter](10-ac-power-meter/README.md) | Designed; parts ordered | Shelly EM Gen3 on the TS-30 output, so AC voltage and power are measured from shore or inverter alike; second clamp on the shore cord gives total shore draw and the live source |
| 11 | [Xantrex Freedom X 2000 inverter to Home Assistant](11-xantrex-freedom-x-inverter/README.md) | Inverter installed; HA integration installed, first live read pending | Xantrex Freedom X 2000 (817-2000) with the Freedom X Bluetooth Remote Panel, read by the trailer's Home Assistant over BLE with the `ha-xantrex-freedom` integration; physical install still to document |
| 12 | [Cold-weather package](12-cold-weather/README.md) | Proposed; nothing ordered or measured | 12 V heating pads and an insulated belly pan on the exposed grey tank, heat cable on the dump valves and drain stubs, warming pads and insulation in the battery compartment so the LiFePO4 bank can charge below freezing, five DS18B20 probes on the mod 07 tank monitor XIAOs, heaters switched by spare mod 06 relays, and Home Assistant freeze alarms and shore-budget automations |

## Template for a new modification

```markdown
# Title

> **Status:** planned / in progress / done (date)

What it does and why.

## Parts
## Wiring / diagrams
## Steps
## Testing
## Safety notes
## Revisions
```
