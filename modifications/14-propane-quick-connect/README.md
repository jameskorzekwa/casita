# Exterior Propane Quick-Connect (passenger side, for the griddle and fire pit)

A low-pressure propane quick-connect outlet on the passenger side of the trailer, between the wheel and the entry door, fed from the capped spare port on the factory propane tee under the front of the trailer. Lets the Blackstone 22" tabletop griddle and the Flame King 24" fire pit run off the trailer's 20 lb cylinders instead of 1 lb bottles and a separate tank.

> [!IMPORTANT]
> **Status: planned, parts list ready, nothing ordered (2026-11-02).** The route was walked under the trailer and photographed on 2026-11-01. The stub's fitting size is from owner reports on other Casita 17s (see [Line size](#line-size-what-casita-uses)), not yet measured on this trailer; confirm it in Step 1 before ordering the fittings. Purchase tracking is in [`components.md`](components.md).

**Contents:** [Why this works](#why-this-works-low-pressure-only) · [Line size](#line-size-what-casita-uses) · [Route](#route) · [Parts](#parts) · [Diagram](#diagram) · [Steps](#steps) · [Testing](#testing) · [Safety notes](#safety-notes) · [Open questions](#open-questions) · [Revisions](#revisions)

## Why this works (low pressure only)

The factory propane system is: two 20 lb cylinders → two-stage automatic changeover regulator at the cylinders → rubber hose down through the tongue area → brass three-port flare tee under the very front of the trailer, just behind the cylinders → copper lines to the range, furnace and water heater. One port of that tee is capped and unused. Everything downstream of the regulator, including the capped port, is **low pressure: 11 inches of water column (about 0.4 PSI)**.

That has one consequence that decides the whole design: **appliances plug in with their own regulator removed.** The Type 1 / QCC1 ACME connector with the black hand-wheel on the fire pit's hose (photographed 2026-11-01) is a tank regulator; it expects cylinder pressure on its inlet and has nothing to do on an 11" WC line. So each appliance gets a quick-connect hose that bypasses its regulator and feeds the burner manifold directly. That is only safe for appliances designed for 11" WC:

| Appliance | Pressure class | Evidence | Inlet once the regulator is off |
| --- | --- | --- | --- |
| Blackstone Adventure Ready 22" tabletop griddle (SKU 2484), 24,000 BTU/h | **Low, 11" WC** (confirmed) | Replacement regulators for the 17"/22" tabletops are rated "outlet pressure 11" W.C."; Blackstone sells its own RV quick-connect kit (SKU 5415) whose instructions are "remove regulator from griddle, connect quick-connect adapter to your griddle" | A male stub on the griddle's gas rail with a proprietary swivel collar; needs a Blackstone-specific elbow adapter |
| Flame King 24" smokeless fire pit (FKG6502D), 58,000 BTU/h ([bought 2026-10-29](components.md)) | **Low, 11" WC** (probable, not stated by Flame King) | Same 58K BTU design as the Outland Firebowl, which Torjik and owners convert by removing the hose and regulator and plugging into the RV's low-pressure quick-connect. Flame King's manual gives only regulator *inlet* pressures (25-250 PSI) and says "do not connect to a remote gas supply", so this is an owner decision outside the manual | 3/8" male SAE flare on the valve box (the factory hose end is a 5/8"-18 = 3/8" female flare swivel, under shrink-wrap) |

Anything with a 5-30 PSI regulator (Camp Chef Explorer-class stoves, turkey fryers, most "outdoor cookers") cannot run from this outlet.

Capacity: a two-stage RV regulator is typically rated 160,000-200,000 BTU/h or more. The griddle (24k) plus the fire pit (58k) plus the furnace (16k), water heater (about 12k) and range (about 20k) is around 130k, inside that. The exact model and rating of this trailer's regulator is still to record ([open question](#open-questions)).

## Line size: what Casita uses

Researched 2026-11-02 because the owner's manual says nothing about line size.

- **The tee's spare port is a 3/8" SAE flare (5/8"-18 thread).** A 2017 Casita 17 owner on fiberglassrv.com, adding a Wave 3 heater: "My 2017 17" Casita has a T with available (closed) port underneath the trailer; the T is 3/8 ... flare connection. Took a bit of muscle to take off the cap ... the T is 3/8, while typical 'quick connect' RV propane devices are 1/4"." He mated a 3/8" female-flare hose to it. ([thread](https://www.fiberglassrv.com/threads/installing-wave-3-in-casita-17.1183988/))
- A July 2025 video of the same tee on a Casita describes "a three-way splitter ... the feed line comes into this larger fitting and then splits off into two additional fittings", replaces it with a four-way from a propane supplier, and mounts a 1/4" quick-disconnect on aluminum angle screwed to the frame, with no extra regulator. ([YouTube](https://www.youtube.com/watch?v=x5J_Q5cIxxM))
- Copper runs are therefore **3/8" OD soft copper** by inference (flare tees match the tube OD). No owner post states the copper OD explicitly. The copper visible in the 2026-11-01 underside photo is consistent with 3/8".
- Casita's own store and Little House Customs sell no quick-connect kit; owners build it from standard parts (SHINESTAR / DOZYANT / Camco / MB Sturgis), or have a propane shop tee a copper branch in (one owner paid about $500 for that).

Confidence: moderate-to-high on 3/8" flare. **Measure before ordering:** a 3/8" SAE flare nut is 5/8"-18 (about 0.62" across the threads); 1/4" SAE flare is 7/16"-20. If the stub is a flare nut on a short tube rather than a male port on the tee body, the hose needs a 3/8" flare union (male-male) between them; that is on the parts list as a contingency.

## Route

From the underside photo (2026-11-01, trailer on its wheels, looking up from the passenger side):

1. **Start at the tee** under the front, right side of the photo, where the brass tee and the capped port sit on the cross member with the existing copper runs.
2. **Along the cross member toward the passenger side**, on the inboard/upper face of the steel so nothing hangs below the bottom of the frame rail. Clamp to the steel, never to the fiberglass shell.
3. **Past the grey tank along its forward edge and the outrigger**, not across the tank face. Nothing is clamped to the tank (it flexes when full). Keep clear of the drain pipe and leave the dump-valve handle free.
4. **Exit at the outer frame edge between the passenger wheel and the entry door**, on an angle bracket bolted to the outrigger, coupler pointing down or outboard, just inside the body line, protected from tire spray.

Length: measure with string before ordering; on a 17 ft Casita this run is expected to be **8-10 ft**, so a 10 ft hose with slack taken up by one extra clamp. Buy 12 ft if the string says more than 9 ft.

A hose rather than copper was chosen because it needs no flaring tool or bender under the trailer, tolerates frame flex, and is what the other Casita owners used. The hose must be LP-rated (CSA/UL "LP gas hose", 350 PSI working pressure); the Amazon hoses sold as "high pressure" are the same hose and are fine at 11" WC.

## Parts

Prices are Amazon, 2026-11-02, point in time, no Prime context. Status and ownership are tracked in [`components.md`](components.md).

### Trailer side (tee to outlet)

| Part | Spec | Qty | Option | Price |
| --- | --- | ---: | --- | --- |
| LP gas hose, 3/8" female SAE flare swivel both ends, 10 ft | LP-rated rubber hose, 350 PSI WP, 5/8"-18 swivels | 1 | [10 ft, B0H5BBFQ93](https://www.amazon.com/dp/B0H5BBFQ93) (4.5, 41 ratings); or [onlyfire 12 ft, B086ZM1Y9D](https://www.amazon.com/dp/B086ZM1Y9D) (4.4, 209) if the run measures over 9 ft | $22.99 / $24.99 |
| Adapter, 3/8" male SAE flare x 1/4" male NPT (half union) | Brass, flare end into the hose swivel, NPT end into the coupler's shutoff valve | 1 | [Anderson Metals 54048-0604, B003RW4IWE](https://www.amazon.com/dp/B003RW4IWE) (4.6, 2,581) | $5.08 |
| Quick-connect coupler with shutoff valve and plug | 1/4" female NPT inlet, 1/4" "industrial interchange" RV propane coupler, integral 1/4-turn valve, male plug included for mating hoses | 1 | [DOZYANT kit, B06Y3HTK8W](https://www.amazon.com/dp/B06Y3HTK8W) (4.7, 3,018) | $13.99 |
| Rubber-cushioned stainless loop (P) clamps, 5/8" | For a 3/8" LP hose (about 0.6" OD); 5-6 used | 6 | [assortment incl. 5/8", B0DK5MR8RV](https://www.amazon.com/dp/B0DK5MR8RV) (4.7, 172); or a 5/8" 10-pack from a hardware store | $27.99 |
| Split loom, 3/4" | Over the last 1-2 ft of hose near the wheel well; any hardware-store split loom works | 2 ft | [60 ft, B0DT8FM8PK](https://www.amazon.com/dp/B0DT8FM8PK) (4.8, 1,351) or hardware store | $24.99 |
| 3/8" SAE flare union (male-male) | **Contingency only.** Needed only if Step 1 shows the stub is a flare nut on a tube, not a male port on the tee | 1 | [LTWFITTING 5-pack, B00MP2V5ZK](https://www.amazon.com/dp/B00MP2V5ZK); a single one is cheaper at a hardware store | $21.99 |
| Angle bracket, about 2 x 2 in, aluminum or steel | Mounts the coupler to the outrigger; the coupler body passes through a 1/2" hole or is held by its hex with a clamp | 1 | Owner stock | — |
| Self-tapping #10 screws or 1/4" bolts | Clamps and bracket to the frame | ~8 | Hardware store | — |
| Gas-rated thread sealant | Yellow PTFE gas tape or Rectorseal No. 5 / T Plus 2, NPT joints only | — | Owner stock | — |
| Gas leak detector | Spray, or soapy water | — | Owner stock ([Camco 10324, B000EDUTMC](https://www.amazon.com/dp/B000EDUTMC) if a bottle is wanted) | — |
| Two wrenches (adjustable or flare) | Backup wrench on every flare joint | — | Owner stock | — |

### Appliance side

| Part | Spec | Qty | Option | Price |
| --- | --- | ---: | --- | --- |
| Blackstone quick-connect hose with elbow adapter, 12 ft | 1/4" male quick-connect plug (mates the DOZYANT coupler) x Blackstone 17"/22" tabletop elbow adapter; replaces the 1 lb-bottle regulator | 1 | [B09NCY6KTM](https://www.amazon.com/dp/B09NCY6KTM) (4.7, 563), includes a shutoff; or [B08BY9SHBS](https://www.amazon.com/dp/B08BY9SHBS) (4.7, 1,589) $28.99; or Blackstone's own kit SKU 5415 | $22.99 |
| Fire pit quick-connect hose, 18 ft | 1/4" male quick-connect plug x 3/8" female SAE flare swivel; screws onto the fire pit's 3/8" male flare once the factory hose/regulator is removed | 1 | [18 ft, B07FRYP6HS](https://www.amazon.com/dp/B07FRYP6HS) (4.7, 2,178); or [8 ft, B0GFWH1J4B](https://www.amazon.com/dp/B0GFWH1J4B) $17.12; Flame King's own 100304-48/-72 RV pigtail is the same thing | $22.49 |
| 1/4" quick-connect Y splitter | Optional, only to run the griddle and fire pit at the same time from one outlet | 0-1 | [B07MNXDXNC](https://www.amazon.com/dp/B07MNXDXNC) (4.7, 1,089) | $18.99 |

Estimated total to buy: about **$115** (hose, adapter, coupler kit, clamps, two appliance hoses), plus about $25 if split loom is bought rather than scrounged, plus $22 if the flare union turns out to be needed. The Y splitter is optional.

## Diagram

```text
20 lb cylinders ── two-stage changeover regulator ── rubber hose ── [brass tee under front]
                                                                     ├── copper ── range
                                                                     ├── copper ── furnace / water heater
                                                                     └── spare port, 3/8" male flare (capped)
                                                                           │
                                                                           │ 3/8" female flare swivel
                                                                     10 ft LP hose, clamped to cross member and outrigger
                                                                           │ 3/8" female flare swivel
                                                                     3/8" male flare x 1/4" MNPT adapter
                                                                           │ 1/4" FNPT (sealant)
                                                                     shutoff valve + 1/4" quick-connect coupler
                                                                     on bracket at the frame edge, wheel-to-door
                                                                           │ 1/4" QC plug
                                                        ┌──────────────────┴──────────────────┐
                                           12 ft hose + Blackstone elbow                18 ft hose, 3/8" female flare
                                           (griddle regulator removed)                 (fire pit hose/regulator removed)
```

## Steps

1. **Confirm the stub.** Cylinders off. Open a range burner for a few seconds to bleed the line pressure, then close it. Under the front, measure the capped port: thread diameter about 0.62" = 3/8" flare (expected); about 0.44" = 1/4" flare (then change the hose and adapter to 1/4" flare equivalents). Note whether it is a male port on the tee body (hose screws straight on) or a flare nut on a stub tube (add the flare union). Photograph it.
2. **Measure the route** with string from the tee to the chosen exit point between the wheel and the door, following the cross member and the outrigger. Decide 10 ft or 12 ft. Order the parts and update [`components.md`](components.md).
3. **Make the outlet assembly on the bench:** sealant on the adapter's NPT threads, adapter into the coupler's shutoff valve, tight with two wrenches. No sealant on the flare end. Drill the bracket for the coupler and for two bolts into the outrigger.
4. **Mount the bracket** to the outrigger between the wheel and the door, coupler pointing down or outboard, inside the body line, with the shutoff handle reachable and clear of the entry step.
5. **Run the hose** from the tee along the cross member, past the forward edge of the grey tank along the outrigger, to the bracket. Dry-fit first. Clamp every 18-24 in with the cushioned clamps, one within 6 in of each end so the fittings carry no load. Nothing lower than the bottom of the frame rail; nothing touching the tank, drain pipe, or dump valve handle; split loom over the last 1-2 ft at the wheel well.
6. **Connect the flares:** remove the cap/plug from the tee port (it may be tight), screw the hose swivel on, hold the tee with a backup wrench, snug plus about a quarter turn. Same at the outlet end onto the adapter.
7. **Leak test** ([Testing](#testing)). Only then fit the plug into the coupler for storage.
8. **Appliances:** on the griddle, remove the 1 lb-bottle regulator (slide collar) and fit the elbow adapter per its instructions. On the fire pit, cut the shrink-wrap, unscrew the factory hose from the 3/8" male flare on the valve box, and screw the 3/8" female flare of the 18 ft hose on. Keep the original regulators with the appliances so they can still run on bottles.
9. Light each appliance from the outlet, check flame height and color at full and low, and soap the appliance-side joints.
10. Add photos to `photos/` and update the status line here.

## Testing

- **Soap test, outlet closed:** cylinders on, outlet valve closed, no appliance. Soap the tee port, both hose swivels, the NPT joint, and the coupler face. No bubbles for 60 s each.
- **Soap test, outlet open with an appliance:** valve open, appliance connected and its valve closed; soap the coupler/plug interface and the appliance-side joints.
- **Lock-up / drop test:** all appliances off, cylinders on, then cylinders closed. Watch the regulator gauge (or the propane sensor from [mod 07](../07-tank-monitor/README.md), which will not resolve this; use the gauge) for 15 min. Any fall means a leak; find it with soap.
- **Function:** range, furnace and water heater still light and run normally with the griddle running (no starvation at the regulator).
- Repeat the soap test on the outlet after the first trip (vibration).

## Safety notes

- **Low pressure only.** Never plug an appliance into this outlet with its own regulator still in the hose, and never plug in a 5-30 PSI appliance. Label the bracket "11" WC LOW PRESSURE PROPANE – NO REGULATOR".
- **Flare joints seal metal to metal:** no tape, no sealant. NPT joints: gas-rated sealant only.
- Cylinders off and line bled before opening any joint. No smoking, no sparks; work outdoors.
- Hose must be LP-rated (not an air or water hose), above the frame bottom, clamped, away from the exhaust of the furnace and water heater and from the tire.
- Close the outlet valve and cap the coupler with the plug when not in use and for towing. Disconnect appliances before towing.
- The Flame King manual says not to connect it to a remote gas supply; running it from this outlet is an owner decision outside the manual, the same as the Outland Firebowl conversions. Never use the fire pit under the awning or closer than its manual's clearances.
- A propane leak detector inside the trailer is unaffected by this mod; the outlet is outside. Keep the factory CO/LP alarm in service.
- Not a licensed-installer job in most jurisdictions for an owner's own RV, but an RV propane shop will do steps 3-7 for about an hour of labor if preferred.

## Open questions

- Confirm the stub's flare size and form (male port vs flare nut on a tube) on this trailer (Step 1). Expected 3/8" male flare.
- Record the regulator model and BTU/h rating (label on the regulator at the cylinders) in `docs/trailer.md`.
- Final hose length after the string measurement (10 vs 12 ft).
- Whether the Flame King fire pit's flame is correct on 11" WC with the regulator removed (expected yes, same as Outland); if it is weak, the burner orifice is sized for a higher pressure and the fire pit stays on its own tank.

## Revisions

| Date | Change |
| --- | --- |
| 2026-11-02 | Created: route walked and photographed 2026-11-01; Casita line size researched (3/8" SAE flare on the tee's spare port, per owner reports); appliance pressure classes confirmed; parts list with Amazon options; nothing ordered |
