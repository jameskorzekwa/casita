# Casita Flic sleep and wake routines

The **trailer** Home Assistant owns these routines (not the mirrored home HA). As read back from the Casita HA API on 2026-10-30:

| Flic Duo big-button gesture | Automation | Script | Climate action |
| --- | --- | --- | --- |
| Double press | `automation.casita_flic_double_press_sleep` | `script.sleep` | Set `climate.inside_casita_thermostat` to **66 °F**, then set fan mode to `low` (continuous fan) |
| Long press | `automation.casita_flic_long_press_wake_up` | `script.wake_up` | Set the thermostat to **68 °F**, then set fan mode to `auto`; do **not** change the HVAC mode |

The Sleep script also turns off both smart DC lights and the TV and turns on the sound machine. Wake Up turns on both lights and turns off the sound machine. Each script retains those actions; the climate actions were added to the scripts so they also apply when the scripts are run by another trigger. Climate actions use `continue_on_error: true`, so a temporarily unavailable thermostat does not block the other routine actions. No HVAC mode is set by either script.

**Verification:** On 2026-10-30, the Casita HA script configuration API returned `result: ok` for both updated scripts and readback confirmed Sleep at 66 °F followed by fan `low`, and Wake Up at 68 °F followed by fan `auto`. Both Flic automations remained enabled. Before the update the live thermostat was in `heat` at 67 °F with fan `auto`; the scripts were edited without invoking them or changing the active thermostat state. The physical fan behavior and a complete sleep/wake cycle remain **to test**.
