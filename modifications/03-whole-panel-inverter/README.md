# Casita 17 - Whole-Panel Inverter Install Guide (Renogy 2000W + Go Power TS-30)

Trailer: 2026 Casita Liberty 17 Deluxe. Goal: when plugged into shore power, the whole trailer runs on shore power and the WFCO converter charges the batteries. When unplugged with the inverter on, the whole WFCO panel, including the A/C, runs from the 600Ah battery bank, automatically, with no breakers to flip. The converter and the water heater's electric element can only ever run on shore power.

> **Status: planned.** Parts purchased: Go Power GP-TS-30 transfer switch and Spartan Power SpartanStart soft start. Still to buy: the shore-only breaker box and wire. The soft start (Phase 2) is also documented on its own in [02-ac-soft-start](../02-ac-soft-start/README.md).

Related: [off-grid upgrade plan](../../docs/off-grid-upgrade-plan.md) · [trailer equipment](../../docs/trailer.md) · manuals: [GP-TS-30](../../manuals/electrical/go-power-gp-ts-30-transfer-switch-manual.pdf), [Renogy 2000W P2](../../manuals/electrical/renogy-2000w-p2-inverter-manual.pdf), [SpartanStart](../../manuals/air-conditioning/spartan-power-spartanstart-instructions-2024-07.pdf)

Originally written as the Google Doc *Casita 17 - Whole-Panel Inverter Install Guide*; this file is now the maintained copy.

## Read this first

### Safety

This guide covers 120V AC shore-power wiring and a high-current lithium battery bank. Both can kill or start a fire. Go Power's own manual says the TS-30 should be installed by qualified service personnel. If any step is unclear, or what you find in the trailer doesn't match this guide, stop and ask, or have an RV electrician do or inspect the 120V work. Having a pro inspect the finished work before first use is cheap insurance.

### What is confirmed vs. what you must verify

Confirmed from manufacturer documents:

- Renogy 2000W P2 inverter: 2000W continuous / 4000W surge for 1 second, max DC draw 166.6A, recommended battery fuse 250A, ships with 1/0 AWG 3 ft battery cables, chassis ground wire 12 AWG, DC terminal torque 14 N-m, hardwire terminal block with L/N/G. Manual: 'Neutral and Ground are bonded inside.'
- Go Power TS-30 'Configuration C' (inverter vs. another source): inverter on terminals 7 and 8 (normally closed, the default source); the dominant source (shore) on 5 and 6 (normally open); output on 3 and 4. 20-45 second delay before switching to the dominant source. 8 AWG chassis ground to the TS-30 ground bar. Manual: 'Ensure the inverter never provides power to the charger.' Do not mount it in a battery or propane compartment.

Verify on your trailer (steps below tell you how):

- The inverter label says '-P2' and the inverter's neutral-ground bond really measures as bonded.
- The WFCO panel has no neutral-to-ground bond of its own.
- Which TS-30 terminal in each pair is hot vs. neutral (from the diagram inside the TS-30 lid).
- Whether the two factory inverted outlets' cable lands on the inverter's hardwire terminal block or plugs into a front receptacle (confirmed: they're wired directly from the inverter).
- The A/C compressor wire colors (for the soft start).
- Fridge: CONFIRMED 12V-only. It runs from the battery/DC side, so it never touches the inverter or the 120V panel. Nothing to move.
- The inverter's existing DC cable size and fuse.

## How the system works

### Diagram 1 - Before (factory)

```text
  Shore cord (30A)
       |
       v
  +-------------------------------------------+
  | WFCO WF-8955-AD power center              |
  |  [30A MAIN]                               |
  |    |-- [20A] A/C (Coleman Mach 8 Plus)    |
  |    |-- [20A] CONVERTER -> charges battery |
  |    |-- [20A] WATER HEATER electric element|
  |    |-- [ .. ] outlets, other circuits     |
  +-------------------------------------------+

  Batteries (600Ah) --> Renogy 2000W --> 2 "inverted" outlets
  (inverter is not connected to the panel; A/C is shore-only)
```

### Diagram 2 - After (this project)

```text
  Shore cord (30A, 10 AWG)
       |
       v
  +-------------------------------------+
  | SHORE-ONLY BOX (new)                |
  |  main lug L1, neutral bar,          |
  |  separate ground bar (NO bond)      |
  |   [30A] -> TS-30 shore input  ------|-----------+
  |   [20A] -> WFCO converter           |           |
  |   [20A] -> water heater element     |           |
  |   [ -- ] -> spare                   |           |
  |                                     |           |
  +-------------------------------------+           |
                                                    |
  Batteries -> Renogy 2000W P2                      |
               hardwire L / N / G --+               |
                                    |               |
                                    v               v
                  +-------------------------------------+
                  | GO POWER TS-30  (Configuration C)   |
                  |   inverter in = 7 / 8  (N.C.)       |
                  |   shore in    = 5 / 6  (N.O.)       |
                  |   output      = 3 / 4               |
                  +-------------------------------------+
                                    |
                                    v
                  +-------------------------------------+
                  | WFCO panel [30A MAIN]               |
                  |   [20A] A/C (+ SpartanStart)        |
                  |   [ .. ] outlets, other circuits    |
                  |   converter + WH breakers: empty    |
                  +-------------------------------------+
```

### Diagram 3 - What powers what

```text
 SITUATION                   PANEL FED BY  CONVERTER  WH ELEC
 --------------------------  ------------  ---------  -------
 Plugged in (after delay)    SHORE         ON         ON
 First 20-45 s after plug-in INVERTER *    ON         ON
 Unplugged, inverter ON      INVERTER      OFF        OFF
 Unplugged, inverter OFF     nothing       OFF        OFF

 * If the inverter is off, the panel is simply dead for
   20-45 s until the TS-30 clicks over to shore.
 The converter can never run from inverter power because it
 is wired upstream of the TS-30, on shore power only.
```

### Diagram 4 - Where neutral meets ground (exactly one place)

```text
 On shore power:  at the campground pedestal.
                  The TS-30 switches BOTH hot and neutral, so
                  the inverter's internal bond is disconnected.
 On inverter:     inside the Renogy 2000W P2 (factory bond).
 NEVER:           WFCO panel, shore-only box, TS-30.
                  Their neutral bars and ground bars stay
                  separate.

 Ground (green) wires are never switched. They all tie together:
   shore-only box GND = TS-30 GND bar = WFCO GND = trailer chassis
```

## Parts, tools, and supplies

### Already purchased

- Go Power GP-TS-30 30A automatic transfer switch
- Spartan Power SpartanStart soft start

### To buy

- Shore-only box: a small indoor 120/240V main-lug load center with at least 6 spaces (Square D QO, Eaton BR, or Siemens), plus that brand's separate ground bar kit. Breakers to match that brand: 1 x 30A single-pole, 2 x 20A single-pole.
- 10/2 with ground cable (10 AWG): shore-only box to TS-30, inverter to TS-30, and TS-30 to WFCO main. Measure each run and add 2 ft per run.
- 12/2 with ground cable (12 AWG): for extending the converter and water heater circuits to the shore-only box, if they don't reach.
- 8 AWG green stranded wire + ring terminals: TS-30 ground bar to chassis.
- 12 AWG green stranded wire + ring terminal (or reuse what's there): inverter chassis ground lug to chassis (Renogy spec for the 2000W).
- Cable clamps/connectors for every knockout, cable staples or straps, and junction boxes with covers for any splice.
- Splice connectors rated for the wire size (Wago 221 for 12 AWG; for 10 AWG use connectors rated for 10 AWG and 30A).
- Labels or a label maker.

### Tools

- Digital multimeter (AC volts, DC volts, continuity/ohms)
- Non-contact voltage tester
- 3-light plug-in outlet tester with GFCI test button
- Clamp meter (DC-capable is ideal; inrush mode is a bonus)
- Torque screwdriver (inch-pounds), wire strippers, crimper for ring terminals, screwdrivers, drill for mounting
- Phone camera: photograph every connection before you change it

## Phase 0 - Gather information (no tools, no risk)

Step 0.1 - Record model numbers and photograph labels: inverter (confirm '-P2'), WFCO power center, A/C data plate (full model number, e.g. 37201-076, plus RLA and LRA), refrigerator, water heater.

Step 0.2 - Trace how the factory 'inverted' outlets are fed. Look at the inverter: is a cable going into its hardwire terminal block (behind the small cover on the AC end), or is a cord plugged into one of its front receptacles? Photograph it. You'll need this in Phase 8.

Step 0.3 - Find the shore cord cable. Follow the cable from the exterior shore inlet to the WFCO panel. Note where it enters the panel and how much slack it has.

Step 0.4 - Choose mounting spots for the TS-30 and the shore-only box. Inside the trailer, out of weather, near the WFCO panel and the shore cord path, and accessible later. NOT in the battery compartment, the propane compartment, or under the sink drain. Make sure the inverter-to-TS-30 cable route is reasonable.

Step 0.5 - Check the inverter's DC wiring. With the A/C on the inverter, it will pull roughly 110-150A for hours. Renogy ships 1/0 AWG cables and recommends a 250A battery fuse. Confirm Casita used 1/0 AWG (or bigger) and a fuse of about 250A, with tight lugs. If the cable is smaller (e.g. 4 AWG), replace it with 1/0 before running the A/C on battery.

Step 0.6 - Call Spartan Power at (775) 800-1725 (or email sales@spartanpower.com) with the A/C's full model number and ask them to confirm the SpartanStart wiring for a Coleman 37200-series R-32 unit with a purple common wire. Their install table doesn't list this model.

Step 0.7 - Read the TS-30 manual and the Renogy P2 manual's AC wiring section once, start to finish.

## Phase 1 - Power-down procedure (use at the start of every work session)

1. Turn the A/C off at the thermostat.
2. Unplug the shore cord at the pedestal or generator. Tag the plug 'DO NOT PLUG IN'.
3. Turn the inverter off at its ON/OFF/REM switch, and at the remote if you have one.
4. Isolate the inverter from the batteries: remove its DC fuse or open its battery disconnect. (Check whether the trailer's battery disconnect switch actually disconnects the inverter. If it doesn't, the inverter's own fuse or disconnect is what you use.)
5. Switch off every breaker in the WFCO panel (and the shore-only box once it exists).
6. Wait at least 2 minutes for capacitors (A/C run capacitor, inverter input capacitors) to discharge.
7. Verify dead with a meter: 0V AC at the WFCO main breaker terminals and neutral bar, and at the inverter's hardwire terminals. Use the non-contact tester as a second check.

## Phase 2 - Install and test the soft start (shore power only)

Do this first, on shore power, before changing any panel wiring. If the soft start doesn't work, you'll know before the A/C is depending on the inverter.

### Diagram 5 - SpartanStart wire identification

```text
 Spliced INLINE twice: supply side AND compressor side
 SpartanStart lead   ->  compressor winding
   BLUE              ->  RUN    (R)   WHITE wire  (confirmed)
   BLACK             ->  COMMON (C)   BLACK wire  (confirmed)
   RED               ->  START  (S)   RED wire    (confirmed)

 * Confirmed from this unit's sticker 1976-764 (PP 03-20)
   - matches Spartan's standard Coleman row.
   Still check the colors at the compressor itself
   before cutting. Never swap RUN and START.
 Remove or isolate any start capacitor, start relay or PTCR.
```

Step 2.1 - Run the Phase 1 power-down. Switch off the A/C's 20A breaker as well.

Step 2.2 - Work from a ladder; Casita doesn't recommend walking or kneeling on the roof. Remove the A/C shroud.

Step 2.3 - Open the A/C's electrical box. Photograph the wiring diagram sticker inside the lid and every wire on the capacitor, terminal board and compressor leads.

Step 2.4 - Identify RUN, COMMON and START from the sticker. Check for a start capacitor, start relay or PTCR. Compare to Spartan's answer from Step 0.6.

Step 2.5 - Wire the SpartanStart per Spartan's instructions (https://spartanpower.com/wp-content/uploads/2024/07/SpartanStart_Instructions_07_18_2024.pdf). It splices INLINE into all three compressor wires (6 splices total):

   - a. Start components (optional on sticker 1976-764, dashed lines). CHECK: the metal dual (run) capacitor's RED/HERM terminal has only ONE red wire, there is no small plastic-cased capacitor with a RED and a YELLOW wire, and no small black plastic PTCR puck on the terminal block = nothing to remove. IF PRESENT (per Micro-Air's Coleman Mach 8 procedure): disconnect the start capacitor's red and yellow wires at BOTH ends and remove them and the start capacitor; unplug the compressor's red wire(s) from the PTCR, remove the PTCR, and plug the red wire(s) onto the PTCR's terminals on the terminal block. End state: compressor Start (red) connects only to the dual capacitor's RED/HERM terminal - check with continuity. Leave the metal dual capacitor in place.
   - b. Find the 3 compressor wires (usually in a sleeve). Pick a mounting spot first, then cut each wire where both cut ends reach the SpartanStart's two harnesses.
   - c. SUPPLY side (wires from the control box): splice to the SpartanStart SUPPLY harness - Run to BLUE, Common to BLACK, Start to RED.
   - d. COMPRESSOR side (wires from the compressor): splice to the SpartanStart COMPRESSOR harness - Run to BLUE, Common to BLACK, Start to RED.
   - e. Strip 1/2 inch, crimp with the included closed-end connectors using a proper crimper, tug-test all 6. Poor crimps overheat.
   - f. R-32 refrigerant is mildly flammable: no torches or open flame near the refrigerant lines.

Step 2.6 - Mount the SpartanStart inside the shroud with the included tape and zip ties: away from fan blades, off the hot compressor and refrigerant lines, and out of any drip or water path. Dress the wires away from moving parts.

Step 2.7 - Close the electrical box and reinstall the shroud.

Step 2.8 - Test on shore power: plug in, turn the A/C breaker on, set the thermostat to cool. The compressor should start smoothly, without the usual hard thunk or light dimming. Run it 20-30 minutes. If you have a clamp meter with inrush mode, measure the A/C supply's starting current.

**Stop point: if the A/C won't start, trips its breaker, or the compressor hums without starting, turn it off immediately and call Spartan before continuing.**

## Phase 3 - Pre-wiring checks (before buying or cutting anything else)

Step 3.1 - Confirm the inverter's neutral-ground bond. With shore unplugged, reconnect the inverter's DC fuse and turn the inverter on. At one of its front receptacles, measure AC volts:

   - Hot to neutral: about 115-120V.  Hot to ground: about 115-120V.  Neutral to ground: about 0V.
   - About 0V neutral-to-ground = bonded, as the manual says. Continue.
   - About 50-60V neutral-to-ground (and about 60V hot-to-ground) = floating neutral. STOP. This design needs a different bonding arrangement; ask before continuing.
   - Turn the inverter off and remove its DC fuse again when done.

Step 3.2 - Confirm the WFCO panel has no neutral-ground bond. Fully powered down (Phase 1). First disconnect the inverted-outlet cable from the inverter (photograph it first); it gets reconnected to the WFCO in Phase 8, and those two outlets are dead until then. Remove the WFCO's AC cover. Measure resistance between the neutral bar and the ground bar.

   - Open / very high resistance = good, no bond. Continue.
   - Near 0 ohms = there's a bond. Look for a bonding screw or strap between the bars, or a neutral and ground tied together somewhere (for example, the factory inverted outlets sharing the WFCO neutral). Find and fix it before continuing.

Step 3.3 - Identify the TS-30's relay poles (unpowered, lid off). Read the wiring diagram inside the TS-30 lid. Then confirm with continuity: with nothing connected, output terminal 3 should show continuity to one of the normally closed terminals (7 or 8), and terminal 4 to the other. Write down your map, e.g.:

```text
 POLE A (use for HOT):     output 3 <-> N.C. 7  and  N.O. 5
 POLE B (use for NEUTRAL): output 4 <-> N.C. 8  and  N.O. 6
 (example only - fill in from YOUR lid diagram + meter)
```

   - The N.O. terminals only connect when the relay is energized, so take the N.O. pairing from the lid diagram. Hot must use the same pole on the inverter input, the shore input and the output; neutral uses the other pole. The polarity tests in Phase 10 will catch a mistake.

## Phase 4 - Mount the enclosures

Step 4.1 - Mount the TS-30 on a solid interior surface with screws through the holes in the bottom corners of the can. It must be accessible later. It contains a relay that can arc: not in the battery compartment, propane compartment, or anywhere fuel is stored.

Step 4.2 - Prepare the shore-only box before mounting:

   - a. Remove the neutral-to-ground bonding screw or strap that load centers often ship with. The neutral bar must be isolated from the metal box.
   - b. Install the ground bar kit, which attaches directly to the metal box.
   - c. Check with a meter: neutral bar to box = open; ground bar to box = 0 ohms.

Step 4.3 - Mount the shore-only box near the WFCO panel and the shore cord route. Label it 'SHORE POWER ONLY - converter / water heater'.

Step 4.4 - Plan every cable route. Use a clamp at every knockout and secure cables along their run. Keep 120V cables away from the battery terminals and DC cables, and away from sharp edges.

## Phase 5 - Wire the shore-only box

### Diagram 6 - Shore-only box

```text
 SHORE-ONLY BOX (6-space main-lug load center)

  Shore cord:  BLACK -> main lug L1 (one leg only)
               WHITE -> NEUTRAL bar (isolated, bond removed)
               GREEN -> GROUND bar (kit, bonded to the box)

  Breakers ONLY in spaces fed by leg L1 (verify with meter):
   [30A] BLACK -> TS-30 shore input HOT
   [20A] BLACK -> WFCO converter HOT
   [20A] BLACK -> water heater element HOT
   [ -- ] spare
  Each circuit's WHITE -> neutral bar, GREEN -> ground bar
  (except the converter's green, which stays in the WFCO)
```

Step 5.1 - Run the Phase 1 power-down.

Step 5.2 - At the WFCO panel, disconnect the shore cord cable: black from the 30A main breaker, white from the neutral bar, green from the ground bar. Photograph first.

Step 5.3 - Get the shore cord cable to the shore-only box. If it reaches, re-route it. If not, splice it to new 10/2 with ground inside a covered junction box, using connectors rated for 10 AWG and 30A.

Step 5.4 - Land it in the shore-only box: black on main lug L1, white on the neutral bar, green on the ground bar. Torque to the values on the box label.

Step 5.5 - Breaker spaces: a 120/240V load center has two hot legs, and with a single 120V feed, only one is live. On most 6-space boxes, spaces 1, 2, 5 and 6 are on one leg and 3 and 4 on the other, but check your box's label. Install breakers only in spaces on the leg you landed the black wire on. You'll confirm with a meter in Phase 10. Do not jumper the two legs unless an electrician signs off.

Step 5.6 - Install the 30A breaker. Run 10/2 with ground from it to the TS-30's location (connected to the TS-30 in Phase 7): black to the 30A breaker, white to the neutral bar, green to the ground bar.

## Phase 6 - Move the converter and the water heater circuits

### Diagram 7 - Converter relocation (inside the WFCO)

```text
 BEFORE                           AFTER
 [20A CONV] <- converter BLACK    [20A CONV] empty, OFF,
 neutral bar <- converter WHITE        labeled "moved"
 ground bar  <- converter GREEN   converter BLACK -+ splice to
                                  converter WHITE -+ new 12/2
                                                   | -> shore-
                                                   |  only box
                                  converter GREEN -> stays on
                                                   WFCO ground bar
```

Step 6.1 - Converter. Inside the WFCO, find the 20A breaker labeled CONV (or Converter) and follow its black wire to the converter section; follow the matching white to the neutral bar.

   - a. Remove the converter's black wire from the CONV breaker and its white wire from the neutral bar. Leave the converter's green wire on the WFCO ground bar.
   - b. Inside the WFCO's wiring area, splice the black and white to a new 12/2 with ground cable (12 AWG, because it stays on a 20A breaker). Connect the new cable's green to the WFCO ground bar.
   - c. Run the new cable out of the WFCO through a knockout with a clamp to the shore-only box: black to a 20A breaker, white to the neutral bar, green to the ground bar.
   - d. Before reusing a 20A breaker, confirm the converter's existing wire is 12 AWG. If it's 14 AWG, use a 15A breaker.

Step 6.2 - Water heater element. Find the WFCO breaker labeled for the water heater (20A) and its branch cable.

   - a. Disconnect its black (breaker), white (neutral bar) and green (ground bar).
   - b. Move the whole cable to the shore-only box if it reaches. If not, splice it to 12/2 with ground in a covered junction box.
   - c. In the shore-only box: black to a 20A breaker, white to the neutral bar, green to the ground bar. Confirm the wire is 12 AWG; if it's 14 AWG, use a 15A breaker.

Step 6.3 - In the WFCO, switch off the two now-empty breakers and label them 'Moved to shore-only box'. One can be reused in Phase 8.

## Phase 7 - Wire the TS-30

### Diagram 8 - TS-30 connections (Configuration C)

```text
 From Renogy hardwire terminal (inverter = default, N.C.)
     L (hot)     -> N.C. terminal on the HOT pole     (7 or 8)
     N (neutral) -> N.C. terminal on the NEUTRAL pole (the other)
     G (ground)  -> TS-30 ground bar

 From shore-only box 30A breaker (shore = dominant, N.O.)
     BLACK       -> N.O. terminal on the HOT pole     (5 or 6)
     WHITE       -> N.O. terminal on the NEUTRAL pole (the other)
     GREEN       -> TS-30 ground bar

 Output to WFCO (wide end of relay)
     HOT pole output     (3 or 4) -> BLACK -> WFCO 30A main breaker
     NEUTRAL pole output (the other) -> WHITE -> WFCO neutral bar
     GREEN from TS-30 ground bar     -> WFCO ground bar

 TS-30 ground bar -> 8 AWG green -> trailer chassis
 Hot/neutral pole assignment comes from YOUR Step 3.3 map.
```

Step 7.1 - Run the Phase 1 power-down.

Step 7.2 - Chassis ground: run 8 AWG green from the TS-30 ground bar to a clean, bare-metal chassis ground point with a ring terminal. Tighten the ground bar to at least 20 in-lb, per the TS-30 manual.

Step 7.3 - Insert each cable through a clamp on a TS-30 knockout. Don't tighten the clamps yet. Route the green wires around the lower area of the enclosure, away from the relay contacts.

Step 7.4 - Connect all green wires to the ground bar first, then the whites, then the blacks, in the order the TS-30 manual gives. For the lever connectors, strip 0.5 in, insert the bare wire fully, and close the lever. Tug-test every wire.

Step 7.5 - Shore input: connect the 10/2 cable from the shore-only box (Step 5.6) to the N.O. terminals (5/6), hot and neutral on the correct poles.

Step 7.6 - Inverter input. FIRST remove the factory outlet cable from the inverter's hardwire terminal (Phase 8, Steps 8.1-8.2), so the terminal is free. Then run 10/2 with ground (or 12/2 if the Renogy terminal won't accept 10 AWG; the inverter can only deliver 16.6A continuous) from the TS-30 to the inverter's hardwire terminal block. Remove the terminal cover and feed the cable through the AC knockout with a clamp. Follow the L, N and G markings printed on the inverter, not the manual: the manual shows two different orders. At the TS-30, connect to the N.C. terminals (7/8) on the correct poles.

Step 7.7 - Inverter chassis ground: connect the inverter's chassis ground lug (on the DC end) to the trailer chassis with 12 AWG or larger stranded green wire, against bare metal.

Step 7.8 - Output: run 10/2 with ground from the TS-30 output (3/4) to the WFCO. Black to the 30A main breaker (where the shore cord used to land), white to the WFCO neutral bar, green to the WFCO ground bar.

Step 7.9 - Leave the TS-30 time delay as shipped (no jumper). The 20-45 second delay lets shore power settle before the switch transfers, which is gentler on the A/C and the relay.

Step 7.10 - Tighten the cable clamps and snap the TS-30 lid on.

## Phase 8 - The factory 'inverted' outlets (do this in the same session as Phase 7)

CONFIRMED: the two factory outlets are wired directly from the inverter's hardwire terminal. That terminal is about to feed the TS-30, so the outlet circuit moves to the WFCO panel. Afterwards these outlets work on shore and on battery like every other outlet. Never feed the same outlets from both the inverter and the panel.

Confirmed: the two outlets are wired directly from the inverter. Move that outlet cable onto the WFCO breaker freed up in Step 6.3 (route it to the WFCO; splice with same-gauge cable in a covered junction box if it doesn't reach). Those outlets will then work on shore and on battery like everything else. Black to the breaker, white to the WFCO neutral bar, green to the WFCO ground bar. Check the wire gauge printed on the cable: the inverter was its only protection before, so it may be 14 AWG. Use 20A only if it's 12 AWG; if it's 14 AWG, use a 15A breaker. If they're in a kitchen or bathroom area, make sure they're GFCI-protected like the trailer's other outlets.

If instead the cable is a cord plugged into the inverter's front receptacle, unplug it and replace the plug end with a proper connection to the WFCO breaker in the same way. Don't leave anything plugged into the inverter's own receptacles as a permanent load.

## Phase 9 - The refrigerator (DONE - nothing to do)

- CONFIRMED: the fridge runs only on 12V, so nothing to do. It's powered from the battery/DC side at all times (the converter keeps the battery up on shore). Budget roughly 25-50Ah per day for it off-grid, more in hot weather.
- (The 3-way fridge scenario from earlier versions of this guide doesn't apply to this trailer.)
- Optional: if the fridge has its own fuse on the WFCO 12V side, note which one so you can find it later.

Nothing else to do in this phase.

## Phase 10 - Inspect, then power up and test

### 10.1 Inspection, still powered down

- Every screw terminal torqued per its label, every lever connector closed and tug-tested, no bare copper showing outside a terminal.
- Every cable clamped at every box; all covers installed.
- Shore-only box: neutral bar to ground bar = open (no continuity). Shore cord unplugged.
- Note: with the TS-30 at rest, the WFCO neutral now connects through the TS-30 to the inverter, whose neutral is bonded to ground inside. A neutral-to-ground continuity reading at the WFCO is now expected. That's the one correct bond when the inverter is the source.

### 10.2 Test A - shore power only (inverter OFF)

1. Reinstall the inverter's DC fuse, but leave the inverter switched OFF. Battery disconnect on.
2. All breakers off in both boxes. Plug in the shore cord.
3. Turn on the shore-only box breakers one at a time. At each, measure about 120V from the breaker's load terminal to the neutral bar. A breaker reading 0V is on the dead leg: unplug, move it to a live-leg space, and retest.
4. With the 30A breaker on, you should hear the TS-30 click within 20-45 seconds.
5. Turn on the WFCO main and branch breakers. Test outlets around the trailer with the 3-light tester: all should show 'correct'. Press the test button on each GFCI outlet: it should trip. Reset it.
6. Converter: the SmartShunt or battery monitor should show charging current flowing into the batteries.
7. Water heater electric: ONLY if the tank is full of water (an element powered with an empty tank burns out in seconds). Turn on its electric switch and confirm it heats.
8. A/C: runs normally with the soft start.

### 10.3 Test B - inverter only (shore unplugged)

1. A/C off at the thermostat. Unplug the shore cord. The panel goes dead, which is expected with the inverter off.
2. Turn the inverter ON. The TS-30 is at rest (no click needed), and the WFCO panel should be live from the inverter.
3. 3-light tester at several outlets: 'correct'. Press a GFCI test button: it should trip. Reset it.
4. At an outlet, measure neutral to ground: about 0V.
5. The battery monitor should show only discharge (current out). No charging current = the converter is isolated, which is the main point of this project. Confirm the water heater element has no power (0V at its breaker in the shore-only box).
6. A/C: set it to cool. The compressor should start through the soft start without the inverter faulting. Expect about 110-150A from the batteries while the compressor runs.
7. Let it run 30-60 minutes. Feel the inverter, the DC cables, the fuse holder and the battery terminals: warm is fine; too hot to keep your hand on means stop and investigate. The inverter's fan should be running.
8. If the inverter faults or its GFCI light comes on: turn everything off and see Troubleshooting.

### 10.4 Test C - switching between sources

1. Inverter on, A/C off. Plug in shore power. The panel stays on the inverter for 20-45 seconds, then the TS-30 clicks over to shore. The battery monitor starts showing charging.
2. A/C off. Unplug shore power. The panel switches straight back to the inverter (lights may blink).
3. Inverter off, shore unplugged: the panel is dead. This is expected.

## Everyday operation

- Turn the A/C off before plugging in or unplugging shore power, and wait about 3 minutes before turning it back on. Restarting a compressor against high pressure right after a power blip is hard on it and can trip the inverter or the relay.
- Arriving at a site with hookups: A/C off, plug in, wait for the click, then A/C on. You can leave the inverter on or off; with the inverter on, it idles at about 1.5-2A while shore power runs the trailer.
- Off-grid: inverter on whenever you want 120V (including the A/C). Turn it off when you don't need it; idle draw is about 1.5-2A, roughly 12-16Ah overnight.
- Water heater: use propane off-grid. The electric element only works on shore power now, automatically.
- Battery: watch the battery monitor and turn the A/C off around 20-30% state of charge. The inverter's own shutdown is at 10.5V, which is close to empty for lithium.
- On a weak campground pedestal (low voltage), the TS-30's relay can chatter when the A/C starts. If you hear rapid clicking, turn the A/C off and check pedestal voltage.
- Fridge: it's 12V, so it always runs from the batteries; budget roughly 25-60Ah per day off-grid.
- Solar: the portable panel charges the batteries directly over 12V DC, separately from the breaker panel. It works on shore power or on inverter power and adds to the converter's charging. Make sure its controller is set to LITHIUM.
- Storage: inverter off, fridge emptied and off, battery disconnect off.

## Troubleshooting

- Panel dead after unplugging: the inverter is off, its DC fuse is out, or it shut down on low battery or overload. Check the inverter's lights.
- Renogy GFCI or fault light trips on inverter power: most likely a second neutral-ground bond (WFCO or shore-only box), hot and neutral on mismatched TS-30 poles, or a neutral tied to the wrong source. Recheck Steps 3.2, 3.3 and 4.2, and the inverted-outlet wiring.
- Battery charges while unplugged / converter runs on inverter: the converter is still fed from the WFCO side. Recheck Step 6.1.
- Outlet tester shows 'hot/neutral reversed' on only one source: hot and neutral are swapped on that TS-30 input. Swap them at that input (powered down).
- TS-30 never clicks over on shore: the 30A breaker in the shore-only box is off or on the dead leg, or the shore input isn't on the N.O. terminals.
- A/C won't start on the inverter but does on shore: soft start wiring or settings. Call Spartan with your clamp-meter readings.
- Inverter overloads with the A/C running: something else is drawing heavily too (for example, the water heater element still on the panel, or a space heater or hair dryer plugged in). Recheck Phase 6.

## Wire and breaker schedule

```text
 RUN                                CABLE         PROTECTION
 ---------------------------------  ------------  ------------------
 Shore cord -> shore-only box       10 AWG exist. pedestal 30A
 Shore-only box -> TS-30 N.O.       10/2 + G      30A breaker (box)
 Renogy hardwire -> TS-30 N.C.      10/2 + G *    inverter output
                                                   (16.6A cont.)
 TS-30 output -> WFCO main          10/2 + G      WFCO 30A main
 Shore-only box -> converter        12/2 + G      20A (15A if 14 AWG)
 Shore-only box -> water heater     12/2 + G      20A (15A if 14 AWG)
 WFCO -> former inverter outlets    existing      20A (15A if 14 AWG)
 TS-30 ground bar -> chassis        8 AWG green   -
 Inverter chassis lug -> chassis    12 AWG+ green -
 Battery -> inverter DC             1/0 AWG       250A fuse
 * 12/2 + G acceptable if the terminal won't take 10 AWG
```

## Open items to confirm

- Spartan's confirmation of the SpartanStart wiring for the 37200-series R-32 A/C, and the colors on your unit's sticker.
- Fridge: RESOLVED (12V-only, nothing to move).
- Inverted outlets: RESOLVED (wired directly from the inverter; moved to a WFCO breaker in Phase 8). Just check the cable gauge (12 vs 14 AWG).
- The inverter's DC cable size and fuse (Step 0.5).
- Physical room for the TS-30 and the shore-only box near the WFCO panel.
- Results of the neutral-ground checks in Steps 3.1 and 3.2. Don't proceed past them on a surprise result.
