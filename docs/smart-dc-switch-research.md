# Smart DC Switch Research

**Research date: 2026-10-13; owner choices updated 2026-10-19. Status: planned; rockers delivered and controller ordered, not installed.** The original four-channel plan selected Carling V8D1-S00B bodies and a KinCony KC868-A4S. On 2026-10-19 the owner instead bought **four [BANDC three-pin momentary SPDT rockers](https://www.amazon.com/dp/B0CNS17ZMK)** and replaced the controller with a **[Waveshare ESP32-S3-POE-ETH-8DI-8RO](https://www.amazon.com/dp/B0FBKGGKK3)**; see [the controller change](#controller-change-2026-10-19). See [mod 06 — Four smart DC switches](../modifications/06-smart-dc-switches/README.md) for the current **Planned / bench-validation required** BOM, control mapping, firmware candidate, diagram and commissioning checklist. This research preserves the original comparison and rationale; the load-side design remains conditional.

## Existing panel: what is known

The owner confirmed that the pictured rockers switch DC circuits. The owner-supplied photo description identifies a visible **Nilight** logo, **four illuminated rocker switches**, and a digital readout that **appears to show 13.5 V**. That display reading is not a calibrated measurement or evidence of the bus's maximum voltage.

The exact panel/switch model, opening dimensions, rear pinout, four load identities, operating and startup currents, and branch fuse sizes are unknown. The logo alone does not establish a particular Nilight model or Carling-compatible fit. A commonly cited **21 x 37 mm** Nilight rocker cutout is only an illustrative dimension from a different product, not a measurement or fit guarantee for this panel. Measure each opening and available rear depth before choosing anything.

See the [equipment record](trailer.md#electrical) for the existing panel and battery system.

## Conclusion and recommended architecture

**No verified smart drop-in replacement for this panel's presumed Carling/Nilight-style openings was found in the sources reviewed.** This is a bounded research result, not a claim that no such product exists. None of the modules below is a verified mechanical replacement for an existing rocker.

**Owner clarification, 2026-10-13:** pressing physical **UP must always command ON**, and pressing **DOWN must always command OFF**, independent of the last Home Assistant state, like a household smart rocker. Manual operation must continue with HA disconnected or the network/router off. Operation with dead electronics is not a requested requirement.

The recommendation is now **four two-direction spring-return rockers feeding one locally programmed KinCony KC868-A4S**, with suitably rated load switching. This supersedes retaining the existing latching switches in edge/toggle mode. See the [explicit UP/DOWN recommendation](#recommended-retrofit-for-explicit-updown-control) below. It is a buildable retrofit architecture, conditional on fit, load protection, and validation; no verified all-in-one off-the-shelf smart rocker drop-in has been established.

- Configure switch-to-relay behavior **on the device**, not through a Home Assistant automation, cloud scene, or network round trip. Manual switching should work with Home Assistant stopped and Wi-Fi unavailable, provided the controller remains powered and functional.
- This is **not** a bypass for loss of controller/relay power, firmware failure, or failed relay hardware. Such a bypass is outside the clarified requirement.
- Home Assistant can provide local network control. The official [Shelly integration](https://www.home-assistant.io/integrations/shelly/) communicates directly with the device and does not require the cloud. Network control and network-independent manual input are separate requirements.
- For four independent loads, allow for four separately controlled channels and their protection. A single-channel module is not a four-channel replacement.

### Rocker behavior and illumination

With a maintained rocker in **edge mode**, each change of physical position toggles the relay regardless of the rocker's new position. After a remote command, the rocker position (and possibly its LED) can disagree with the relay state. **This cannot provide the requested explicit UP = ON / DOWN = OFF behavior.** A latching switch already in the UP position also cannot accept another UP press after HA turns the load off without first moving it down.

Use separate momentary UP and DOWN contacts for explicit commands, not a single momentary toggle action. The proposed rocker returns to center after either press; its physical resting position does not indicate load state. The requested manual behavior is settled; BANDC fit, included actuator and continuity/pinout remain to be verified on received parts.

**Do not connect the illuminated rocker harness to a controller input without identifying every pin.** Its lamp supply, shared feed, or internal connections could inject 12 V into an input intended only for a dry contact. A relay's dry-contact *output* does not establish the electrical requirements of its switch *input*. Lamp power, input reference, and any isolation/interface must follow the exact controller and rocker documentation; the present pinout is unknown.

## Recommended retrofit for explicit UP/DOWN control

**Owner-selected architecture: not purchased, installed or bench-tested; firmware candidate compiled separately in mod 06.** The following Carling comparison is the 2026-10-13 research history, not the current switch purchase choice; the [project](../modifications/06-smart-dc-switches/README.md) carries the updated BANDC BOM and control-signal design. Exact load-side components and wiring remain pending measurements.

### Switch bodies, actuators, and controller

- **Original selection (superseded): four Carling V8D1-S00B switch bodies**, SPDT, spring-return **(ON)-OFF-(ON)**, **no lamp**, plus **four compatible caps/actuators**. The [specific SKU at New Wire Marine](https://newwiremarine.com/product/v8d1-s00b-mom-off-mom-rocker-switch/) corroborates the three-terminal, no-lamp body and momentary action in both directions. Do not assume a body includes the desired actuator or that the existing Nilight caps fit.
- The primary [Carling V-Series datasheet](https://www.carlingtech.com/sites/default/files/documents/V-Series_datasheet.pdf) identifies circuit code **8** as **(ON)-OFF-(ON)** and the nominal panel cutout as **0.830 x 1.450 in (21.08 x 36.83 mm)**. Parentheses denote momentary contact closure, not the controlled load's commanded state. **Fit in this Nilight panel is unverified**; confirm cutout tolerances, panel thickness, body depth, and actuator clearance against the drawing and measurements.
- **Current choice (2026-10-19): four BANDC three-pin momentary SPDT rockers**, [Amazon listing B0CNS17ZMK](https://www.amazon.com/dp/B0CNS17ZMK), selected by the owner for planned purchase; no purchase confirmed. The listing describes a no-LED `(ON)-OFF-(ON)` switch and approximately 0.83 x 1.46 in opening. These seller claims are not evidence of installed fit or received-part pin numbering; continuity-test common and both throws and measure the actual panel. Do not carry the Carling terminal map or cap assumptions over to this switch.
- **One KinCony KC868-A4S**, locally programmed with ESPHome: use **8 of its 12 dry-contact inputs**, arranged as four UP/DOWN pairs, and **all four relay outputs**, one per load-control channel. The [manufacturer pin mapping](https://www.kincony.com/forum/showthread.php?tid=2617) and [manufacturer ESPHome example](https://www.kincony.com/forum/showthread.php?tid=2618) document the board's I/O. The older example is a mapping reference, not a compiled configuration for this project.
- Its **9-24 V DC** supply range encompasses the expected normal operating range of this nominal 12 V battery system, including 14.4-14.6 V charging. That is **not automotive transient qualification**. Verify the actual supply envelope and provide appropriate transient protection. Power the electronics from **unswitched, fused DC independent of the switched load paths**, so turning a load off does not disable its controller.
- The **146 x 105 mm PCB** need not fit behind the rocker panel. It can be remote-mounted in a suitable enclosure in a nearby cavity, with low-current control wires to the panel; confirm enclosure space, wire routing, terminal clearance, and access.

### Controller change, 2026-10-19

The KinCony KC868-A4S described above was never ordered. It is not sold on Amazon (only from KinCony's own store), publishes only AC relay ratings, and ships as a bare 146 x 105 mm board. The owner bought a **Waveshare ESP32-S3-POE-ETH-8DI-8RO** instead ([manufacturer wiki](https://www.waveshare.com/wiki/ESP32-S3-ETH-8DI-8RO), [ESPHome device page](https://devices.esphome.io/devices/waveshare-esp32-s3-eth-8di-8ro/)): eight optocoupler-isolated digital inputs (passive dry-contact or active), eight relays rated ≤10 A at 30 V DC / 250 V AC, a 7–36 V DC supply terminal and a rail-mount ABS case (175 x 90 x 40 mm). All eight inputs are needed for four UP/DOWN pairs, leaving none spare. The KinCony text in this section is kept as research history; current mapping and firmware are in [mod 06](../modifications/06-smart-dc-switches/README.md).

Other options considered on 2026-10-19 and not chosen: a generic ESP32 four-relay board (inputs would be unprotected ESP32 pins on long panel runs; no published DC relay rating), and four Shelly Plus Uni modules (300 mA outputs requiring an external relay for every load; four devices to manage).

### Local control contract

For each of the four load channels, program these actions directly in ESPHome on the controller:

| Physical event | On-device action | Result regardless of previous HA command |
| --- | --- | --- |
| UP contact pressed | `switch.turn_on` for that channel | ON, including when already on |
| DOWN contact pressed | `switch.turn_off` for that channel | OFF, including when already off |
| Either contact released; rocker returns to center | No action | Output retains its current state |

Use the documented [ESPHome switch actions](https://esphome.io/components/switch/), **never `switch.toggle` or an HA service call** for these manual inputs. The rocker commands the load state; center release does not turn the load off. HA should expose the same output switch state, not infer it from the momentary input. While connected, HA reflects that output state and resynchronizes after reconnecting; without separate feedback, this is not proof that a relay contact or appliance physically operated.

Set **`wifi.reboot_timeout: 0s`** and **`api.reboot_timeout: 0s`** in the proposed Wi-Fi configuration (that is, `reboot_timeout: 0s` under each respective component). The [Wi-Fi documentation](https://esphome.io/components/wifi/) and [native API documentation](https://esphome.io/components/api/) describe their default 15-minute offline reboot timers and how `0s` disables them. This avoids default reboot cycling when the router or HA is absent. It does not guarantee network recovery or operation through hardware failure.

Select an explicit **per-load `restore_mode`** after identifying the loads; do not blindly restore every appliance ON. Bench-check input debounce, startup/reset/brownout output glitches, and behavior with a contact held during boot. Test both HA disconnection and router-off operation longer than the default timeout interval, with a healthy powered controller. Local UP/DOWN actions must remain functional throughout.

### Load interface and remaining limits

The onboard relay sheet does not establish a DC-motor rating. **Use external appropriately DC-rated power relays for motor/inrush loads unless an exact suitable onboard rating is established**, and verify the board's compatibility with the external relay coil/interface and suppression. Preserve each branch's fuse and correctly sized wiring; separately protect the electronics supply. The four onboard outputs may be control stages rather than the final load-power contacts.

Do not blindly reuse the existing battery-feed jumpers or illumination wiring on the new dry-contact inputs. **Do not put battery voltage onto GPIO or dry-contact inputs.** The no-lamp switch bodies avoid an intentional lamp feed, but the old harness still requires identification and separation from the low-current control circuit.

The project now provides a source-checked **controller input mapping** and planning BOM. Final **load-side wiring and component ratings** remain blocked on the four load identities, fuse sizes, normal/startup currents, backside pinout, actual cutouts and enclosure space. The BANDC common, throws and physical UP orientation must be identified by continuity on received parts; Carling pin numbers are not applicable. The UP/DOWN user experience does not need further clarification.

## Candidate comparison

Supply ratings describe power for the controller; output ratings describe the circuit it can switch. They are not interchangeable. Published maximum current alone is not approval for a pump, motor, or LED-driver startup surge.

| Candidate | Controller power and physical size | Outputs / inputs | Conditional assessment |
| --- | --- | --- | --- |
| **Shelly 1 Gen4** ([manufacturer](https://kb.shelly.cloud/knowledge-base/shelly-1-gen4)); **Shelly 1 Gen3** ([manufacturer](https://kb.shelly.cloud/knowledge-base/shelly-1-gen3)) | **12 V DC stabilized OR 24-48 V DC**, distinct supply options, not a continuous 12-48 V range. Both are **37 x 42 x 16 mm**, before wiring clearance/enclosure. | One potential-free relay output and one switch/button input per module. Maximum DC switching: **30 V DC, 10 A**; the **16 A** rating is for AC, not DC. | Earlier single-channel candidate, superseded for the clarified UX: its single switch input alone does not provide separate UP and DOWN contacts per load. Protected regulated power and verified load suitability would still be required. External DC-rated power relays may be necessary. |
| **Shelly 1 Mini Gen4** ([manufacturer](https://kb.shelly.cloud/knowledge-base/shelly-1-mini-gen4)) | **110-240 V AC powered**. | Can switch DC through its potential-free output, but that does not mean it can be powered by DC. | **Not suitable for direct power from the trailer's DC bus.** Its smaller size does not solve the supply requirement. |
| **Shelly Plus Uni** ([manufacturer](https://kb.shelly.cloud/knowledge-base/shelly-plus-uni)) | **9-28 V DC** supply option. | Two potential-free **solid-state** outputs, maximum **30 V, 300 mA**. | A control/sensing option for small loads, not a direct RV power or pump switch. External correctly rated DC relays are possible only after verifying coil current, startup demand, suppression, and output compatibility. |
| **KinCony KC868-A4S** ([ESPHome device documentation](https://devices.esphome.io/devices/kincony-kc868-a4s/); [manufacturer parameter sheet](https://www.kincony.com/images/KC868-A4S/KC868-A4S-1_05.jpg)) | **9-24 V DC**; board **146 x 105 mm**, plus enclosure, terminals, cable bends, and service access. | **Four relays and 12 dry-contact inputs**. ESPHome documentation provides the board mapping and example configuration. | A centralized four-channel option if space and input compatibility are confirmed. The manufacturer's **277 V AC / 10 A** and **125 V AC / 12 A** ratings do **not** validate DC motor switching. Require external DC-rated power relays unless an exact rating for the proposed DC load is verified; also verify any interface/coil load placed on the board outputs. |
| **Waveshare ESP32-S3-ETH-8DI-8RO / POE-ETH-8DI-8RO** ([manufacturer wiki](https://www.waveshare.com/wiki/ESP32-S3-ETH-8DI-8RO)), added 2026-10-19 | **7-36 V DC** screw terminal or 5 V USB-C; rail-mount case **175 x 90 x 40 mm**. | **Eight relays (≤10 A 30 V DC / 250 V AC, 1NO 1NC) and eight isolated digital inputs**; ESPHome device page with mapping. | **Owner-purchased 2026-10-19.** Covers four UP/DOWN pairs with no spare inputs. The DC contact rating still does not validate motor startup or stall; verify per load. |
| **SONOFF MINI-D** ([manufacturer](https://help.sonoff.tech/docs/mini-d)) | **12-48 V DC** supply option; operation **below 12 V is unsupported** by the published range. | Output: **24 V DC / 2 A resistive OR 12/24 V DC / 8 W motor**. Wi-Fi with Matter, **not Thread**. | Possible dry-contact/control or small-load candidate, not a typical RV pump solution. Do not substitute the resistive rating for the motor limit or assume that a nominal 12 V battery always stays within its supply range. |

This comparison is research history, not a purchase list; the current BANDC/KinCony plan is documented in mod 06. The wider input ranges of the Uni and KinCony do not by themselves establish automotive/RV transient tolerance, environmental suitability, or permission to attach an unidentified load.

### Shelly supply: why regulation is required

A nominal 12 V RV battery bus is not a stabilized 12 V supply. Charging can raise it to **14.4-14.6 V**; the photographed apparent 13.5 V reading also does not establish stabilized 12 V operation. The Gen3/Gen4 documentation distinguishes **12 V stabilized** from **24-48 V DC**. It does not establish that the gap between those options is supported.

For a Shelly 1 powered from this bus, use a **protected, regulated supply**, not a direct battery connection. Select the regulator only after establishing the full operating range, including low battery, all charging sources, and expected transients. It must maintain the required output across that range, provide adequate current and thermal margin, and have appropriate transient protection and fusing. If the input can fall below the desired output, a step-down-only regulator may not suffice. No exact regulator or terminal wiring is selected here, and no manufacturer-verified **±10%** input tolerance is assumed.

Regulating the controller's supply does not establish the relay's suitability for switching an unregulated load bus. Verify the actual load voltage, DC current, startup/inrush or stall demand, and required suppression separately.

## Firsthand RV precedent and its limits

In [Adventurous Way's Smart RV Tour, Lights section](https://www.adventurousway.com/blog/smart-rv-tour#lights) (2021-04-15), the owners report using **Sonoff SV modules with ESPHome** for their 12 V lights and replacing locking switches with **momentary switches** so physical ON/OFF positions would not conflict with phone control. They also describe local Home Assistant operation without internet.

This is firsthand evidence for a separate relay/controller plus revised manual-switch approach. It is **not** a successful drop-in smart Carling/Nilight rocker replacement, a verified wiring design for this Casita, or validation of another product's pump rating. On-device manual operation during a Wi-Fi outage remains a requirement to configure and test on any chosen implementation.

## Information still needed before final parts selection or load wiring

1. **Identify all four loads.** Record what each rocker operates, the equipment model, whether it switches full load power or only a control signal, and any existing interlocks.
2. **Record protection and demand per circuit.** Fuse size, wire gauge, normal current, startup surge/inrush (and motor stall requirements where applicable), and the manufacturer's DC switching requirements. Do not infer current from a fuse alone.
3. **Document the panel rear.** Clear photos of switch labels, pin numbers, connectors, illumination feeds, and shared jumpers; establish the exact model and pinout without relying on wire color alone.
4. **Measure fit.** Each cutout's width/height, panel thickness, available rear depth, terminal and wire-bend clearance, and a possible enclosure location.
5. **Confirm mechanical layout for the settled behavior.** UP commands ON and DOWN commands OFF, with spring return to center. Verify the selected BANDC part's included actuator, fit, pinout and orientation; unlit rockers are proposed. Network-independent operation is required; dead-electronics bypass is not.
6. **Establish the supply envelope.** Confirm minimum/maximum bus voltage under battery and charging conditions and the protection needed for the chosen controller and regulator.

## Installation boundaries and later acceptance checks

Final wiring should be designed and carried out by a **qualified RV installer** after the measurements and component ratings are confirmed. **Isolate battery, shore, and solar feeds and verify the conductors are de-energized before exposing them**; account for the inverter and every source capable of backfeeding the circuit.

Preserve branch fusing and correctly sized wiring. Provide appropriate protection for new controller/regulator wiring and use DC-rated switching hardware suitable for each load's inrush and duty. An AC contact rating does not establish a DC motor rating. Include suitable enclosures, strain relief, and secure connections for vibration. **Final load-power terminal instructions require verified measurements and pinouts.** The project's separate control diagram uses documented board mappings and explicitly leaves rocker orientation and load-side interfaces subject to validation.

For a future implementation, verify each UP press commands ON and each DOWN press commands OFF after either HA state, including repeated same-direction presses; release must do nothing. Repeat with HA stopped and the router off; verify local HA control without cloud access and state resynchronization on reconnect. Confirm per-load restore behavior and absence of startup/reset glitches, and check voltage, load startup, and temperature under intended operating conditions. Document these as actual tests only after they are performed.

**Work performed on 2026-10-13:** documentation and source review only. No physical changes, device configuration, or electrical tests were performed. All product and integration links above were accessed for this research on that date; installed fit and load compatibility remain unverified.
