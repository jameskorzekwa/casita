# Second 300 Ah Battery (600 Ah Bank)

> **Status: done.** Installed and paralleled with the factory battery.

The factory Solar System Package came with one Renogy 300 Ah LiFePO4 battery. A second, identical battery (confirmed with Casita to be the same model) was added in parallel, doubling the bank to 600 Ah (about 7.7 kWh nominal).

## Battery

Renogy Core Mini 12.8 V 300 Ah LiFePO4 with low-temperature protection, model RBT12300LFP-M ([manual](../../manuals/electrical/renogy-core-mini-300ah-battery-manual.pdf)).

| Spec | Value |
| --- | --- |
| Continuous discharge / BMS | 200 A |
| Peak discharge | 380 A for 10 s |
| Max charge current | 150 A |
| Dimensions | 15.12 x 7.64 x 9.96 in |
| Weight | 55.1 lb |
| Terminals | M8 threaded inserts, 8 N-m (70.8 in-lb). Use the supplied 16 mm bolts where two lugs stack |
| Low temperature | Charging disabled at or below 32 F (resumes at 41 F); discharge allowed to -4 F. No self-heating |
| Parallel limit | Up to 4 in parallel |
| Bluetooth | None (use a shunt monitor) |

## Location

The factory battery sits in the rear exterior battery compartment, which holds only one battery. The plan was to mount the second battery inside, low and close to the axle (under the dinette), so it adds almost nothing to tongue weight.

**To record:** where the second battery was actually mounted, how it is secured, and the cable length to the busbar. Add a photo to `photos/`.

## Wiring

- Each battery has **its own fuse** at its positive terminal (the factory battery keeps its factory fuse; the new one has a matching fuse). Per-battery fuses protect each battery's cable; the inverter is protected by its own fuse (Renogy recommends 250 A).
- Both batteries connect to a **common positive and negative busbar** with equal-length, equal-gauge cables. Battery 2 is not daisy-chained off battery 1.
- Fuses should be Class-T (or at least ANL) because a lithium bank can deliver very high fault current.

**To record:** cable gauge, fuse type and rating for each battery, and the busbar used.

## Connecting the batteries (procedure used)

1. Charge each battery to full separately.
2. Measure each battery's resting voltage directly at its terminals after at least 2 hours without charging or load. **They must be within 0.1 V of each other** (Renogy's requirement). An initial 0.2 V difference was corrected by charging before connecting.
3. With everything off and shore power unplugged, connect **both negatives first, then the positives**. The last positive connection is the only point where a small spark can occur.
4. Let the bank rest connected for 12-24 hours before putting it into service.

To disconnect later: positives first, then negatives.

## Maintenance

- Re-check that the two batteries are within 0.1 V of each other about every 6 months.
- Retorque terminals to 8 N-m when inspecting.
- Below freezing the batteries will not accept charge; that is normal for this model.

## Revisions

| Date | Change |
| --- | --- |
| 2026-10 | Second battery installed and paralleled |
