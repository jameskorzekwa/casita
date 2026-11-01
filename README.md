# Casita Liberty 17 (2026 Deluxe)

Everything about our 2026 Casita Liberty 17 Deluxe travel trailer: what it came with, every modification made to it, and its manuals. Shared so other Casita owners can learn from (and improve on) these projects.

This repository is the maintained record. The Google Docs that some of this started in are kept only as history (see [Sources](#sources)).

## Layout

| Path | Contents |
| --- | --- |
| [`docs/trailer.md`](docs/trailer.md) | Specifications, factory equipment, model numbers, breakers, and weight limits |
| [`docs/off-grid-upgrade-plan.md`](docs/off-grid-upgrade-plan.md) | The overall off-grid upgrade plan, including research and decisions |
| [`docs/smart-dc-switch-research.md`](docs/smart-dc-switch-research.md) | Smart DC rocker research; BANDC rocker / Waveshare controller plan in mod 06, installed 2026-10-23 |
| [`docs/ha-flic-sleep-wake.md`](docs/ha-flic-sleep-wake.md) | Flic-triggered sleep/wake and small-button light controls on the trailer Home Assistant |
| [`docs/ha-tv-fan-volume.md`](docs/ha-tv-fan-volume.md) | Insignia Fire TV volume adjustment (+15/−15) based on thermostat fan operation |
| [`modifications/`](modifications/) | One folder per modification, each with its own instructions, diagrams and status |
| [`manuals/`](manuals/) | Equipment manuals and datasheets, organized by system |
| [`photos/`](photos/) | General trailer photos (modification photos live in each modification's folder) |

## Modifications

| # | Modification | Status |
| --- | --- | --- |
| 01 | [Second 300 Ah battery (600 Ah bank)](modifications/01-second-battery/README.md) | Done |
| 02 | [A/C soft start (SpartanStart)](modifications/02-ac-soft-start/README.md) | Done |
| 03 | [Whole-panel inverter with automatic transfer switch](modifications/03-whole-panel-inverter/README.md) | Done |
| 04 | [Battery monitor to Home Assistant (XIAO ESP32-S3 + INA228)](modifications/04-battery-monitor-esp32/README.md) | Installed, running and calibrated; mirrored to the home Home Assistant |
| 05 | [Starlink Mini on 12 V battery power](modifications/05-starlink-12v-power/README.md) | Installed; inline fuse still to add |
| 06 | [Four smart DC switches (BANDC + Waveshare)](modifications/06-smart-dc-switches/README.md) | Installed 2026-10-23: two LED light circuits on the Waveshare relays, two spare channels, rockers and Home Assistant; cabinet cover pending |
| 07 | [Tank monitor to Home Assistant (propane on a XIAO ESP32-S3, fresh via a Garnet Bluetooth display, grey via Mopeka)](modifications/07-tank-monitor/README.md) | Propane reading (uncalibrated); fresh live; grey Mopeka mounted, no echo yet |
| 08 | [E-ink dashboard (TRMNL 7.5" kit + ESPHome)](modifications/08-eink-dashboard/README.md) | Running; real tank entities and a Power page since 2026-10-28 |
| 10 | [AC voltage and power meter (Shelly EM Gen3)](modifications/10-ac-power-meter/README.md) | Both clamps reporting; shore/inverter/no-AC tests passed; intermittent dropout and water-heater heating unverified |
| 11 | [Xantrex Freedom X 2000 inverter to Home Assistant](modifications/11-xantrex-freedom-x-inverter/README.md) | Inverter installed; HA integration installed, first live read pending |
| 12 | [Cold-weather package (grey tank heat, drain protection, battery warming, freeze monitoring)](modifications/12-cold-weather/README.md) | Proposed; nothing ordered or measured |
| 13 | [Level sensor to Home Assistant (LSM6DS3 + XIAO ESP32-S3)](modifications/13-rv-level-sensor/README.md) | Designed; all parts on hand, firmware compiles; leveling view for HA written |

Planned or under consideration (details in the [upgrade plan](docs/off-grid-upgrade-plan.md)):

- Replace the Coleman Mach 8 with a 12 V rooftop A/C (Nomadic X2 Helix or Velit 2000R)
- Inverter/charger to replace the standalone inverter and the WFCO converter
- Roof solar, a DC-DC charger from the tow vehicle, and a roof fan for low-power cooling

Open safety follow-ups:

- Add a 10 A inline fuse on the Starlink adapter's positive wire ([mod 05](modifications/05-starlink-12v-power/README.md#required-fix-add-an-inline-fuse))
- Replace the 1/0 copper-clad aluminum battery cables with pure copper, add a Class-T main fuse, and add a DC disconnect for the inverter ([mod 01](modifications/01-second-battery/README.md#recommended-follow-ups))
- Replace the two IEC-only 20 A breakers in the shore-only box with UL 489 breakers ([mod 03](modifications/03-whole-panel-inverter/README.md#recommended-follow-ups))

## Quick Facts

| Item | Value |
| --- | --- |
| Trailer | 2026 Casita Liberty 17 Deluxe, factory Solar System Package |
| GVWR / dry weight | 3,500 lb / about 2,480 lb |
| Tow vehicle | 2026 Toyota RAV4 PHEV: 3,500 lb tow rating; hitch 750 lb tongue / 5,000 lb |
| Battery bank | 2 x Renogy Core Mini 12.8 V 300 Ah LiFePO4 in parallel (600 Ah) |
| Inverter | Xantrex Freedom X 2000 (817-2000), installed October 2026, replacing the factory Renogy 2000 W ([mod 11](modifications/11-xantrex-freedom-x-inverter/README.md)) |
| Power center | WFCO WF-8900-AD series (auto-detect) |
| A/C | Coleman-Mach Mach 8 Plus Cub, 37200 series (R-32), 9,200 BTU |
| Refrigerator | 12 V only |
| Water heater | Gas/electric; expected 6 US gal (22.7 L), installed label to confirm. [Capacity and electric heat-up estimates](docs/trailer.md#water-heater-capacity-and-electric-heat-up) |

Full details are in [`docs/trailer.md`](docs/trailer.md).

**Seeing the trailer's status:** the **Casita Status** dashboard on the trailer's Home Assistant (sidebar), the **Casita RV** dashboard on the home Home Assistant (mirrored over Tailscale), and the e-ink panel in the trailer ([mod 08](modifications/08-eink-dashboard/README.md)). See [mod 07](modifications/07-tank-monitor/README.md#dashboards).

## Adding Manuals and Documents

- **Manuals** go in `manuals/<system>/` as PDF, named `manufacturer-model-document-type.pdf` in lowercase with hyphens. Add a row to the index in [`manuals/README.md`](manuals/README.md).
- Scan at 300 dpi to searchable (OCR) PDF where possible. GitHub rejects files over 100 MB and warns above 50 MB; split or compress very large scans.

**This repository is public.** Do not add ownership documents (build sheet, purchase agreement, title, registration, warranty registrations) or anything showing the VIN, home address, phone numbers, or home network details. Keep those somewhere private. Check scanned manuals and warranty cards for handwritten personal information before adding them.

The manuals are the manufacturers' and Casita's copyrighted documents, included here for reference.

## Sources

- Google Doc: [Casita 17 Off-Grid Upgrade Plan](https://docs.google.com/document/d/19vtmnKSUH-ELgTdLj574IR7fOklQ4ubDvtKm2_Idk6U/edit), converted to [`docs/off-grid-upgrade-plan.md`](docs/off-grid-upgrade-plan.md) on 2026-10-09.
- Google Doc: [Casita 17 - Whole-Panel Inverter Install Guide](https://docs.google.com/document/d/1UxKIZB7UzQihbwPCcxAGNO0TLYZFERZ462aFt-3PrFA/edit), converted to [`modifications/03-whole-panel-inverter/README.md`](modifications/03-whole-panel-inverter/README.md) on 2026-10-09.
- The battery monitor project moved here from `jameskorzekwa/maker-projects` (`projects/renogy-battery-monitor-esp32`, including the unmerged INA228 redesign from PR #43).
