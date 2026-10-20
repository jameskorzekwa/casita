# Mod 07 components

List created **2026-10-19** from the [Parts](README.md#parts) table; purchase tracking searched Amazon order history back to 2026-10-10 (project start 2026-10-13) and Gmail for other vendors. This file tracks ownership and purchase status only; specifications live in the README.

Status values: `need`, `have` (owner confirmed), `probably-have` (in purchase history, unconfirmed), `to-buy`, `ordered`, `shipped`, `delivered`, `not-needed`.

The repository is public: order references record vendor and date only. Look up an Amazon order with `amazon-shop orders --since 2026-10-10 --match "<ASIN or title words>"`.

**Summary 2026-10-19:** everything is on hand or in transit. Nothing to buy. Waiting on the two sensors (arriving 2026-10-19 to 10-21); check each label reads **L062MTW** before anything else.

| # | Component | Spec / acceptable substitute | Qty | Status | Source / option | Order ref | Notes |
|---|---|---|---:|---|---|---|---|
| 1 | DYP-L062MTW-V1.0 LPG level sensor | UART **controlled** variant only (not MUW/MCW/M4W) | 2 | `ordered` | [Amazon B0C1GHF2M8](https://www.amazon.com/dp/B0C1GHF2M8), Size = UART Controlled | Amazon, ordered 2026-10-12 (qty 2) | Arriving 2026-10-19 to 10-21. Both ordered at once rather than one-then-one. Confirm model label, and whether mating cables/couplant kit are in the box |
| 2 | Magnetic collar, 3D-printed | ASA or PETG, 100 % infill; drawing in README | 2 | `need` | Print at home | — | Filament on hand (owner confirmed 2026-10-19). Print one and test-fit before the second |
| 3 | Neodymium disc magnets 8 x 3 mm, N42 | 3 per collar | 6 | `delivered` | [Amazon B0GFCBFKKQ](https://www.amazon.com/dp/B0GFCBFKKQ) (100 pack) | Amazon, ordered 2026-10-13 | Delivered 2026-10-16 |
| 4 | Silicone dielectric grease (couplant) | Permatex 22058 or Mopeka Sonic Grease | 1 | `delivered` | [Amazon B000AL8VD2](https://www.amazon.com/dp/B000AL8VD2) and [B0CVQVGMWB](https://www.amazon.com/dp/B0CVQVGMWB) | Amazon, ordered 2026-10-13 | Delivered 2026-10-14. Both bought; shared with mod 09 |
| 5 | Seeed Studio XIAO ESP32-S3 | Plain board with U.FL antenna | 1 | `delivered` | [Amazon B0DJ6NQFKX](https://www.amazon.com/dp/B0DJ6NQFKX) (3 pack) | Amazon, ordered 2026-10-14 | Delivered 2026-10-17. One each for mods 07 and 09, one spare |
| 6 | Pololu D24V5F5 12 V to 5 V regulator | 500 mA or more, input to 36 V | 1 | `have` | Owner stock | — | Owner confirmed 2026-10-19 that two are on hand (one each for mods 07 and 09) |
| 7 | 470 uF 25 V electrolytic capacitor | 25 V or higher | 1 | `have` | Owner stock | — | Owner confirmed 2026-10-19 (two on hand) |
| 8 | Inline ATO/ATC fuse holder and 2 A fuse | 2 A | 1 | `have` | Owner stock | — | Owner confirmed 2026-10-19 |
| 9 | 4-conductor shielded cable, 22 AWG | About 2 x 3 m | ~6 m | `have` | Owner stock | — | Owner confirmed 2026-10-19 there is enough (33 ft or more) for mods 07 and 09 together |
| 10 | 1.25 mm pitch 4-pin mating pigtails | Mates with the sensor's white 1.25 mm plug; confirm on the first sensor | 2 | `have` | Owner stock | — | Owner confirmed 2026-10-19 |
| 11 | Small ABS enclosure, about 83 x 58 x 33 mm | IP65 | 1 | `delivered` | [Amazon B0FDQCHNQP](https://www.amazon.com/dp/B0FDQCHNQP) (2 pack) | Amazon, ordered 2026-10-13 | Delivered 2026-10-14. One each for mods 07 and 09 |
| 12 | PG7 cable glands | 3.1-6.6 mm | 1-2 | `delivered` | [Amazon B0CTCG4HMM](https://www.amazon.com/dp/B0CTCG4HMM) (50 pack) | Amazon, ordered 2026-10-13 and again 2026-10-14 | Both delivered; 100 on hand, shared with mod 09 |
| 13 | Adhesive-lined heat-shrink, zip ties | | As needed | `have` | Owner stock | — | Owner confirmed 2026-10-19 |
| 14 | Kapton tape, 10 mm | | 1 roll | `delivered` | [Amazon B07S227ZLH](https://www.amazon.com/dp/B07S227ZLH) (4 rolls) | Amazon, ordered 2026-10-13 | Delivered 2026-10-16 |
| 15 | USB to TTL serial adapter (CP2102) | Bench tool for Steps 1-4 | 1 | `delivered` | [Amazon B078W5L8W1](https://www.amazon.com/dp/B078W5L8W1) (2 pack) | Amazon, ordered 2026-10-13 | Delivered 2026-10-16. Tool, not part of the install |
