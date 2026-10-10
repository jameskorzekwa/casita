# A/C Soft Start (Spartan Power SpartanStart)

> **Status: purchased; install status to confirm.** The wiring sticker has been read (1976-764). Update this line with the install date and test results.

The Coleman-Mach Mach 8 Plus Cub's compressor draws a large surge when it starts (locked-rotor current around 58 A on the older R-410A version; not published for the R-32 version). That surge is far more than the factory Renogy 2000 W inverter's 4000 W one-second peak can supply. A soft start ramps the compressor up gently so the inverter can start it. It is a prerequisite for running the A/C from the batteries ([mod 03](../03-whole-panel-inverter/README.md)).

## Parts

| Part | Notes |
| --- | --- |
| Spartan Power SpartanStart (Amazon B09WHDXDYG, about $189) | Bought instead of the Coleman 1497-3601 kit because of delivery time. 3-year warranty, rated for RV A/Cs up to 20,000 BTU on a 2000 W source, no learning cycles. [Instructions](../../manuals/air-conditioning/spartan-power-spartanstart-instructions-2024-07.pdf) |

Spartan Power support: (775) 800-1725, sales@spartanpower.com.

Alternatives considered: Coleman-Mach 1497-3601 (OEM, keeps the Coleman warranty simple), Micro-Air EasyStart Breeze, SoftStartRV. Avoid low-cost "compatible with 1497-3601" clones.

## Wiring (confirmed from this unit's sticker)

The A/C is a 37200-series (R-32) unit. Spartan's install table does not list it, but this unit's wiring sticker, **1976-764 (PP 03-20)**, matches Spartan's standard Coleman row:

| SpartanStart lead | Compressor winding | Wire color on this unit |
| --- | --- | --- |
| Blue | Run (R) | White |
| Black | Common (C) | Black |
| Red | Start (S) | Red |

The SpartanStart splices **inline** into all three compressor wires: each wire is cut, and the supply-side end goes to the SpartanStart's supply harness while the compressor-side end goes to its compressor harness (six splices). Still check the colors at the compressor before cutting, and never swap Run and Start.

Start components (start capacitor, start relay, PTCR) are optional on this sticker. If any are present, remove them as described in the procedure below.

## Procedure

The full step-by-step procedure, including the power-down sequence, the start-component check, splicing, mounting and the shore-power test, is **Phase 2** of the [whole-panel inverter guide](../03-whole-panel-inverter/README.md#phase-2---install-and-test-the-soft-start-shore-power-only).

Key points:

- Kill all power (A/C breaker, shore power, inverter) and wait 2 minutes for the run capacitor to discharge.
- Work from a ladder; Casita does not recommend walking on the roof.
- Photograph the sticker and all wiring before changing anything; keep any removed parts for warranty purposes.
- R-32 refrigerant is mildly flammable: no torches or open flame near the refrigerant lines.
- Test on shore power first. Then test on the inverter once the transfer switch is installed.

## Results

**To record:** install date, start current before and after (clamp meter with inrush mode, if available), and whether the A/C starts from the inverter.

## Revisions

| Date | Change |
| --- | --- |
| 2026-10 | SpartanStart purchased; wiring confirmed from sticker 1976-764 |
