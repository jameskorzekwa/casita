# Mod 06 components

List created **2026-10-19**; purchase tracking searches from that date (the rocker order of 2026-10-18 was found by searching back from the project start, 2026-10-13). Specifications and gates come from the [project README](README.md#parts--planning-bom); this file tracks ownership and purchase status only.

Status values: `need`, `have` (owner confirmed), `probably-have` (in purchase history, unconfirmed), `to-buy`, `ordered`, `shipped`, `delivered`, `not-needed`. "TBD" rows cannot be bought until the load worksheet and panel measurements in the README are complete.

The repository is public: order references record vendor and date only. Look up an Amazon order with `amazon-shop orders --since 2026-10-13 --match "<ASIN or title words>"`.

| # | Component | Spec / acceptable substitute | Qty | Status | Source / option | Order ref | Notes |
|---|---|---|---:|---|---|---|---|
| 1 | Momentary rocker switch | 3-pin SPDT `(ON)-OFF-(ON)`, no lamp; BANDC B0CNS17ZMK. Substitute only with the same contact form and a fit check | 4 | `delivered` | [Amazon B0CNS17ZMK](https://www.amazon.com/dp/B0CNS17ZMK) | Amazon, ordered 2026-10-18 | Delivered 2026-10-19 (Amazon order status). Received variant, pin map, UP orientation and fit not yet checked |
| 2 | Waveshare ESP32-S3-POE-ETH-8DI-8RO controller | Exact model (firmware maps DI1–DI8 to GPIO4–GPIO11 and relays to TCA9554 0x20); the non-PoE ESP32-S3-ETH-8DI-8RO uses the same mapping | 1 | `delivered` | [Amazon B0FBKGGKK3](https://www.amazon.com/dp/B0FBKGGKK3) (PoE version) | Amazon, ordered 2026-10-19 | Delivered 2026-10-22 (Amazon order status). Replaces the KinCony KC868-A4S, which was never ordered. Package contents per Waveshare: board in rail-mount case, 2.4 GHz 4 dBi SMA antenna; confirm on unboxing. Not yet inspected or powered |
| 3 | Mounting: 35 mm DIN rail section, location, strain relief | Rail-mount ABS case is included with the board (175 x 90 x 40 mm); needs a mounting spot with wiring, thermal and antenna clearance | 1 | `need` | TBD after the board arrives and a location is measured | — | LMioEtool 83 x 58 mm and DJC 4 x 4 in boxes already owned are too small for the case |
| 4 | Controller input fuse and holder | DC-rated; rating from measured controller demand and conductor | 1 set | `have` | Owner stock (inline/ATC) | — | Rating still to be chosen |
| 5 | Supply transient / reverse-polarity protection | Designed against the measured RV supply envelope | 1, TBD | `need` | TBD | — | Not purchasable until the supply is measured |
| 6 | Signal wire, rocker to board | Fresh 22-18 AWG, labeled; 8 conductors plus common | As measured | `have` | Owner stock | — | 50 ft of 22/4 shielded alarm cable arrived 2026-10-20 (Amazon); one 4-conductor run per rocker covers common, UP, DOWN and a spare |
| 7 | Power wire, supply and loads | Gauge from the load worksheet | As measured | `have` | Owner stock | — | Confirm gauge against the worksheet before use |
| 8 | Insulated quick-disconnects | Female, sized to the received rocker terminals | 12+ | `have` | Owner stock | — | Confirm size against the received rockers |
| 9 | Ring / fork terminals and crimper | Sized to the board and relay terminals | As needed | `have` | Owner stock | — | |
| 10 | Heat-shrink and labels | Conductor ID, durable UP ON / DOWN OFF switch labels | 4 sets + wiring | `have` | Owner stock | — | Check whether the rockers include usable caps or labels |
| 11 | External DC power relays / sockets | DC-rated for each load's running, startup and stall current | Per load, TBD | `need` | TBD | — | Blocked on identifying the four loads. The board's relays are rated ≤10 A / 30 V DC, so small resistive loads may not need these |
| 12 | Coil / load suppression | Matched to the chosen relays | Per inductive circuit, TBD | `need` | TBD | — | Blocked on item 11 |
| 13 | Branch fuses / holders | Per new conductor, from wire and load | Per circuit, TBD | `need` | TBD | — | Blocked on the load worksheet |
| 14 | Multimeter | Continuity and DC voltage | 1 | `have` | Owner stock | — | Tool |
| 15 | Bench 12 V current-limited supply | For off-trailer bench tests | 1 | `have` | Owner stock | — | Tool |
| 16 | WAGO 221 lever nuts | Splices only, not rocker or board terminals | — | `probably-have` | Amazon, ordered 2026-10-11 | — | Owned, but not in the plan; vibration suitability is the owner's call |
