# Mod 09 components

List created **2026-10-19** from the [Parts](README.md#parts) table; purchase tracking searched Amazon order history back to 2026-10-10 and Gmail for other vendors. Reorganized **2026-10-20** when the project split into two devices (fresh and grey), each with its own XIAO, regulator, capacitor, fuse and enclosure. This file tracks ownership and purchase status only; specifications live in the README.

Status values: `need`, `have` (owner confirmed), `probably-have` (in purchase history, unconfirmed), `to-buy`, `ordered`, `shipped`, `delivered`, `not-needed`.

The repository is public: order references record vendor and date only. Look up an Amazon order with `amazon-shop orders --since 2026-10-10 --match "<ASIN or title words>"`.

**Summary 2026-10-20:** nothing to buy. The SeeLeveL sender is on hand, so the fresh device can be built now. Waiting only on the DYP L02 for the grey device (due 2026-10-21 to 10-23); follow the arrival checks in [What to order](README.md#what-to-order). The second device's extra regulator, capacitor, enclosure and fuse holder with fuse are owner stock (confirmed 2026-10-20); Amazon order history could not be read that day (the `amazon-shop orders` parser failed), so their order references are not recorded.

## Fresh device (`casita-water-monitor-fresh`)

| # | Component | Spec / acceptable substitute | Qty | Status | Source / option | Order ref | Notes |
|---|---|---|---:|---|---|---|---|
| 1 | Garnet SeeLeveL II 710-ES3 sender, 12 in | Sold by RecPro as "SeeLevel 710 RV Tank Level Sensor (12")" | 1 | `delivered` | [Amazon B0GWJR52N8](https://www.amazon.com/dp/B0GWJR52N8) | Amazon, ordered 2026-10-14 | On hand (owner, 2026-10-20). Paid about $56 |
| 2 | Seeed Studio XIAO ESP32-S3 | Plain board with U.FL antenna | 1 | `delivered` | [Amazon B0DJ6NQFKX](https://www.amazon.com/dp/B0DJ6NQFKX) (3 pack) | Amazon, ordered 2026-10-14 | Delivered 2026-10-17. 3 pack: one each for mod 07, fresh and grey |
| 3 | Pololu D24V5F5 12 V to 5 V regulator | | 1 | `have` | Owner stock | — | Owner confirmed 2026-10-19 (two on hand, mods 07 and 09) |
| 4 | 470 uF 25 V electrolytic capacitor | | 1 | `have` | Owner stock | — | Owner confirmed 2026-10-19 |
| 5 | 2N3906 PNP transistor (TO-92) | Q101; 2N2907, S8550 or BC557 (reversed pinout) substitute | 1 | `delivered` | [Amazon B0DGT7RTZC](https://www.amazon.com/dp/B0DGT7RTZC) (32-value kit) | Amazon, ordered 2026-10-14 | Delivered 2026-10-16/17 |
| 6 | 2N3904 NPN transistor (TO-92) | Q102, Q103; same kit | 2 | `delivered` | Same kit as #5 | Same order | |
| 7 | Resistors 1/4 W: 2.2 k x2, 1 k x2, 220, 22 k, 10 k | R101-R107 | 7 | `have` | Owner stock | — | Per README |
| 8 | Perfboard about 30 x 40 mm, 5-pin terminal or header | | 1 | `delivered` | [Amazon B07ZYNWJ1S](https://www.amazon.com/dp/B07ZYNWJ1S) | Amazon, ordered 2026-10-14 | Delivered 2026-10-16/17 |
| 9 | Inline ATO/ATC fuse holder and 2 A fuse | On the pump-circuit tap | 1 | `have` | Owner stock | — | Owner confirmed 2026-10-19 |
| 10 | Small ABS enclosure, about 83 x 58 x 33 mm | IP65 | 1 | `delivered` | [Amazon B0FDQCHNQP](https://www.amazon.com/dp/B0FDQCHNQP) (2 pack) | Amazon, ordered 2026-10-13 | Delivered 2026-10-14. 2 pack shared with mod 07 |

## Grey device (`casita-water-monitor-grey`)

| # | Component | Spec / acceptable substitute | Qty | Status | Source / option | Order ref | Notes |
|---|---|---|---:|---|---|---|---|
| 11 | DYP-L023MUW-V1.0 (L02, UART Automatic) | Size option must be **UART Automatic** | 1 | `ordered` | [Amazon B0C1GFJKMV](https://www.amazon.com/dp/B0C1GFJKMV) | Amazon, ordered 2026-10-14 | Arriving 2026-10-21 to 10-23. Confirm the plug pitch (2.54 mm XH vs 1.25 mm) on arrival; pigtails for both are on hand |
| 12 | Seeed Studio XIAO ESP32-S3 | Plain board with U.FL antenna | 1 | `delivered` | Same 3 pack as #2 | Same order | The pack's third board (formerly the spare) |
| 13 | Pololu D24V5F5 12 V to 5 V regulator | Second one for mod 09 | 1 | `have` | Owner stock | — | Owner confirmed 2026-10-20 |
| 14 | 470 uF 25 V electrolytic capacitor | Second one for mod 09 | 1 | `have` | Owner stock | — | Owner confirmed 2026-10-20 |
| 15 | Inline ATO/ATC fuse holder and 2 A fuse | On the closet 12 V tap | 1 | `have` | Owner stock | — | Owner confirmed 2026-10-20 |
| 16 | Small ABS enclosure, about 83 x 58 x 33 mm | IP65 or similar | 1 | `have` | Owner stock | — | Owner confirmed 2026-10-20 (a third box beyond the mod 07 / fresh 2 pack) |
| 17 | 4-conductor shielded cable, 22 AWG | Tank to closet; measure in Step G1 | 1-2 m | `have` | Owner stock | — | Owner confirmed 2026-10-19 enough for mods 07 and 09 together |
| 18 | JST-XH 2.54 mm 4-pin pigtails | For the L02 plug if it is XH; 1.25 mm pigtails (mod 07) if not | 1 pack | `have` | Owner stock | — | Owner confirmed 2026-10-19 |
| 19 | Silicone dielectric grease | Permatex 22058 | 1 | `delivered` | [Amazon B000AL8VD2](https://www.amazon.com/dp/B000AL8VD2) | Amazon, ordered 2026-10-13 | Delivered 2026-10-14. Mopeka Sonic Grease sachets also on hand |
| 20 | 3M 9495LE (300LSE) double-sided tape | Holds the L02 to the tank | 1 roll | `have` | Owner stock | — | Owner confirmed 2026-10-19 |
| 21 | 3M Primer 94 (adhesion promoter) | Polyolefin primer | 1 | `delivered` | [Amazon B0GM1GQW94](https://www.amazon.com/dp/B0GM1GQW94) | Amazon, ordered 2026-10-14 | Delivered 2026-10-16 |
| 22 | PG7 cable glands | Floor penetration and enclosure entry | 1-3 | `delivered` | [Amazon B0CTCG4HMM](https://www.amazon.com/dp/B0CTCG4HMM) (50 pack) | Amazon, ordered 2026-10-13 and 2026-10-14 | 100 on hand, shared with mod 07 |

## Shared supplies

| # | Component | Spec / acceptable substitute | Qty | Status | Source / option | Order ref | Notes |
|---|---|---|---:|---|---|---|---|
| 23 | Rubberized undercoating | Garnet names 3M 03584; Barrier Bond bought as the equivalent | 1 can | `delivered` | [Amazon B083ZKP5L9](https://www.amazon.com/dp/B083ZKP5L9) | Amazon, ordered 2026-10-14 | Delivered 2026-10-16/17 |
| 24 | Adhesive-lined heat-shrink, zip ties, painter's tape, Gorilla tape | | As needed | `have` | Owner stock | — | Owner confirmed 2026-10-19 |
| 25 | 18-20 AWG red and black wire, crimp butt splices | Both 12 V taps | As needed | `have` | Owner stock | — | Owner confirmed 2026-10-19 |
