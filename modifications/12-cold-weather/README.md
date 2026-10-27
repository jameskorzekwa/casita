# Cold-Weather Package (grey tank heat, drain protection, battery warming, freeze monitoring)

A set of changes so the trailer can be camped in with water in the system when nights drop below freezing: a heating pad and insulated enclosure on the belly-mounted grey tank, heat on the exposed dump valves and drain stubs, warming for the battery compartment so the LiFePO4 bank can still charge, temperature probes on everything that can freeze, and Home Assistant automations that run the heaters and raise alarms. Cabin heat, the shore-power budget, condensation and propane are covered as operating practice rather than hardware.

> [!IMPORTANT]
> **Status: proposed, nothing ordered, nothing measured (2026-10-21).** This is a plan for review. No parts have been bought, no tank or compartment dimensions have been measured, and no product on the parts list has been checked against this trailer. Every "about" figure below is an estimate from the manuals and general RV practice, marked as such. The [open questions](#open-questions) decide the final design.
>
> **Scope.** "Cold weather" here means **camping with the furnace running** and water in the tanks, down to roughly **10-15 °F overnight** with daytime highs around freezing. It does **not** cover leaving the trailer unheated below freezing; for that, the owner's manual's winterization procedure (drain, blow out, RV antifreeze; page 36 of the [owner's manual](../../manuals/casita/casita-owners-manual.md)) still applies and none of this replaces it.

**Contents:** [What can freeze](#what-can-freeze-on-this-trailer) · [Design](#design) · [Power budget](#power-budget) · [Parts](#parts-proposed) · [Wiring](#wiring) · [Home Assistant](#home-assistant-automations) · [Steps](#steps) · [Testing](#testing-checklist) · [Operating practice](#operating-practice) · [Safety](#safety-notes) · [Open questions](#open-questions) · [Revisions](#revisions)

## What can freeze on this trailer

From [`docs/trailer.md`](../../docs/trailer.md) and the owner's manual. The important thing about this Casita is that **two of the three tanks are inside** the heated shell; the grey tank and the drain hardware are the real exposure.

| Item | Where | Exposure | Risk while the furnace runs |
| --- | --- | --- | --- |
| Fresh tank, 25 gal, 12 in tall, with the Shurflo pump | Inside, rear passenger side bay | Cabin air, but a floor-level bay with the fill, vent and drain penetrations in it | Low; the manual says cabin heat is normally enough. Watch for cold air entering at the penetrations |
| Black tank, 15 gal | Inside, under the toilet in the wet bath | Cabin air | Low. Its 3 in ABS drain from the floor to the termination valve is outside |
| **Grey tank, 32 gal, about 4 in tall, black polyethylene** | **Under the floor, open to the air** | **Full exposure, large flat area, wide and shallow** | **High.** A shallow tank with a big surface freezes fast, and shower and sink water goes into it all day. This is the main job |
| Termination assembly: black and grey dump valves, the 3 in and 1-1/2 in drain stubs, outlet cap | Under the trailer, rear | Full exposure | High. A frozen gate valve will not open, and ice in the stub can split the valve body |
| Fresh tank drain (grey cap) | Under the coach, rear passenger side | Full exposure, short stub | Moderate; a small amount of water, and a split cap is cheap |
| City water inlet, low-point drains, blow-out plug | Exterior wall and underside | Full exposure | Moderate. Only matters if connected to city water or if the low-point stubs hold water |
| Water heater, Suburban SW6DE (6 gal, gas and 1440 W element) | Sidewall, exterior access door; bypass valve behind the cabinet under the sink | The exterior door is a thin panel over the tank | Moderate. On shore the element keeps it warm; off-grid the gas burner does only while heating |
| PEX runs to the sinks and shower | Inside, along the floor behind the lower cabinets | Cabin air, but the coldest cabin air | Low to moderate. The manual tells Casita owners to open the lower cabinet doors at night in cold weather |
| Sewer hose in the rear bumper | Bumper tube | Full exposure | Only if stored wet |
| **Battery bank, 2 x Renogy Core Mini 300 Ah** | Rear center battery compartment | Exterior compartment | Not a freeze-damage risk, but a **charging** risk: the BMS blocks charging at or below 32 °F (resumes at 41 °F) and allows discharge to -4 °F, with no self-heating ([mod 01](../01-second-battery/README.md)) |

What this trailer already has going for it: the 12 V compressor fridge has no cold-weather quirks, the Suburban NT-16SEQ furnace (16,000 BTU/h, 12 V blower on a 7.5 A circuit) is sealed-combustion so it adds no moisture, the water heater element is on the shore-only breaker box ([mod 03](../03-whole-panel-inverter/README.md)) so it cannot drain the batteries, there are two 20 lb propane cylinders, and the 600 Ah bank can run the furnace blower and the heating pads for days.

## Design

In order of importance. Items A, B and G are the minimum for a trip with water on board; F matters for winter boondocking; the rest is comfort and practice.

### A. Grey tank: 12 V heating pad under the tank, foam insulation, belly enclosure

**Pad.** A 12 V thermostatic RV holding-tank pad (the Ultra-Heat / UltraHeat type: a thin silicone or vinyl heater with a built-in thermostat that closes at about 45 °F and opens at about 68 °F, applied to the tank bottom with its own adhesive). Pads come in sizes up to about 12 x 24 in; this tank's footprint is unknown but is large. Working from 32 gal at about 3.5 in inside height gives a footprint on the order of 2,100 in², roughly 36 x 60 in, so **two pads** spaced along the bottom are more likely than one. Measure the tank in Step 1 before choosing; the pads must also stay clear of the DYP L02 sensor spot from [mod 09](../09-water-tank-monitor/README.md#step-1-measure-and-plan-the-sender-and-sensor-positions), the drain fitting, and any support straps.

Pads of this type draw about 3-4 A each at 12 V when on. Two pads are 6-8 A, well inside the 10 A contact rating of the Waveshare board's spare relays from [mod 06](../06-smart-dc-switches/README.md), but mod 06's rule is that no trailer load goes directly on those relays until its rating is proven, so the pads are switched through an external automotive relay (Section [Wiring](#wiring)).

Why 12 V, not 120 V pads: the pads must work on the inverter and off-grid, and a 12 V pad can be switched from Home Assistant without touching the AC side. On shore the converter carries the load anyway.

**Insulation.** 1 in foil-faced polyisocyanurate board (about R-6) cut to the tank bottom with openings for the pads' lead exits, the L02 and the drain, plus strips around the tank sides. The foil faces the tank. Polyiso, not polystyrene: it tolerates the pad's surface temperature and does not crumble on the road.

**Enclosure.** A sheet of 4 mm coroplast (or 0.025 in aluminum if the coroplast proves too flimsy) under the foam, screwed to the tank's steel support angles or the frame, never to the fiberglass shell, with the edges sealed to the floor with foam tape and a drip gap at the lowest point so any leak or condensation drains instead of pooling. The enclosure also protects the L02 and its cable from road spray, which mod 09 currently does with undercoating alone. Make the pan removable: the L02 and the pads will need attention at some point.

**What this does not do:** it does not keep the tank warm with the pads off. The enclosure slows heat loss; the pads supply the heat. Both are needed below about 20 °F.

### B. Dump valves and drain stubs: 12 V pipe heater, foam, protective sleeve

A 12 V self-regulating pipe heating cable (or two short thermostatic 12 V pipe heaters of the same family as the tank pads) spiralled along the 3 in black drain stub, the 1-1/2 in grey drain, and wrapped twice around each gate valve body, held with aluminum foil tape (foil spreads the heat along plastic). Over that, closed-cell foam pipe insulation split to fit, then a wrap of vinyl tape or a short coroplast sleeve where road spray hits. The valve handles must stay free to pull. The outlet cap stays on; the sewer hose is connected only to dump and comes straight back into the bumper.

If a purpose-made gate-valve heater pad fits the Valterra-style valve bodies on this trailer, use that on the valves and the cable on the pipe; check the valve body size in Step 1 before buying either.

Draw: about 1-2 A at 12 V for a short run, thermostatic. Switched with the tank pads on the same relay.

### C. Water heater

- **On shore:** leave the electric element on (it is on the 20 A breaker in the shore-only box). The tank's own standby losses keep the heater bay above freezing.
- **Off-grid:** run it on gas. Between burns in hard cold the tank cools slowly; 6 gal at 120 °F takes many hours to reach freezing in a sheltered bay, but the cold and hot stubs near the exterior door can freeze first. If the trailer will sit unheated for more than a night, bypass and drain it (bypass valve horizontal behind the cabinet under the sink; drain plug is the anode, 1-1/16 in socket; manual page 36).
- **Insulated door cover:** a magnetic insulated cover (the RV "water heater door insulation" type) over the exterior access door **only while the heater is on electric or off**. On gas, the door is the burner's combustion air and exhaust path; **never cover it with the burner enabled** (see [Safety](#safety-notes)).

### D. Fresh tank bay, pump and interior lines

- Add the temperature probe (Section G) in the bay at floor level next to the pump.
- Seal around the fill, vent and drain penetrations in the bay floor with closed-cell foam or backer rod so outside air does not blow across the tank and pump.
- Open the lower cabinet doors under the sink and in the bath at night, as the manual says.
- If the bay is behind a solid cabinet face with no airflow from the cabin, cut a small vent in the lower corner (a louvre or a 2 in hole saw with a plastic grille) so furnace air reaches it. Decide in Step 1.
- Put a 3/4 in foam pipe insulation sleeve on the city inlet elbow behind the wall and a cap of foam on each low-point drain stub outside.

### E. City water and sewer practice

Below freezing, run from the fresh tank with the pump and keep the city inlet capped. If a hookup is unavoidable: a heated hose (Camco or Pirit type, 120 V, about 0.5-2 A on shore), connected only as long as needed, with the inlet insulated. Dump valves stay closed; dump when the grey is nearly full (mod 09 raises that alarm), then pour about a quart of RV antifreeze down the shower and sink and flush a quart into the black tank so the small amount left in the tank bottoms and traps cannot freeze solid. The manual says not to put automotive antifreeze in the waste system.

### F. Battery compartment: warming pads and insulation

The Core Mini's BMS refuses charge at or below 32 °F. On shore power that only means the converter runs the DC loads while the batteries sit; off-grid it means the bank discharges all trip and never refills, and solar is useless. For winter boondocking the compartment needs to stay above about 41 °F.

- **Warming pads:** two 12 V thermostatic battery pads (the same product family as the tank pads, sized to the Core Mini footprint) under or against the long side of each battery, or one larger pad on the compartment floor. Switched from Home Assistant on the battery probe temperature, not left on the pad's own thermostat only, so the automation can hold off when the bank is nearly empty. Draw about 2-3 A each. Do not stick anything to the battery terminals or vents; the Core Mini is a sealed LiFePO4 case with M8 terminals and no gas venting, so there is no venting requirement to work around, but the compartment should not be sealed airtight either (moisture).
- **Insulation:** 1 in polyiso board on the compartment's outer walls, floor and lid, fitted around the busbars, MEGA fuses and 1/0 cables from [mod 01](../01-second-battery/README.md) with a minimum 1 in clearance from any fuse or lug. Foil faces inward. Nothing may touch a busbar.
- **Energy:** warming 2 x 27 kg of cells and case from 25 °F to 41 °F is roughly 150 Wh, about 12 Ah at 12.8 V, before losses; holding them there on a 10 °F night costs more, perhaps 30-60 Ah per night with the board insulation. Acceptable on a 600 Ah bank, and it unlocks the converter and solar.
- **Charging note:** the WFCO WF-8900-AD auto-detects lithium; if the batteries are below the BMS cutoff when the converter comes on, the converter sees no battery and may mis-detect. Let the pads bring the bank above 41 °F before plugging in, or expect to power-cycle the converter after.

### G. Temperature probes and freeze alarms

Five DS18B20 waterproof probes on one 1-Wire bus, read by the **mod 09 XIAO** (it already has a cable route through the floor to the grey tank and sits in the fresh tank bay):

| Probe | Where | Used for |
| --- | --- | --- |
| Grey tank | Under the tank, inside the enclosure, taped to the tank wall away from a pad | Pad control and the freeze alarm |
| Dump valves | Taped to the black valve body under the insulation | Alarm; valve heater control |
| Fresh tank bay | Floor level next to the pump | Alarm; "open the cabinet doors" reminder |
| Battery compartment | Taped to a battery case side, not a terminal | Battery pad control; charge-block warning. Runs from the mod 09 XIAO only if the compartment is within reach of a cable; otherwise this probe goes on a second XIAO or the mod 06 controller (open question) |
| Outside air | Under the trailer in the shade, off the enclosure | Automation enable; logging |

The INA228 temperature in [mod 04](../04-battery-monitor-esp32/README.md) is the chip's die temperature inside the display housing, not the battery; it cannot stand in for the battery probe.

Add to the mod 09 firmware: a `dallas_temp` / `one_wire` bus on a free XIAO pin (D1 is free in the current mapping; D2/GPIO3 is a strapping pin, avoid), a 4.7 k pull-up, five `sensor` entries with 30 s updates. Entity names `Casita Water Monitor Grey Tank Temperature`, `... Dump Valve Temperature`, `... Fresh Bay Temperature`, `... Battery Temperature`, `... Outside Temperature`.

### H. Cabin heat and the 30 A shore budget

- **Furnace:** NT-16SEQ, 16,000 BTU/h input. A 20 lb cylinder holds about 430,000 BTU. At a 40-50 % duty cycle on a 15 °F night (an estimate; the Casita's thin shell is the unknown), that is 6,500-8,000 BTU/h, so a cylinder lasts roughly 2.5-3 days of continuous heating. Two cylinders: about 5-6 days. The blower is about 3 A running; call it 40-60 Ah/day at that duty cycle.
- **Electric heat on shore:** a 1,500 W heater is 12.5 A. With the water heater element (12 A) and the converter at full 55 A charge (about 8-10 A AC) that is 33-35 A on a 30 A main. The [upgrade plan](../../docs/off-grid-upgrade-plan.md) already notes the same conflict with the A/C. The fix is sequencing, not more heaters: an automation that drops the space heater's smart plug when the [mod 10](../10-ac-power-meter/README.md) Shelly EM reports shore current above about 26 A, and the water heater element off while the batteries are bulk charging.
- **Never** the range or an unvented catalytic heater for cabin heat; the manual is explicit, and the LP/CO detector is the backstop.
- Any portable electric heater goes on an outlet that is **not** on the inverter side unless the inverter is intended to carry it (1,500 W from the bank is about 125 A, the whole 600 Ah in under five hours).

### I. Shell, windows, moisture

Not hardware in this mod, but part of the package:

- Cut-to-fit Reflectix or insulated fabric panels for every window and the door window, held with the window frames or magnets. Windows are the largest heat loss in a fiberglass egg.
- A vent pillow in the MaxxFan opening when it is closed; crack it open on low exhaust at night with a window cracked on the opposite end. The manual says the same.
- Door gasket check; a draft stopper at the sill.
- Rugs on the floor.
- On shore: a small compressor dehumidifier (about 300 W), or run the A/C in dry mode for an hour when it is above 60 °F outside. Off-grid: ventilation only; wipe the windows in the morning and keep bedding off the walls.
- Insulated covers on the fridge and furnace exterior vents are **not** used; the fridge needs its airflow and the furnace vent is combustion.

### J. Propane

- Cylinders below about 30 % lose pressure quickly in the cold; refill earlier than in summer. [Mod 07](../07-propane-tank-monitor/README.md) (level monitor) becomes a cold-weather tool.
- Regulator "freeze-up" is moisture in the gas freezing in the regulator (manual page 23). If the furnace cycles off with gas in the tank, that is the first suspect; the fix is a purged refill, not a new regulator.
- For a stationary stay, an extend-a-stay fitting and a 100 lb cylinder on the ground removes the refill problem. Not part of this mod.

## Power budget

All figures estimated from product ratings and duty-cycle guesses; measure with the mod 04 battery monitor on the first cold night.

| Load | Draw when on | Duty on a 10-15 °F night | Ah per 24 h (estimate) |
| --- | --- | --- | --- |
| Furnace blower | 3 A | 40-50 % | 30-40 |
| Grey tank pads (two) | 6-8 A | 30-50 % with insulation | 45-95 |
| Valve and drain heater | 1-2 A | 50 % | 12-24 |
| Battery pads (two) | 4-6 A | 30-50 % with insulation | 30-70 |
| Fridge | existing | | 25-50 (from `docs/trailer.md`) |
| Inverter idle, HA Pi, router, monitors, Starlink | existing | | 60-120 |
| **Total** | | | **about 200-400 Ah/day** |

On a 600 Ah bank with about 510 Ah usable that is one to two days off-grid in hard cold before the bank needs a charge, and the charge needs the batteries above 41 °F. Plan winter boondocking around shore power, a generator, or a tow-vehicle DC-DC charger (on the upgrade plan's list), and treat the suitcase solar as a bonus in short December days.

On shore: the converter supplies all of the 12 V heat (8-10 A AC at full output) and the pads are not a battery concern.

## Parts (proposed)

Nothing ordered. Links are searches, not checked listings; the right pad sizes depend on the Step 1 measurements. Prices are rough 2026 figures.

| Component | Qty | Notes | Approx. |
| --- | ---: | --- | --- |
| 12 V thermostatic holding-tank heating pad, largest size that fits (12 x 24 in class, about 3-4 A) | 2 | Ultra-Heat or equivalent with built-in 45/68 °F thermostat. Size from the tank measurement. [Search: 12V RV holding tank heater pad](https://www.amazon.com/s?k=12v+rv+holding+tank+heater+pad) | $60-80 each |
| 12 V thermostatic pipe heater or self-regulating 12 V heat cable, 6-10 ft | 1 | For the drain stubs and valves. [Search: 12V RV pipe heater](https://www.amazon.com/s?k=12v+rv+pipe+heater) | $40-60 |
| 12 V gate-valve heater pad, if one fits the valve bodies | 2 | Optional, replaces the cable wrap on the valves. Measure first | $25-35 each |
| 12 V thermostatic battery warming pad, sized to the Core Mini footprint | 2 | Same family as the tank pads. [Search: 12V RV battery heater pad](https://www.amazon.com/s?k=12v+rv+battery+heater+pad) | $40-60 each |
| 1 in foil-faced polyiso board, 4 x 8 ft sheet | 2 | Grey tank bottom and sides, battery compartment walls, water-heater door cover backing | $35 each |
| 4 mm coroplast, 4 x 8 ft (or 0.025 in aluminum sheet) | 1 | Belly pan under the grey tank | $30-60 |
| Aluminum foil tape, closed-cell foam pipe insulation (3/4, 1-1/2, 3 in), foam weatherstrip tape, backer rod | | Heat spreading, pipe and penetration insulation | $40 |
| Self-tapping screws with neoprene washers, aluminum angle or strap | | Belly pan to the tank supports and frame | $20 |
| Magnetic insulated water heater door cover | 1 | Shore/electric use only | $25 |
| DS18B20 waterproof probe, 1 m lead | 5 | [Search: DS18B20 waterproof](https://www.amazon.com/s?k=DS18B20+waterproof+probe) | $2-3 each |
| 4.7 k resistor; 3-conductor 22 AWG cable, about 10 m | | 1-Wire bus; the mod 07 shielded roll may cover it | on hand? |
| 12 V automotive relay, 30 A, with socket and suppression diode | 2 | One for the tank+valve heaters, one for the battery pads; driven by Waveshare relays 5 and 6 from mod 06 | $8 each |
| Inline ATC fuse holders and fuses (10 A for the tank/valve branch, 10 A for the battery branch), 14 AWG wire | | Every new conductor fused at its source | $20 |
| Reflectix roll or insulated window panels; vent pillow; door draft stopper | | Section I | $60-100 |
| RV antifreeze, 2 gal | | Waste tanks and traps after each dump in freezing weather | $10 |
| Heated fresh water hose, 25 ft, 120 V | 1 | Optional, only if a city hookup is unavoidable | $90-120 |

About **$500-700** for A, B, F and G without the optional items.

## Wiring

No diagram yet; an SVG in `images/` is a follow-up once the relay source and probe host are decided.

**Heater branches (12 V).** Two fused branches from the 12 V distribution (a spare WFCO fuse position, or the busbar side of the shunt as every load must be, per [mod 04](../04-battery-monitor-esp32/README.md)):

```
12 V +  --[10 A fuse]--  relay 1 (30 A auto)  --  grey tank pad 1 (+)
                                               --  grey tank pad 2 (+)
                                               --  valve/drain heater (+)
12 V +  --[10 A fuse]--  relay 2 (30 A auto)  --  battery pad 1 (+)
                                               --  battery pad 2 (+)
All (-) to the chassis ground stud nearest each load, which returns through the shunt's P- side.
```

Relay coils (about 150 mA each) are switched by two of the four unused relays (5-8) on the mod 06 Waveshare ESP32-S3-ETH-8DI-8RO: Waveshare COM to 12 V through a 1 A fuse, NO to the coil. The coil's other side to ground, with the suppression diode across the coil. This keeps the Waveshare contacts at a fraction of their 10 A rating, which is what mod 06's rules require until a direct-load rating is proven. Firmware: two more `switch` entities in [`casita-smart-dc-switches.yaml`](../06-smart-dc-switches/esphome/casita-smart-dc-switches.yaml), `restore_mode: ALWAYS_OFF` like the others, named `Tank Heaters` and `Battery Heaters`. No rocker; HA and the device web page control them.

If mod 06 is not installed by the time this is built, the fallback is a plain fused 12 V switch for each branch and the pads' own thermostats, with Home Assistant watching the probes but not controlling the heat.

**Probes.** One 3-wire cable from the mod 09 enclosure: 3V3, GND and data (XIAO D1 / GPIO2) with the 4.7 k pull-up at the XIAO, daisy-chained to each probe; the grey tank and valve probes go out through the same floor penetration as the L02 cable. Battery and outside probes as decided in the open questions.

## Home Assistant automations

All on the trailer's Home Assistant. Thresholds are starting points.

| Automation | Trigger | Action |
| --- | --- | --- |
| Tank heaters on | Grey tank temperature below 38 °F **or** dump valve temperature below 36 °F, and outside below 40 °F | `switch.casita_smart_dc_switches_tank_heaters` on |
| Tank heaters off | Grey tank above 50 °F **and** valve above 45 °F, for 10 min; **or** outside above 45 °F | off |
| Battery heaters on | Battery temperature below 38 °F and state of charge (mod 04) above 20 % | `..._battery_heaters` on |
| Battery heaters off | Battery above 46 °F for 10 min; or state of charge below 15 % (protect the bank; alert instead) | off |
| Freeze warning | Any probe below 34 °F for 15 min, or any probe unavailable in freezing weather | Phone notification with the probe name and value; e-ink dashboard shows a snowflake (mod 08) |
| Charge blocked | Battery temperature at or below 33 °F and shore connected (mod 10) or solar present | Notification: "batteries below the charge cutoff; warming" |
| Shore budget | Mod 10 shore current above 26 A for 30 s | Turn off the space heater's smart plug; notify. Turn back on when below 20 A for 5 min |
| Cabinet reminder | Fresh bay temperature below 40 °F at 21:00 | Notification: open the lower cabinet doors |
| Heater interlock | Grey tank sensor online (mod 09) is off, or the grey tank is empty after a dump | Keep the tank heaters off unless the valve probe is below 36 °F; most pads are not rated to run on an empty tank for long (check the product) |

The same entities are mirrored to the home Home Assistant over the existing link, so the freeze warnings reach a phone wherever it is.

## Steps

### Phase 0: measure and decide (no purchases)

1. **Grey tank:** outside length, width, height; where the support angles, straps, drain fitting and vent are; the flat area for the mod 09 L02; the wall thickness estimate from mod 09 Step 1. Photograph from below. Decide pad count and size, and the L02 spot, together.
2. **Termination assembly:** valve body make and size (Valterra T1003 class 3 in and T1001 class 1-1/2 in are typical; confirm), stub lengths from the floor to the valves, clearance for insulation around the handles.
3. **Fresh tank bay:** whether it shares air with the cabin; where the fill, vent and drain penetrations are; whether the pump is at floor level.
4. **Battery compartment:** inside dimensions, clearances around the busbars and fuses, whether the lid seals, cable route to the nearest XIAO for a probe.
5. **12 V source:** a spare WFCO fuse position or the busbar; distance to the grey tank and to the battery compartment for wire sizing.
6. **Water heater door:** confirm it is a standard Suburban 6 gal door so a stock magnetic cover fits.
7. Record all of it here and in `photos/`; then fill in the parts list with real sizes and links.

### Phase 1: probes and alarms (do first; cheap, and gives the data for everything else)

8. Add the 1-Wire bus to the mod 09 firmware and enclosure; route the probes; name the entities.
9. Add the freeze-warning and charge-blocked automations. Camp one cold night with no heaters and read what the grey tank, valves, bay and battery actually do. That tells you whether the battery pads and the bay vent are needed.

### Phase 2: grey tank and drain protection

10. With the mod 09 L02 glued and tested, clean the tank bottom and apply the pads per their instructions (surface above 50 °F, alcohol-cleaned, pressed firmly; a heat gun in cold weather).
11. Wire the pads and the valve heater to relay 1 through the 10 A fuse; wire relay 1's coil to the Waveshare; flash the mod 06 firmware change. Test with the automation before any insulation goes on.
12. Spiral the heat cable on the stubs and valves with foil tape; foam insulation over it; sleeve.
13. Fit the polyiso to the tank bottom and sides, cut around the pads' leads, the L02, the drain and the probe; tape the joints.
14. Fit the belly pan to the supports and frame; seal the edges to the floor with foam tape, leaving the drip gap at the low point. Mark the pan "grey tank heater and sensors inside; remove before service".

### Phase 3: battery compartment

15. Fit the polyiso to the compartment walls, floor and lid with the clearances from Phase 0; nothing touching a busbar, fuse or lug.
16. Fit the battery pads; wire to relay 2 through the 10 A fuse; relay 2's coil to the Waveshare.
17. Test the battery automation against the probe with a known temperature (a bag of ice against the probe is enough).

### Phase 4: shell and practice

18. Window panels, vent pillow, draft stopper, water heater door cover, foam at the bay penetrations and the city inlet.
19. Write the cold-weather checklist (dump, antifreeze, cabinet doors, which heaters are on) into this README's [Operating practice](#operating-practice) after the first trip.

## Testing checklist

1. Each probe reads within 2 °F of a reference thermometer at room temperature and tracks ice water.
2. Each heater branch draws the expected current (pads 3-4 A each, cable 1-2 A, battery pads 2-3 A each) measured at the fuse holder; no warm wire or connector after 30 min.
3. Relay 1 and 2 default off at Waveshare power-up (watch the contacts through boot, as mod 06's [TESTS.md](../06-smart-dc-switches/TESTS.md) requires) and switch from Home Assistant and the device web page.
4. Pad surface temperature with the tank half full: warm to the touch, never hot (under about 110 °F at the pad surface against the tank).
5. Overnight at or below 25 °F with the automations on: grey tank probe stays above 38 °F; valve probe above 36 °F; battery probe above 41 °F; the mod 04 monitor's 24 h discharge matches the power budget within reason. Record the numbers here.
6. Dump valves pull freely in the morning; the outlet cap comes off; no ice in the stubs.
7. After a tow: belly pan secure, probes still reading, undercoating and sleeves intact.
8. Charge-blocked automation fires when the battery probe is forced below 33 °F; converter charges once the probe is above 41 °F.

## Operating practice

To be refined after the first cold trip:

- Before leaving: tanks dumped and the antifreeze quart in each; fresh tank full (water in the inside tank is the furnace's thermal mass, not a liability); cylinders above 50 %.
- Arriving: furnace on, heater automations enabled, cabinet doors open at night, vent cracked, window panels in.
- Daily: check the probe card on the dashboard; dump the grey when mod 09 says 80 %; antifreeze after.
- Leaving the trailer unheated for more than a night below freezing: drain and winterize per the manual, no exceptions.

## Safety notes

- **Water heater door:** never cover the exterior door while the gas burner is enabled. The door is the combustion air inlet and the exhaust path. Cover only on electric or with the gas switched off.
- **Furnace and range:** the furnace is the only cabin heat source that is vented outside. The manual forbids heating with the range. No unvented propane heater inside. Check the Safe-T-Alert LP/CO detector's date and test it before the season.
- **Heating pads on polyethylene:** follow the pad maker's surface-temperature and adhesion instructions; keep the pad flat with no air pocket (a hot spot can soften the tank); do not run a tank pad on a dry tank unless the product is rated for it. Keep pads away from the drain fitting and the L02.
- **Battery compartment:** nothing conductive or combustible within 1 in of a busbar, MEGA fuse or lug. Polyiso foil is conductive: keep the foil faces away from every live part, and tape the cut edges. No pad on or near a terminal. Pull the inline fuses before working in the compartment.
- **Every new 12 V conductor** has a fuse at its source sized to the wire, as in every other mod; the relay coil feeds included.
- **Polyiso and coroplast** are combustible; keep them clear of the furnace exhaust and the water heater vent on the sidewall and of anything on the underside that gets hot.
- **Shore power:** keep the sum of the space heater, water heater element and converter under the 30 A main; the automation is a backstop, not the plan.
- **Working under the trailer:** chocked, level, firm ground; clear of the valves when they are pulled.
- **Condensation** inside a cold fiberglass shell is a mold risk within days. Ventilate every night even when it costs heat.

## Open questions

1. Grey tank footprint, support layout and L02 spot: one pad or two, and where. (Phase 0, item 1.)
2. Where does the battery compartment probe connect: a cable from the mod 09 XIAO in the rear passenger bay to the rear center compartment, a second small XIAO, or a spare input on the mod 06 Waveshare board (it has no spare DI, but 1-Wire needs a GPIO, not a DI)? Decide after Phase 0, item 4.
3. Is mod 06 going to be installed before the first winter trip? If not, the fallback switches in [Wiring](#wiring) are used and the automations only alarm.
4. Does the fresh tank bay need a vent for furnace air, or does it already share air with the cabin?
5. Is the water heater on this trailer the SW6DE as the manual set suggests, with a standard door? (`docs/trailer.md` still says "model to record".)
6. The pad makers' instructions for running on an empty tank; this decides the heater interlock automation.
7. Whether the trailer will be used off-grid in the cold at all. If it is shore-only in winter, Section F shrinks to insulation and a probe, and the budget drops by half.

## Revisions

| Date | Change |
| --- | --- |
| 2026-10-21 | Proposed. Plan written from `docs/trailer.md`, the owner's manual (winter precautions page 46, winterization page 36, LP regulator page 23), the Suburban furnace and water heater manuals, and mods 01, 03, 04, 06, 09 and 10. Nothing measured, ordered or built |
