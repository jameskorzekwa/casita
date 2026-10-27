# Propane Sensors (DYP L06 under the 20 lb cylinders)

Part of [mod 07, the tank monitor](README.md). This guide covers the two propane sensors: choosing them, proving they read through the cylinder, the magnetic collars, mounting and calibration. The ESP32 that reads them is the tank monitor's **main device** (`casita-tank-monitor`), which also reads the grey tank sensor; its wiring, firmware, installation and Home Assistant setup are in the [README](README.md).

Two DYP L06 ultrasonic liquid-level sensors, one held magnetically against the bottom of each 20 lb propane cylinder. Every minute the main device wakes each sensor, reads the liquid height through the steel tank wall, converts it to a percentage and pounds remaining, and publishes everything to Home Assistant over Wi-Fi. The sensors take their power from the main device, so **there are no batteries to replace**.

> [!IMPORTANT]
> **Status: designed, not built (updated 2026-10-27).** Both DYP-L06 (UART Controlled) sensors were ordered from Amazon on 2026-10-12; Amazon shows them delivered 2026-10-27. Check the label on each says **L062MTW** before anything else. The combined ESPHome configuration compiles but has not run on hardware, and no L06 has been tried on a Casita cylinder yet. Bench-test one sensor (Steps P1-P4) before mounting either.
>
> **Mounting:** DYP's documented method is epoxy, which ties the sensor to one cylinder. This project mounts the sensor in a small **magnetic collar** with silicone grease as the couplant instead, the same way Mopeka and Safiery hold their ultrasonic sensors on the same spot, so a sensor moves to a new cylinder in a minute. The collar is **not tested on an L06 yet**; the epoxy method stays as the fallback (Step P5b).

**Contents:** [What to order](#what-to-order) · [Why this design](#why-this-design) · [How it works](#how-it-works) · [Known limitations](#known-limitations) · [Parts](#parts) · [Sensor wiring](#sensor-wiring) · [Steps](#steps) · [Testing](#testing-checklist) · [Troubleshooting](#troubleshooting) · [Safety](#safety-notes)

## What to order

### The sensor: DYP-L062MTW-V1.0, and only that model

The L06 comes in four versions that look identical. Only one is right for this project:

| Model | Interface | Order? |
| --- | --- | --- |
| **DYP-L062MTW-V1.0** | **UART, controlled** (sleeps until the ESP32 sends a byte) | **Yes. This one.** |
| DYP-L062MUW-V1.0 | UART, automatic (streams readings all the time) | No |
| DYP-L062MCW-V1.0 | I2C | No: I2C is not reliable over the 3 m cable runs, and both sensors would share one bus with the same default address |
| DYP-L062M4W-V1.0 | RS-485 Modbus | No: needs transceivers; nothing here speaks RS-485 |

**Why UART controlled:** each sensor gets its own UART on the ESP32 (one failing cannot affect the other), the 115200 baud serial is fine over 3 m of shielded cable, the protocol is one byte out and ten bytes back, and the sensor sleeps at under 15 uA between readings.

### Ordering checklist

Order **one sensor first**, bench-test it (Steps P1-P4), then order the second if it works.

1. **Easiest: Amazon.** [DYP-L06 ... (UART Controlled, 1)](https://www.amazon.com/dp/B0C1GHF2M8), about $25 (seen 2026-10-13). On the listing, the **Size** option must say **UART Controlled**, not **IIC**. The listing carries DYP's own spec text (sleep current under 15 uA, 115200 baud, 3 cm blind zone), which is the UART-controlled model, but it does not say whether the couplant/EVA/epoxy kit or mating cables are included, and the brand shows as "Generic". Message the seller to ask, or just buy the [mating cables](#parts) and grease separately (both are on the parts list; the kit is only needed for the epoxy fallback).
2. **Or direct from DYP** (confirms the exact model and the propane setting, slower): the [DYP product page](https://www.dypcn.com/dyp-l06-gas-tank-lpg-level-measuring-sensor-product/) has a **Send email to us** button, or use DYP's Alibaba store (`dypsensor.en.alibaba.com`) or a distributor such as [Evelta](https://evelta.com/l06-ip67-waterproof-ultrasonic-lpg-gas-level-measuring-sensor-3-100cm/). Send this message, copied as-is:

   > Hello, I would like to order **1 x DYP-L062MTW-V1.0** (L06 liquefied gas level sensor, **UART controlled output**, TTL level, 115200 baud). Please confirm:
   >
   > 1. Measuring medium configured for **propane (LPG)**, steel cylinder wall 2-3 mm thick.
   > 2. Include the **installation kit** (ultrasonic couplant, double-sided EVA ring, AB glue).
   > 3. Include **2 x mating cables** for the sensor's white 1.25 mm 4-pin connector, at least 30 cm long with bare wire ends (or tell me the connector part number so I can buy them).
   > 4. A link to the current L06 datasheet and the Windows "Sensor Assistant" software.
   >
   > Shipping to the USA. Thank you.

3. When it arrives, check the label on the sensor says **L062MTW** (not MUW, MCW or M4W) before doing anything else. If it is the wrong model, do not try to make it work; return or exchange it.
4. Order the rest of the [Parts](#parts) list at the same time; every row has an Amazon link. Skip the second sensor until the first has passed the bench test. (Both were in fact ordered together on 2026-10-12.)

## Why this design

The requirement was tank level in Home Assistant with no batteries to maintain. The usual RV products do not meet it:

| Option | Power | Home Assistant | Verdict |
| --- | --- | --- | --- |
| Mopeka Pro Check / Pro Check Universal | CR2032 or similar coin cell, 1-2 years | Native Bluetooth integration | Simplest, but batteries |
| Mopeka Pro Plus | 2 x AAA lithium | Native Bluetooth integration | Batteries |
| Gaslock GASLEVEL with external display | 12 V | Wired LED only; no data output | Threshold (above/below the sensor) only, no percentage |
| Safiery magnetic LPG sensor (LPG05080001-A) | 12 V | 0-5 V analog; needs an interface | Real option; about A$183 each plus a preprocessor, designed for Victron GX |
| **DYP L06 (this project)** | **3.3-5 V from the ESP32** | **Serial data, read directly by ESPHome** | **Chosen: cheapest, digital output, continuous level; mounted magnetically like the Mopeka** |

The L06 is an OEM sensor module made for exactly this job (bottom-mounted, non-contact LPG level through a steel wall, with built-in temperature compensation), not a finished consumer product. This project supplies the rest: power, mounting, wiring, firmware and the Home Assistant side.

## How It Works

1. The sensor is mushroom-shaped: a 33.8 mm flange that holds the electronics and the cable, with a 17.5 mm boss standing 7.9 mm off one face. **The boss face is the probe.** The sensor sits in the recess inside the cylinder's foot ring, at the center of the domed bottom, boss face pressed against the steel through a thin film of silicone grease by three magnets in a collar around the boss (or, as the fallback, bonded with DYP's couplant and two-part epoxy). It fires a high-frequency ultrasonic pulse through the steel into the liquid propane and times the echo from the liquid surface. Propane vapor above the liquid returns almost no echo, so the first strong echo marks the liquid height.
2. The ESP32 sends one byte to the sensor's `RX` lead. That wakes the sensor (it sleeps at under 15 uA otherwise), it measures once (about 730 ms) and replies on `TX` with a 10-byte frame: liquid height in mm, temperature, echo strength and tilt angle, with a checksum. ESPHome parses the frame and publishes the values.
3. Percentage = liquid height / "Full Level". Full Level is a per-cylinder calibration number stored on the ESP32, set once by pressing **Mark Full** on a freshly filled cylinder. Pounds remaining = percentage x 20 lb.
4. If the liquid is below the sensor's 30 mm blind zone the sensor reports "no liquid" (`0xFFFD`). The firmware shows that as 0 mm / 0%, and the **Liquid Detected** diagnostic turns off. A near-empty 20 lb cylinder still has roughly 1-2 lb of propane at that point, so the low-propane alert should fire well above 0%.

Everything is powered from the trailer through the main device: 12 V from a fused circuit to a 5 V buck regulator, 5 V to the XIAO, and the XIAO's 3.3 V output to both propane sensors and the grey tank sensor. The sensors' serial lines are 3.3 V when they are powered at 3.3 V, which is what the ESP32 needs. Each propane sensor has its own hardware UART, so one failing cannot affect the other or the grey tank.

## Known Limitations

- **The magnetic collar is this project's design, not DYP's.** DYP only documents epoxy. Mopeka's magnetic sensors mount in the same spot with the same kind of grease couplant, which is reassuring about the physics and the geometry, but the L06 has not been tested on a US DOT 20 lb cylinder with either method. The foot-ring recess depth and the surface at the center of the dome are the two things to check in Steps P1 and P4, and echo strength after the first tow is the proof that the collar holds.
- **Grease needs refreshing.** Silicone grease does not dry out, but it should be renewed whenever the sensor is moved and about yearly. A falling **Echo Strength** reading is the signal.
- **Exchanged cylinders still need a minute of work:** move the collar, wipe the dome, fresh grease, check echo strength, press **Mark Full** on the next proper fill. With the epoxy fallback the sensor stays with the old cylinder.
- **The bottom 30 mm is invisible.** Below about 30 mm of liquid the sensor reports nothing. Treat "0%" as "under about 1-2 lb".
- **Percent is linear in height.** The cylinder's domed bottom and shoulder mean the true volume per millimeter is lower near the ends. Readings are honest at full and near empty (the calibration points) and a little pessimistic in the middle. That is fine for "time to refill".
- **Level moves with temperature.** Liquid propane expands about 0.15% per degC, so a tank reads a few percent higher on a hot afternoon than on a cold morning with no gas used. The sensor's temperature entity shows why.
- **Temperature range.** DYP guarantees accuracy from 0 to 35 degC and operation from -10 (or -15, the datasheet says both) to 60 degC. Under a black tank cover in Texas sun the tank bottom may exceed 60 degC; expect odd readings then. Below -10 degC in winter the sensor may stop reading until it warms up.
- **Not a certified hazardous-location device.** The sensor runs at 3.3 V and under 50 mA and the ESP32 lives inside the trailer, but nothing here carries an intrinsic-safety rating. See Safety notes.
- **Tilt.** The sensor reports its tilt; a tank leaning more than a few degrees reads low. The trailer should be level anyway.
- **Always on.** The main device draws roughly 50-100 mA from 12 V with Wi-Fi on, about 1-2.5 Ah per day from the 600 Ah bank, shared with the grey tank. See the [README](README.md#power).
- **Away from home** the Home Assistant connection needs a network path, the same as the battery monitor: see [mod 04](../04-battery-monitor-esp32/README.md#reading-the-battery-away-from-home).

## Parts

| Component | Qty | Notes | Purchase link |
| --- | ---: | --- | --- |
| DYP-L062MTW-V1.0 LPG level sensor (UART controlled) | 2 | **See [What to order](#what-to-order): the exact model and what to check.** About $25 each on Amazon; choose the **UART Controlled** size option, not IIC | [Amazon](https://www.amazon.com/dp/B0C1GHF2M8), or [DYP direct](https://www.dypcn.com/dyp-l06-gas-tank-lpg-level-measuring-sensor-product/) |
| Magnetic collar (3D-printed, ASA or PETG, 100% infill) | 2 | Ring that sits on the sensor's flange around the 17.5 mm probe boss, with three magnet pockets on the tank face and a cable notch; drawing in Step P5a. Print one and test-fit before printing the second | |
| Neodymium disc magnets, 8 mm x 3 mm, N42-N52 | 6 (3 per collar) | About 1 kg pull each; nickel plated. Glued into the collar pockets with CA or epoxy, faces flush with the collar. Smallest sensible pack is far more than 6 | [Amazon: LiftSun N42 8x3 mm, 100 pack](https://www.amazon.com/dp/B0GFCBFKKQ) |
| Silicone dielectric grease (couplant) | 1 tube | Any silicone dielectric grease; Mopeka's "Sonic Grease" is the same idea in single-use sachets. Not DYP's water-based gel, which dries out | [Amazon: Permatex 22058, 3 oz](https://www.amazon.com/dp/B000AL8VD2) or [Amazon: Mopeka Sonic Grease, 4 packets](https://www.amazon.com/dp/B0CVQVGMWB) |
| 4-conductor shielded cable, 22 AWG | About 2 x 3 m (25 ft roll, shared with the grey tank) | Sensor leads are only 140 mm; this runs from the main device to each cylinder. Shield grounded at the ESP32 end only | [Amazon: 22/4 shielded, tinned stranded, 25 ft](https://www.amazon.com/dp/B0D9JY3MC4) |
| 1.25 mm pitch 4-pin mating cables for the sensor connector | 2 (pack of 20 pairs) | "Micro JST 1.25 mm" pigtails are the usual match for the sensor's white 1.25 mm connector, to confirm on the first sensor. The female half mates with the sensor's plug and is soldered to the long cable; that joint is the disconnect point at each tank. Buy once, use two | [Amazon: Micro JST 1.25 mm 4-pin, 20 pairs, 150 mm](https://www.amazon.com/dp/B09DYLY95R) |
| Cable gland (PG7) and sealant | 1-2 | Where the sensor cables pass through to the tongue | [Amazon: PG7 nylon glands, 50 pack](https://www.amazon.com/dp/B0CTCG4HMM) |
| Heat-shrink (adhesive-lined), Kapton tape, zip ties | As needed | | [Amazon: 3:1 adhesive-lined heat-shrink kit](https://www.amazon.com/dp/B0DC5YN5CD), [Amazon: Kapton tape 10 mm, 4 rolls](https://www.amazon.com/dp/B07S227ZLH) |

The XIAO, regulator, capacitor, fuse and enclosure are the main device's, listed in the [README](README.md#parts). Ownership and purchase status for everything: [components.md](components.md).

Amazon links checked on 2026-10-13; prices then were roughly: sensor $25, magnets $18, grease $10, cable $17, pigtails $9, glands $10, heat-shrink $10, Kapton $10.

## Tools and Supplies

- Fine-tip soldering iron, solder, flux
- Multimeter with continuity
- Isopropyl alcohol (99%, [Amazon](https://www.amazon.com/dp/B08CGVVYWV)) and lint-free cloths for cleaning the tank bottom
- Small digital scale or bathroom scale (to weigh cylinders for calibration)
- A level for checking the tank

## Sensor wiring

Each sensor's four leads go to the main device. The full schematic, with the grey tank sensor and the power supply, is in the [README](README.md#main-device-wiring).

| Sensor lead | Propane 1 | Propane 2 | Notes |
| --- | --- | --- | --- |
| red `VCC` | XIAO `3V3` | XIAO `3V3` | 3.3 V, so the serial lines are 3.3 V |
| black `GND` | XIAO `GND` | XIAO `GND` | Cable shield to `GND` at the ESP32 end only |
| yellow `RX` (into the sensor) | XIAO `D6` (GPIO43) | XIAO `D4` (GPIO5) | ESP32 transmits the wake-up byte |
| green `TX` (out of the sensor) | XIAO `D7` (GPIO44) | XIAO `D5` (GPIO6) | ESP32 receives the 10-byte frame at 115200 baud |

Lead colors from the DYP datasheet. The ESP32's TX goes to the sensor's RX and vice versa.

### Where things go

- **Sensors:** under each cylinder, inside the foot ring, at the center of the domed bottom, in their magnetic collars. The sensor's own 140 mm lead ends in a small white 1.25 mm plug; that plug, mated to a pigtail from the parts list, is the disconnect point and sits just outside the foot ring. The pigtail is soldered to the long cable, which exits through one of the foot ring's drain notches and is zip-tied up the cylinder's side under the tank cover, with enough slack to lift the cylinder out. Unplug the little connector to take a cylinder out or move the sensor to a new one; nothing gets cut.
- **Cables to the main device:** through the front wall from the tongue, through an existing grommet (the propane line and 7-way harness come through somewhere nearby) or a new sealed gland. **To confirm:** find the pass-through. Keep each run under about 3 m; the main device's spot is chosen in [Step M1](README.md#step-m1-pick-the-main-enclosure-spot-and-measure-the-runs).

## Steps

Do them in this order, alongside the main device steps in the [README](README.md#build-order). Steps P1-P4 use one sensor and prove the idea before anything is printed, mounted or installed in the trailer.

### Step P1: Measure the cylinder

Close the valve, lift one cylinder out of the tray and set it on blocks or its side so you can see the bottom.

1. Lay a straightedge across the bottom of the foot ring and measure from it up to the center of the domed bottom. That is the recess depth.
2. The sensor is 12.1 mm tall and 33.8 mm across; the collar adds nothing to the height and is 44 mm across. You need **at least about 15 mm** of recess so the cylinder still stands on its foot ring and nothing presses on the sensor. Also check the foot ring has a drain notch or gap the cable can leave through.
3. Note the recess depth in the README's [Revisions](README.md#revisions). Less than 15 mm: stop and rethink (a cylinder with a taller foot ring, or a tray spacer).

### Step P2: Wire one sensor to the main XIAO on the bench

The main device's XIAO, on the bench. No regulator or trailer wiring yet; the XIAO can run from its USB-C port for this.

1. Plug a **female** Micro JST 1.25 mm pigtail into the sensor's white plug. Note which pigtail wire lands on each sensor wire (red, black, yellow, green); the pigtail colors will not match.
2. Solder the pigtail's four bare ends to the XIAO pads. The pad names are printed on the board:

   | Sensor wire | XIAO pad |
   | --- | --- |
   | red (VCC) | `3V3` |
   | black (GND) | `GND` |
   | yellow (sensor RX) | `D6` |
   | green (sensor TX) | `D7` |

   Solder to the pads directly or fit the XIAO's header pins and use the matching sockets; either is fine. Header pins make it easier to add the second propane sensor and the grey tank sensor later. Keep the pigtail's wire order written down for Step P6.
3. Fit the U.FL antenna to the XIAO.

### Step P3: Flash the main device

Follow [Step M2](README.md#step-m2-flash-the-main-device) in the README: it puts `casita-tank-monitor.yaml` and its propane package on the trailer's ESPHome Device Builder and flashes the XIAO.

Then open **Logs**. Once a minute you should see `propane1` log a line like `level=none ... echo=0 mV` (the sensor is in the air) and `propane2` log `No valid frame` (nothing is connected yet); after 30 s the grey tank logs `No frame from the L02 for 30 s` until its sensor is connected. That is correct for now. If `propane1` also says `No valid frame`, check the four solder joints from Step P2. The device's web page (`http://casita-tank-monitor.local`) is the tool for the next steps.

### Step P4: Bench-test the sensor on a cylinder

The go / no-go test. It needs the cylinder from Step P1 **at least a third full**: the sensor needs more than 10 cm of liquid above it to read reliably.

1. Clean the center of the dome with isopropyl alcohol.
2. Put a pea-sized blob of silicone grease on the face of the sensor's raised 17.5 mm boss (the probe; the wide 33.8 mm flange with the cable is the back and never touches the tank) and spread it to cover the face. (This is the same coupling the collar provides later, so a good reading here means the collar will work.)
3. Press the sensor by hand onto the center of the dome, boss face to the steel, and press **Read Propane Now** on the web page a few times. **Propane 1 Liquid Level** should show a plausible height in millimeters and **Propane 1 Echo Strength** should be well above zero; DYP's examples show about 1,500 mV at a good spot.
4. Slide the sensor around the center a few millimeters at a time. The spot with the highest echo strength and a level that stays within a few millimeters between readings is the installation spot. Mark it with a paint pen or a scratch in the dirt line so you can find it in Step P6.
5. If the echo is weak or the level jumps around everywhere, try a cleaner spot. If it never settles, the sensor does not read through this cylinder; stop here rather than buying more parts.
6. Weigh the cylinder (propane weight = scale weight minus the tare weight stamped `TW` on the collar) and write down the weight next to the height reading. This is the first calibration point.

Passed? **Order the second sensor now** and go on.

### Step P5a: Make the magnetic collars

![Magnetic collar](images/magnetic-collar.svg)

The sensor (datasheet section 1.6) is a 33.8 mm x 4.2 mm flange with a 17.5 mm boss standing 7.9 mm off one face, 12.1 mm overall, cable out of the flange edge. The boss face is the ultrasonic probe and is the side that goes against the tank; DYP's own EVA ring goes over the boss onto the flange face and the couplant goes on the boss face inside the ring (installation instruction 5.2-5.8). The flange is the back.

The collar is a 44 mm ring, 11.8 mm thick, that does the EVA ring's job with magnets instead of adhesive. The sensor goes in from the back: the flange drops into a 34.2 mm x 4.2 mm recess in the back face and the boss passes through an 18.5 mm bore to the tank face. The shoulder between the recess and the bore is 7.6 mm thick, so the 7.9 mm boss face stands about 0.3 mm proud of the three 8 x 3 mm magnets set flush in the tank face. The magnets pull the collar to the steel, the shoulder pushes on the flange, and the boss face is pressed into the grease film first; the magnets stop just short of the steel. A notch through the back wall lets the cable out.

1. Print one collar (ASA or PETG, 100% infill, 0.2 mm layers, tank face down so the magnet pockets are on the bed) and test-fit: the boss should slide through the bore and the flange should drop into the recess without force, and the boss face should sit just proud of the tank face. Measure the real part first: if the boss is not 7.9 mm tall or its face is domed, change the shoulder thickness so the face still stands about 0.3 mm proud. Then print the second.
2. Glue the three magnets into their pockets with CA or epoxy, **all with the same pole facing out** (stack the magnets first; they will all be oriented the same way, then slide them off one at a time). Faces flush with the ring. Let it cure.
3. Put the sensor into the collar from the back, boss first through the bore, cable through the notch. Two dabs of CA where the flange edge meets the recess wall keep it from dropping out of the back when the collar is off the tank.

**No 3D printer?** The minimum version is three stacks of magnets glued to the flange face around the boss at 120 degrees, each stack built up to about 0.3 mm short of the boss face (two 8 x 3 mm magnets on a 1.5 mm steel washer is about 7.5 mm), with grease on the boss face. It holds less well and is harder to get square; try the collar first.

### Step P5b (fallback only): Epoxy

Use DYP's documented epoxy method ([installation instruction](../../manuals/propane/dyp-l06-lpg-level-sensor-installation-instruction.pdf)) only if a collar will not hold on your cylinders or the echo strength through a grease film is poor. This ties the sensor to one cylinder: refilled cylinders only.

1. Clean the spot with isopropyl alcohol: no dirt, rust, water or loose paint. Wipe the sensor face clean of grease.
2. Stick the double-sided EVA ring to the sensor (bottom release paper only).
3. Mix the AB epoxy for at least 30 seconds and spread it over the whole center face of the sensor, no gaps.
4. Peel the top release paper, press the sensor onto the spot and hold for a moment. Check the reading on the web page again: it must still show the same level and echo strength. At 25 degC the epoxy sets in 5-10 minutes and is fully cured after an hour; longer when cold.

### Step P6: Mount the sensors on the cylinders

For each cylinder, valve closed and lifted out of the tray:

1. Make the long cable: solder a **female** Micro JST pigtail to one end of a 3 m length of the shielded 4-conductor cable, matching the wire order you wrote down in Step P2 (red, black, yellow, green). Heat-shrink each joint and the whole junction. Leave the other end bare for now. Mark the cable "1" or "2".
2. Wipe the spot found in Step P4 with isopropyl alcohol. Put a pea-sized blob of silicone grease on the boss face and spread it to cover the face; no air pockets.
3. Press the collar onto the spot, give it a small twist to spread the grease, and check the reading on the web page (the sensor is on the bench XIAO for now, or on the installed main device after [Step M3](README.md#step-m3-install-the-main-device)): level and echo strength should match the Step P4 reading. If echo strength is much lower, lift it off, re-grease and try again.
4. Plug the sensor's lead into the pigtail. Slide a short piece of adhesive heat-shrink over the mated connectors, or wrap them in self-fusing silicone tape, to keep water out; this is the disconnect point and is cut off to unplug.
5. Route the cable out through the foot ring notch and zip-tie it up the side of the cylinder, leaving a loop of slack, then put the cylinder back in the tray.

**Moving a sensor to a new cylinder:** unplug at the connector, pull the collar off, wipe both surfaces, fresh grease, and repeat steps 2-5. Press **Mark Full** on the next full fill.

### Step P7: Calibrate

The main device is installed and in Home Assistant ([Steps M3 and M4](README.md#step-m3-install-the-main-device)).

1. With a cylinder freshly filled (a proper 80% fill by weight, not an exchange cage's partial fill), wait for the reading to settle and press **Propane N Mark Full**. The current height becomes that cylinder's **Full Level** (stored in the ESP32's flash; also editable as a number). Until then Full Level is the default 280 mm, an **assumed** value, so percentages are approximate.
2. Over the next refill cycle, weigh the cylinder a few times and compare pounds on the scale against **Propane N Remaining**. Expect agreement within about 10% except near empty.
3. Each cylinder has its own Full Level; calibrate each on its own fill.

## Firmware and Home Assistant

The propane sensors are read by the main device's configuration, [`esphome/casita-tank-monitor.yaml`](esphome/casita-tank-monitor.yaml), which includes [`esphome/packages/dyp-l06-propane.yaml`](esphome/packages/dyp-l06-propane.yaml) once per cylinder. How a reading works (`read_propaneN` script): flush the UART receive buffer, send one byte (`0x55`), wait 900 ms, read everything received, find the last 10-byte frame that starts with `0xFF` and whose last byte equals the low 8 bits of the sum of the other nine, then decode it. The frame layout and worked example are in the package file's header comment, copied from the DYP datasheet (section 2.2). Three consecutive bad or missing frames set the cylinder's entities to unknown.

Entities, the dashboard card and the low-propane alert are in the README's [Home Assistant setup](README.md#home-assistant-setup).

## Testing Checklist

1. Bench: with the sensor pressed on a part-full cylinder with grease, **Liquid Level** is steady within a few millimeters across ten readings and **Echo Strength** is well above zero.
2. Bench: lifting the sensor off the tank makes **Liquid Detected** turn off and the level read 0 within three readings; putting it back restores the reading.
3. After mounting in the collar, the level and echo strength match the hand-held Step P4 reading.
4. 3.3 V at each sensor's red lead; XIAO and regulator only slightly warm after an hour.
5. Weigh a cylinder: pounds from the scale (gross minus `TW`) agree with **Propane Remaining** within about 10% after Mark Full.
6. Reading survives a tow: level and echo strength are the same before and after a trip, and the collar has not moved on the dome (checks that the magnets and grease hold and the cable connectors are tight). Repeat after the first long or rough trip.
7. A full-to-empty cycle on one tank shows a steady decline and the low-propane alert fires once at 20%.

## Troubleshooting

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| `No valid frame (0 bytes received)` every reading | Sensor not powered, TX/RX swapped, or broken cable | Check 3.3 V at the red lead, that ESP32 TX goes to sensor yellow and sensor green goes to ESP32 RX, continuity through the connectors |
| `No valid frame (n bytes received)` with n > 0 | Baud rate or checksum problem; noise on a long cable | Confirm the sensor was supplied at 115200 baud; shorten or shield the cable; try the other cylinder's port to separate sensor from wiring |
| Liquid Detected off and Echo Strength near 0 on a tank you know has gas | Sensor not coupled: grease film dried or squeezed out, collar moved, dirt under it, or (epoxy) a gap | Pull the collar, clean, fresh grease, re-seat; if the collar keeps moving, add a strip of foam under it or fall back to epoxy |
| Liquid Detected off, Echo Strength normal | Less than 30 mm of liquid | The tank is nearly empty |
| Level jumps between two values | Sensor near the edge of the dome, or the tank is tilted | Check Tilt; re-position closer to the center |
| Percentage over 100% after a fill | Full Level is too low (different fill level than last time) | Press Mark Full again on the new fill |
| Readings drift a few percent over the day with no use | Thermal expansion of the propane | Expected; compare readings at similar temperatures |
| Entities unknown after a tow | A connector pulled apart | Re-connect; add strain relief |

### Troubleshooting extras

**DYP Sensor Assistant (Windows) with a USB-to-TTL adapter.** Not needed for the build; the ESPHome firmware already shows echo strength and level. It becomes useful if:

- a cylinder gives a weak or jumpy reading and you want to see the actual echo waveform to tell a bad spot from a bad sensor (DYP's installation instruction shows what good and bad look like);
- a sensor arrives at the wrong baud rate or address (every read logs `No valid frame` with some bytes received) and you need to reset it;
- you want DYP's "installation mode", which grades the spot 0-9 and reports the adaptive-media result.

You need a Windows PC, a 3.3 V USB-to-TTL adapter such as the [DSD TECH CP2102, 2 pack](https://www.amazon.com/dp/B078W5L8W1) (about $12), and the Sensor Assistant download from DYP (ask them; the install instruction shows version 1.0.3.x). Wire sensor red to the adapter's **3.3 V** (not 5 V), black to GND, yellow (sensor RX) to the adapter's TXD, green (sensor TX) to RXD. Open the port at 115200 and use the waveform tab. Whether the UART-controlled model answers the tool's Modbus commands for installation mode is to confirm; the waveform view is the main point.

## Safety Notes

- Propane is heavier than air and collects low. The sensors are low-voltage (3.3 V, under 50 mA) and have no switching contacts, but they are not certified intrinsically safe and neither is anything else here. Keep the ESP32, regulator and all connectors inside the trailer or well away from the regulator, pigtails and valve area; never put an open connector or the ESP32 enclosure inside the tank cover.
- Turn both cylinder valves off before working under the tanks, and lift cylinders out to fit the sensors rather than working under a tank in the tray.
- Do not drill, grind or heat the cylinders. The sensor is held by magnets (or, as the fallback, adhesive) only.
- Neodymium magnets are brittle and snap together hard; keep them away from fingers, cards and the ESP32 when loose. Silicone grease is harmless to the cylinder's paint. If using the epoxy fallback, DYP's AB adhesive and gel are consumer products; read their labels and do not substitute a solvent-based adhesive that could attack the paint.
- Fuse the 12 V feed at 2 A close to the source. The regulator and XIAO draw well under 0.5 A.
- A sensor under the cylinder does not change its DOT status, but a refill station may ask about it. It is a passive sensor; be ready to say so, and with the collar it lifts off in seconds if asked.
- The Safe-T-Alert LP/CO detector in the trailer remains the leak protection; this project only measures level.

## Photos

Add photos to `photos/` as the build progresses:

- `cylinder-recess.jpg`: the foot ring recess with a ruler, from Step P1
- `bench-test.jpg`: sensor held on the cylinder with grease, web page in view (Step P4)
- `collar.jpg`: the printed collar with magnets, sensor fitted
- `sensor-mounted.jpg`: the sensor on the dome with the cable routed out of the foot ring
- `enclosure.jpg`: the XIAO and regulator in their box
- `installed.jpg`: both tanks in the tray with cables routed

## References

- [DYP L06 datasheet](../../manuals/propane/dyp-l06-lpg-level-sensor-datasheet.pdf) ([text](../../manuals/propane/dyp-l06-lpg-level-sensor-datasheet.md)): specifications, pinout, UART frame format, Modbus and I2C registers
- [DYP L06 installation instruction](../../manuals/propane/dyp-l06-lpg-level-sensor-installation-instruction.pdf) ([text](../../manuals/propane/dyp-l06-lpg-level-sensor-installation-instruction.md)): couplant, EVA ring and epoxy procedure, good and bad echo waveforms
- [DYP L06 product page](https://www.dypcn.com/dyp-l06-gas-tank-lpg-level-measuring-sensor-product/): model list (MTW/MCW/MUW/M4W)
- [ESPHome UART bus](https://esphome.io/components/uart/) and [packages](https://esphome.io/components/packages/)
- [Seeed Studio XIAO ESP32-S3 wiki](https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/): pin map (`D4` = GPIO5, `D5` = GPIO6, `D6` = GPIO43, `D7` = GPIO44)
- [Home Assistant Mopeka integration](https://www.home-assistant.io/integrations/mopeka/): the battery-powered alternative, for comparison
- [Safiery LPG sensor manual](https://university.safiery.com/view/733081500): the 12 V analog alternative, for comparison

Revision history is in the [README](README.md#revisions).
