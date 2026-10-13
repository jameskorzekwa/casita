# Second 300 Ah Battery (600 Ah Bank)

> **Status: done, October 2026.** Installed and paralleled with the factory battery.

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

Both batteries are in the factory battery compartment at the back center of the trailer. The compartment was rearranged to fit the second battery. (The original plan was to mount it inside near the axle; it fit in the existing compartment instead.)

**To record:** how the batteries are secured, and a photo in `photos/`.

## Wiring (as built)

| Item | Part | Link |
| --- | --- | --- |
| Per-battery fuse | Chatovalo MEGA fuse holder with 200 A MEGA fuse, one on each battery's positive (2-pack). M8 studs, 4 AWG to 2/0 | [Amazon](https://www.amazon.com/dp/B0FS27VSYM) |
| Busbars | Joinfworld 250 A power distribution blocks, red and black pair, 4 x M8 studs + 3 x #8 screws each, with covers | [Amazon](https://www.amazon.com/dp/B0BYMNL4YX) |
| Cable | JURPLIX 1/0 AWG **copper-clad aluminum (CCA)** battery cable kit, red and black, with lugs | [Amazon](https://www.amazon.com/dp/B0F8BNBKPB) |

- Each battery connects through its own 200 A fuse to the common positive busbar, and its negative to the common negative busbar. Battery 2 is not daisy-chained off battery 1.
- The **inverter's cables run from the busbars** to the inverter, so the per-battery 200 A fuses are the inverter cable's only protection. There is **no battery disconnect switch**.
- The Renogy RBM500 shunt is in the negative path: battery negatives on **B-**, every load and charger on **P-**. The WFCO converter's negative was originally on B- (so charging was not measured) and was moved to P- in October 2026; the monitor now reads charging correctly. The Starlink adapter's negative is also on P- ([mod 05](../05-starlink-12v-power/README.md)).

## Recommended follow-ups

- **Replace the CCA cable with pure copper (OFC) 1/0.** Copper-clad aluminum carries roughly what 2 AWG copper does, and copper lugs on aluminum strands can loosen and heat over time. This matters for long A/C runs on the inverter at 110-150 A. Until then, feel the lugs after an hour of heavy load.
- **Add a Class-T main fuse** (for example 300 A in a Blue Sea 5502 holder) between the positive busbar and the loads. MEGA fuses interrupt about 2,000 A; a 600 Ah lithium bank can deliver well over 10,000 A into a short. Class-T is rated about 20,000 A.
- **Add a DC disconnect** for the inverter. A 250 A DC circuit breaker in the inverter's positive cable would serve as both its fuse (Renogy recommends 250 A) and an off switch for maintenance.

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
| 2026-10 | Second battery installed and paralleled in the rear compartment; MEGA fuses, busbars and CCA cable recorded; converter negative moved to shunt P- |
