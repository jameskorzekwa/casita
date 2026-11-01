# Water Tank Sensors (Garnet SeeLeveL fresh + Mopeka grey)

Part of [mod 07, the tank monitor](README.md). Fresh and grey water tank levels in the trailer's Home Assistant, with nothing inside either tank and no wiring to an ESP32: both sensors talk to the trailer's Home Assistant Pi over Bluetooth.

- **Fresh tank: Garnet SeeLeveL II 709-BTP7 Bluetooth display** reading a SeeLeveL sender on the side of the 25 gal fresh tank, through the community [`garnet`](https://github.com/danTapps/garnet) integration. A template sensor turns its reading into `sensor.casita_fresh_tank`.
- **Grey tank: a Mopeka Pro Check Universal** under the 32 gal grey belly tank, through Home Assistant's built-in Mopeka integration. A template sensor turns its reading into `sensor.casita_grey_tank`.

The black tank is left for later; the BTP7 has a channel for a second sender when one is fitted.

![System overview](images/system-overview.svg)

> [!IMPORTANT]
> **Status (updated 2026-10-28): fresh tank live through the Garnet 709-BTP7; grey Mopeka mounted, no echo yet.** The BTP7 reads the fresh sender at 95% on 2026-10-28 (a full tank, by the owner's template); its physical installation (sender position, display mounting, 12 V feed) is **not yet documented**, see [To document](#to-document). The Mopeka is paired, has Bluetooth reach from under the trailer, and reports no echo so far (level `unknown`, quality 0%), which is also what an empty tank looks like: [Step G2](#step-g2-test-the-mopeka-under-the-grey-tank).
>
> **Earlier plan, retired 2026-10-28:** an ESPHome device (`casita-water-monitor-fresh`, a XIAO ESP32-S3 driving the sender through a three-transistor interface) was designed, flashed and adopted on 2026-10-21, then superseded by the BTP7 display. Its configuration, interface schematic and wiring diagram were removed from this repository on 2026-10-28 (they are in the history before that date), the device was deleted from the trailer's Home Assistant and Device Builder, and its XIAO, regulator, capacitor, fuse holder and enclosure are spares. The grey tank's first sensor, a wired DYP L02, never sent a byte and was replaced by the Mopeka on 2026-10-27.

**Contents:** [What to order](#what-to-order) · [Build order](#build-order) · [Why this design](#why-this-design) · [How it works](#how-it-works) · [Known limitations](#known-limitations) · [Parts](#parts) · [Fresh tank (Garnet)](#fresh-tank-garnet) · [Grey tank (Mopeka)](#grey-tank-mopeka) · [Grey tank steps](#grey-tank-steps) · [Home Assistant](#home-assistant) · [Calibrate](#calibrate) · [Testing](#testing-checklist) · [Troubleshooting](#troubleshooting) · [Safety](#safety-notes) · [To document](#to-document) · [Black tank later](#adding-the-black-tank-later)

## What to order

| Tank | Part | Notes |
| --- | --- | --- |
| Fresh | **Garnet SeeLeveL II 709-BTP7** Bluetooth tank display with a **710-ES3** 12 in sender (RecPro "SeeLevel 710 RV Tank Level Sensor (12\")": [Amazon B0GWJR52N8](https://www.amazon.com/dp/B0GWJR52N8); also [Garnet direct](https://shopusa.garnetinstruments.com/solutions/holding-tanks/710-es3-710-es3-12-sender)) | Installed by the owner, October 2026. The display is on the trailer's 12 V and talks Bluetooth to the Pi |
| Grey | **Mopeka Pro Check Universal, the version for aluminium, plastic and poly tanks** (with the mounting collar; not the magnetic steel-tank version): [Amazon B0C7HM61BP](https://www.amazon.com/dp/B0C7HM61BP), about $81 (seen 2026-10-27) | A round sensor with a plastic collar, a CR2032 cell and a sachet of couplant. Delivered and mounted 2026-10-28 |

## Build order

| Step | Grey tank (Mopeka Pro Check Universal) | Result |
| --- | --- | --- |
| G1 | Unbox, fit the battery, pair it with the trailer's Home Assistant, set the medium to Waste Water | A **Tank level** entity. Done 2026-10-28 |
| G2 | With water in the tank, read it from inside the trailer | **Go / no-go for the tank wall and the Bluetooth reach** |
| G3 | Mount it in its collar under the tank | Done 2026-10-28, before G2 was conclusive |
| G4 | Percent template, dashboard gauge, alert; calibrate with a measured fill | Template done 2026-10-28; calibration pending |

The fresh tank needs no steps here; its installation is to be written up ([To document](#to-document)).

## Why this design

The requirement was fresh and grey levels in Home Assistant, powered by the trailer, with nothing inside the tanks. Options considered for the sensors:

| Option | Fresh | Grey (about 4 in tall, under the floor) | Home Assistant | Verdict |
| --- | --- | --- | --- | --- |
| **Mopeka Pro Check Universal (bottom-mount ultrasonic)** | Yes | **Yes; one Casita owner reports 6+ months without trouble** | **Native Bluetooth integration; the medium can be set to Waste Water** | **Chosen for the grey tank on 2026-10-27.** A coin cell to change, and a template sensor turns its millimetres into a percentage |
| **Garnet SeeLeveL sender + 709-BTP7 Bluetooth display** | **Yes** | Only if a flat side wall exists; a 4 in tank leaves little | **Community integration (danTapps/garnet)** | **Chosen for the fresh tank (October 2026).** A proven RV product; the display costs more than a XIAO but needs no interface board, firmware or enclosure |
| Capacitive point switches (XKC-Y25) on the grey tank side | | 2-3 steps only | GPIO | Fallback: cheap and robust, no percentage |
| SeeLeveL 710-ES3 on the fresh tank, driven by an ESP32 directly | Yes | | ESPHome component (j9brown/esphome-seelevel) + a 3-transistor interface | **Built, then retired 2026-10-28** in favour of the BTP7 display: same sender, no custom hardware or firmware to maintain |
| DYP L02 under the grey tank | | Specified for 0.6-5 mm non-foamed plastic, 2 cm dead zone | ESPHome's built-in `ds1603l` platform reads its frame | **Tried and dropped.** The first choice (wired, no battery), but the unit that arrived never sent a byte |

**How the grey tank got here.** The first design (2026-10-14) had one XIAO in the fresh tank bay reading the sender and a wired DYP L02 under the grey tank. On 2026-10-20 that became one device per tank, and on 2026-10-27 the L02 moved onto the propane monitor's XIAO when the projects were combined. The L02 was then wired up (3.3 V confirmed at the sensor, yellow TX on the ESP32's D3 per DYP's datasheet pinout, no LED ever lit) and a UART byte dump on the device showed **nothing at all** on that pin. Rather than chase a possibly dead sensor that was also out of stock, the owner ordered the Mopeka the same evening. It trades the L02's advantages (no battery, wired into the ESP32) for a sensor already proven on this tank, with a native Home Assistant integration and nothing to run under the trailer. The L02, its UART and its entities were removed from the main device's firmware.

Both tanks now use finished products with their own radios, read by the Pi; nothing in this project needs an ESP32 for water. The [e-ink dashboard (mod 08)](../08-eink-dashboard/README.md) reads `sensor.casita_fresh_tank` and `sensor.casita_grey_tank`, both Home Assistant templates. ## How It Works

## How It Works

**Fresh tank (Garnet).** The sender is a flexible circuit board with a column of copper pads, stuck to the outside of the tank. Each pad and the water behind the wall form a capacitor; the sender measures each pad's capacitance and reports it to the 709-BTP7 display over the sender's two-wire bus. The display shows the level and broadcasts it over Bluetooth Low Energy, which the `garnet` integration on the Pi decodes into a per-tank percentage (`sensor.inside_fresh_water_tank_sensor_fresh_tank`: 95 with the tank full, 11-12 when the pump runs dry) plus the display's supply voltage. The template `sensor.casita_fresh_tank` rescales that so 95 reads 100% and 12 reads 0%: "empty" means the pump has nothing left to draw.

**Grey tank (Mopeka).** The Pro Check Universal is a self-contained ultrasonic sensor: it sits in a collar stuck to the underside of the tank with a film of couplant, fires a pulse up through the wall and the water every few seconds, times the echo from the surface, and broadcasts the result over Bluetooth Low Energy. The trailer's Home Assistant Pi (which already has Bluetooth, see [Grey tank (Mopeka)](#grey-tank-mopeka)) picks the broadcasts up with the built-in **Mopeka** integration and publishes **Tank level** in millimetres, plus temperature, battery, signal strength and a reading-quality score. The integration's medium setting (Waste Water for this tank) sets the speed of sound it uses. A template sensor in Home Assistant divides the millimetres by the tank's full height to give the percent the dashboard and alerts use.

**Power.** The BTP7 display runs on the trailer's 12 V (its `Battery` entity shows that voltage, 13.7 V on 2026-10-28) and powers the sender. The Mopeka runs on a CR2032 coin cell, which Mopeka rates for a year or more; Home Assistant shows its battery percentage.

## Known Limitations

- **The grey tank is shallow, and a bottom-mounted ultrasonic sensor struggles with it.** The tank is 3.75 in outside, about 85 mm inside (measured 2026-10-28). Below the sensor's dead zone the Mopeka reports no echo (0%); just above it, the sensor mostly reports multiples of the level (see [Grey tank (Mopeka)](#grey-tank-mopeka)), which the template folds down when they exceed the tank's height but cannot always tell apart from a nearly full tank. Expect a trustworthy reading only in roughly the top inch and a half.
- **The tank wall and the Bluetooth reach are untested on this trailer.** Mopeka does not publish a wall-thickness limit for the Universal on plastic; one Casita owner's working install is the evidence. The sensor broadcasts from under the belly tank and the Pi is inside; Step G2 checks both before anything is stuck on. If the reach is marginal, a cheap ESPHome Bluetooth proxy near the floor fixes it.
- **Sloshing and slope.** Both sensors read the water where they are. The Mopeka's reading-quality score drops while the trailer moves; trust readings when parked. If the trailer is not level, a wide, shallow grey tank reads quite differently at opposite ends. Park level before judging.
- **The fresh reading is in Garnet's steps.** The display reports the sender's pads as a percentage: 95 full and 12 at the pump's limit on this tank, which the template maps to 100% and 0%; resolution is one pad, 1.33 in, about 3 gal on this tank.
- **Metal near the sender reads as water.** Keep steel, aluminum and copper 2 in from the sender's face and 1 in from its edges; check again with doors and covers closed.
- **One shot at sticking the sender.** Its 3M 300LSE adhesive does not survive removal.
- **Polyethylene is hard to glue.** Epoxy, CA and most tapes peel off it. The Mopeka collar comes with its own adhesive; if it lets go of this tank, 3M 9495LE (300LSE) tape with Primer 94, the same combination Garnet uses on the sender, is on hand (Step G3).
- **A battery to change.** The Mopeka's CR2032 is the only battery in the whole project. Home Assistant shows its level; expect a year or two.
- **Always on.** The BTP7 display draws from the trailer's 12 V continuously (to measure); the main propane device's draw is in the [README](README.md#power).
- **Temperature.** The sender is rated 0 to 60 degC. The Mopeka's cold-weather rating is to check in its manual; coin cells fade in deep cold; see [mod 12](../12-cold-weather/README.md) for the belly pan that keeps the tank, and the sensor, warmer.
- **Both tanks depend on the Pi's Bluetooth.** If the Pi is off, nothing is read; the BTP7's own screen still shows the fresh level.
- **Away from home** the Home Assistant connection needs a network path, the same as the battery monitor: see [mod 04](../04-battery-monitor-esp32/README.md#reading-the-battery-away-from-home).

## Parts

Ownership and purchase status, kept current as parts arrive: [components.md](components.md).

### Fresh tank (Garnet)

| Component | Qty | Notes | Purchase link |
| --- | ---: | --- | --- |
| Garnet SeeLeveL II 709-BTP7 Bluetooth display | 1 | Installed by the owner; part number and source to record | [Garnet](https://www.garnetinstruments.com/) |
| Garnet SeeLeveL II 710-ES3 sender, 12 in | 1 | See [What to order](#what-to-order) | [Amazon B0GWJR52N8](https://www.amazon.com/dp/B0GWJR52N8) |

### Grey tank (Mopeka)

| Component | Qty | Notes | Purchase link |
| --- | ---: | --- | --- |
| Mopeka Pro Check Universal, aluminium/plastic/poly version with collar | 1 | See [What to order](#what-to-order). Ordered 2026-10-27 | [Amazon B0C7HM61BP](https://www.amazon.com/dp/B0C7HM61BP) |
| CR2032 coin cell | 1 spare | One comes with the sensor | |
| Silicone dielectric grease or Mopeka Sonic Grease | 1 | Couplant between the sensor and the tank; both on hand | [Amazon: Permatex 22058](https://www.amazon.com/dp/B000AL8VD2), [Mopeka Sonic Grease](https://www.amazon.com/dp/B0CVQVGMWB) |
| 3M 9495LE double-sided tape and 3M Primer 94 | | Only if the collar's own adhesive will not hold on the polyethylene; both on hand | |

### Shared supplies

| Component | Notes | Purchase link |
| --- | --- | --- |
| Rubberized undercoating | Over the sender if road spray can reach it. Garnet names 3M 03584. Do not coat the Mopeka: it needs its battery door and its radio | [Amazon search: 3M 03584](https://www.amazon.com/s?k=3M+03584+rubberized+undercoating) |
| Adhesive-lined heat-shrink, zip ties, painter's tape, Gorilla tape | | [Amazon: heat-shrink kit](https://www.amazon.com/dp/B0DC5YN5CD) |

Prices seen 2026-10-14: sender about $70, the rest $5-15 each; Mopeka about $81 on 2026-10-27. Links marked "search" were not checked against a specific listing; pick the genuine 3M part.

## Tools and Supplies

- Isopropyl alcohol (99%) and lint-free cloths; 220-grit sandpaper
- Heat gun or hair dryer (adhesives want the tank above 15 degC / 60 degF)
- A flat-bottomed plastic tub for the Mopeka bench test; a 1 gal jug for calibration

## Wiring

Nothing in this project is wired to an ESP32. The BTP7 display is on the trailer's 12 V with the sender on its two-wire bus (to document); the Mopeka is wireless and battery-powered.

### Where things go

- **Sender:** on the fresh tank's side, in the rear passenger bay (position to document).
- **BTP7 display:** inside the trailer (location to document).
- **Mopeka:** under the grey tank in its collar, on a flat, smooth spot away from the drain end and the support angles ([Step G3](#step-g3-mount-the-mopeka-under-the-grey-tank)). Nothing runs from it.

## Fresh tank (Garnet)

The trailer's Home Assistant runs the community **`garnet`** integration (HACS, [danTapps/garnet](https://github.com/danTapps/garnet)), which found the display over Bluetooth as **Garnet 709-BTP7 EAC6** (`E0:72:A1:69:EA:C6`); the owner renamed the device **Fresh Water Tank Sensor** (area *Inside*). The integration exposes one percentage per display channel plus the display's supply voltage. Only the fresh channel and the voltage are in use; the other channels (grey, grey 2, fresh 2, black, black 2, LPG) have no sender and were disabled in the entity registry on 2026-10-28 so the device page only shows what is real. Re-enable a channel if a sender is ever added to it.

| Entity | ID | Notes |
| --- | --- | --- |
| Fresh Water Tank Sensor Fresh Tank | `sensor.inside_fresh_water_tank_sensor_fresh_tank` | %, the display's figure: 95 with the tank full, 11-12 when the pump runs dry (the sender's bottom pad sits below the pump pickup, so it still sees water the pump cannot reach) |
| Fresh Water Tank Sensor Battery | `sensor.inside_fresh_water_tank_sensor_battery` | the display's 12 V supply |
| Fresh Tank (corrected) | `sensor.casita_fresh_tank` | template helper: `{{ ([0, ((states('sensor.inside_fresh_water_tank_sensor_fresh_tank') \| float(0) - 12) / (95 - 12) * 100) \| round(0), 100] \| sort)[1] \| int }}` with availability `{{ has_value('sensor.inside_fresh_water_tank_sensor_fresh_tank') }}`: the display's 95 (full) reads 100% and its 12 (the pump runs dry) reads 0%. **Used by mod 08** |

## Grey tank (Mopeka)

The trailer's Home Assistant already has Bluetooth: the Pi 4's built-in radio and a Realtek USB adapter are both loaded (checked 2026-10-27). The built-in **Mopeka** integration discovers Pro Check sensors automatically and publishes, per sensor: **Tank level** (mm), **Temperature** (degC), **Battery** (%) and battery voltage, **Reading quality** (%), **Signal strength** (dBm) and two accelerometer axes. Its options let you pick the medium; **Waste Water** is the one for this tank.

**As paired on 2026-10-28:** the sensor is **Pro Check Universal 5FA8** (Bluetooth `F2:FA:BD:30:5F:A8`), renamed **Grey Water Sensor** in the area *Outside*, medium **Waste Water**. Its entities are `sensor.outside_grey_water_sensor_tank_level` (shown in inches because the trailer's Home Assistant uses US units; the integration's native unit is mm), `..._reading_quality`, `..._temperature` and `..._battery`.

**What the sensor reports, and how it is turned into a level.** Home Assistant's Mopeka integration publishes every Bluetooth broadcast as it comes (about one every 8 s), but only records a value when it changes. On this tank (3.75 in outside, sensor at the inlet end) the raw reading is, most of the time, a **multiple** of the real level at the sensor: the echo that has bounced surface-bottom-surface two, three or four times. On 2026-10-28, with 18-20 gal in, the raw level read 43 mm once, then 64-77 (2x), 108-123 (3x) and 137-166 (4x); on 2026-11-01 a full tank read 75-82 (1x) and 150-165 (2x), and a drain from 54 to about 40 mm made the sensor switch from 109 (2x 54) to 80 (2x 40). There is also the odd junk reading with quality 0% (283 mm once) and short no-echo dropouts.

The level is built in three stages, all helpers on the trailer's Home Assistant (**Settings > Devices & services > Helpers**), attached to the Mopeka device and renamed so their IDs are short:

| Stage | Helper | ID | What it does |
| --- | --- | --- | --- |
| 1 | Template sensor **Grey Water Level (folded)** | `sensor.casita_grey_level_folded` | Resolves each raw reading **by continuity**: of the candidates raw, raw/2, raw/3 and raw/4 (dropping any above 95 mm, since a full tank's real echo is at most about 82 mm here), the one nearest the previous folded value wins; ties go to the larger. The water level moves a few millimetres per gallon while an echo switch jumps instantly, so a fill or a drain is followed step by step and a sudden doubling is treated as the bounce it is. Starts from 40 mm when there is no previous value (after a restart or a no-echo spell). **Unavailable** while the raw level is not a number or the reading quality is below 33% (drops the quality-0 junk) |
| 2 | Statistics helper **Grey Water Level (smoothed)** | `sensor.casita_grey_level_min` (ID kept from its first version) | The **median of the last 5** folded readings, with no age limit: enough to swallow one stray reading, and it follows a real change after three new readings. No time window, because a steady tank produces no new readings for long stretches and a time window would empty |
| 3 | Template sensor **Casita Grey Tank** | `sensor.casita_grey_tank` (name **Grey Tank**) | The percent: smoothed level divided by **Grey tank full level**, capped at 100%. Holds its value through a dropout of up to 3 min, then shows 0% while there is no echo; unavailable only when the Mopeka itself is out of Bluetooth reach. **Used by mod 08** |
| 3a | Number helper **Grey tank full level** | `input_number.casita_grey_full_mm` | The smoothed level that counts as 100%, in mm. **76 mm**, set 2026-11-01 with the tank full (water backing up into the sink) |
| 3b | Script **Mark grey tank full** | `script.casita_grey_mark_full` | Copies the current smoothed level into the number. On the Casita Status dashboard's Water card. Run it with the tank full and settled |

Stage 1 state template and availability:

```jinja
{% set r = states('sensor.outside_grey_water_sensor_tank_level') %}
{% set u = state_attr('sensor.outside_grey_water_sensor_tank_level', 'unit_of_measurement') %}
{% set mm = r | float(0) * (25.4 if u == 'in' else 1) %}
{% set prev = (this.state | float(40)) if (this is defined and this is not none and is_number(this.state)) else 40 %}
{% set ns = namespace(best=none, d=1e9) %}
{% for k in [1, 2, 3, 4] %}{% set c = mm / k %}
  {% if c <= 95 %}{% set d = (c - prev) | abs %}
    {% if d < ns.d or (d == ns.d and c > ns.best) %}{% set ns.d = d %}{% set ns.best = c %}{% endif %}
  {% endif %}
{% endfor %}
{{ (ns.best if ns.best is not none else mm) | round(1) }}
```

```jinja
{{ is_number(states('sensor.outside_grey_water_sensor_tank_level')) and (states('sensor.outside_grey_water_sensor_reading_quality') | int(0)) >= 33 }}
```

Stage 3 (unit %, state class measurement; availability `{{ states('sensor.outside_grey_water_sensor_tank_level') != 'unavailable' }}`):

```jinja
{% set m = states('sensor.casita_grey_level_min') %}
{% set raw = states('sensor.outside_grey_water_sensor_tank_level') %}
{% set h = states('input_number.casita_grey_full_mm') | float(85) %}
{% set prev = (this.state if this is defined and this is not none else 'unknown') %}
{% set age = ((now() - states.sensor.casita_grey_level_folded.last_updated).total_seconds() if states.sensor.casita_grey_level_folded else 9999) %}
{% if raw == 'unknown' %}
  {% if age > 180 or not is_number(prev) %}0{% else %}{{ prev }}{% endif %}
{% elif not is_number(m) %}
  {% if is_number(prev) %}{{ prev }}{% else %}unknown{% endif %}
{% else %}{{ ([0, (m | float(0) / h * 100) | round(0), 100] | sort)[1] | int }}{% endif %}
```

**Response time:** a real change shows on the gauge after three changed readings, which is a minute or two while the level is moving. One gallon is only about 2.7 mm (3.5%) in a tank this wide and shallow, so 20 s at the dump valve is 3-5 gal, 10-16 points.

**Known weakness:** stage 1 needs a sane starting point. After a Home Assistant restart or a no-echo spell it assumes about 40 mm; if the sensor's first readings after that are doubles of a much higher level it can lock onto the half. The next real change in level corrects it, as does **Mark grey tank full** with the tank full.

**How it got here (2026-10-28 to 11-01), for the record.** Five rules were tried in four days: a plain median of the raw readings (returns whichever multiple is commonest); halving anything taller than the tank (called a full tank, which reads about 95 mm raw, half full); believing anything up to 110 mm (called a half-full tank, doubled, full); a 15 min time window (emptied on a steady tank and left one stale sample, reading 100%); and a 20-reading window (lagged a drain indefinitely on a steady tank). Each failed on the next real event. Continuity is the first rule built on the one thing the bounce cannot fake, which is time, and it has held through a drain; judge it on the next full fill and dump.

**Where the sensor sits, and what the percentage means.** The tank is wide and only 3.75 in tall, and the owner mounted the Mopeka **near the inlet end**, which is the high end: water pools at the outlet end first and only reaches the sensor's spot once that end is full. So the gauge is a "how close to full" gauge, not a volume gauge:

- **100%** (76 mm of water at the sensor) means the tank is full everywhere: confirmed 2026-11-01, when 100% coincided with water backing up into the sink.
- **0%** means the water at the sensor is below what it can see, which is about **40 mm (53%)**: on 2026-11-01 the echo was lost at a steady 40 mm and came back at 53% when a little water was added. So the gauge reads 0% for most of the fill and then jumps to about 53% and climbs to 100%; it is a top-end gauge. 0% does **not** mean empty; there can be a lot of water at the outlet end, and because the sensor is at the high end, water reaching it at all already means most of the tank is full. The dashboards label the gauge "0% = below sensor" for this reason.
- The usable 53-100% range covers only the last slice of the tank's volume, so the "nearly full" alert at 60% fires soon after the water becomes visible at the sensor; the 95% "full" alert is the one that means water is about to back up. This placement also explains the echo multiples seen in the first days: when water first reaches the sensor it is only an inch or so deep, at the edge of what the sensor can resolve.

**The full level is calibrated, not computed from the height.** On 2026-11-01 the tank was full (water backing up into the sink) and the raw readings over 90 minutes clustered at 75-82 mm (the real echo) and 150-165 mm (its double), with the filtered value at 76 mm; **Mark grey tank full** set **Grey tank full level** to 76. That is less than the 85 mm expected from the 3.75 in outside height (measured 2026-10-28), presumably the sensor's offset and the wall; it is the number that matters. Earlier values were 90 mm (an old "about 4 in" note), 150 mm (mistaking a doubled echo for the level) and 85 mm (from the measured height); the first two read 100% on a half-full tank, the last read 89% on a full one.

## Grey tank steps

### Step G1: Pair the Mopeka on the bench

1. Pull the battery tab (or fit the CR2032). The sensor starts broadcasting at once.
2. In the trailer's Home Assistant, **Settings > Devices & services** should show a discovered **Mopeka** device within a minute. **Add**, then open its options and set the medium to **Waste Water**. Rename the device so its entities get sensible IDs (done 2026-10-28: **Grey Water Sensor**, which gives `sensor.outside_grey_water_sensor_tank_level`); note the **Tank level** entity ID for the template above.
3. With the sensor face up on the bench, **Tank level** should read 0 and **Reading quality** low. Press it, with a dab of grease, against the underside of a plastic tub of water about 60 mm deep: the level should read close to that within a few readings.

### Step G2: Test the Mopeka under the grey tank

Nothing here is permanent.

1. Dump the grey tank, then put a known amount of water in through the sink: about 10 gal (roughly 25-30 mm in a tank this size). Park level.
2. Under the trailer, clean the chosen spot (flat, smooth, supported, away from the drain end) with alcohol. Grease the sensor face and hold it up against the tank, flat, no air gap; a strip of Gorilla tape across the collar holds it for the test.
3. Inside the trailer, read **Tank level** and **Reading quality**. **Pass:** a steady, non-zero level that rises when you add 5 more gallons, with quality well above zero, and **Signal strength** comfortably readable from where the Pi is. **Fail:** level `unknown` with quality 0% while there is water above it (wall or coupling), or no updates at all (Bluetooth reach). Note that quality 0% and level `unknown` is also exactly what an **empty** tank looks like: the Mopeka cannot see the first inch or two of water, so put water in before judging.
4. If the reach is the problem, try the USB Bluetooth adapter on a short extension nearer the floor, or plan an ESPHome Bluetooth proxy; if the wall is the problem, try another spot before giving up.
5. Note the reading and the gallons in; that is the first calibration point.

### Step G3: Mount the Mopeka under the grey tank

1. Dump the tank and park level. Clean the spot from Step G2 with alcohol; sand lightly with 220 grit if textured; wipe again; dry. Warm the plastic with a heat gun in cold weather.
2. Follow Mopeka's collar instructions: couplant on the sensor face, the sensor in the collar, the collar's adhesive onto the primed tank, firm pressure for a minute. If the collar adhesive does not grab the polyethylene, use a ring of 3M 9495LE on Primer 94 instead, as the sender uses.
3. Leave the tank empty for 24 h so the adhesive cures. Do not undercoat the sensor.
4. Check the reading again after mounting; it should match the taped test.

### Step G4: Calibrate and finish

See [Calibrate: grey tank](#grey-tank). Then add the gauge and the grey-full alert from the [README](README.md#home-assistant-setup), and the `rv_` mirror at home.

## Home Assistant

Both tanks are read by integrations on the trailer's Home Assistant, not by ESPHome: `garnet` (HACS) for the fresh display and the built-in **Mopeka** for the grey sensor. The two percent sensors the dashboard, alerts and the home mirror use are template helpers:

| Entity | Built on | Notes |
| --- | --- | --- |
| `sensor.casita_fresh_tank` | the BTP7's fresh channel | 12 to 95 on the display mapped to 0 to 100%; see [Fresh tank (Garnet)](#fresh-tank-garnet) |
| `sensor.casita_grey_tank` | the Mopeka's tank level | inches to mm, 90 mm assumed full; see [Grey tank (Mopeka)](#grey-tank-mopeka) |

The dashboard card, the fresh-low and grey-full alerts, and mirroring to the home Home Assistant are in the README's [Home Assistant setup](README.md#home-assistant-setup).

## Calibrate

Park level for all of this.

### Fresh tank

The BTP7 does its own level estimation; what is calibrated is the template, whose two numbers are the display's reading with the tank full (**95**) and when the pump runs dry (**12**, observed by the owner on 2026-10-28). To refine them: run the pump until it loses prime and note the display; then refill in measured steps (a 1 gal jug, or time the hose against a bucket), noting the display's figure at each step. Change the numbers in the template if they differ, and if the steps are far from linear, note it here.

### Grey tank

After dumping, with the tank empty, the Mopeka's **Tank level** should read `unknown` (below its dead zone). Then add water through the sink in 5 gal steps, wait for the water to settle, and record **Grey Water Level (folded)** each time (the smoothed helper needs three readings; the folded value is immediate). From two points above the dead zone, compute millimeters per gallon; then:

`full level (mm) = 32 gal x (mm per gal)`, adjusted by the intercept if the line does not pass through zero (the first few gallons fill the tank's low spots).

Enter that number in **Grey tank full level** (or simply press **Mark grey tank full** when the tank is full). The number is 76 mm as of 2026-11-01. Alternatively, keep filling while watching the shower drain, note **Tank level** the moment water appears in the shower pan, and use that; it defines 100% as "about to back up", which is the practical meaning. Dump afterwards.

Repeat the grey calibration once after the first trip, since a belly tank's shape under load can differ from the empty tank's.

## Testing Checklist

**Fresh tank (Garnet)**

1. The BTP7's own screen and `sensor.inside_fresh_water_tank_sensor_fresh_tank` agree.
2. Full tank reads 95 on the display and 100% on `sensor.casita_fresh_tank`; the pump running dry reads about 12 on the display and 0%.
3. The reading survives a tow and a Pi restart (the `garnet` integration reconnects on its own).

**Grey tank (Mopeka)**

7. On the bench against a tub of water: **Tank level** within about 5 mm of a ruler; 0 in air.
8. Taped under the grey tank with 10 gal in: steady non-zero level that rises with 5 more gallons; **Reading quality** well above zero; updates arrive inside the trailer.
9. Mounted: reading matches the taped test; `sensor.casita_grey_tank` follows it.
10. Calibration: the template's full level set from a measured fill; 32 gal reads about 100%.

**Both**

11. Home Assistant shows the BTP7, the Mopeka, `sensor.casita_fresh_tank` and `sensor.casita_grey_tank`; the e-ink dashboard's water gauges fill in on its next refresh; the home Home Assistant shows the `rv_` mirrors in the Casita RV area.
12. After the first tow: both tanks still read; the Mopeka has not moved; undercoating on the sender intact.

## Troubleshooting

| Device | Symptom | Likely cause | Fix |
| --- | --- | --- | --- |
| Fresh | `sensor.inside_fresh_water_tank_sensor_fresh_tank` unavailable | The BTP7 is unpowered (its 12 V feed), or out of the Pi's Bluetooth reach, or the `garnet` integration is not loaded | Check the display is lit; **Settings > Devices & services > Garnet** |
| Fresh | Reads 95 when the tank is not full, or never reaches 95; or the pump runs dry at a reading other than about 12 | The sender's pad count or position; or the template's 95 / 12 need changing | Compare with a measured fill and a run-dry ([Calibrate](#fresh-tank)) |
| Grey | No Mopeka device discovered | Battery tab still in, flat cell, or the sensor out of Bluetooth reach of the Pi | Check the cell; bring the sensor inside to pair, then test reach at the tank (Step G2) |
| Grey | Updates stop when the sensor is under the tank | Bluetooth reach through the floor | USB adapter nearer the floor, or an ESPHome Bluetooth proxy |
| Grey | Level always 0 with water above it, low reading quality | No couplant, air gap, wrong medium setting, or the wall is beyond the sensor | Re-grease and press; set the medium to Waste Water; try another spot |
| Grey | The raw **Tank level** jumps to about twice the level, or to hundreds of mm with quality 0%, while the gauge stays put | Multiple-bounce and junk readings; the folded and smoothed helpers are doing their job | Nothing to fix. If the gauge itself jumps, check the chain raw > `sensor.casita_grey_level_folded` > `sensor.casita_grey_level_min` > `sensor.casita_grey_tank` |
| Grey | Gauge reads 0% but there is water in the tank | The water has not reached the sensor at the inlet (high) end yet | Expected; 0% means below the sensor, not empty |
| Grey | A short drain moves the gauge less than expected | One gallon is only about 2.7 mm (3.5%) in a tank this wide and shallow, so 20 s at the valve is 3-5 gal, 10-16 points | Expected |
| Grey | Home Assistant and the Mopeka app disagree | The app shows the raw reading against the tank height set in the app; it does not resolve the echo multiples | Trust Home Assistant's gauge; the app is only useful for confirming the sensor is alive |
| Grey | Gauge under-reads a full tank | **Grey tank full level** is too high | Press **Mark grey tank full** with the tank full and settled |
| Grey | Gauge reads 100% with the tank clearly not full | The continuity rule locked onto the wrong multiple after a restart or a no-echo spell; or **Grey tank full level** was set with the tank not full | Expect it between a third and a half full; a capacitive point switch at the nearly-full height would make the alert definite ([Grey tank (Mopeka)](#grey-tank-mopeka)) |
| Grey | `sensor.casita_grey_tank` unknown | Wrong Tank level entity ID in the template | Fix the ID (Step G1) |
| Grey | Level far off the ruler | Wrong full level in the template, or the tank is tilted | Recalibrate on level ground |

## Safety Notes

- The BTP7 display's 12 V feed should have its own fuse (to confirm and document).
- The Mopeka's coin cell is a swallowing hazard for children and pets; keep the spare put away.
- Working under the trailer: chock the wheels, park on firm level ground, keep clear of the drain valves.
- Undercoating and primer: ventilate, no flames, keep off the fiberglass body.
- The fresh tank is potable. Nothing in this project touches the water; keep adhesives, grease and undercoating away from the fill, vent and drain fittings.

## To document

The fresh tank's physical installation was done by the owner and is not yet in this repository:

- Where the sender sits on the tank (and whether it was cut to 8 pads), how its wires run to the display, and the tank number it is programmed as.
- Where the BTP7 display is mounted and which 12 V circuit and fuse feed it.
- The display's part number and where it was bought; add both to [components.md](components.md).
- Photos: `fresh-sender-installed.jpg`, `btp7-display.jpg`.

## Adding the black tank later

Put a second SeeLeveL sender on the black tank (a 710-AR2, 9 in with 1 in pads, if the black tank is short), programmed as tank 3 (cut the `3/BLK` tab) and wired to the BTP7's sender bus; re-enable `sensor.inside_fresh_water_tank_sensor_black_tank` in the entity registry and make a template `sensor.casita_black_tank` like the fresh one. Mod 08's dashboard expects `sensor.casita_water_monitor_black_tank` today; change its `water_black` substitution to the new ID. Garnet's rule for waste tanks: bias the sender toward the top of the tank.

## Photos

Add photos to `photos/` as the build progresses:

- `fresh-sender-installed.jpg` and `btp7-display.jpg`
- `grey-tank-underside.jpg`: the tank bottom and the sensor spot before mounting
- `mopeka-taped.jpg` and `mopeka-installed.jpg`

## References

- [Garnet SeeLeveL 709 Series manual v2.0 (Nov 2025)](https://www.garnetinstruments.com/wp-content/uploads/2025/11/SeeLeveL-709-Series-Manual-v2.0.pdf): sender cutting, tab programming, placement gaps, metal clearance, adhesion, undercoating
- [danTapps/garnet](https://github.com/danTapps/garnet): the Home Assistant integration for the SeeLeveL 709 Bluetooth displays
- [Garnet 710-ES3 product page](https://shopusa.garnetinstruments.com/solutions/holding-tanks/710-es3-710-es3-12-sender): 12.15 x 2.20 in, 9 pads, 300LSE adhesive, 0-60 degC
- [Home Assistant Mopeka integration](https://www.home-assistant.io/integrations/mopeka/): auto-discovery over Bluetooth, the medium list (Waste Water among them), supported sensors including the Pro Check Universal
- [Mopeka Pro Check Universal](https://www.mopekaiot.com/procheckuniversal): the sensor and its collar
- [DYP L02 datasheet](https://www.dypcn.com/uploads/L02-Datasheet1.pdf): the sensor tried first (pinout red VCC, black GND, yellow TX, white RX; 2.8-5 V; 9600 baud 4-byte frame), kept for the record
- [Mopeka grey tank install on a Casita (video)](https://www.youtube.com/watch?v=rsI1zkrDrD4): the tank measured at about 4 in tall; a Mopeka working on this tank for 6+ months
- [Mod 08 e-ink dashboard](../08-eink-dashboard/README.md#entities-shown): the entity names this project must produce

Revision history is in the [README](README.md#revisions).
