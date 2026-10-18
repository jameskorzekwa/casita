# Manuals

Equipment manuals and datasheets, one folder per system. The files below were downloaded on 2026-10-09 from the manufacturer or from Casita's [user manuals page](https://casitatraveltrailers.com/user-manuals/). Manuals digitized from the paper documents that came with the trailer go in the same folders.

## Text versions

Every PDF has a Markdown text version next to it with the same name (for example `furnace-manual.pdf` and `furnace-manual.md`), so the manuals can be searched on GitHub and read without opening the PDF. GitHub search indexes the Markdown files but not the text inside PDFs.

- Pages with embedded text were extracted directly. Pages that are only images were OCR'd (RapidOCR at 200 dpi); each file's header lists which pages. The Casita owner's manual, the SpartanStart instructions and the water pump manual are entirely OCR'd.
- Diagrams, photos and table layouts are not reproduced, and OCR text inside diagrams is mostly unreadable. Always check the PDF for wiring diagrams, torque values and anything safety-critical.
- Regenerate a text version whenever its PDF is replaced.

## Conventions

- File names: lowercase, hyphens, `manufacturer-model-document-type.pdf` (for example `dometic-dm2652-owners-manual.pdf`).
- Paper manuals you scan: add `-scan` before `.pdf` if an online copy of the same document is also present, so both can be kept.
- Scan at 300 dpi to a searchable (OCR) PDF where possible. Keep files under 50 MB.
- Add every new file to the index below, including where it came from, and add its `.md` text version.

## Index

### Casita

| File | Covers | Source |
| --- | --- | --- |
| [casita-owners-manual.pdf](casita/casita-owners-manual.pdf) | Casita owner's manual (scanned image, no text layer) | [Casita](https://casitatraveltrailers.com/wp-content/uploads/2023/11/Casita-Manual-d1.pdf) |

### Electrical

| File | Covers | Source |
| --- | --- | --- |
| [renogy-core-mini-300ah-battery-manual.pdf](electrical/renogy-core-mini-300ah-battery-manual.pdf) | Renogy Core Mini 12.8 V 300 Ah battery (RBT12300LFP-M), both batteries | [Renogy](https://www.renogy.com/cdn/shop/files/UM_12V_300Ah_Core_Mini_Battery_1.pdf) |
| [renogy-2000w-p2-inverter-manual.pdf](electrical/renogy-2000w-p2-inverter-manual.pdf) | Renogy 700/1000/2000/3000 W P2 pure sine inverters, version A2 | [Renogy](https://www.renogy.com/products/2000w-12v-pure-sine-wave-inverter) |
| [renogy-rbm500-battery-monitor-manual-g3.pdf](electrical/renogy-rbm500-battery-monitor-manual-g3.pdf) | Renogy 500 A Battery Monitor with Shunt (RBM500), G3 manual | [Renogy](https://www.renogy.com/products/500a-battery-monitor-with-shunt) |
| [go-power-gp-ts-30-transfer-switch-manual.pdf](electrical/go-power-gp-ts-30-transfer-switch-manual.pdf) | Go Power GP-TS-30 transfer switch, rev E | [Go Power](https://gopowersolar.com/products/30-amp-transfer-switch/) |
| [ti-ina228-datasheet.pdf](electrical/ti-ina228-datasheet.pdf) | TI INA228 power monitor (battery monitor project) | [TI](https://www.ti.com/lit/ds/symlink/ina228.pdf) |
| [xantrex-freedom-x-owners-guide.pdf](electrical/xantrex-freedom-x-owners-guide.pdf) | Xantrex Freedom X 1000/2000/3000 inverter owner's guide, 975-0787-01-01 Rev G | [Xantrex](https://xantrex.com/wp-content/uploads/2025/10/975-0787-01-01_Rev-G.pdf) |
| [xantrex-freedom-x-datasheet.pdf](electrical/xantrex-freedom-x-datasheet.pdf) | Xantrex Freedom X data sheet (817-1000/2000/3000) | [Xantrex](https://xantrex.com/wp-content/uploads/2021/12/DataSheet_Xantrex_FREEDOM-X_20260819.pdf) |
| [xantrex-freedom-x-remote-panel-owners-guide.pdf](electrical/xantrex-freedom-x-remote-panel-owners-guide.pdf) | Freedom X/XC Remote Panel (808-0817, 808-0817-02 Bluetooth) owner's guide, 976-0367-01-01 Rev G | [Xantrex](https://xantrex.com/wp-content/uploads/2021/12/976-0367-01-01_G.pdf) |

### Air conditioning

| File | Covers | Source |
| --- | --- | --- |
| [coleman-mach-37200-series-rooftop-ac-manual-1980-207.pdf](air-conditioning/coleman-mach-37200-series-rooftop-ac-manual-1980-207.pdf) | Coleman-Mach 37200-series (R-32) rooftop A/C, doc 1980-207 | [Coleman-Mach](https://campaigns.coleman-mach.com/hubfs/1980-207.pdf) |
| [airxcel-47000-series-rooftop-ac-installation.pdf](air-conditioning/airxcel-47000-series-rooftop-ac-installation.pdf) | Airxcel 47000-series (older R-410A) installation instructions, as linked by Casita | [Casita](https://casitatraveltrailers.com/user-manuals/) |
| [airxcel-thermostat-manual.pdf](air-conditioning/airxcel-thermostat-manual.pdf) | Airxcel wall thermostat | [Casita](https://casitatraveltrailers.com/user-manuals/) |
| [spartan-power-spartanstart-instructions-2024-07.pdf](air-conditioning/spartan-power-spartanstart-instructions-2024-07.pdf) | Spartan Power SpartanStart soft start, July 2024 instructions and install table | [Spartan Power](https://spartanpower.com/product/spartan-power-spartanstart/) |

### Appliances

| File | Covers | Source |
| --- | --- | --- |
| [furnace-manual.pdf](appliances/furnace-manual.pdf) | Furnace | [Casita](https://casitatraveltrailers.com/user-manuals/) |
| [direct-vent-gas-water-heater-manual.pdf](appliances/direct-vent-gas-water-heater-manual.pdf) | Direct-vent gas water heater | [Casita](https://casitatraveltrailers.com/user-manuals/) |
| [suburban-srna3-range-cooktop-manual.pdf](appliances/suburban-srna3-range-cooktop-manual.pdf) | Suburban SRNA3 range/cooktop | [Casita](https://casitatraveltrailers.com/user-manuals/) |
| [shurflo-flojet-water-pump-11560.pdf](appliances/shurflo-flojet-water-pump-11560.pdf) | Flojet water system pump | [Casita](https://casitatraveltrailers.com/user-manuals/) |
| [maxxair-maxxfan-deluxe-installation-rev-b-2016.pdf](appliances/maxxair-maxxfan-deluxe-installation-rev-b-2016.pdf) | MaxxAir MaxxFan Deluxe roof fan | [Casita](https://casitatraveltrailers.com/user-manuals/) |
| [tv-ntd-2256-manual.pdf](appliances/tv-ntd-2256-manual.pdf) | NTD-2256 TV | [Casita](https://casitatraveltrailers.com/user-manuals/) |

### Safety

| File | Covers | Source |
| --- | --- | --- |
| [safe-t-alert-30-series-detector.pdf](safety/safe-t-alert-30-series-detector.pdf) | Safe-T-Alert 30-series LP/CO detector | [Casita](https://casitatraveltrailers.com/user-manuals/) |
| [fire-extinguisher-manual.pdf](safety/fire-extinguisher-manual.pdf) | Fire extinguisher | [Casita](https://casitatraveltrailers.com/user-manuals/) |

### Exterior and chassis

| File | Covers | Source |
| --- | --- | --- |
| [fiamma-f45s-awning-manual.pdf](exterior/fiamma-f45s-awning-manual.pdf) | Fiamma F45s awning | [Casita](https://casitatraveltrailers.com/user-manuals/) |
| [dexter-axle-600-8k-service-manual.pdf](exterior/dexter-axle-600-8k-service-manual.pdf) | Dexter axle service manual (600-8K) | [Dexter](https://www.dexteraxle.com/user_area/content_media/raw/600-8k_complete_service_manual.pdf) |

The Casita-published manuals are for Casita trailers generally. Check each against the equipment actually installed (see [`../docs/trailer.md`](../docs/trailer.md)).

## Still to add

- Paper manuals that came with the trailer (digitize and add here; remove or redact any handwritten personal details first. Warranty cards and registrations stay out of this public repository)
- Refrigerator (12 V) manual, once the model is recorded
- Water heater manual for the installed gas/electric model. Casita also links a Dometic 6-gallon gas/electric manual (`epi.dometic.com`), which could not be downloaded on 2026-10-09
- WFCO WF-8900-AD series power center manual
- 200 W portable solar panel and controller manual
- Battery disconnect, fuse and busbar datasheets for the second-battery install
- Pololu D24V5F5 regulator, Seeed XIAO ESP32-S3 and INA228 breakout documentation (battery monitor project)
