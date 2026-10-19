# Trailer Specifications and Equipment

What is installed on the trailer, with the source of each fact. "To confirm" means the value is believed correct but has not been read off the equipment label. Update this file whenever a label is read or equipment changes.

## Trailer

| Item | Value | Source / status |
| --- | --- | --- |
| Model | 2026 Casita Liberty 17 Deluxe | Owner |
| Options | Factory Solar System Package (300 Ah LiFePO4, 2000 W inverter with two inverted outlets, 200 W portable solar panel) | Casita add-ons page |
| GVWR | 3,500 lb | Casita / dealer listings |
| Dry weight | About 2,480 lb (17' Deluxe) | Dealer listings; weigh the actual trailer |
| Dry tongue weight | Not published; owners report 350-450 lb loaded | To measure |
| Length / width | 204 in (17 ft) / 80 in | Dealer listings |
| Fresh water | 16 gal, tank 12 in tall (natural polyethylene, rear passenger side bay) | Owner manual (16 gal); height measured by owner 2026-10 |
| Grey water | 32 gal, belly tank under the floor, about 4 in tall, black polyethylene | Casita store (32 gal); height from an owner video, to confirm |
| Black water | 15 gal, under the toilet | Owner manual |
| Tank monitor | None from the factory; [mod 09](../modifications/09-water-tank-monitor/README.md) adds fresh and grey sensors | Owner reports |
| Propane | 2 x 20 lb tanks | |
| Microwave | None | Owner |

## Tow Vehicle

| Item | Value |
| --- | --- |
| Vehicle | 2026 Toyota RAV4 PHEV |
| Tow rating | 3,500 lb (equal to the trailer's GVWR, so there is no margin) |
| Hitch | 750 lb tongue weight limit, 5,000 lb towing |

Keep loaded tongue weight at 10-15% of the actual trailer weight (about 300-450 lb). See the weight section of the [upgrade plan](off-grid-upgrade-plan.md).

## Electrical

| Component | Model | Notes |
| --- | --- | --- |
| Batteries | 2 x Renogy Core Mini 12.8 V 300 Ah LiFePO4 w/ low-temperature protection (RBT12300LFP-M) | One factory, one added ([mod 01](../modifications/01-second-battery/README.md)), both in the rear center battery compartment. 200 A BMS, 150 A max charge, M8 terminals at 8 N-m, no self-heating (charging stops below 32 F), no Bluetooth |
| Battery fusing and distribution | 200 A MEGA fuse on each battery; Joinfworld 250 A positive and negative busbars; 1/0 AWG copper-clad aluminum cable | No battery disconnect switch. Upgrades recommended in [mod 01](../modifications/01-second-battery/README.md#recommended-follow-ups) |
| Inverter | Renogy 2000 W 12 V pure sine (RNG-INVT-2000-12V-P2) | Factory. 4000 W surge for 1 s, 166.6 A max DC, 250 A fuse recommended. Manual says neutral and ground are bonded inside. `-P2` suffix to confirm on the label |
| Transfer switch | Go Power GP-TS-30 | Shore on the GENERATOR (dominant) leads, inverter on the SHORE/Power Cord leads, output to the WFCO main ([mod 03](../modifications/03-whole-panel-inverter/README.md)) |
| Shore-only breaker box | SYIZYEN HT-5 DIN enclosure: 30 A US Breaker C60X1C30 (to TS-30), 2 x 20 A CHTAIXI C20 (converter, water heater element) | Next to the WFCO under the seat by the sink |
| Former inverted outlets | 2 outlets, factory-wired from the inverter's hardwire terminal | Now on the WFCO's former water heater 20 A breaker (12 AWG), so they work on shore and inverter |
| Power center | WFCO WF-8900-AD series (auto-detect lithium/lead-acid), 55 A converter | Exact model (for example WF-8955-AD) to confirm |
| DC rocker panel | Nilight logo visible; exact model unknown | Owner confirmed DC rockers, 2026-10-13. Photo description: four illuminated rocker switches and digital readout apparently 13.5 V. Cutout, rear pinout, load identities, currents, and fuse sizes unknown. [Mod 06](../modifications/06-smart-dc-switches/README.md) plans four BANDC momentary rockers (delivered 2026-10-19) with a Waveshare ESP32-S3-POE-ETH-8DI-8RO controller (ordered 2026-10-19); not installed |
| WFCO breakers | 30 A main (fed from the TS-30) and five 20 A branches | The former converter breaker now feeds only the sink and door outlets; the former water heater breaker feeds the former inverted outlets. A/C breaker size to confirm |
| Shore power | 30 A, 25 ft 10-gauge cord | Casita FAQ |
| Solar | 200 W portable suitcase panel with its own controller | Factory. Set the controller to lithium |
| Battery monitor | Renogy 500 A Battery Monitor with Shunt (RBM500); display board Baiway TF03H V35 | Batteries on shunt B-; every load and charger (including the converter and Starlink) on P-. Shunt confirmed 500 A / 75 mV (0.00015 ohm) on 2026-10-14; see [mod 04](../modifications/04-battery-monitor-esp32/README.md) |
| Starlink | Starlink Mini on 12 V via RVMARINEPAT 12-36 V adapter; Casita factory exterior Starlink port | [mod 05](../modifications/05-starlink-12v-power/README.md). Needs a 10 A inline fuse added |
| Trailer network | GL.iNet Slate 7 (GL-BE3600) travel router; Home Assistant OS on a Raspberry Pi 4 Model B on the trailer network, with the ESPHome Device Builder, Tailscale, Matter Server and OpenThread Border Router add-ons and a Home Assistant Connect ZBT-1 (Thread) | Hosts the battery monitor ([mod 04](../modifications/04-battery-monitor-esp32/README.md)). Reachable remotely over Tailscale only. Its entities are mirrored to the home Home Assistant (Remote Home-Assistant integration) |
| Home Assistant monitor | `casita-battery-monitor`: Seeed XIAO ESP32-S3 in the RBM500 housing, with a GODIYMODULES INA228 module (B0GX5HM4X3) reading the RBM500 shunt | ESPHome device in the trailer's Home Assistant, running since 2026-10-13 with plausible readings; shunt calibration to confirm; see [mod 04](../modifications/04-battery-monitor-esp32/README.md) |
| E-ink dashboard | Seeed/TRMNL 7.5" (OG) DIY Kit: XIAO ESP32-S3 Plus driver board, 800 x 480 e-paper | Ordered, not built; ESPHome device `casita-dashboard` on the trailer's Home Assistant; see [mod 08](../modifications/08-eink-dashboard/README.md) |
| AC meter | Shelly EM Gen3 on the TS-30 PANEL output, second clamp on the shore cord | Planned, not purchased; see [mod 10](../modifications/10-ac-power-meter/README.md) |

## Heating, Cooling and Appliances

| Component | Model | Notes |
| --- | --- | --- |
| Air conditioner | Coleman-Mach Mach 8 Plus Cub, 37200 series (R-32), 9,200 BTU | Likely 37201-076. Wiring sticker 1976-764 (PP 03-20): compressor Run = white, Common = black, Start = red. About 9.3-9.9 A cooling. SpartanStart soft start installed; factory start capacitor and PTCR removed ([mod 02](../modifications/02-ac-soft-start/README.md)) |
| Thermostat | Airxcel | [Manual](../manuals/air-conditioning/airxcel-thermostat-manual.pdf) |
| Refrigerator | 12 V only (compressor) | Model to record |
| Water heater | Gas/electric | Electric element now on the shore-only box (works only on shore power). Model to record. Casita lists both a direct-vent gas manual and a Dometic 6-gal gas/electric manual |
| Furnace | Propane | Model to record; [manual from Casita](../manuals/appliances/furnace-manual.pdf) |
| Range/cooktop | Suburban SRNA3 (per Casita's manual list) | To confirm |
| Water pump | Shurflo/Flojet (per Casita's manual list) | To confirm |
| Roof vent fan | MaxxAir MaxxFan Deluxe (per Casita's manual list) | To confirm |
| TV | NTD-2256 (per Casita's manual list) | To confirm |
| Awning | Fiamma F45s (per Casita's manual list) | To confirm |
| Axle | Dexter (per Casita's manual list) | To confirm |
| LP/CO detector | Safe-T-Alert 30 series (per Casita's manual list) | To confirm |

Items marked "per Casita's manual list" come from the manuals Casita publishes for its trailers, not from this trailer's labels.

## Battery Bank Energy

- 600 Ah x 12.8 V = about 7.7 kWh nominal; about 510 Ah usable at 85%.
- The fridge draws from the batteries all the time off-grid: budget about 25-50 Ah per day, more in hot weather.
- The inverter draws about 1.5-2 A just being on.
