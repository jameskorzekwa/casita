# Modifications

Each modification has its own folder with instructions, diagrams, parts, and a status line. Number new folders in order (`05-...`, `06-...`).

| # | Modification | Status | Summary |
| --- | --- | --- | --- |
| 01 | [Second battery](01-second-battery/README.md) | Done | Second Renogy 300 Ah battery in parallel for a 600 Ah bank, each battery individually fused to a common busbar |
| 02 | [A/C soft start](02-ac-soft-start/README.md) | Purchased; install status to confirm | Spartan Power SpartanStart on the Coleman Mach 8 so the inverter can start the compressor |
| 03 | [Whole-panel inverter](03-whole-panel-inverter/README.md) | Planned; transfer switch purchased | Go Power TS-30 so the whole WFCO panel, including the A/C, runs from the inverter when unplugged, with the converter and water heater element on a shore-only sub-panel |
| 04 | [Battery monitor to Home Assistant](04-battery-monitor-esp32/README.md) | In progress | XIAO ESP32-S3 and INA228 inside the Renogy display housing; publishes state of charge and power to Home Assistant |

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
