# Mod 10 components

List created **2026-10-19** from the [Parts](README.md#parts) table; purchase tracking searched Amazon order history back to 2026-10-10 and Gmail for other vendors. This file tracks ownership and purchase status only; specifications live in the README.

Status values: `need`, `have` (owner confirmed), `probably-have` (in purchase history, unconfirmed), `to-buy`, `ordered`, `shipped`, `delivered`, `not-needed`.

The repository is public: order references record vendor and date only. Look up an Amazon order with `amazon-shop orders --since 2026-10-19 --match "<ASIN or title words>"`.

**Update 2026-11-01:** owner confirms the second current transformer was installed. After an initial negative shore-power reading, HA reported positive shore watts and `Casita AC Source: shore` at 22:23 UTC; inverter/transfer and energy tests remain pending (see README revisions). The meter and panel clamp were observed working on 2026-10-28.

| # | Component | Spec / acceptable substitute | Qty | Status | Source / option | Order ref | Notes |
|---|---|---|---:|---|---|---|---|
| 1 | Shelly EM Gen3 with 50 A clamp | 110-240 V supply, two CT inputs; includes one 50 A clamp | 1 | `ordered` | [Amazon B0DKFY2ZNV](https://www.amazon.com/dp/B0DKFY2ZNV), $69.99 (same as shelly.com) | Amazon, ordered 2026-10-19 | Arriving 2026-10-21/22. Not the EM **Mini** Gen4 (B0DZHY3VNB), which has no clamp input |
| 2 | Shelly 50 A clamp (CT), second channel | Same clamp as the one in the EM Gen3 box; the 80/120 A clamps are not needed for 30 A service | 1 | `have` | [Amazon B0FJXTPJL5](https://www.amazon.com/dp/B0FJXTPJL5), sold by Shelly USA | Amazon, ordered 2026-10-19 | Installed per owner 2026-11-01; label and placement not independently inspected; HA shore watts positive on follow-up. A duplicate order placed the same day was cancelled |
| 3 | Inline fuse holder, 5 x 20 mm, 250 V, with 2 A fuse | Shelly specifies 2 A external protection; insulated body | 1 | `ordered` | [Amazon B0813Q4S6P](https://www.amazon.com/dp/B0813Q4S6P) (BOJACK inline holder + 150 glass fuses incl. 2 A) | Amazon, ordered 2026-10-19 | Arriving 2026-10-21/22, same order as #1. Confirm the 2 A fuse used is marked 250 V |
| 4 | Plastic junction box, about 4 x 4 x 2 in, with glands or clamps | Same style as the DJC box in mod 03 | 1 | `delivered` | [Amazon B08RHN8H2B](https://www.amazon.com/dp/B08RHN8H2B) (4 pack) | Amazon, ordered 2026-10-07 | Delivered 2026-10-10; mod 03 used one, spares on hand |
| 5 | 14 or 16 AWG stranded wire, black and white, about 1 m each | Shelly terminals take 20-11 AWG | ~1 m each | `have` | Owner stock | — | Owner confirmed 2026-10-19 |
| 6 | Wago 221 lever connectors, rated to 10 AWG | 3- or 5-port | 2 | `delivered` | [Amazon B0DG635MMY](https://www.amazon.com/dp/B0DG635MMY) (60-piece 221-612/613/615 kit) | Amazon, ordered 2026-10-11 | Delivered 2026-10-13 |
| 7 | Ferrules for 14/16 AWG | Optional | 2 | `not-needed` | — | — | Shelly terminals accept bare stranded wire; add later if wanted |
| 8 | Zip ties, labels | | As needed | `have` | Owner stock | — | |
