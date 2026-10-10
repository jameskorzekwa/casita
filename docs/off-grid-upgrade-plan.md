# Casita 17 Off-Grid Upgrade Plan

> Converted from the Google Doc *Casita 17 Off-Grid Upgrade Plan*. The **Latest updates** section supersedes anything in the **Original plan** that conflicts.

## Latest updates

### Update: fridge is 12V-only; inverted outlets wired directly from the inverter

- Fridge runs only on 12V (compressor type). This replaces the earlier '3-way absorption / run it on propane' notes. It never touches the inverter or the 120V panel, so nothing moves into the shore-only box for it. It draws from the batteries all the time off-grid: budget roughly 25-50Ah/day (more in heat). Add that to the overnight A/C estimates, which assumed a propane fridge.
- Shore-only box is now: 30A (to TS-30), 20A converter, 20A water heater, spare.
- The two factory inverted outlets are wired directly from the inverter. In the install guide, they come off the inverter and move onto a freed WFCO breaker (Phase 8), so they work on shore and battery. Check their wire gauge: 12 AWG = 20A breaker, 14 AWG = 15A breaker.

Step-by-step install guide (TS-30 + Renogy 2000W whole-panel inverter, with diagrams): [modifications/03-whole-panel-inverter](../modifications/03-whole-panel-inverter/README.md)

### Update: A/C is Coleman 37200 series (R-32); SpartanStart compatibility

The Casita A/C is a Coleman-Mach 37200-series unit = Mach 8 Plus family, R-32 refrigerant. 37201-xxx = Mach 8 Plus Cub 9,200 BTU (successor to the R-410A 47201). Published specs for 37201-076: 9.3A (low fan) / 9.9A (high fan) cooling, ~1,150W running, ~87 lb. LRA not published - read the rating plate under the shroud.

SpartanStart install table (https://spartanpower.com/wp-content/uploads/2024/07/SpartanStart_Instructions_07_18_2024.pdf, p.4): does NOT list the 37200 series, R-32, or 'Mach 8' at all. It only has two generic Coleman rows: Run=White/Common=Black/Start=Red-or-Orange, and Run=Yellow/Common=Orange/Start=Purple. Spartan: 'Don't see your model? ... we can let you know how to wire it correctly.' Call (775) 800-1725 or sales@spartanpower.com with the full model number.

Likely R-32 compressor colors (from Coleman sticker 1976A760 on the sister R-32 38000 series - NOT confirmed for 37201): Run=WHITE, Start=RED, Common=PURPLE (purple all the way to the compressor). This matches neither generic Spartan row. If confirmed: SpartanStart Blue -> Run (white), Black -> Common (purple), Red -> Start (red). Never swap Run and Start.

The diagram sticker inside the unit's electrical-box lid is authoritative; another R-32 Mach 8 owner found generic Coleman diagrams did not match the box.

Start-assist parts: the older 47201 had a start capacitor + PTCR; the R-32 diagram shows them as optional. If present, Spartan requires removing/isolating them. Spartan: allow 2 minutes for the run capacitor to discharge.

Fallback: Forest River owners installed the Coleman 1497-3601 on R-32 38000-series units with Coleman support guidance.

### Update: shore-only box breaker sizes (correction)

Converter and water heater are both on 20A breakers in the WFCO panel. Keep both at 20A in the shore-only box (this replaces the earlier '15A converter' note). Confirm each wire is 12 AWG (printed on the jacket); if either is 14 AWG, use a 15A breaker for that circuit instead.

Shore-only box: 4-space with a 30A main breaker (or main-lug box fed by 10 AWG from the shore side); 20A converter, 20A water heater, fridge outlet TBD, spare. Feed it with 10 AWG tapped from the shore side upstream of the TS-30.

### Update: water heater confirmed gas/electric; move it to the shore-only box

The water heater has an electric element (it has its own 120V breaker in the WFCO panel). Its circuit moves to the shore-only box along with the converter.

Shore-only box (4-space) contents:
1. WFCO converter - 15A
2. Water heater electric element - same breaker size as the WFCO panel breaker it came from (check 15A vs 20A), same wire gauge
3. Fridge 120V outlet - pending fridge model check (if 3-way with AUTO)
4. Spare
Move black (hot) and white (neutral) to the shore-only box; ground (green) stays on the WFCO ground bar. Extend with same-gauge wire in a junction box if needed. Label the empty WFCO slots 'Moved to shore-only box'.

Why: the ~1,400W element would draw ~120A DC on inverter (drains the bank in ~4 hours) and with the A/C exceeds the 2,000W inverter. Propane mode is unaffected (its 12V control power comes from the DC fuse side).

Shore-power note: A/C (~12A) + water heater element (~12A) + converter charging (up to ~8-10A AC) can approach the 30A main. If the main trips on shore, switch the water heater to propane while the A/C runs.

### Update: soft start purchased (Spartan Power SpartanStart)

Bought SpartanStart (Spartan Power) instead of the Coleman 1497-3601 because of delivery time. ~$189, 4.5 stars (~270 ratings), 3-year warranty, rated for RV A/Cs up to 20K BTU on a 2,000W inverter/generator, 3-wire install at the compressor (R/C/S), no learning cycles. Reviews include successful Coleman Mach installs. Reduction percentage is not published.

Notes: confirm the Mach 8 Cub is on Spartan's install table; kill power at the A/C breaker AND unplug shore/turn off inverter before opening the rooftop box; discharge the run capacitor before touching terminals; if the unit has an existing start capacitor/relay or PTCR, follow Spartan's instructions for it. A third-party soft start on a trailer under warranty can complicate an A/C warranty claim - keep the removed parts/photos. Test on shore first (clamp meter with inrush mode), then on inverter once the transfer switch is installed.

### Update: overnight A/C runtime estimate (Colorado summer, 600 Ah)

Amps vs amp-hours: amps (A) = rate of flow right now; amp-hours (Ah) = total used. 36A for 1 hour = 36Ah. Usable bank ~510Ah (85% of 600Ah).

Why nights are easy in Colorado: typical July lows ~60F on the Front Range, ~65F on the Western Slope (Grand Junction), 40s-50s in the mountains. A 17' Casita with two sleeping people has a small night heat load (~1,300-1,800 BTU/hr at 75-80F outside; near zero once outside drops below ~68F). Most of the A/C energy goes to the bedtime pull-down of the heat stored in the trailer from the day.

Estimated battery use per night (A/C + ~20Ah of other overnight loads). These are calculated estimates - measure with the shunt on the first trips.
- Cool night (mountains / typical Front Range): Mach 8 on inverter ~20-60Ah; 12V X2 ~20-50Ah. Fan/open windows often enough.
- Warm night (Western Slope, Front Range warm spell: 75-80F at bedtime, lows mid-60s; A/C needed ~3-4 hours): Mach 8 ~220-280Ah; 12V X2 ~110-150Ah.
- Hot all-night (rare heat wave, lows 70F+): Mach 8 ~420-500Ah (empties the bank in ~1 night); 12V X2 ~200-250Ah.

Solar refill: 200W portable in Colorado sun ~50-65Ah/day, ~30-45Ah net after daytime loads.

Nights per charge (no daytime A/C): Cool = indefinitely with solar. Warm = Mach 8 ~2-3 nights, X2 ~5-7 nights. Hot all-night = Mach 8 ~1 night, X2 ~2.5-3 nights.

Mach 8 watch-out: many RV analog thermostats run the indoor fan continuously in COOL mode. Through the inverter that fan alone is ~13-16A DC (~100+Ah over 8 hours). Use a thermostat/fan setting that cycles the fan with the compressor, or switch the A/C off once the night cools.

Also: turn the inverter off when not needed (~1.5-2A idle, ~12-16Ah overnight).

Tactics: shade + Reflectix/closed blinds during the day; pre-cool before bed; set 72-74F; once outside is cooler than inside, switch to windows + MaxxAir fan (~2-3A); camp above ~7,000 ft when possible (A/C rarely needed).

### Update: second battery installed

Both Renogy Core Mini 12.8V 300Ah (RBT12300LFP-M) batteries are installed in parallel (600Ah bank). Battery facts: 200A continuous BMS, 150A max charge, M8 terminals (8 N-m / 70.8 in-lb), 55.1 lb, NO self-heating (charging disabled below 32F), NO Bluetooth (use a shunt monitor), max 4 in parallel. Each battery has its own fuse at its positive terminal; both land on a common busbar. Re-check balance (<0.1V apart) every ~6 months.

Note: the factory solar package has no microwave on this trailer.

### Next project: automatic shore/inverter transfer to the whole panel

Goal: the WFCO panel (WF-8900-AD series) is fed by shore power when plugged in, or by the Renogy 2000W inverter when not, automatically. The built-in WFCO converter must never run from inverter power.

**DESIGN**

- Transfer switch: Go Power GP-TS-30 (30A, switches BOTH hot and neutral). Shore on the dominant (N.O.) side, inverter hardwire output on the default (N.C.) side, output to the WFCO 30A main breaker. Manual 'Configuration C' covers inverter vs shore.
- 'Shore-only' mini sub-panel: a small 2-4 space breaker enclosure fed from the shore side UPSTREAM of the TS-30. Move these circuits into it so they only ever get shore power:
  - 1. WFCO converter (its black hot leaves the CONV breaker; white leaves the panel neutral bar; green stays on the panel ground bar). 15A breaker.
  - 2. Refrigerator 120V outlet (if 3-way absorption fridge in AUTO mode) - otherwise on inverter it will run its ~300W electric heater continuously. On shore-only, AUTO falls back to propane when unplugged.
  - 3. Water heater electric element (if equipped) - otherwise it can drain the bank.
- Result: fully automatic, no breakers to flip. Plugged in: everything on shore, converter charges. Unplugged + inverter on: outlets and A/C on battery; converter, fridge electric, and water heater electric are simply dead.
- Factory 'inverted outlets': find out how Casita feeds them. If from the inverter's hardwire terminal or front receptacles, move them onto a panel breaker (they then follow the TS-30 automatically). Never feed them from both the inverter and the panel.

NEUTRAL-GROUND BONDING (Renogy 2000W P2)
- Renogy P2 manual (Version A2, Feb 2023), terminal table: 'Note that Neutral and Ground are bonded inside.' Manual: https://www.renogy.com/cdn/shop/files/INVT-P2-Manual_21ceaa11-23a7-48d5-ab94-d5c37b200c96.pdf
- This is the CORRECT behavior for this design, provided: (a) the TS-30 switches neutral (it does), and (b) the WFCO panel has NO neutral-ground bond of its own (RV panels should not; confirm neutral and ground bars are separate, no bonding screw/strap).
- Owners who saw the Renogy built-in GFCI trip were feeding panels that had their own N-G bond, or transfer switches that did not switch neutral.
- VERIFY your unit: label says '-P2'. Test with inverter on and disconnected from everything: N-to-G ~0V = bonded (expected); ~50-60V = floating (stop and reassess).
- Terminal-block order differs between manual pages (N-G-L vs L-N-G): go by the markings on the unit.
- Ground the inverter chassis lug to the trailer chassis with 12 AWG.
- Renogy specs: 2000W continuous, 4000W surge (1 s), max DC 166.6A, recommended battery fuse 250A, low-voltage shutdown 10.5V.
- The manual warns never to connect inverter output to a panel also fed from shore at the same time; the TS-30 prevents that.
- Built-in GFCI trips at 50-100 mA (not a 5 mA personnel-grade GFCI); keep the trailer's GFCI outlets in place.

**PARTS**

- Go Power GP-TS-30 transfer switch (~$124)
- 2-4 space breaker enclosure + breakers (~$30-50)
- 10 AWG THHN black/white/green for the 30A path (~$25); 12/14 AWG for relocated branch circuits; junction boxes, strain reliefs, Wagos (~$25)
- Soft start for the Mach 8 (below)

**TEST SEQUENCE**

1. Install soft start; confirm the A/C starts cleanly on shore.
2. Install TS-30 + shore-only sub-panel in one de-energized session.
3. On shore: panel live, shunt shows charge current, fridge works.
4. Unplug shore, inverter on: outlets and A/C live; shunt shows NO charge current (converter isolated); fridge on LP; GFCI outlets test correctly.
5. Clamp-meter A/C start and running current on inverter.

### Soft start for the Mach 8 (stopgap until a 12V A/C)

Recommended (cheapest genuine OEM, preserves Coleman warranty): Coleman-Mach Soft Start Kit 1497-3601 - https://www.amazon.com/dp/B0CF41ZW4W (~$214). Airxcel's 2025 catalog lists it as fitting ALL Coleman-Mach rooftop units, including the R-32 37201-076 Mach 8 Cub Plus.

Alternatives: Micro-Air EasyStart Breeze Bluetooth ASY-399-X20-BL - https://www.amazon.com/dp/B0FDMQY1MF (~$355); SoftStartRV - https://www.amazon.com/dp/B07YBMCTBC (~$295).

AVOID: $39-100 'compatible with 1497-3601' clones (some are just a hard-start capacitor/relay, not an electronic soft start).

### Updated 12V A/C options (re-verified; supersedes the earlier A/C section)

**#1:** Nomadic Cooling X2 Helix Gen II 12V - ~9,586 BTU rated / ~8,950 avg, ~36A eco / ~59-64A max, 42.8 lb, 14x14 drop-in, ~$3,425. https://nomadicinnovations.com/products/x2-helix-12v-48v-dc-rv-van-rooftop-air-conditioner (Panther: https://pantherrvproducts.com/nom-697/ white, https://pantherrvproducts.com/nom-333/ black). US support, Elkhart IN.

Value: Velit 2000R 12V - 8,000 BTU at 12V, ~20A eco / up to 60A, ~66 lb, 14x14, $1,829. https://velitcamping.com/products/velit-2000r-rooftop-air-conditioner-12v-24v (etrailer VE87QV black / VE77QV white).

Middle: Velit V3 12V - ~10,000 BTU claimed, 25-63A, 65 lb, 14x14, built-in exhaust fan, $2,399 (new, few reviews; ratings likely optimistic). https://velitcamping.com/products/velit-v3-with-ventilation-12v-24v-48v-rooftop-air-conditioner

Skip: Dometic RTX 2000 (larger cutout, 6,800 BTU), Mabru (12.6x25.2 slot, 90 lb), CountryMod (flat-roof install only), generic Amazon units.

Before buying: measure roof thickness at the opening (crossbar clamp range) and roof curvature across the ~30x27 in footprint; plan for a shim/butyl bed on the curved fiberglass roof.

Shore-power note: the WFCO 55A converter cannot keep up with an X2 at full power (~60A) plus other DC loads, so the bank slowly drains even when plugged in. Eco mode is fine. A future inverter/charger (higher charge current) fixes this.

## Original plan

Vehicle / Trailer
- Trailer: 2026 Casita Liberty 17 (Deluxe) with factory Solar System Package
- Factory equipment: 300Ah LiFePO4 battery, 2,000W inverter, 200W portable solar panel, Coleman Mach 8 Plus Cub 9,200-BTU A/C
- Tow vehicle: 2026 Toyota RAV4 PHEV — 3,500 lb tow rating, 750 lb hitch tongue-weight limit, hitch rated to 5,000 lb

Goal

A camper that runs its normal appliances off-grid without routinely flipping breakers, switches automatically between shore and battery power, provides useful battery-powered A/C, recharges from solar/shore/tow vehicle, clearly shows remaining battery capacity, and stays within all trailer, axle, roof, hitch, and tow-vehicle limits.

### The #1 constraint: weight (RAV4 PHEV)

The binding limit is the RAV4's 3,500 lb tow rating, which is IDENTICAL to the Casita's 3,500 lb GVWR. You have essentially zero margin at the trailer's max rating.

Where a loaded Liberty Deluxe sits before this project:
- Dry weight: ~2,480 lb
- Fresh water (16 gal): ~130 lb
- Two 20 lb propane tanks (full): ~80 lb
- Second 300Ah battery: +60 lb
- Gear/food/bedding/tools: 200–400 lb
= ~2,950–3,150 lb before adding inverter/charger, extra solar, wiring, or a generator.

You will hit the 3,500 lb ceiling before you run out of physical space. This likely forces a choice between a generator and maximum battery/solar — you probably cannot have everything on a RAV4.

Tongue weight: Your 750 lb hitch limit is generous (loaded Casita 17 runs 350–450 lb). But tongue weight must stay at 10–15% of actual trailer weight (~300–450 lb) for stability, so the 750 lb rating is safety margin, NOT a target. Do not pile weight on the tongue just because the hitch can hold it.

### Step one: second battery

You already bought a matching second 300Ah battery (confirmed identical with Casita). Good — matching model/age is the right call for a parallel bank.

**WHERE TO INSTALL THE SECOND BATTERY**

Factory battery location: a rear exterior side compartment (Group-31 sized). It is full and cannot hold a second large battery. Your second battery (~20.5" long, ~60 lb) is too big for that box and should NOT go on the tongue.

Recommended: mount the second battery INSIDE, low, and as close to the axle as possible.
- BEST: Under the dinette seat (street side, over/near the wheel well). Closest to the axle = best handling; short-ish cable run forward to meet the existing harness; keeps battery warm/dry. Needs a secure, vented tray.
- Avoid: Front bench/bed pedestal (adds tongue weight; longer DC run).
- Avoid: Rear near the factory box (pulls tongue weight down; sway risk).
- Bunk area is not available on a Deluxe (bathroom is there).

Why over the axle: 60 lb over the axle adds almost nothing to tongue weight and keeps the trailer balanced.

SPLIT-BANK WIRING (batteries in two locations) — do this carefully:
1. Use equal-length, equal-gauge cables from EACH battery to a COMMON busbar. Do not daisy-chain one battery off the other.
2. Fuse each battery individually at its own terminal, plus a main system fuse.
3. Balance both batteries to the same resting voltage (ideally full, ~13.4V) before paralleling the first time.
4. Confirm Renogy's parallel rules and any pre-charge procedure in the manual for your exact model.
Cleanest approach: run the new battery's cables to the same interior busbar/breaker point where the factory battery's cabling already terminates.

### A/C recommendation: replace, don't add

Replace the Mach 8, don't add a second unit. A 17' Casita has only one A/C roof opening; the other 14x14 opening is the vent/fan (keep a MaxxAir there for low-power cooling). Two ~80 lb units on a curved fiberglass roof is needless weight and leak risk.

DO 12V A/Cs WEIGH MORE? NO — THEY WEIGH LESS.
- Nomadic X2: ~44 lb (−43 lb vs Mach 8, about half!)
- Nomadic X3: ~57 lb (−30 lb)
- Velit 2000R: ~66 lb (−21 lb)
- Coleman Mach 8 Cub (baseline): ~87 lb
Swapping to 12V actually GIVES BACK payload — a real win for the RAV4 weight budget.

**#1 RECOMMENDATION: NOMADIC COOLING X2**

Buy: https://pantherrvproducts.com/nom-5/  (~$3,075–3,175)
- True 14x14 drop-in (matches existing opening, no cutting)
- ~44 lb (lightest option)
- ~8,200–8,950 BTU (matches Mach 8's 9,200 for a 17' trailer)
- 27A eco / ~55A max at 12V
- US company (Elkhart, IN), real dealer support (Panther RV), app control

**VALUE ALTERNATIVE: VELIT 2000R**

Buy: https://velitcamping.com/products/velit-2000r-rooftop-air-conditioner-12v-24v  (~$1,829)
- ~$1,300 cheaper, fits 14x14, ~66 lb, only ~20A eco draw (lowest of the group)
- Trade-offs: ~8,000 BTU (slightly less), smaller US support/parts network

**SKIP THESE:**

- Dometic RTX 2000 — needs 18.9x15.3" cutout (not 14x14) and only ~6,800 BTU (undersized)
- Mabru RV12 — needs a long slot cutout; maker says do not self-install

IMPORTANT: These 12V A/Cs are DC-only — they do NOT run on shore power directly. Even plugged in at a campground, the A/C runs off the battery while the charger replenishes it. So the A/C swap COMMITS you to the battery + inverter/charger build. Buy the A/C alongside the charging upgrades, not in isolation.

### Why an inverter/charger (not just a bigger inverter)

To make everything automatic, replace the standalone 2,000W inverter with an INVERTER/CHARGER (e.g., Victron MultiPlus class), which provides:
1. Built-in automatic transfer switch — shore in, whole panel out; unplug and it switches to battery in ~20 ms. No manual transfer switch, nothing to remember.
2. It IS the charger — permanently retire the WFCO converter so the charging "loop" cannot exist.
3. PowerAssist — supplement weak shore power or a small generator with battery power.
4. Automatic neutral-ground bonding — the safety detail the original plan missed.

With a 12V A/C, the A/C no longer loads the inverter, so a MultiPlus 12/2000 (~$900) is likely plenty (microwave + everything else). If you keep a 120V A/C instead, you need a larger inverter and possibly automatic load management. Note: your 30A/120V shore connection is only ~3.6 kVA — a bigger inverter does not create unlimited campground power.

### Full phased plan

Phase 1 — Document the trailer and establish the energy budget
- Record exact models/labels: battery, inverter, converter/power center, A/C, fridge, microwave, water heater, solar controller, existing fuses/breakers/cabling.
- Get factory dry weight AND dry tongue weight for YOUR exact build (with options) from Casita.
- Build a paper weight budget for the WHOLE planned build vs. 3,500 lb and 750 lb limits.
- Install a shunt-based battery monitor (e.g., Victron SmartShunt) early.
- Measure several days of real consumption (daily, overnight, microwave, fridge mode, electronics), and measure the existing A/C's energy use on shore power.

Phase 2 — Select the A/C and finalize the electrical design
- Compare: keep Mach 8 + soft start vs 12V variable-speed vs 120V variable-speed. Choose by documented performance/fit, not "12V" alone.
- Select the inverter/charger sized to the A/C decision and simultaneous loads.
- Design automatic load management (shed low-priority loads instead of flipping breakers).
- Produce AC/DC single-line diagrams, cable schedule, fuse/breaker schedule, grounding/bonding design, bank layout, mounting/ventilation plan, and BOM. Have a qualified RV electrical installer review.

Phase 3 — Expand the battery bank and build the DC foundation
- Expand to at least 600Ah if the design supports it (600Ah ~ 7.68 kWh nominal; ~6.1–6.9 kWh usable at 80–90%).
- Verify battery compatibility and parallel rules; balance before connecting.
- Install rated distribution: restraints, per-battery fusing, main protection, covered busbars, disconnects, shunt, dedicated fused circuits, protected routing, labels.
- Choose placement deliberately (tongue weight, structure, cable length, temperature, water, ventilation, service access).

Phase 4 — Automatic shore/battery power and appliance controls
- Integrate the inverter/charger with protected AC input/output.
- Remove the old standalone inverter (or retain only for a separately designed purpose).
- Permanently disconnect/isolate the original converter per the design (labeled, documented).
- Verify neutral/ground behavior and protective-device operation on both sources.
- Configure input-current and charge limits.

Phase 5 — Install the selected A/C
- Confirm approved mounting for the Casita's curved roof; remove old unit; inspect opening.
- Install support/adapter/gasket/ceiling assembly and the dedicated supply circuit.
- For 12V: test shore-power energy balance (charger must supply A/C + desired charging, or reduce within the shore limit). Being plugged in does NOT guarantee charging.
- Verify sealing, drainage, clearances, roadworthiness; leak-check.

Phase 6 — Expand solar around the measured requirement
- Survey the roof (space around A/C and vent, curvature, shading, access) before selecting panels; approve the mounting method.
- Use roof panels for unattended daily charging plus the existing 200W portable for supplemental production.
- Budget realistically: Daily solar ~ panel rating x peak-sun-hours x ~0.75 yield. Example at 4 sun-hours: 200W~0.6 kWh, 600W~1.8 kWh, 1000W~3.0 kWh/day.
- Reality: more battery extends time between charges; more generation determines whether you can stay indefinitely. Solar on a 17' Casita restores roughly ~1 hour of A/C per sunny day.

Phase 7 — Travel charging and backup source
- DC-DC charger from the RAV4 (verify alternator capacity, manufacturer restrictions, cable route/voltage drop, connector rating, protection, engine-run detection, start-battery protection). Useful if you drive regularly.
- Backup generator for long hot-weather stays (size for loads + charger + altitude/temp derating). Never run a generator in the camper or any enclosed space. Note: on a RAV4 you may have to choose generator OR max battery/solar due to weight.

Phase 8 — Commission and prove on a short trip
- Installer acceptance tests: transfer both directions, simultaneous loads, load shedding, low-SOC reserve, A/C restart protection, charging with A/C running, GFCI/grounding, no backfeed to the inlet, thermal checks under sustained load, solar/DC-DC operation, shunt calibration.
- Keep documentation in the camper (diagrams, models/serials, fuse schedule, settings, operating + emergency instructions, maintenance schedule).
- Do a 2–3 night trial trip close to support; log start/end SOC, solar harvest, A/C energy, overnight reserve, water/waste use, any need for backup charging.
- Do not rely on battery A/C alone to protect unattended people or pets.

### Recommended order of spending

1. Inspection, weighing, monitoring — establishes facts, avoids incompatible purchases
2. A/C comparison + complete system design — sets inverter/charger/battery/cable requirements
3. Battery expansion + protected DC distribution — foundation (STEP ONE, in progress)
4. Inverter/charger + automatic controls — delivers no-breaker-flipping operation
5. A/C installation — delivers the cooling target
6. Solar expansion — replaces daily energy
7. DC-DC charging and/or generator backup — resilience
8. Commissioning + trial trip — proves the system

### Other considerations

- Fridge: 3-way absorption — run it on PROPANE off-grid (12V is maintain-only; inverter/AC mode uses ~300W continuously — never do that on battery).
- Never run A/C + microwave together on battery (combined load exceeds inverter and BMS limits).
- Reduce cooling demand: window covers/Reflectix, awning, park nose-east, MaxxAir roof fan (~2–3A) — each A/C hour avoided is ~1.4 kWh you don't have to generate.
- Water/waste (~16 gal fresh) may limit a long stay before electricity does; carry jugs and a portable grey tank.
- Propane: two 20 lb tanks run fridge/water heater/furnace/stove ~1–3 weeks; consider a Mopeka tank gauge.
- Starlink: run on 12V (DC adapter), not through the inverter.
- Inverter idle draw: ~15–20W; use search/AES mode or turn off overnight.
- Preserve safety systems: disconnects/load-shedding must not disable breakaway braking or required alarms.

### Notes and unconfirmed items

- Exact 2026 factory models (inverter, converter/WFCO or PD, A/C part number) are inferred from owner reports; your trailer's labels are authoritative. Confirm with Casita on your build order.
- Factory location of the 300Ah lithium on 2025–2026 solar-package builds is inferred (rear exterior Group-31 compartment) but not factory-documented.
- Published factory dry tongue weight for the Liberty Deluxe not cleanly available; owner-measured tongue weights are 350–450 lb.
- All prices/weights captured during research and subject to change; verify at purchase.
- Cable gauges, fuse sizes, roof mounting, and A/C fit in this document are preliminary guidance, not a final installation specification. Final choices must follow equipment instructions, actual routing/lengths, and installer review.
