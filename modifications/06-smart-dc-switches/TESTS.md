# Commissioning and acceptance — four smart DC switches

**Bench session 2026-10-23: first physical tests passed** (see the result table at the end; unchecked items remain pending). This checklist is the plan; only items with recorded evidence count as done. Record date, board version (Waveshare ESP32-S3-POE-ETH-8DI-8RO as purchased), firmware version/hash, instruments, observations and pass/fail for each channel. Resolve failures before progressing to trailer loads. See [design and wiring boundaries](README.md).

## 1. Unpowered inspection and continuity (no battery)

- [ ] Preserve original panel/harness; photograph and label every connector, shared feed, illumination wire, load and fuse. Identify all four loads and any interlocks.
- [ ] Isolate battery, shore, solar, tow and all possible backfeeds before opening the trailer panel; verify dead. Loose-body continuity work is off-trailer, with no battery or bench supply attached.
- [ ] Confirm all four received parts match the owner-selected BANDC three-pin momentary SPDT listing variant; confirm spring return in both directions and inspect included actuators. Existing Nilight caps and panel fit are unverified. A listing alone is not a pinout test.
- [ ] Measure all cutouts, panel thickness, rear clearance and enclosure location; allow for the 175 x 90 x 40 mm rail-mount case, 35 mm DIN rail, terminals, cable bends, antenna routing and access.
- [ ] On each of four loose bodies, continuity-identify the common and two throws (do not assume Carling terminal numbering); prove center opens both common-to-throw paths and each press closes only one. Record which throw corresponds to installed UP. Mark UP → odd DI and DOWN → even DI.
- [ ] Confirm no dry-input conductor is connected to old positive jumpers, lamp supply or load power. Identify the received board's digital-input common terminal for passive (dry-contact) wiring from its silkscreen and the Waveshare wiki diagram. Confirm the external antenna is present and connected to the module's antenna socket.
- [ ] Confirm durable load names and UP ON / DOWN OFF instructions on or beside the actuators. The selected BANDC listing describes **no LED**; confirm on received parts. Center position does not indicate output state.

| Channel | Verified common pin | UP closes common–? | DOWN closes common–? | Center both open | Label / fit | Date / result |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Owner-identified by meter | DI1 | DI2 | Confirmed by behaviour | Loose, not panel-mounted | 2026-10-23 pass (functional) |
| 2 | Owner-identified by meter | DI3 | DI4 | Confirmed by behaviour | Loose, not panel-mounted | 2026-10-23 pass (functional) |
| 3 | Owner-identified by meter | DI5 | DI6 | Confirmed by behaviour | Loose, not panel-mounted | 2026-10-23 pass (functional) |
| 4 | Owner-identified by meter | DI7 | DI8 | Confirmed by behaviour | Loose, not panel-mounted | 2026-10-23 pass (functional) |

Physical pin positions on the BANDC bodies were not written down; the functional result (UP → odd DI → ON on every channel) is the evidence. Record the pin positions when the rockers are labelled for installation.

## 2. Static source and separate build gates

- [ ] Run `python3 modifications/06-smart-dc-switches/tests/test_config.py` from repo root. Requires PyYAML; missing dependency is not a pass. It does not read/create real secrets, contact HA, compile or flash.
- [ ] Run `git diff --check`; check relative documentation links and SVG title/description. Review a rendered SVG before any future commit.
- [ ] Validate and compile with an actual ESPHome version; record exact version/result. Use synthetic credentials for a source-only validation build and **never deploy that artifact**. The example API marker is intentionally invalid; a later authorized device build needs privately provisioned credentials. **Static parsing is not ESPHome schema validation or compilation.**
- [ ] Review `ALWAYS_OFF` separately for each identified load; all four stay at that default until a deliberate documented decision. Review held-contact boot behavior before accepting any change.

## 3. Low-energy bench tests

Use a current-limited bench supply in the board's operating range and appropriately current-limited LED test loads. No trailer battery or appliance load is connected. Verify board revision/terminal labeling and safe programming power arrangements before applying power; avoid USB backfeeding.

- [ ] I2C scan shows the TCA9554 at 0x20 on SDA GPIO42 / SCL GPIO41 (the board also has an RTC on this bus). Verify all eight DI channels (GPIO4–GPIO11) and their active-low polarity with dry contacts to the input common. There are no spare inputs.
- [ ] Verify each software switch energizes the intended relay, and logical OFF leaves its verified COM–NO path open. Prove `inverted: false` is correct for the received hardware. Check all four channels independently and together; no cross-coupling. Confirm unused relays 5–8 stay open at all times, including during boot.
- [ ] For each channel: UP gives ON, release retains ON; DOWN gives OFF, release retains OFF. Repeat UP at least ten times while ON and DOWN at least ten times while OFF; no toggle. Test brief presses, long holds and bounce with 25 ms filtering.
- [ ] Verify a held button does not continuously override remote commands: these are press events, not a maintained position. Releasing must do nothing; a subsequent press commands its direction again.
- [ ] Confirm controller stays powered with all four outputs OFF. Measure idle and all-relays-on power draw and temperature.

## 4. HA/button state and network independence

For every channel, observe both physical test load and the corresponding native ESPHome switch state:

- [ ] HA OFF → UP ON; HA ON → DOWN OFF. Repeat UP after HA ON and DOWN after HA OFF (idempotent).
- [ ] UP ON → HA OFF → UP ON; DOWN OFF → HA ON → DOWN OFF. Release never changes output. Test other channels for isolation.
- [ ] Button change updates HA while connected; HA change updates the same output. HA state is a command-state report, not actual load feedback.
- [ ] Disconnect/stop the bench HA connection for **more than 30 minutes** with Wi-Fi still available. Exercise all buttons near start, after 15 minutes and after 30 minutes; monitor serial logs/reset reason or another independent uptime observation for unexpected reboot.
- [ ] Turn off the bench Wi-Fi/router for **more than 30 minutes**; repeat all button operations and reboot observations. The YAML has `wifi.reboot_timeout: 0s` and `api.reboot_timeout: 0s`, not the default 15-minute timers. No production network changes are needed for this test.
- [ ] Restore connectivity; HA resynchronizes to the current output states without replaying stale commands. Confirm local control works without internet/cloud.

## 5. Boot, reset and failure behavior

- [ ] Before any load: power the board from the screw terminal and from USB-C separately, and watch all eight relays (LEDs and an ohmmeter or test lamp on COM–NO) from power-on until ESPHome finishes booting. The TCA9554 starts with its pins as inputs; record any relay click or contact closure during that window. A closure is a blocking failure for every load until a hardware inhibit is designed.
- [ ] Start with all outputs OFF, then ON, then mixed; power-cycle. With rockers centered, every output initializes OFF. Observe physical contacts/test loads during the entire power ramp, not just after logs appear.
- [ ] Repeat reset and controlled supply brownout/recovery on the bench. Look for transient pulses/chatter with suitable instrumentation. Document voltage envelope and whether hardware inhibition is required. `ALWAYS_OFF` is not proof of glitch-free startup.
- [ ] Boot with each UP or DOWN contact held; release and re-press. Record whether initialization creates a press event. Do not claim a held UP cannot energize the load after boot. Resolve acceptability per load.
- [ ] Evaluate firmware-update and failed-boot/safe-mode behavior on the bench. Safe mode may disable normal inputs/outputs; no offline-control guarantee applies during safe mode, hung firmware, power loss or hardware failure.
- [ ] Review disconnected/shorted control conductors and both-inputs-active faults with test loads only. There is no OFF-priority or fault interlock in this candidate. Add hardware/firmware protection if a selected load requires it.
- [ ] Test loss of communication with the TCA9554 relay expander and its recovery (inputs are direct GPIO and should keep reporting), with trailer loads disconnected. First agree a reversible, non-destructive fault-injection method for the received board revision with a qualified bench tester; isolate power before changing a test fixture. Do not short the live bus, cut traces or lift soldered pins. If no suitable fixture/method is available, record this gate as **unverified**, not passed. Observe contacts/test loads with outputs previously OFF and ON, exercise physical DOWN during the fault, and record stale output state, loss of manual OFF, recovery pulses and whether restart or independent power isolation is required. An I2C fault can defeat local button control; network independence is not fault tolerance.

## 6. DC-load and installation gates

- [ ] Complete the README load worksheet: models, switched power versus control signal, existing interlocks, voltage, operating current, measured startup/inrush and motor stall requirement. Do not deliberately stall a motor without an approved procedure; use manufacturer limits where appropriate.
- [ ] Obtain appropriate **DC** contact/terminal/PCB ratings for direct switching, or select external DC-rated relays/interfaces. The board's published ≤10 A / 30 V DC contact rating is a starting point, not motor or inrush approval; compare it to each load's measured running and startup current and switching type. Check external coil load compatibility and correctly polarized suppression too.
- [ ] Size each conductor, fuse, terminal and relay for its own circuit, environment and duty. Preserve branch protection; no guessed gauge/fuse rating, unprotected battery feed or shunt bypass.
- [ ] Confirm independently fused unswitched controller supply, surge/reverse-polarity protection and any regulation against measured RV supply conditions. All new returns remain on shunt P-/system side.
- [ ] Qualified installer verifies enclosure, clearances, secure terminations, strain relief, labels, source isolation and load schematic before installation. Capture final as-built diagram and photographs.
- [ ] After an authorized installation, repeat behavior tests and check approved load startup, voltage drop, fuse coordination, relay/coil release and temperatures over intended duty. Only then record installed status.

## 7. Future HA organization / import acceptance

- [ ] Native ESPHome integration is added to **Casita HA**, assigned to **Casita RV**; actual four output entity IDs and meaningful load labels are recorded without public network details.
- [ ] If imported elsewhere, explicitly select just the intended four output entities, use an **`rv_` prefix**, assign **Casita RV** area, and verify command/state propagation. Do not broadly import unrelated Casita entities; internal momentary inputs remain unexposed.
- [ ] No HA automation, HA service call or remote importer is required for manual switching. No IPs, MACs, real SSIDs, phone identifiers, tailnet details or credentials enter public documentation.

## 8. Rollback readiness and result record

- [ ] Original panel/harness, labeled photos and protection map are retained. A failed bench build leaves the trailer unchanged.
- [ ] Any later rollback starts with battery, shore, solar, tow and all feeds isolated and verified dead. Remove/isolate new components and restore original labeled circuits and fuses; verify original operation. No live jumper bypass.

| Evidence | Date / version / observations | Result |
| --- | --- | --- |
| Static tests | 2026-10-13 (KC868-A4S design, superseded): Python/PyYAML contract tests, relative link targets, SVG XML/title/description and source whitespace | Passed; not ESPHome validation/compile |
| SVG visual render | 2026-10-13 (KC868-A4S design, superseded): rendered with librsvg/Cairo to 1200 x 820 PNG; visually checked for clipping, readable labels and correct arrows | Passed; conceptual control diagram, not an approved load schematic |
| ESPHome config / compile | 2026-10-13 (KC868-A4S design, superseded): `ghcr.io/esphome/esphome:2026.9.1`, ESP-IDF, isolated copy with synthetic build-only credentials | Passed; no upload. Warning recommends replacing password-based OTA with required encrypted OTA; that optional change is not applied or claimed tested. The first synthetic all-zero API key was rejected; rerun with a nonzero synthetic key succeeded. Never deploy the validation artifact. |
| Controller change | 2026-10-19: firmware rewritten for the Waveshare ESP32-S3-POE-ETH-8DI-8RO; earlier KC868-A4S results above apply to the superseded configuration only | See rows below |
| Static tests (Waveshare) | 2026-10-19: five contract tests updated for GPIO4–GPIO11 inputs and TCA9554 0x20 relays | Passed; not ESPHome validation/compile |
| ESPHome config / compile (Waveshare) | 2026-10-19: `ghcr.io/esphome/esphome:2026.9.1`, ESP-IDF, ESP32-S3, isolated copy with synthetic build-only credentials. RAM 29.8%, flash 9.4% | Passed; no upload. Same OTA-password warning as 2026-10-13 (recommends `ota` encryption instead); not applied. Never deploy the validation artifact. |
| SVG visual render (Waveshare) | 2026-10-19: rendered with resvg and DejaVu Sans to 1200 x 820 PNG; checked for clipping, readable labels and correct arrows | Passed; conceptual control diagram, not an approved load schematic |
| Device Builder validate / compile | 2026-10-22: `casita-smart-dc-switches.yaml` in the trailer HA Device Builder, real secrets, ESPHome 2026.10.0 `devices/validate` and `firmware/compile` | Passed (compile ~14 min on the Pi 4) |
| First flash | 2026-10-23: factory image downloaded from the Device Builder, written with esptool 4.12 over the board's native USB from the laptop; chip ESP32-S3 rev v0.2, 8 MB embedded PSRAM, 16 MB flash, hash verified | Passed |
| Boot / I2C | 2026-10-23 serial log: I2C scan found `0x20` (TCA9554) and `0x51` (onboard RTC); PCA9554 init warning 0 / error 0; joined the trailer Wi-Fi first attempt at −68 dB; HA discovered the device by mDNS and adopted it (key fetched from the Device Builder); device in area Casita RV; entities `switch.casita_smart_dc_switches_load_1`–`_4`, all `off` at first contact | Passed |
| HA → relay | 2026-10-23: `switch.turn_on` / `turn_off` on Load 1 from HA; state followed within 1.5 s; relay click audible | Passed |
| Rocker → relay, all channels | 2026-10-23 recorder: Rocker 1 UP/DOWN → Load 1 on 19:29:25 / off 19:29:26 UTC; Rocker 2 → Load 2 on :31 / off :32; Rocker 3 → Load 3 on :35 / off :35; Rocker 4 → Load 4 on :38 / off :39. UP = odd DI = ON on every channel; no mapping change needed | Passed |
| No toggle / idempotent presses | 2026-10-23: Rocker 1 UP ×3 → single `on` (19:38:00); DOWN ×3 → single `off`; Rocker 2 UP ×2 → single `on`; owner heard one click per group, none on repeats | Passed |
| Relay terminal order | 2026-10-23 meter on CH1, labels upright, left→right: **NO – COM – NC** (L–M closed with Load 1 ON, M–R closed with it OFF). CH2–CH4 assumed identical; spot-check before any load | CH1 verified |
| DC power-up | 2026-10-23: USB removed (device unavailable 19:44:25), board powered from a bench 12 V supply on the `7~36V` block, current-limited; owner observed no relay movement during boot; HA reconnected 19:44:26 with all four outputs `off` | Passed (clean power-on only) |
| Offline 30 min (HA down / Wi-Fi down), held-button boot, brownout, safe mode, I2C fault injection | Not run | Pending |
| Load ratings / installed acceptance | Loads not yet identified | Pending |
| Load ratings / installed acceptance | Loads not yet identified | Pending |
