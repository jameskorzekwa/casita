# Four Smart DC Switches — Carling Rockers + KinCony KC868-A4S

> **Status: Planned / bench-validation required (2026-10-13).** The owner selected four **Carling V8D1-S00B** bodies and one **KinCony KC868-A4S**. Not purchased or installed. This project contains a control design and firmware candidate, not approval to connect the trailer's unidentified loads. The candidate compiled successfully with ESPHome 2026.9.1 using synthetic build-only credentials; physical tests remain pending.

Replace four existing illuminated DC rockers with unlit, two-direction momentary rockers. One controller handles four independent channels locally and exposes those same output switches to Home Assistant. Background and alternatives remain in [the research record](../../docs/smart-dc-switch-research.md).

## Required behavior

| Event | Required result, regardless of last HA or button command |
| --- | --- |
| Press UP | Command that channel ON, including when already ON |
| Press DOWN | Command that channel OFF, including when already OFF |
| Release either direction | Spring return to center; **no output action** |
| HA disconnected or Wi-Fi/router unavailable | Physical UP/DOWN still works with a powered, functioning controller |
| Power restored / normal restart | All four outputs default to `ALWAYS_OFF`; deliberate per-load review required before changing this |

This is explicit ON/OFF, never toggle. The rocker resting position is not a state indicator. Manual operation depends on the ESP32, firmware, I2C expanders, relays, and their supply; **there is no dead-controller bypass guarantee**. Commands are processed locally; HA is not in the physical control path. The most recently processed command wins; simultaneous remote/physical commands have no special priority. Contradictory contacts from a wiring fault have no safety arbitration in this candidate.

## Parts / planning BOM

Quantities below are for four channels. Only bodies and controller are owner-selected; remaining exact parts and ratings are TBD. No purchases are recorded.

| Part | Qty | Selection / specification gate |
| --- | ---: | --- |
| Carling V8D1-S00B SPDT `(ON)-OFF-(ON)`, no lamp | 4 | [Carling V-Series manufacturer datasheet](https://www.carlingtech.com/sites/default/files/documents/V-Series_datasheet.pdf); [specific body / supplier](https://newwiremarine.com/product/v8d1-s00b-mom-off-mom-rocker-switch/) |
| Compatible Carling actuators/caps with durable load labels | 4 | Select exact compatible series and legend after identifying loads. Existing Nilight caps are not assumed compatible. These bodies provide **no illumination** |
| KinCony KC868-A4S | 1 | [Manufacturer I/O definition](https://www.kincony.com/forum/showthread.php?tid=2617), [manufacturer ESPHome mapping](https://www.kincony.com/forum/showthread.php?tid=2618), [manufacturer parameter sheet](https://www.kincony.com/images/KC868-A4S/KC868-A4S-1_05.jpg) |
| Enclosure with standoffs, terminal covers and strain relief | 1 | Board is published as **146 x 105 mm**; allow extra depth, wiring bends, thermal clearance, antenna space and service access |
| DC-rated controller input fuse and holder | 1 set | Rating TBD from electronics demand, conductor ampacity, voltage and interrupt rating; place at source of new supply branch |
| Supply transient/reverse-polarity protection, regulation if required | 1 assembly, TBD | Board published supply **9–24 V DC** is not RV transient qualification; design against measured full supply envelope |
| Signal wiring, insulated quick-disconnects, power wiring, terminals, labels | As measured | Exact lengths, gauges, terminal sizes and ratings TBD; vibration-resistant connections and no exposed energized terminals |
| External DC-rated power relays / sockets / interfaces | Per load, TBD | Required unless exact onboard DC rating is proven sufficient; motor startup/stall, duty, contact life and voltage must be covered |
| Coil suppression and any load suppression | Per inductive circuit, TBD | Match relay/coil polarity and driver capability; follow manufacturer guidance, including release-time consequences |
| Branch fuses / holders | Per circuit, TBD | Preserve existing protection and add protection for every new conductor as required; select by wire and load, not guesswork |

Published nominal Carling panel cutout is **0.830 x 1.450 in (21.08 x 36.83 mm)**. This does not prove fit in the existing Nilight panel. Measure all four openings, thickness, actuator clearance, body depth and terminal clearance. Remote-mount the board if necessary. Do not order caps or alter the panel on assumed dimensions.

## Control wiring — separate from load power

![Planned control architecture, conditional load side](images/control-overview.svg)

### Rocker continuity and orientation

Carling's circuit uses **terminal 2 as common**, with **1 and 3 as the two throws**. Treat this as the documented pin assignment, **not a completed continuity measurement** on purchased parts. With each loose body disconnected from all power, verify 2–1 and 2–3 continuity through both presses and center. Record which throw closes when pressing the installed actuator's physical UP side. **Exact UP-to-1/3 orientation is not yet known.** Never infer it from the rear view or terminal position.

- Terminal **2** of each rocker goes to the board's documented **dry-input GND/common reference**, after verifying that terminal on the received board's schematic/silkscreen.
- The throw verified to close on **UP** goes to the odd DI input in the table below; the other throw goes to the even DI input.
- Center must leave both circuits open. Pressing one direction must close only its intended circuit. Use fresh labeled signal conductors, or reuse conductors only after complete isolation and identification.
- **Never connect the old 12 V switch-positive jumpers, illumination feed, or battery positive to any DI/GPIO or rocker common in this dry-contact circuit.** The old lamp harness is not an input harness. Keep load supply and dry signals separated.

### Exact controller signal map

Verified against the [manufacturer pin definition](https://www.kincony.com/forum/showthread.php?tid=2617), [manufacturer example](https://www.kincony.com/forum/showthread.php?tid=2618), and [ESPHome A4S device page](https://devices.esphome.io/devices/kincony-kc868-a4s/) on 2026-10-13. Match the received board revision and schematic before wiring; these sources establish software mapping, not an as-built harness.

**I2C: SDA GPIO4, SCL GPIO16.** `pcf_inputs` at **0x22**, `pcf_relays` at **0x24**. Input and relay polarity is `inverted: true` per the examples, subject to bench confirmation.

| Channel / firmware ID | UP → ON | DOWN → OFF | Board output |
| --- | --- | --- | --- |
| Load 1 / `load_1` | DI1, 0x22 P0 | DI2, 0x22 P1 | Relay 1, 0x24 P0 |
| Load 2 / `load_2` | DI3, 0x22 P2 | DI4, 0x22 P3 | Relay 2, 0x24 P1 |
| Load 3 / `load_3` | DI5, 0x22 P4 | DI6, 0x22 P5 | Relay 3, 0x24 P2 |
| Load 4 / `load_4` | DI7, 0x22 P6 | DI8, 0x22 P7 | Relay 4, 0x24 P3 |

Eight of twelve dry inputs are used. DI9–DI12 are 0x24 P4–P7, unused and unwired here. Do not confuse these with the first eight inputs or repurpose output pins. Each physical input is internal to ESPHome and has **25 ms debounce on both transitions**. Only `on_press` invokes `switch.turn_on` / `switch.turn_off`; release has no action.

## Supply and CONDITIONAL load-side design

The controller must remain powered when all four loads are OFF. Supply it from **independently fused, unswitched RV DC**, independent of the four switched load paths. “Unswitched” means not controlled by these rockers; it is not an instruction to bypass a master disconnect or battery protection. Use the protected distribution system. Return board, coil and load current to the **load/system side of the battery shunt (P-)**, never B-; do not create a shunt bypass or add unprotected direct battery wiring. See [battery distribution](../01-second-battery/README.md) and the [equipment record](../../docs/trailer.md#electrical).

Measure minimum/maximum supply during battery operation, charging, startup and disturbances. Normal charging around 14.4–14.6 V fits the published 9–24 V range, but spikes, reverse polarity and brownouts still need engineering review. Choose protection/regulation only after this assessment. Measure continuous controller/relay consumption for storage planning.

**No direct DC load connection is approved by this document.** The board's published **277 V AC / 10 A** and **125 V AC / 12 A** relay ratings do not establish DC breaking capability, especially for motors. Obtain an exact suitable DC rating for the relay contacts, PCB path and terminals, or use external suitably DC-rated power relays. Even an external relay coil is a load: verify its current/voltage, onboard-contact suitability and suppression/interface before connecting it.

Conceptually, each board relay controls an approved external relay/interface; that external relay's normally open contact switches the separately fused load branch. Final COM/NO terminal wiring, coil feed, polarity and suppression are **TBD per selected part**. The SVG intentionally does not specify unidentified power terminals. Preserve appliance interlocks and determine whether the original switch switches power or only a control input. Do not put mains or a life-safety circuit on this project by assumption.

Complete this worksheet before selecting power components or installing:

| Channel | Actual load/model; power or control signal | Existing fuse / conductor | Measured running / startup; stall requirement | DC-rated interface + suppression | Deliberate restore decision |
| --- | --- | --- | --- | --- | --- |
| 1 | TBD | TBD | TBD | TBD | `ALWAYS_OFF` pending review |
| 2 | TBD | TBD | TBD | TBD | `ALWAYS_OFF` pending review |
| 3 | TBD | TBD | TBD | TBD | `ALWAYS_OFF` pending review |
| 4 | TBD | TBD | TBD | TBD | `ALWAYS_OFF` pending review |

No fuse amperage or wire gauge is selected here. Fuses protect conductors; choose wire, protection and connectors for run length, voltage drop, environment, load and fault current. Final load wiring requires a qualified RV installer and the completed worksheet.

## Firmware candidate

[`esphome/casita-smart-dc-switches.yaml`](esphome/casita-smart-dc-switches.yaml) is a complete four-channel candidate using built-in ESPHome components. It uses Wi-Fi, the encrypted native API, and current OTA list syntax (`platform: esphome`). All credentials are `!secret` references. [`secrets.example.yaml`](esphome/secrets.example.yaml) contains only deliberately fake replacement markers; its API marker is **not** a valid encryption key. A future private build must supply valid credentials in ignored `secrets.yaml`; never publish actual SSIDs, IPs, MACs, phone identifiers, tailnet details or credentials.

Both `wifi.reboot_timeout` and `api.reboot_timeout` are **`0s`**, disabling their default 15-minute disconnected reboot timers. See [Wi-Fi](https://esphome.io/components/wifi/), [API](https://esphome.io/components/api/), [switch restore/actions](https://esphome.io/components/switch/), [PCF8574](https://esphome.io/components/pcf8574/) and [OTA](https://esphome.io/components/ota/esphome/).

`ALWAYS_OFF` is a software initialization choice, **not a glitch-free hardware guarantee**. Reset, slow power ramps, brownout, I2C failure, boot ordering, a held input and failed boots must be tested. ESPHome OTA safe mode can disable normal components after failed boots; local switching is not guaranteed in safe mode or during firmware updates. Disabling disconnected reboot timers does not disable watchdogs, prevent crashes or guarantee network recovery. Do not enable loads until startup behavior is acceptable for each appliance; add a hardware inhibit if the load requires it.

Static checks do not compile firmware or emulate the controller:

```sh
# From repository root; requires Python 3 and PyYAML.
python3 modifications/06-smart-dc-switches/tests/test_config.py
git diff --check
```

The test never reads or provisions `secrets.yaml`. If PyYAML is missing, it exits with a dependency message rather than reporting a false pass. Actual ESPHome schema validation/compilation is a separate check; results are recorded in [TESTS.md](TESTS.md). Build-only validation uses synthetic credentials, and its firmware must never be deployed. No firmware upload is authorized by this project-file task.

## Planned build sequence

1. Photograph and label the original panel, every connector, fuse and conductor. Identify all four loads and complete the worksheet. Keep the original panel/harness intact for rollback.
2. Measure mechanical fit; select compatible actuators, enclosure and rated protection/interface parts. Confirm exact received board revision against its schematic and terminal legends.
3. Off-trailer, with **no battery connected**, perform the loose-rocker continuity/orientation checks. Label each UP/DOWN conductor and match the table.
4. After separate firmware validation/compile, bench-test on a current-limited supply with low-energy, current-limited LED test loads; keep trailer loads disconnected. Verify relay contact polarity before any load trial.
5. Complete the [commissioning checklist](TESTS.md), including extended network outages, power disturbances and both orders of HA/button control. Record actual observations and firmware version.
6. Only after load ratings, protection and all acceptance gates are resolved, plan installation with an RV installer. Isolate battery, shore, solar, tow feed and every possible backfeed (including converter/inverter paths); prove dead before working. No live power changes are authorized by this document task.
7. Re-test installed behavior and temperatures under the approved operating conditions, record dated photos/as-built wiring, then change status to installed. Until then this remains **Planned**.

## Home Assistant and future import hook

Future setup uses the **native ESPHome integration in Casita's HA** for this device. Assign it to the **Casita RV** area and give the four outputs meaningful load names after identification. The API publishes the same switch state the local buttons control. That state represents the commanded output, **not proof of closed contacts or a running appliance**; separate feedback would be needed for that.

If the Casita HA entities are later imported into another HA instance, explicitly select only the intended four output entities, use an **`rv_` prefix** for imported IDs (for example `switch.rv_load_1` until meaningful names are chosen), and put them in **Casita RV**. Verify actual generated IDs; do not assume names alone enforce an ID. Do not broadly import unrelated entities or expose the eight internal buttons. This is a future integration hook, not configured automation, deployment or a dependency for manual control. No network addressing is recorded here.

## Rollback / safety notes

Keep the original panel, switches and labeled harness, plus before photos and a circuit/fuse map. If bench tests fail, leave the original trailer wiring untouched. If a later installation must be reversed, isolate **battery, shore, solar, tow and every other feed**, verify de-energized, remove/isolate the new controller and interfaces, and restore the documented original connections and branch protection. Verify original function before returning to service. Do not improvise an energized jumper bypass, combine dry-input and power wiring, or move returns to the battery side of the shunt.

## Revisions

| Date | Change / evidence |
| --- | --- |
| 2026-10-13 | Owner-selected bodies/controller; planned four-channel project, source-checked mapping, firmware candidate, diagram and acceptance checklist. Five static tests passed; SVG rendered and visually reviewed; ESPHome 2026.9.1 compilation passed using synthetic credentials. Independent review completed and I2C-failure acceptance gate added. No purchases, physical tests, firmware upload or installation recorded. |
