# Mod 09 components

List created **2026-10-19** from the [Parts](README.md#parts) table; purchase tracking searched Amazon order history back to 2026-10-10 and Gmail for other vendors. This file tracks ownership and purchase status only; specifications live in the README.

Status values: `need`, `have` (owner confirmed), `probably-have` (in purchase history, unconfirmed), `to-buy`, `ordered`, `shipped`, `delivered`, `not-needed`.

The repository is public: order references record vendor and date only. Look up an Amazon order with `amazon-shop orders --since 2026-10-10 --match "<ASIN or title words>"`.

**Summary 2026-10-19:** everything is on hand or in transit. Nothing to buy. Waiting on the two sensors: the SeeLeveL sender arrives 2026-10-22, the DYP L02 2026-10-21 to 10-23. Follow the arrival checks in [What to order](README.md#what-to-order).

| # | Component | Spec / acceptable substitute | Qty | Status | Source / option | Order ref | Notes |
|---|---|---|---:|---|---|---|---|
| 1 | Garnet SeeLeveL II 710-ES3 sender, 12 in | Sold by RecPro as "SeeLevel 710 RV Tank Level Sensor (12")" | 1 | `ordered` | [Amazon B0GWJR52N8](https://www.amazon.com/dp/B0GWJR52N8) | Amazon, ordered 2026-10-14 | Arriving 2026-10-22. Paid about $56 (README estimate of $70 was high) |
| 2 | DYP-L023MUW-V1.0 (L02, UART Automatic) | Size option must be **UART Automatic** | 1 | `ordered` | [Amazon B0C1GFJKMV](https://www.amazon.com/dp/B0C1GFJKMV) | Amazon, ordered 2026-10-14 | Arriving 2026-10-21 to 10-23. Confirm the plug pitch (2.54 mm XH vs 1.25 mm) on arrival; pigtails for both are on hand |
| 3 | Seeed Studio XIAO ESP32-S3 | Plain board with U.FL antenna | 1 | `delivered` | [Amazon B0DJ6NQFKX](https://www.amazon.com/dp/B0DJ6NQFKX) (3 pack) | Amazon, ordered 2026-10-14 | Delivered 2026-10-17. Shared with mod 07 |
| 4 | Pololu D24V5F5 12 V to 5 V regulator | | 1 | `have` | Owner stock | — | Owner confirmed 2026-10-19 (two on hand, one each for mods 07 and 09) |
| 5 | 470 uF 25 V electrolytic capacitor | | 1 | `have` | Owner stock | — | Owner confirmed 2026-10-19 |
| 6 | 2N3906 PNP transistor (TO-92) | Q101; 2N2907, S8550 or BC557 (reversed pinout) substitute | 1 | `delivered` | [Amazon B0DGT7RTZC](https://www.amazon.com/dp/B0DGT7RTZC) (32-value kit) | Amazon, ordered 2026-10-14 | Delivered 2026-10-16/17 |
| 7 | 2N3904 NPN transistor (TO-92) | Q102, Q103; same kit | 2 | `delivered` | Same kit as #6 | Same order | |
| 8 | Resistors 1/4 W: 2.2 k x2, 1 k x2, 220, 22 k, 10 k | R101-R107 | 7 | `have` | Owner stock | — | Per README |
| 9 | Perfboard about 30 x 40 mm, 5-pin terminal or header | | 1 | `delivered` | [Amazon B07ZYNWJ1S](https://www.amazon.com/dp/B07ZYNWJ1S) | Amazon, ordered 2026-10-14 | Delivered 2026-10-16/17 |
| 10 | 4-conductor shielded cable, 22 AWG | About 3 m to the grey tank, 1 m to the sender | ~4 m | `have` | Owner stock | — | Owner confirmed 2026-10-19 enough for mods 07 and 09 together |
| 11 | JST-XH 2.54 mm 4-pin pigtails | For the L02 plug if it is XH; 1.25 mm pigtails (mod 07) if not | 1 pack | `have` | Owner stock | — | Owner confirmed 2026-10-19 |
| 12 | Inline ATO/ATC fuse holder and 2 A fuses | On the 12 V tap | 1 | `have` | Owner stock | — | Owner confirmed 2026-10-19 |
| 13 | Small ABS enclosure, about 83 x 58 x 33 mm | IP65 | 1 | `delivered` | [Amazon B0FDQCHNQP](https://www.amazon.com/dp/B0FDQCHNQP) (2 pack) | Amazon, ordered 2026-10-13 | Delivered 2026-10-14. Shared with mod 07 |
| 14 | Silicone dielectric grease | Permatex 22058 | 1 | `delivered` | [Amazon B000AL8VD2](https://www.amazon.com/dp/B000AL8VD2) | Amazon, ordered 2026-10-13 | Delivered 2026-10-14. Mopeka Sonic Grease sachets also on hand |
| 15 | 3M 9495LE (300LSE) double-sided tape | Holds the L02 to the tank | 1 roll | `have` | Owner stock | — | Owner confirmed 2026-10-19 |
| 16 | 3M Primer 94 (adhesion promoter) | Polyolefin primer | 1 | `delivered` | [Amazon B0GM1GQW94](https://www.amazon.com/dp/B0GM1GQW94) | Amazon, ordered 2026-10-14 | Delivered 2026-10-16 |
| 17 | Rubberized undercoating | Garnet names 3M 03584; Barrier Bond bought as the equivalent | 1 can | `delivered` | [Amazon B083ZKP5L9](https://www.amazon.com/dp/B083ZKP5L9) | Amazon, ordered 2026-10-14 | Delivered 2026-10-16/17 |
| 18 | Adhesive-lined heat-shrink, zip ties, painter's tape, Gorilla tape | | As needed | `have` | Owner stock | — | Owner confirmed 2026-10-19 |
| 19 | 18-20 AWG red and black wire, crimp butt splices | 12 V tap to the enclosure | As needed | `have` | Owner stock | — | Owner confirmed 2026-10-19 |
| 20 | PG7 cable glands | | 1-2 | `delivered` | [Amazon B0CTCG4HMM](https://www.amazon.com/dp/B0CTCG4HMM) (50 pack) | Amazon, ordered 2026-10-13 and 2026-10-14 | 100 on hand, shared with mod 07 |
