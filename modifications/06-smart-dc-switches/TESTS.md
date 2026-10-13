# Commissioning and acceptance — four smart DC switches

**All physical checks below are pending.** This checklist is a plan, not evidence of tests performed. Record date, board revision, firmware version/hash, instruments, observations and pass/fail for each channel. Resolve failures before progressing to trailer loads. See [design and wiring boundaries](README.md).

## 1. Unpowered inspection and continuity (no battery)

- [ ] Preserve original panel/harness; photograph and label every connector, shared feed, illumination wire, load and fuse. Identify all four loads and any interlocks.
- [ ] Isolate battery, shore, solar, tow and all possible backfeeds before opening the trailer panel; verify dead. Loose-body continuity work is off-trailer, with no battery or bench supply attached.
- [ ] Confirm each part is V8D1-S00B, spring-return both ways; confirm compatible new actuators. Existing Nilight caps and panel fit are unverified.
- [ ] Measure all cutouts, panel thickness, rear clearance and enclosure location; allow for the 146 x 105 mm board, terminals, cable bends and access.
- [ ] On each of four loose bodies, prove terminal 2 is common; center opens 2–1 and 2–3; each press closes only one pair. Record which of 1/3 corresponds to installed UP. Mark UP → odd DI and DOWN → even DI.
- [ ] Confirm no dry-input conductor is connected to old positive jumpers, lamp supply or load power. Identify the received board's input GND/common from its matching schematic and legends.
- [ ] Confirm caps have durable load names and UP ON / DOWN OFF instructions. These Carling bodies are **unlit**; no lamp-state indication is present. Center position does not indicate output state.

| Channel | UP closes 2–? | DOWN closes 2–? | Center both open | Label / fit | Date / result |
| --- | --- | --- | --- | --- | --- |
| 1 | TBD | TBD | Pending | TBD | Pending |
| 2 | TBD | TBD | Pending | TBD | Pending |
| 3 | TBD | TBD | Pending | TBD | Pending |
| 4 | TBD | TBD | Pending | TBD | Pending |

## 2. Static source and separate build gates

- [ ] Run `python3 modifications/06-smart-dc-switches/tests/test_config.py` from repo root. Requires PyYAML; missing dependency is not a pass. It does not read/create real secrets, contact HA, compile or flash.
- [ ] Run `git diff --check`; check relative documentation links and SVG title/description. Review a rendered SVG before any future commit.
- [ ] Validate and compile with an actual ESPHome version; record exact version/result. Use synthetic credentials for a source-only validation build and **never deploy that artifact**. The example API marker is intentionally invalid; a later authorized device build needs privately provisioned credentials. **Static parsing is not ESPHome schema validation or compilation.**
- [ ] Review `ALWAYS_OFF` separately for each identified load; all four stay at that default until a deliberate documented decision. Review held-contact boot behavior before accepting any change.

## 3. Low-energy bench tests

Use a current-limited bench supply in the board's operating range and appropriately current-limited LED test loads. No trailer battery or appliance load is connected. Verify board revision/terminal labeling and safe programming power arrangements before applying power; avoid USB backfeeding.

- [ ] I2C shows 0x22 and 0x24 on SDA GPIO4 / SCL GPIO16. Verify all eight DI channels and their active-low polarity. Unused DI9–DI12 stay unwired.
- [ ] Verify each software switch energizes the intended relay, and logical OFF leaves its verified COM–NO path open. Prove `inverted: true` is correct for the received hardware. Check all four channels independently and together; no cross-coupling.
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

- [ ] Start with all outputs OFF, then ON, then mixed; power-cycle. With rockers centered, every output initializes OFF. Observe physical contacts/test loads during the entire power ramp, not just after logs appear.
- [ ] Repeat reset and controlled supply brownout/recovery on the bench. Look for transient pulses/chatter with suitable instrumentation. Document voltage envelope and whether hardware inhibition is required. `ALWAYS_OFF` is not proof of glitch-free startup.
- [ ] Boot with each UP or DOWN contact held; release and re-press. Record whether initialization creates a press event. Do not claim a held UP cannot energize the load after boot. Resolve acceptability per load.
- [ ] Evaluate firmware-update and failed-boot/safe-mode behavior on the bench. Safe mode may disable normal inputs/outputs; no offline-control guarantee applies during safe mode, hung firmware, power loss or hardware failure.
- [ ] Review disconnected/shorted control conductors and both-inputs-active faults with test loads only. There is no OFF-priority or fault interlock in this candidate. Add hardware/firmware protection if a selected load requires it.
- [ ] Test loss of communication with each I2C expander and its recovery, with trailer loads disconnected. First agree a reversible, non-destructive fault-injection method for the received board revision with a qualified bench tester; isolate power before changing a test fixture. Do not short the live bus, cut traces or lift soldered pins. If no suitable fixture/method is available, record this gate as **unverified**, not passed. Observe contacts/test loads with outputs previously OFF and ON, exercise physical DOWN during the fault, and record stale output state, loss of manual OFF, recovery pulses and whether restart or independent power isolation is required. An I2C fault can defeat local button control; network independence is not fault tolerance.

## 6. DC-load and installation gates

- [ ] Complete the README load worksheet: models, switched power versus control signal, existing interlocks, voltage, operating current, measured startup/inrush and motor stall requirement. Do not deliberately stall a motor without an approved procedure; use manufacturer limits where appropriate.
- [ ] Obtain appropriate **DC** contact/terminal/PCB ratings for direct switching, or select external DC-rated relays/interfaces. An AC 10 A marking does not pass this gate. Check external coil load compatibility and correctly polarized suppression too.
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
| Static tests | 2026-10-13: Python/PyYAML contract tests, relative link targets, SVG XML/title/description and source whitespace | Passed; not ESPHome validation/compile |
| SVG visual render | 2026-10-13: rendered with librsvg/Cairo to 1200 x 820 PNG; visually checked for clipping, readable labels and correct arrows | Passed; conceptual control diagram, not an approved load schematic |
| ESPHome config / compile | 2026-10-13: `ghcr.io/esphome/esphome:2026.9.1`, ESP-IDF, isolated copy with synthetic build-only credentials | Passed; no upload. Warning recommends replacing password-based OTA with required encrypted OTA; that optional change is not applied or claimed tested. The first synthetic all-zero API key was rejected; rerun with a nonzero synthetic key succeeded. Never deploy the validation artifact. |
| Continuity / bench / offline / boot | No hardware tests performed | Pending |
| Load ratings / installed acceptance | Loads not yet identified | Pending |
