# Renogy Battery Monitor to Home Assistant (XIAO ESP32-S3 + INA228)

A Seeed Studio XIAO ESP32-S3 and a TI INA228 current/voltage monitor, built into the display housing of the Renogy 500 A Battery Monitor with Shunt (RBM500) in the Casita travel trailer. The INA228 measures the existing 500 A shunt and the battery voltage. The ESP32 counts amp-hours to track state of charge, then publishes voltage, current, power, state of charge, remaining amp-hours, time to empty or full, a charging indicator, and daily charged/discharged energy to Home Assistant. It also serves a local web page so a phone on the trailer's Wi-Fi can check the battery without Home Assistant.

The Renogy display keeps working exactly as before. The INA228 reads the same shunt in parallel through the display cable's sense wires, so you end up with two independent monitors.

![System overview](images/system-overview.svg)

> [!IMPORTANT]
> **Status (2026-10-14): installed, running and calibrated.**
>
> | Item | State |
> | --- | --- |
> | XIAO, buck regulator, C1, INA228 and wiring | Installed in the display housing. The INA228 answers at `0x40` and reports plausible readings (13.8-14.6 V on shore power; -6 A discharging to +32 A charging seen on 2026-10-13) |
> | Firmware on the XIAO | [`esphome/casita-battery-monitor.yaml`](esphome/casita-battery-monitor.yaml) as committed here, installed wirelessly from the trailer Home Assistant's ESPHome Device Builder (ESPHome 2026.9.1) on 2026-10-13. The XIAO is on the trailer Wi-Fi |
> | Calibration | Done 2026-10-14 against the Renogy display: at a steady 67 A discharge (A/C on the inverter) the INA228 read 67.3 A from 10.09 mV across the shunt while the Renogy read 67.5 A, a 0.3% difference, inside the Renogy's own 1% rating. The shunt is therefore 500 A / 75 mV and `shunt_resistance` stays at `0.00015 ohm` (measured 0.000150). Sign confirmed: discharge negative |
> | Trailer Home Assistant | Device adopted; all entities listed under [Entities](#entities) exist with the IDs shown. State of charge was set to 100% with **Mark Battery Full** on 2026-10-13 after the bank was on shore power |
> | Home Home Assistant | The trailer's entities are mirrored to the home Home Assistant over Tailscale and shown on a **Casita RV** sidebar page there; see [Mirroring to the home Home Assistant](#mirroring-to-the-home-home-assistant) |
> | Renogy display | Reads correctly since the WFCO converter's negative was moved from the shunt's `B-` to `P-` (see [mod 01](../01-second-battery/README.md#wiring-as-built)) |
>
> **Remaining work:** the unrecorded items of the [Testing Checklist](#testing-checklist) and [photos](#photos). The [Build](#build) steps are kept below as the record of how it was done and for rebuilding.

## How It Works

1. The 500 A shunt sits in the battery negative. The display's shielded cable carries battery positive and negative (`B+`, `B-`) and the shunt's sense pair (`Rs+`, `Rs-`) to the display board.
2. A 12 V to 5 V buck regulator, fed from the backs of the display connector's `B+` and `B-` pins, powers the XIAO. The XIAO's 3.3 V pin powers the INA228.
3. The INA228's differential inputs (`VIN+`, `VIN-`) connect to the `Rs+`/`Rs-` pins through 10 ohm resistors, with a 0.1 uF capacitor across them. It measures the millivolts across the shunt with 20-bit resolution and its own hardware charge accumulator.
4. The INA228's `VBUS` pin connects to `B+` and measures battery voltage against its ground (`B-`).
5. Every second, ESPHome reads the INA228 over I2C. The change in the INA228's charge accumulator is added to a stored "remaining amp-hours" value, which becomes the state of charge.
6. When the bank reaches full charge (high voltage with tapering charge current), state of charge resets to 100%, which cancels any accumulated drift.

Everything inside the housing shares one ground: the display's `B-`, which is the battery side of the shunt. The XIAO has no other wired connection, so nothing creates a second current path around the shunt.

## Why Not the Display's Serial Port

The first version of this project tried to read the display's own serial output. It does not work on this unit, and the files are kept in [`esphome/archive/`](esphome/archive/) for reference.

The display board is a Baiway TF03H V35. Baiway's TF03 meters can output a 9600-baud serial frame, but only on "customized" models fitted with an isolator module at `MK1`; this one is not. Tests run on 2026-10-09 with diagnostic firmware that logged every UART byte and counted every signal edge:

| Pad tested (with display awake) | Result |
| --- | --- |
| `Tx` (6-hole row) | Idle at 3.0 V, zero edges for 20+ minutes |
| `Tx` with a 10 kohm pull-up from `TEN` to `V+` | Zero edges |
| `Rx`, `TEN`, `MK2 T`, `MK2 R` | Zero edges |

Baiway's documentation describes serial output as a customized model option, the display menu has no communication setting, and no one online has reported enabling it on a standard unit. The conclusion is that serial output is disabled in this display's firmware. Measuring the shunt directly with an INA228 avoids the problem entirely.

## Known Limitations

- **The XIAO's own power is not metered.** It is taken from the battery side of the shunt, so neither the INA228 nor the Renogy display sees it (roughly 0.5 W, about 1 Ah per day, plus the display's own 10-15 mA). State of charge slowly reads high by that amount until the next full-charge resync.
- **Coulomb counting drifts.** Calibration errors accumulate over days. The full-charge resync corrects it, so the bank needs to reach full occasionally: at or above `full_voltage` (default 14.0 V) with the charge current tapered to `full_tail_current` (default 6 A) for 2 minutes. If your charger never exceeds about 13.8 V, the resync will not trigger; use the **Mark Battery Full** button after a known full charge.
- **It is always on.** `B+` comes straight from the battery, so the XIAO runs even when the trailer's battery disconnect switch is off: about 1 Ah per day in storage.
- **State of charge is saved to flash every 10 minutes.** After an unexpected power loss, up to 10 minutes of counting can be lost.
- **Remote reading away from home needs a network path.** See [Reading the battery away from home](#reading-the-battery-away-from-home).

## Parts

| Component | Quantity | Notes | Purchase link |
| --- | ---: | --- | --- |
| Seeed Studio XIAO ESP32-S3 | 1 | Already installed. Uses an external U.FL antenna | [Seeed](https://www.seeedstudio.com/XIAO-ESP32S3-p-5627.html) |
| 12 V to 5 V buck regulator | 1 | Already installed. Example: Pololu D24V5F5 | [Pololu](https://www.pololu.com/product/2843) |
| C1: electrolytic capacitor, 220-470 uF, **25 V or higher** | 1 | Across the buck's input. Pololu recommends at least 33 uF at the input when the supply leads are long, against destructive LC spikes at power-up; it also smooths the XIAO's Wi-Fi bursts. **Not fitted during the serial-tap build**; a 220 uF 25 V part was added on 2026-10-13. Do not use a 10 V or 16 V part: the bank reaches 14.6 V while charging | |
| INA228 breakout | 1 | Owned: GODIYMODULES INA228 module (10 A version, 2 mohm shunt marked `R002`). The Adafruit 5832 also works. **The onboard shunt must be removed** | [Amazon B0GX5HM4X3](https://www.amazon.com/dp/B0GX5HM4X3), [Adafruit](https://www.adafruit.com/product/5832) |
| 10 ohm resistors | 2 | 1/4 W or 0805; input filter and protection | |
| C2: 0.1 uF ceramic capacitor | 1 | X7R or C0G, 25 V or higher; across `VIN+`/`VIN-` | |
| Thin stranded hookup wire | About 0.5 m | 26-28 AWG silicone; use a twisted pair for `Rs+`/`Rs-` | |
| Inline fuse holder and 1 A fuse | 1 | On the RBM500's `B+` wire, close to the battery, if not already fused | |
| Kapton tape, heat-shrink, hot glue | As needed | Insulation and mounting inside the housing | |

Check that the INA228 breakout fits inside the housing next to the XIAO and regulator. If it does not, mount everything in a small enclosure directly behind the display and run the same wires to it.

## Tools and Supplies

- Fine-tip soldering iron, solder, flux and solder wick; hot air helps to remove the breakout's onboard shunt
- Multimeter with DC millivolts, resistance and continuity
- DC clamp meter (optional, for the most accurate calibration)

## Prepare the INA228 Breakout

![Preparing the INA228 breakout](images/ina228-board-prep.svg)

INA228 breakouts are built to measure current through their own small shunt. **That shunt must come off.** Here the INA228 is used only as a precise millivolt meter across the trailer's 500 A shunt, so nothing else may sit across its `VIN+`/`VIN-` inputs. If the onboard shunt stays:

- **With the 10 ohm filter resistors (as designed),** the two 10 ohm resistors and the 2 mohm onboard shunt form a divider, so the INA228 sees about 1/10,000 of the shunt signal and reads close to 0 A all the time.
- **Without the resistors,** the onboard shunt sits through the thin sense wires directly across the 500 A shunt: the sense wires carry part of the trailer's load current, both the INA228 and the Renogy display read wrong, and at high current the thin wires can heat up.

The board used here is the GODIYMODULES INA228 module (10 A version). Its 3-screw terminal is labelled `VIN+`, `VBUS`, `VIN-`; its 5-pin header is `GND`, `ALE`, `SCL`, `SDA`, `VCC`; it has 10 kohm I2C pull-ups and no input filter. The Adafruit 5832 differences are noted in each step.

1. **Chip check:** TI marks a genuine INA228 (`INA228AIDGSR`, VSSOP-10) **`228I`**, usually above a date/lot code and the TI logo; it is easy to misread as `2281`. An INA226, which some low-cost "INA228" modules carry and this configuration does not support, is marked just `226`. The module used here is marked `228I` (checked 2026-10-13).
2. **Remove the onboard shunt.** On the GODIYMODULES module it is the large resistor marked `R002` (2 mohm) next to the terminal block. On the Adafruit 5832 it is R1, marked `R015` (15 mohm). Other modules may use `R010` or `R100`. Desolder it with hot air, or with two irons or a solder blob heating both ends at once. Do not cut it off: leftover metal can still bridge the pads.
3. **Check:** resistance from `VIN+` to `VIN-` must now read tens of kilohms (the chip's input), not near zero.
4. **VBUS:** `VBUS` must not be tied to `VIN+`, because it gets its own wire to `B+`. Check that `VBUS` to `VIN+` reads open. If it does not, open the solder jumper that links them: the two-pad `V+` jumper beside the shunt on the GODIYMODULES module (open as shipped), or SJ1 on the back of the Adafruit board (open by default).
5. **Address 0x40:** `A0` and `A1` must both connect to GND. On the GODIYMODULES module the pad grid has a column for each address pin and rows `G`, `V`, `SDA`, `SCL`; only the `G` row should be bridged for both (as shipped). Do not leave either pin floating. On the Adafruit board leave A0 and A1 open (pulled down on the board). The boot log's I2C scan confirms the address.
6. **Header:** solder the 5-pin header, or wires directly to the pads. Leave `ALE` (alert) unconnected.

## Where to Connect on the Display Board

![RBM500 display board connection points](images/display-board-header.svg)

All four connections are made to the backs of the white shunt connector's pins on the display board:

| Pin | Goes to |
| --- | --- |
| `B+` | Buck regulator `VIN` (already connected) and INA228 `VBUS` |
| `B-` | Buck regulator `GND` (already connected). This is the ground for everything |
| `Rs+` | 10 ohm resistor, then INA228 `VIN+` |
| `Rs-` | 10 ohm resistor, then INA228 `VIN-` |

Which way round `Rs+`/`Rs-` go only sets the sign of the reading; `current_sign` in the YAML corrects it. Do not use anything in the six-hole row, `MK1`, `MK2` or `PROG`.

## Wiring

![Wiring inside the display housing](images/wiring-schematic.svg)

| From | To | Notes |
| --- | --- | --- |
| Display `B+` pin (back) | Buck `VIN`, C1 `+`, INA228 `VBUS` | C1's unstriped (longer) leg |
| Display `B-` pin (back) | Buck `GND`, C1 `-` | C1's striped leg. Backwards, an electrolytic can bulge or vent |
| Buck `VOUT` (5 V) | XIAO `5V` | Already installed |
| Buck `GND` | XIAO `GND`, INA228 `GND` | |
| XIAO `3V3` | INA228 `VCC` (GODIYMODULES) or `VIN` (Adafruit), the breakout's power pin | Not to be confused with `VIN+`/`VIN-` |
| XIAO `D4` (GPIO5) | INA228 `SDA` | Both boards have 10 kohm pull-ups |
| XIAO `D5` (GPIO6) | INA228 `SCL` | |
| Display `Rs+` | 10 ohm, then INA228 `VIN+` | Twist with the `Rs-` wire |
| Display `Rs-` | 10 ohm, then INA228 `VIN-` | |
| C2, 0.1 uF | Across INA228 `VIN+` and `VIN-` | At the breakout, after the 10 ohm resistors |

### XIAO ESP32-S3 pins

![XIAO ESP32-S3 pins used](images/xiao-esp32s3-pins.svg)

> [!WARNING]
> Never plug USB into the XIAO while the shunt cable is connected to the display. Use wireless updates once the XIAO is installed.

## Build

### Step 1: Remove the serial-tap test wiring

Unplug the shunt cable from the display, then remove:

- the `Tx` wire and its 1 kohm resistor to XIAO `D7`
- the probe wires from `Rx`, `TEN`, `MK2 T` and `MK2 R` to XIAO `D0`, `D1`, `D3` and `D4`, with their 1 kohm resistors
- the 10 kohm resistor between `TEN` and `V+`

Leave the buck regulator and the XIAO's `5V`/`GND` power wiring in place. If C1 is not already across the buck's input, fit it now (see [Parts](#parts)): stripe to `GND`, the other leg to `VIN`. Clean any solder bridges on the six-hole row.

### Step 2: Confirm the sense pair is passive

This confirms that `Rs+`/`Rs-` carry the raw shunt voltage and not an amplified signal.

1. Plug the shunt cable back in. Turn on a steady load of at least 20 A (for example the A/C on the inverter), or charge at a known current.
2. Measure DC millivolts between the `Rs+` and `Rs-` pin backs. Expect current x 0.10-0.15 mohm, for example 2-3 mV at 20 A.
3. Measure each of `Rs+` and `Rs-` against `B-`. Both should be within a few millivolts of zero.

If the reading is hundreds of millivolts or more, or either pin sits at a bias voltage against `B-`, the sense pair is not a plain shunt connection. Stop: the INA228 cannot be connected there.

### Step 3: Prepare the INA228

Follow [Prepare the INA228 breakout](#prepare-the-ina228-breakout). Do not skip the check that `VIN+` to `VIN-` no longer reads near zero.

### Step 4: Wire the INA228

1. Unplug the shunt cable from the display.
2. Solder a 10 ohm resistor in series with each of two thin wires, then twist the wires together. Connect one end to the `Rs+` and `Rs-` pin backs, without bridging to the neighboring `B-` pin.
3. At the breakout's screw terminal, clamp the resistor ends into `VIN+` and `VIN-`, with C2's two leads clamped in the same two screws so the capacitor sits directly across them.
4. Connect the terminal's middle screw, `VBUS`, to the `B+` pin back (or to the buck's `VIN` joint).
5. Connect the header's `VCC` to XIAO `3V3`, `GND` to the shared ground, `SDA` to `D4` and `SCL` to `D5`. Leave `ALE` unconnected. (Adafruit 5832: the power pin is `VIN`.)
6. Insulate every joint, secure the breakout with Kapton tape or hot glue so nothing can touch the display board, and keep the U.FL antenna against the housing wall.

### Step 5: Check before power

With the shunt cable still unplugged:

- INA228 `VIN+` to `VIN-`: tens of kilohms, not near zero
- INA228 `GND` to display `B-`: continuity
- INA228 `VBUS` to display `B+`: continuity
- display `B+` to `B-`: not a short

### Step 6: Install the firmware

The firmware is installed wirelessly from the ESPHome Device Builder on the trailer's Home Assistant (**Settings > Add-ons > ESPHome Device Builder**, or **ESPHome** in the sidebar). `casita-battery-monitor.yaml` is already there, set for the trailer Wi-Fi with the device's existing API key and OTA password. This is how the running firmware was installed on 2026-10-13; repeat items 4-5 after any configuration change.

1. Plug the shunt cable back into the display. The XIAO powers up.
2. **Move the XIAO to the trailer Wi-Fi** (done 2026-10-13; needed again only if the XIAO is ever flashed with firmware that knows a different network). Firmware that only knows the home Wi-Fi starts its fallback hotspot after about a minute away from home. On a phone, join the **Casita Battery Fallback** hotspot (password: `fallback_ap_password` from the configuration). A setup page opens; if not, browse to `192.168.4.1`, ESPHome's standard hotspot address. Choose the trailer Wi-Fi network, enter its password and save. The XIAO restarts and joins it. If the trailer is parked at home, the XIAO may join the home Wi-Fi instead and no hotspot appears; do this step away from home's Wi-Fi range.
3. In the travel router's admin page, give the XIAO a DHCP reservation so its address never changes.
4. In the Device Builder, open `casita-battery-monitor` and select **Install**, then **Wirelessly**. The **first** build on the trailer's Raspberry Pi 4 took about 25 minutes (it compiles the whole ESP32 framework); later builds take a few minutes.
5. Open **Logs**. The I2C scan should report a device at `0x40`, and the INA228 component should log `Supported device found: INA228`.

> [!IMPORTANT]
> **AP isolation must be off on the travel router.** With it on (or with the XIAO on a guest network), Home Assistant discovers the XIAO through mDNS but every connection fails with `[Errno 113] no route to host`, because the router blocks Wi-Fi clients from talking to each other. Turn **AP Isolation** off for the trailer network in the GL.iNet admin page (**Wireless**); this was the fix on 2026-10-13.

**Home Wi-Fi as a backup network.** The configuration running on the XIAO (in the trailer's Device Builder) lists the trailer Wi-Fi first and the home Wi-Fi as a lower-priority backup, so the XIAO stays reachable instead of falling back to its hotspot if the trailer router is off while parked at home:

```yaml
wifi:
  networks:
    - ssid: !secret wifi_ssid          # trailer Wi-Fi
      password: !secret wifi_password
      priority: 10
    - ssid: !secret home_wifi_ssid     # backup only
      password: !secret home_wifi_password
      priority: 0
```

The committed configuration keeps a single network so it builds with the example secrets; add the block above (and the two `home_wifi_*` secrets) to match the running device.

If the configuration ever needs rebuilding, copy [`esphome/casita-battery-monitor.yaml`](esphome/casita-battery-monitor.yaml) into the Device Builder and fill in `secrets.yaml` (see [Secrets](#secrets)).

### Step 7: Calibrate

The configuration assumes a 500 A / 75 mV shunt (0.00015 ohm). Renogy does not publish the rating, so measure it. **Done 2026-10-14; the result is in the table below the steps.**

1. **Sign.** Turn on a known discharge load. **Current** should be negative. If it is positive, change `current_sign` from `"-1"` to `"1"` and reinstall.
2. **Shunt resistance.** With a steady load of at least 20 A, note the diagnostic **Shunt Voltage** (mV) and the true current: a DC clamp meter on the battery cable is best; the Renogy display (rated about 1%) is a reasonable reference. Calculate:

   `shunt_resistance = Shunt Voltage (mV) / 1000 / true current (A)`

   For example, 3.00 mV at 20.0 A gives 0.000150 ohm. About 0.00015 means a 75 mV shunt; about 0.0001 means a 50 mV shunt. Enter the value with the `ohm` unit, for example `shunt_resistance: 0.000150 ohm`, and reinstall. Check that **Current** now matches the reference within 1%.
3. **Voltage.** Compare **Voltage** with a multimeter across the battery terminals. They should agree within about 0.05 V.
4. **Zero.** With the trailer's loads off, **Current** should read close to 0 A (within about 0.05 A). Anything still powered behind the shunt, such as the fridge or monitors, will show up here as real current.

Result, 2026-10-14, A/C running on the inverter with the trailer otherwise idle (readings are the published 5 s averages, logged every 5 s from Home Assistant):

| Time (UTC) | Shunt Voltage | INA228 Current | Voltage | Renogy display |
| --- | ---: | ---: | ---: | ---: |
| 00:24:10 | 9.97 mV | -67.10 A | 13.43 V | |
| 00:24:15 | 10.09 mV | -67.27 A | 13.40 V | **-67.5 A** |
| 00:24:20 | 10.09 mV | -67.35 A | 13.37 V | |
| 00:24:25 | 10.10 mV | -67.35 A | 13.36 V | |

`10.09 mV / 1000 / 67.3 A = 0.000150 ohm`: a 75 mV shunt, matching the default. The INA228 and the Renogy agree within 0.3%, better than the Renogy's 1% rating can resolve, so `shunt_resistance` was left at `0.00015 ohm` rather than adjusted inside the reference's error. The compressor ran for only about 40 s before the thermostat stopped it; the plateau above was steady to 0.1 A, which is all the measurement needs. After the compressor stopped, the fan and inverter overhead drew about 15 A (200 W). A clamp-meter check at a higher current would tighten this further but is not required.

### Step 8: Set the starting state of charge

The state of charge starts at 100% the first time the firmware runs. Either:

- charge the bank fully and let the automatic resync set 100% (or press **Mark Battery Full** at the end of a full charge), or
- enter the Renogy display's percentage into **Set State of Charge**.

## ESPHome Configuration

The configuration is [`esphome/casita-battery-monitor.yaml`](esphome/casita-battery-monitor.yaml). It uses ESPHome's built-in `ina2xx_i2c` component, so there are no third-party components.

| Substitution | Default | Meaning |
| --- | --- | --- |
| `shunt_resistance` | `0.00015 ohm` | Measured shunt resistance (Step 7) |
| `current_sign` | `"-1"` | Makes charging positive and discharging negative |
| `battery_capacity_ah` | `"600"` | Usable bank capacity: two 300 Ah batteries |
| `charge_efficiency` | `"0.99"` | Fraction of charging amp-hours counted as stored |
| `full_voltage` | `"14.0"` | Voltage at or above which the bank can be declared full |
| `full_tail_current` | `"6.0"` | Charge current (A) at or below which charging has tapered |
| `full_hold_seconds` | `"120"` | How long both must hold before SoC resets to 100% |
| `empty_voltage` | `"11.8"` | Low-voltage floor; `"0"` disables it |
| `empty_max_current` | `"20.0"` | Floor applies only under a light discharge load (A) |
| `empty_soc` | `"5.0"` | SoC (%) the floor caps to |
| `charging_on_current` | `"0.5"` | Net current into the bank (A) at or above which **Charging** turns on (after 10 s) |
| `charging_off_current` | `"0.2"` | Current (A) at or below which **Charging** turns off (after 30 s). The gap between the two stops it flickering around zero |
| `sda_pin`, `scl_pin` | `GPIO5`, `GPIO6` | XIAO `D4`, `D5` |
| `ina228_address` | `"0x40"` | A0 and A1 tied to GND (GODIYMODULES as shipped; Adafruit with A0/A1 open) |

INA228 settings: `adc_range: 0` (plus or minus 163.84 mV, enough for a 500 A shunt at 75 mV or 50 mV), 64-sample averaging, and 1 s updates. Raw 1 s readings stay internal; published voltage and current are 5 s averages.

How state of charge is calculated:

1. The INA228 integrates current into its charge accumulator on every conversion, so short spikes between readings are still counted.
2. Each second, the change in that accumulator (multiplied by `current_sign`) is added to `remaining_ah`. Charging amp-hours are multiplied by `charge_efficiency`. The value is clamped between 0 and `battery_capacity_ah`.
3. `remaining_ah` is saved to flash at most every 10 minutes (`preferences: flash_write_interval: 10min`) and restored after a reboot.
4. Full-charge resync and the low-voltage floor run every 5 seconds.
5. **Charging** is a template binary sensor on the published current with hysteresis (`charging_on_current` / `charging_off_current`) and `delayed_on: 10s` / `delayed_off: 30s`, so a brief load or charge pulse does not toggle it.

The committed configuration is the one running on the XIAO: it was compiled by the trailer Home Assistant's ESPHome Device Builder (ESPHome 2026.9.1) and installed wirelessly on 2026-10-13. The Device Builder copy and this file were compared on the same day and match apart from the secrets.

### Secrets

The configuration references `api_encryption_key`, `ota_password`, `wifi_ssid`, `wifi_password`, `fallback_ap_password`, `web_username` and `web_password`. Copy [`esphome/secrets.example.yaml`](esphome/secrets.example.yaml) into ESPHome's `secrets.yaml` and replace every placeholder. The copy in the trailer's Device Builder has these values filled in already. Generate a new API key with `openssl rand -base64 32`.

## Home Assistant Setup

The device belongs in the trailer's Home Assistant, which runs on the trailer network and so can always reach it.

1. After Step 6, open **Settings > Devices & services**. **Casita Battery Monitor** should appear as a discovered ESPHome device. Select **Add** (or **Configure**) and enter the API encryption key from the configuration if asked.
2. If it is not discovered, select **Add integration > ESPHome** and enter the XIAO's reserved address, port 6053.
3. The serial-tap firmware's **Monitor Online** and **Time Remaining** entities do not exist in the new firmware. If they appear, delete them on the device page.

### Entities

These are the entity IDs as created in the trailer's Home Assistant (confirmed 2026-10-13).

| Entity name | Entity ID | Unit |
| --- | --- | --- |
| State of Charge | `sensor.casita_battery_monitor_state_of_charge` | % |
| Voltage | `sensor.casita_battery_monitor_voltage` | V |
| Current | `sensor.casita_battery_monitor_current` | A (negative = discharging) |
| Power | `sensor.casita_battery_monitor_power` | W (negative = discharging) |
| Charging | `binary_sensor.casita_battery_monitor_charging` | on while net current flows into the bank |
| Remaining Capacity | `sensor.casita_battery_monitor_remaining_capacity` | Ah |
| Time to Empty | `sensor.casita_battery_monitor_time_to_empty` | h (unknown unless discharging) |
| Time to Full | `sensor.casita_battery_monitor_time_to_full` | h (unknown unless charging) |
| Daily Charged Energy | `sensor.casita_battery_monitor_daily_charged_energy` | kWh |
| Daily Discharged Energy | `sensor.casita_battery_monitor_daily_discharged_energy` | kWh |
| Set State of Charge | `number.casita_battery_monitor_set_state_of_charge` | % (configuration) |
| Mark Battery Full | `button.casita_battery_monitor_mark_battery_full` | (configuration) |
| Restart | `button.casita_battery_monitor_restart` | (configuration) |
| Shunt Voltage, INA228 Temperature, Wi-Fi Signal, Uptime | `sensor.casita_battery_monitor_shunt_voltage`, `..._ina228_temperature`, `..._wi_fi_signal`, `..._uptime` | diagnostic |

### Dashboard card

This is the card used on the home Home Assistant's **Casita RV** page (there the entity IDs carry the `rv_` prefix described below). On the trailer's own Home Assistant use the IDs as shown.

```yaml
type: vertical-stack
cards:
  - type: gauge
    entity: sensor.casita_battery_monitor_state_of_charge
    name: Casita Battery
    min: 0
    max: 100
    severity:
      green: 50
      yellow: 25
      red: 0
  - type: entities
    title: Battery
    entities:
      - entity: binary_sensor.casita_battery_monitor_charging
      - entity: sensor.casita_battery_monitor_voltage
      - entity: sensor.casita_battery_monitor_current
      - entity: sensor.casita_battery_monitor_power
      - entity: sensor.casita_battery_monitor_remaining_capacity
      - entity: sensor.casita_battery_monitor_time_to_empty
      - entity: sensor.casita_battery_monitor_time_to_full
      - entity: sensor.casita_battery_monitor_daily_charged_energy
      - entity: sensor.casita_battery_monitor_daily_discharged_energy
```

### Low-battery alert (optional)

Replace `notify.mobile_app_your_phone` with your phone's notify service.

```yaml
alias: Casita battery low
triggers:
  - trigger: numeric_state
    entity_id: sensor.casita_battery_monitor_state_of_charge
    below: 25
    for: "00:05:00"
actions:
  - action: notify.mobile_app_your_phone
    data:
      title: Casita battery low
      message: >-
        Battery at {{ states('sensor.casita_battery_monitor_state_of_charge') }}%
        ({{ states('sensor.casita_battery_monitor_voltage') }} V).
mode: single
```

### Local web page

On the trailer's Wi-Fi, open `http://casita-battery-monitor.local` (or the device's IP address) and log in with the `web_server` username and password. It shows every entity and the **Set State of Charge** and **Mark Battery Full** controls, without Home Assistant.

### Mirroring to the home Home Assistant

Set up 2026-10-13. The trailer's Home Assistant is linked to the home one with the [Remote Home-Assistant](https://github.com/custom-components/remote_homeassistant) custom integration (version 4.6, installed through HACS on both ends) over Tailscale. The home side opens the connection, so it works wherever the trailer has internet; no port forwarding is involved.

- **What is mirrored:** everything in the trailer's Home Assistant except an exclude list. Excluded are the `sun`, `weather`, `zone`, `person`, `device_tracker`, `conversation`, `tts`, `todo`, `notify` and `event` domains, the four backup sensors, the six sun-time sensors, the Raspberry Pi power-status sensor, and this device's **Restart** button. Anything added to the trailer's Home Assistant later appears at home on its own.
- **Naming at home:** entity IDs get an `rv_` prefix and friendly names an `RV ` prefix, so the state of charge is `sensor.rv_casita_battery_monitor_state_of_charge` ("RV Casita Battery Monitor State of Charge") at home. 30 entities were mirrored on 2026-10-13: this device, the Matter test plug, and the trailer's 12 `update.*` entities (core, OS, Supervisor, add-ons, HACS, Pi and ZBT-1 firmware).
- **Control works both ways for what is mirrored:** pressing **Mark Battery Full** or changing **Set State of Charge** at home is forwarded to the trailer. Verified 2026-10-13: a **Mark Battery Full** press at home reached the trailer in about half a second and the new timestamp mirrored back.
- **Rounding at home:** ESPHome's `accuracy_decimals` does not travel with the mirrored entities, so at home each `sensor.rv_casita_battery_monitor_*` entity has its display precision set by hand in the entity settings (voltage 2, current 2, power 0, state of charge 1, capacity 1, hours 1, energy 3, shunt voltage 4). Without this the page shows 13-digit floats. Repeat for any new sensor.
- **Casita RV sidebar page at home:** a dashboard with an **Open Casita Home Assistant** button (opens the trailer's own Home Assistant in a new tab; only devices on the Tailscale network can reach it), the state-of-charge gauge and battery card above, and the 12 trailer update entities. Checked in a browser on 2026-10-13: everything renders and the button opens the trailer's Home Assistant. Installing a trailer update from the home page has not been tried; nothing has been pending yet.
- **Trailer Home Assistant restart:** a controlled Core restart on the trailer (2026-10-13) took about 30 s; the home link reconnected about 50 s after the restart and this device was reporting again at about 60 s, without the XIAO rebooting.
- **Why a button and not an embedded page:** Home Assistant refuses to be shown inside another site's frame (`X-Frame-Options`) unless that protection is turned off, which was left on.
- **Why the ESPHome device itself is not in the home Home Assistant:** see below.

The trailer's Home Assistant remains the place to manage the device (ESPHome Device Builder, firmware installs, logs). The home copy is a mirror.

## Reading the Battery Away From Home

ESPHome's Home Assistant connection is opened **by Home Assistant** to the device on port 6053, so the Home Assistant must be on the same network as the XIAO. That is why the device lives in the trailer's own Home Assistant: the trailer's travel router, its Home Assistant and the XIAO travel together, and the readings keep recording wherever the trailer is.

- **From a phone away from the trailer:** open the trailer's Home Assistant over Tailscale, or use the home Home Assistant's **Casita RV** page.
- **At the campsite:** use the trailer's Home Assistant, or the local web page above, on the trailer Wi-Fi.
- **In the home Home Assistant:** the entities are mirrored there; see [Mirroring to the home Home Assistant](#mirroring-to-the-home-home-assistant). This has only been exercised with the trailer parked at home on the home Wi-Fi; a Starlink or cellular uplink has not been tested yet.

## Testing Checklist

1. Step 2 shows a few millivolts between `Rs+` and `Rs-` under load, with no bias voltage.
2. `VIN+` to `VIN-` on the breakout reads tens of kilohms before wiring.
3. Logs show the INA228 found at `0x40` with no I2C errors.
4. **Voltage** matches a multimeter within about 0.05 V.
5. **Current** has the right sign and matches a clamp meter or the Renogy display within 1% at 20 A or more.
6. **State of Charge** falls steadily under a known load: for example, 10 A for 1 hour should remove about 10 Ah (about 1.7% of 600 Ah).
7. After a full charge, the log shows `Full charge detected` and SoC reads 100%.
8. The Renogy display's current reading is the same as before the INA228 was added.
9. After an hour, the housing, regulator and breakout are no more than slightly warm.

Observed so far (2026-10-13, trailer on shore power at home):

| Item | Result |
| --- | --- |
| 3 | The device is up and reporting; the INA228 is read at `0x40` (the readings would be `unknown` otherwise). The boot log itself was not kept |
| 5 | Discharge reads negative, charge positive (+32 A at 14.1 V while the converter was charging). 2026-10-14: -67.3 A on the INA228 against -67.5 A on the Renogy display at a steady 67 A load, 0.3% apart (Step 7) |
| 7 (manual) | **Mark Battery Full** set the state of charge to 100% after the bank had been on shore power. The automatic `Full charge detected` resync has not been observed yet |
| Charging indicator | Turned on with charge current and off again as it tapered, without flicker |
| Home mirror | Entities, control and the Casita RV page checked from the home Home Assistant; survived a trailer Home Assistant restart (see [Mirroring](#mirroring-to-the-home-home-assistant)) |
| INA228 Temperature | About 66 °F inside the housing at low current; no long high-current run yet |
| 8 | The Renogy display read -67.5 A with the INA228 connected, consistent with the load; no change in its behaviour noticed |
| 1, 2, 4, 6, 9 | Not recorded |

## Troubleshooting

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| No device at `0x40` in the I2C scan | SDA/SCL swapped, no power to the breakout, or the address pads changed | Check `D4`=SDA, `D5`=SCL and 3.3 V on `VCC`. If the scan shows another address, either set `ina228_address` to it or re-bridge A0/A1 to `G` |
| Logs say the device is not an INA228 | Clone module with an INA226 | Use a genuine INA228 breakout |
| Current reads about 0 A under load | Onboard shunt still fitted, sense wires not connected, or a filter resistor open | Check continuity from `Rs+`/`Rs-` to `VIN+`/`VIN-` through the 10 ohm resistors |
| Current is far too small and the Renogy display changed too | The breakout's onboard shunt is still fitted | Remove it (see Prepare the INA228) |
| Current sign is backwards | `Rs+`/`Rs-` order | Flip `current_sign` |
| Current off by a fixed percentage | `shunt_resistance` not calibrated | Repeat Step 7 |
| Voltage reads 0 or very low | `VBUS` not connected to `B+` | Wire `VBUS` to the `B+` pin back |
| SoC never returns to 100% | Charger never meets the full-charge conditions | Lower `full_voltage` to just below your charger's absorption voltage, or press **Mark Battery Full** after a full charge |
| SoC drifts high over days | XIAO and display draw are not metered | Expected; the full-charge resync corrects it |
| XIAO resets or drops Wi-Fi | Supply sags during Wi-Fi bursts | Check the regulator and C1 |
| XIAO not on the network after power-up | Still running firmware with the home Wi-Fi | Use its fallback hotspot (Step 6, item 2) |
| Home Assistant discovers the device but **Add** fails with `connection_error` / `[Errno 113]` | AP isolation on the travel router, or the XIAO on a guest network | Turn AP Isolation off for the trailer network (Step 6) |

## Safety Notes

- Always unplug the shunt cable from the display before soldering inside it. The display is powered from the battery through `B+`, which should be fused close to the battery.
- Never connect the sense wires to an INA228 that still has its onboard shunt.
- Do not bridge the solder joints on the connector pin backs; `Rs+`, `Rs-` and `B-` sit next to each other.
- Never connect anything inside the housing to the trailer's 12 V negative or to a USB device while installed. The shunt cable is the only wired connection.
- Insulate every joint. A short from `B+` inside the housing is limited only by the `B+` fuse.
- Opening the display almost certainly voids Renogy's warranty on it.

## Photos

Add photos to `photos/` as the build progresses:

- `rbm500-board-back.jpg`: the display board before modification
- `ina228-shunt-removed.jpg`: the breakout with its onboard shunt removed
- `inside-housing.jpg`: the XIAO, regulator, INA228 and wiring inside the housing
- `installed.jpg`: the finished display installed in the trailer

## References

- [TI INA228 datasheet](https://www.ti.com/lit/ds/symlink/ina228.pdf): input range, filtering (10 ohm series resistors, 0.1-1 uF capacitor), VBUS and address table
- [GODIYMODULES INA228 module (Amazon B0GX5HM4X3)](https://www.amazon.com/dp/B0GX5HM4X3): the board used here; 2 mohm `R002` shunt, pinout and address pads from the listing photos and schematic
- [Adafruit INA228 guide](https://learn.adafruit.com/adafruit-ina228-i2c-power-monitor): onboard 15 mohm shunt, VBUS jumper, pinout
- [ESPHome INA2xx component](https://esphome.io/components/sensor/ina2xx/)
- [Renogy RBM500 product page](https://www.renogy.com/products/500a-battery-monitor-with-shunt) and [G3 manual](https://cdn.shopify.com/s/files/1/0631/0137/0483/files/RBM500-G3-Manual_26f37388-12d7-442a-99e6-77ee6e79f8bf.pdf)
- [edillmann/esphome-tf03k-smart-shunt](https://github.com/edillmann/esphome-tf03k-smart-shunt): TF03K serial protocol (for meters that have it). [Issue #1](https://github.com/edillmann/esphome-tf03k-smart-shunt/issues/1) shows the same TF03H V35 board without the module, unanswered
- [Seeed Studio XIAO ESP32-S3 wiki](https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/)

## Revisions

| Date | Change |
| --- | --- |
| 2026-10-08 | Serial-tap design: XIAO inside the display housing reading the display's serial output (built; did not work) |
| 2026-10-09 | Serial output proven absent on the TF03H V35. Redesigned around an INA228 measuring the shunt sense pair, with software state-of-charge tracking (not yet built) |
| 2026-10-13 | ESPHome moved to the trailer's own Home Assistant; configuration set for the trailer Wi-Fi. INA228 board chosen: GODIYMODULES module (B0GX5HM4X3). Board preparation, wiring steps and diagrams updated for its `R002` shunt, pinout and address pads |
| 2026-10-13 | INA228 wired and the firmware installed wirelessly; the device is live in the trailer's Home Assistant. Added the **Charging** binary sensor (hysteresis plus on/off delays). Trailer entities mirrored to the home Home Assistant with Remote Home-Assistant over Tailscale and a **Casita RV** sidebar page added there. Calibration (Step 7) still to do |
| 2026-10-13 | Corrections: why the onboard shunt must go (with the 10 ohm resistors it makes the INA228 read about 0 A); genuine INA228 marking `228I`; C1 was never fitted in the serial-tap build, 220 uF 25 V added, 25 V minimum; travel-router AP isolation must be off; home Wi-Fi backup network; first Device Builder build time |
| 2026-10-14 | Calibrated: 67.3 A (INA228) against 67.5 A (Renogy display) at a steady A/C load; shunt confirmed 500 A / 75 mV, `shunt_resistance` kept at `0.00015 ohm` |
