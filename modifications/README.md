# Modifications

Each modification has its own folder with instructions, diagrams, parts, and a status line. Number new folders in order; 06 and 07 are on open branches, so the next free number is 09.

| # | Modification | Status | Summary |
| --- | --- | --- | --- |
| 01 | [Second battery](01-second-battery/README.md) | Done | Second Renogy 300 Ah battery in parallel for a 600 Ah bank, each battery individually fused to a common busbar |
| 02 | [A/C soft start](02-ac-soft-start/README.md) | Done | Spartan Power SpartanStart on the Coleman Mach 8 so the inverter can start the compressor; start capacitor and PTCR removed |
| 03 | [Whole-panel inverter](03-whole-panel-inverter/README.md) | Done | Go Power TS-30 so the whole WFCO panel, including the A/C, runs from the inverter when unplugged, with the converter and water heater element on a shore-only breaker box |
| 04 | [Battery monitor to Home Assistant](04-battery-monitor-esp32/README.md) | Installed; calibration to confirm | XIAO ESP32-S3 and INA228 inside the Renogy display housing; publishes state of charge, power and a charging indicator to the trailer's Home Assistant, mirrored to the home one over Tailscale |
| 05 | [Starlink Mini on 12 V](05-starlink-12v-power/README.md) | Installed; fuse to add | Starlink Mini powered from the battery bank through a 12-36 V adapter and Casita's exterior Starlink port |
| 08 | [E-ink dashboard](08-eink-dashboard/README.md) | Designed; kit ordered | TRMNL 7.5" e-paper kit running ESPHome, mounted in the trailer, showing battery, propane and water levels from the trailer's Home Assistant |

## Template for a new modification

```markdown
# Title

> **Status:** planned / in progress / done (date)

What it does and why.

## Parts
## Wiring / diagrams
## Steps
## Testing
## Safety notes
## Revisions
```
