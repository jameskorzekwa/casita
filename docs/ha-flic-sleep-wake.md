# Casita Flic sleep and wake routines

The **trailer** Home Assistant owns these routines (not the mirrored home HA). As read back from the Casita HA API on 2026-10-30:

| Flic Duo big-button gesture | Automation | Script | Climate action |
| --- | --- | --- | --- |
| Double press | `automation.casita_flic_double_press_sleep` | `script.sleep` | Set `climate.inside_casita_thermostat` to **68 °F**, then set fan mode to `low` (continuous fan) |
| Long press | `automation.casita_flic_long_press_wake_up` | `script.wake_up` | Set fan mode to `auto` only; do **not** change the temperature or HVAC mode |

The Sleep script also turns off both smart DC lights and the TV and turns on the sound machine. Wake Up turns on both lights and turns off the sound machine. Each script retains those actions; the climate actions were added to the scripts so they also apply when the scripts are run by another trigger. Climate actions use `continue_on_error: true`, so a temporarily unavailable thermostat does not block the other routine actions. No HVAC mode is set by either script.

**Verification:** The Casita HA script configuration API returned `result: ok` for both saves and a subsequent readback matched both new sequences on 2026-10-30. Before editing, the live thermostat advertised fan modes `low`, `high`, `auto` and was in `heat` with a 69 °F setpoint and `auto` fan. Neither script nor Flic button was triggered during verification: physical fan behavior and a full overnight/wake cycle remain **to test**. The live settings were not changed by the configuration edit.
