# Mod 07 components (tank monitor)

Merged **2026-10-27** from the propane monitor and water tank monitor lists, both created **2026-10-19** from their Parts tables; purchase tracking searched Amazon order history back to 2026-10-10 and Gmail for other vendors. This file tracks ownership and purchase status only; specifications are in the [README](README.md#parts), [propane.md](propane.md#parts) and [water-tanks.md](water-tanks.md#parts).

Status values: `need`, `have` (owner confirmed), `probably-have` (in purchase history, unconfirmed), `to-buy`, `ordered`, `shipped`, `delivered`, `not-needed`.

The repository is public: order references record vendor and date only. Look up an Amazon order with `amazon-shop orders --since 2026-10-10 --match "<ASIN or title words>"`.

**Summary 2026-10-27:** nothing to buy except optional split loom for the grey cable. All four sensors are here: the SeeLeveL sender and the DYP L02 (owner confirmed) and both DYP L06 (Amazon shows them delivered 2026-10-27; check each label reads **L062MTW**). Moving the grey sensor onto the main device freed the former grey device's XIAO, regulator, capacitor, fuse holder and enclosure as spares. Still to make: the two magnetic collars.

## Main device (`casita-tank-monitor`)

| # | Component | Spec / acceptable substitute | Qty | Status | Source / option | Order ref | Notes |
|---|---|---|---:|---|---|---|---|
| 1 | Seeed Studio XIAO ESP32-S3 | Plain board with U.FL antenna | 1 | `have` | [Amazon B0DJ6NQFKX](https://www.amazon.com/dp/B0DJ6NQFKX) (3 pack) | Amazon, ordered 2026-10-14 | Delivered 2026-10-17. 3 pack: main, fresh, one spare. Main board flashed 2026-10-27 |
| 2 | Pololu D24V5F5 12 V to 5 V regulator | 500 mA or more, input to 36 V | 1 | `have` | Owner stock | — | Owner confirmed 2026-10-19 and 2026-10-20 (three on hand) |
| 3 | 470 uF 25 V electrolytic capacitor | 25 V or higher | 1 | `have` | Owner stock | — | Owner confirmed 2026-10-19 |
| 4 | Inline ATO/ATC fuse holder and 2 A fuse | 2 A | 1 | `have` | Owner stock | — | Owner confirmed 2026-10-19 |
| 5 | Small ABS enclosure, about 83 x 58 x 33 mm | IP65; four glands | 1 | `delivered` | [Amazon B0FDQCHNQP](https://www.amazon.com/dp/B0FDQCHNQP) (2 pack) | Amazon, ordered 2026-10-13 | Delivered 2026-10-14. 2 pack: main and fresh |
| 6 | PG7 cable glands | 3.1-6.6 mm | 4-6 | `delivered` | [Amazon B0CTCG4HMM](https://www.amazon.com/dp/B0CTCG4HMM) (50 pack) | Amazon, ordered 2026-10-13 and 2026-10-14 | 100 on hand, shared with the fresh device |
| 7 | 18-20 AWG red and black wire, crimp butt splices | 12 V taps | As needed | `have` | Owner stock | — | Owner confirmed 2026-10-19 |
| 8 | Header pins or small screw-terminal strip | Shared 3V3 / GND for three sensors | 1 | `need` | Owner stock? | — | Ask the owner; any small terminal strip works |

## Propane sensors

| # | Component | Spec / acceptable substitute | Qty | Status | Source / option | Order ref | Notes |
|---|---|---|---:|---|---|---|---|
| 9 | DYP-L062MTW-V1.0 LPG level sensor | UART **controlled** variant only (not MUW/MCW/M4W) | 2 | `delivered` | [Amazon B0C1GHF2M8](https://www.amazon.com/dp/B0C1GHF2M8), Size = UART Controlled | Amazon, ordered 2026-10-12 (qty 2) | Amazon shows delivered 2026-10-27. Confirm the model label, and whether mating cables or a couplant kit are in the box |
| 10 | Magnetic collar, 3D-printed | ASA or PETG, 100 % infill; drawing in propane.md | 2 | `need` | Print at home | — | Filament on hand (owner confirmed 2026-10-19). Print one and test-fit before the second |
| 11 | Neodymium disc magnets 8 x 3 mm, N42 | 3 per collar | 6 | `delivered` | [Amazon B0GFCBFKKQ](https://www.amazon.com/dp/B0GFCBFKKQ) (100 pack) | Amazon, ordered 2026-10-13 | Delivered 2026-10-16 |
| 12 | Silicone dielectric grease (couplant) | Permatex 22058 or Mopeka Sonic Grease | 1 | `delivered` | [Amazon B000AL8VD2](https://www.amazon.com/dp/B000AL8VD2) and [B0CVQVGMWB](https://www.amazon.com/dp/B0CVQVGMWB) | Amazon, ordered 2026-10-13 | Delivered 2026-10-14. Shared with the grey sensor |
| 13 | 4-conductor shielded cable, 22 AWG | About 2 x 3 m propane, plus the grey run | ~6 m + grey | `have` | Owner stock | — | Owner confirmed 2026-10-19 at least 33 ft on hand. Measure the grey run in Step M1 and check the roll still covers all three |
| 14 | 1.25 mm pitch 4-pin mating pigtails | Mates with the L06's white 1.25 mm plug; confirm on the first sensor | 2 | `have` | Owner stock | — | Owner confirmed 2026-10-19 |
| 15 | Adhesive-lined heat-shrink, zip ties, Kapton tape | | As needed | `have` / `delivered` | Owner stock; [Amazon B07S227ZLH](https://www.amazon.com/dp/B07S227ZLH) (Kapton) | Amazon, ordered 2026-10-13 | Kapton delivered 2026-10-16 |
| 16 | USB to TTL serial adapter (CP2102) | Bench tool, troubleshooting only | 1 | `delivered` | [Amazon B078W5L8W1](https://www.amazon.com/dp/B078W5L8W1) (2 pack) | Amazon, ordered 2026-10-13 | Delivered 2026-10-16. Tool, not part of the install |

## Grey sensor (on the main device)

| # | Component | Spec / acceptable substitute | Qty | Status | Source / option | Order ref | Notes |
|---|---|---|---:|---|---|---|---|
| 17 | DYP-L023MUW-V1.0 (L02, UART Automatic) | Size option must be **UART Automatic** | 1 | `have` | [Amazon B0C1GFJKMV](https://www.amazon.com/dp/B0C1GFJKMV) | Amazon, ordered 2026-10-14 | On hand (owner, 2026-10-27). Confirm the plug pitch (2.54 mm XH vs 1.25 mm); pigtails for both are on hand |
| 18 | JST-XH 2.54 mm 4-pin pigtails | For the L02 plug if it is XH; 1.25 mm pigtails (#14) if not | 1 pack | `have` | Owner stock | — | Owner confirmed 2026-10-19 |
| 19 | 3M 9495LE (300LSE) double-sided tape | Holds the L02 to the tank | 1 roll | `have` | Owner stock | — | Owner confirmed 2026-10-19 |
| 20 | 3M Primer 94 (adhesion promoter) | Polyolefin primer | 1 | `delivered` | [Amazon B0GM1GQW94](https://www.amazon.com/dp/B0GM1GQW94) | Amazon, ordered 2026-10-14 | Delivered 2026-10-16 |
| 21 | Split loom, about 10 mm | Protects the L02 cable along the frame | Measure | `need` | Owner stock or any auto-parts loom | — | Added 2026-10-27 with the longer cable run; ask the owner before buying |
| 22 | Rubberized undercoating | Garnet names 3M 03584; Barrier Bond bought as the equivalent | 1 can | `delivered` | [Amazon B083ZKP5L9](https://www.amazon.com/dp/B083ZKP5L9) | Amazon, ordered 2026-10-14 | Delivered 2026-10-16/17. Shared with the fresh sender |

## Fresh device (`casita-water-monitor-fresh`)

| # | Component | Spec / acceptable substitute | Qty | Status | Source / option | Order ref | Notes |
|---|---|---|---:|---|---|---|---|
| 23 | Garnet SeeLeveL II 710-ES3 sender, 12 in | Sold by RecPro as "SeeLevel 710 RV Tank Level Sensor (12")" | 1 | `have` | [Amazon B0GWJR52N8](https://www.amazon.com/dp/B0GWJR52N8) | Amazon, ordered 2026-10-14 | On hand (owner, 2026-10-20). Paid about $56 |
| 24 | Seeed Studio XIAO ESP32-S3 | Plain board with U.FL antenna | 1 | `delivered` | Same 3 pack as #1 | Same order | |
| 25 | Pololu D24V5F5 regulator | | 1 | `have` | Owner stock | — | Owner confirmed 2026-10-19 |
| 26 | 470 uF 25 V electrolytic capacitor | | 1 | `have` | Owner stock | — | Owner confirmed 2026-10-19 |
| 27 | 2N3906 PNP transistor (TO-92) | Q101; 2N2907, S8550 or BC557 (reversed pinout) substitute | 1 | `delivered` | [Amazon B0DGT7RTZC](https://www.amazon.com/dp/B0DGT7RTZC) (32-value kit) | Amazon, ordered 2026-10-14 | Delivered 2026-10-16/17 |
| 28 | 2N3904 NPN transistor (TO-92) | Q102, Q103; same kit | 2 | `delivered` | Same kit as #27 | Same order | |
| 29 | Resistors 1/4 W: 2.2 k x2, 1 k x2, 220, 22 k, 10 k | R101-R107 | 7 | `have` | Owner stock | — | Per the original README |
| 30 | Perfboard about 30 x 40 mm, 5-pin terminal or header | | 1 | `delivered` | [Amazon B07ZYNWJ1S](https://www.amazon.com/dp/B07ZYNWJ1S) | Amazon, ordered 2026-10-14 | Delivered 2026-10-16/17 |
| 31 | Inline ATO/ATC fuse holder and 2 A fuse | On the pump-circuit tap | 1 | `have` | Owner stock | — | Owner confirmed 2026-10-19 |
| 32 | Small ABS enclosure, about 83 x 58 x 33 mm | IP65 | 1 | `delivered` | Same 2 pack as #5 | Same order | |

## Freed by the 2026-10-27 combination

These were the separate grey device's parts. They are no longer needed for this project and are spares.

| # | Component | Qty | Status | Notes |
|---|---|---:|---|---|
| 33 | Seeed Studio XIAO ESP32-S3 | 1 | `not-needed` | Third board of the 3 pack (#1) |
| 34 | Pololu D24V5F5 regulator | 1 | `not-needed` | Owner stock |
| 35 | 470 uF 25 V capacitor | 1 | `not-needed` | Owner stock |
| 36 | Inline fuse holder and 2 A fuse | 1 | `not-needed` | Owner stock |
| 37 | Small ABS enclosure | 1 | `not-needed` | Owner stock (third box) |
