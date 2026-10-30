# Mod 13 components

List created **2026-10-25** from the [Parts](README.md#parts) table. Amazon order history for 2024-2026 showed no accelerometer or IMU purchases (searched LSM6DS3, LSM6DSO, BMI270, MPU6050, accelerometer, gyroscope). The owner confirmed every other line on hand on 2026-10-25. Purchase tracking searches from 2026-10-25. This file tracks ownership and purchase status only; specifications live in the README.

Status values: `need`, `have` (owner confirmed), `probably-have` (in purchase history, unconfirmed), `to-buy`, `ordered`, `shipped`, `delivered`, `not-needed`.

The repository is public: order references record vendor and date only. Look up an Amazon order with `amazon-shop orders --since 2026-10-25 --match "<ASIN or title words>"`. For an Adafruit or Digi-Key order, search Gmail for the vendor name after 2026/10/25.

**Summary 2026-10-25:** one item to buy, the LSM6DS3TR-C sensor board (about $10 plus shipping). Everything else is on hand.

| # | Component | Spec / acceptable substitute | Qty | Status | Source / option | Order ref | Notes |
|---|---|---|---:|---|---|---|---|
| 1 | LSM6DS3TR-C 6-DoF IMU breakout | Chip ID 0x6A (LSM6DS3TR-C) or 0x69 (LSM6DS3) only; **not** LSM6DSO/DSOX (0x6C), which ESPHome 2026.10.0 rejects | 1 | `to-buy` | [Adafruit 4503](https://www.adafruit.com/product/4503) $9.95 (recommended); alternatives [Amazon B0FKT9ZR2X](https://www.amazon.com/dp/B0FKT9ZR2X) 2 pcs $8.99, [Amazon B07K5LVMZ2](https://www.amazon.com/dp/B07K5LVMZ2) $6.99 | — | Not from Amazon by default: no Amazon listing is a known-genuine board with a confirmed chip. 2026-10-25: owner asked about B0FKT9ZR2X (acceptable; on arrival confirm chip ID 0x69/0x6A and the I2C address, which may be 0x6B) and HiLetgo GY-521 MPU6050 B00LP25V1A (rejected: ESPHome's `mpu6050` platform is not a `motion` hub, so no pitch/roll, calibration or moving detection without rewriting the firmware) |
| 2 | STEMMA QT to male header cable | Adafruit 4209, 4-pin JST SH; or solder four wires | 1 | `not-needed` | [Adafruit 4209](https://www.adafruit.com/product/4209) $0.95 | — | Optional add-on to the Adafruit order if you do not want to solder at the sensor end |
| 3 | Seeed Studio XIAO ESP32-S3 | Plain board with U.FL antenna | 1 | `have` | Owner stock | — | Owner confirmed a spare beyond mods 07/09, 2026-10-25 |
| 4 | Pololu D24V5F5 12 V to 5 V regulator | 500 mA or more, input to 36 V | 1 | `have` | Owner stock | — | Owner confirmed 2026-10-25 |
| 5 | 470 uF 25 V electrolytic capacitor | 25 V or higher | 1 | `have` | Owner stock | — | Owner confirmed 2026-10-25 |
| 6 | Inline ATO/ATC fuse holder and 2 A fuse | 2 A | 1 | `have` | Owner stock | — | Owner confirmed 2026-10-25 |
| 7 | ABS box with mounting ears, about 83 x 58 x 33 mm | Must screw down rigidly | 1 | `have` | Owner stock | — | Owner confirmed 2026-10-25 |
| 8 | PG7 cable gland | 3.1-6.6 mm | 1 | `have` | Owner stock (Amazon B0CTCG4HMM, 2026-10-13/14) | — | Shared stock with mods 07/09 |
| 9 | 18-20 AWG red and black wire, butt splices | 12 V feed | As needed | `have` | Owner stock | — | Owner confirmed 2026-10-25 |
| 10 | Heat-shrink, Kapton tape, zip ties | | As needed | `have` | Owner stock | — | Owner confirmed 2026-10-25 |
| 11 | M2.5/M3 nylon standoffs and screws | Hold the IMU rigidly to the box floor | 4 | `have` | Owner stock | — | Owner confirmed 2026-10-25 |
| 12 | #8 pan-head screws | Shorter than the floor thickness at the chosen spot | 2-4 | `have` | Owner stock | — | Length chosen on site |
| 13 | Reference level (digital or machinist) | Tool, for calibration | 1 | `have` | Owner stock | — | Owner confirmed 2026-10-25 |
| 14 | USB-C data cable | Tool, first flash | 1 | `have` | Owner stock | — | Owner confirmed 2026-10-25 |
| 15 | Leveling blocks and wheel chocks | For example Lynx Levelers, Andersen Camper Leveler | 1 set | `have` | Owner stock | — | Owner confirmed 2026-10-25 |
