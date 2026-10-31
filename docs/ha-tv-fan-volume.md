# TV volume compensation for the thermostat fan

Installed and enabled on the **trailer Home Assistant**, 2026-10-31 UTC.
Owner confirmed the TV is an **Insignia Fire TV**; exact model to confirm.

## Behavior

- Fan starts with TV on: read current speaker volume and add **15**.
- Fan stops: read current volume again and subtract **15**.
- Manual adjustments become the new baseline: 35 → automatic 50 → manually
  40 → automatic 25. This does not restore the original saved volume.
- Clamp to 0–100; limits make the adjustment non-reversible.
- TV off cancels the outstanding adjustment. TV on with fan running gets a
  new boost. Unknown/unavailable states do not change volume.
- Continuous low/high fan (with HVAC not off), fan-only mode, or active
  heating/cooling/fan means running. Auto fan with idle/off means stopped.
  This is inferred from thermostat state, not physical fan sensing; startup
  and run-on delays are not measured.
- Ambient noise is a future replacement trigger, not installed.

## Configuration

- `automation.casita_tv_thermostat_fan_volume`
- `input_boolean.casita_tv_fan_boost_active` (UI-created, persistent)
- `media_player.casita_tv_adb` (new Android Debug Bridge integration)
- `climate.inside_casita_thermostat`
- [Saved automation configuration](ha-tv-fan-volume.json)

Existing TV integrations retained. ADB was enabled by the owner and connected
successfully. `media volume --stream 3 --get` reads speaker level;
`media volume --stream 3 --set N --get` sets and confirms it. Fresh service
response variables are used rather than cached entity attributes.

Single execution prevents overlapping adjustments. The persistent helper
prevents repeated boosts; state updates, HA start and a 30-second reconciliation
trigger compare fan state to the helper. Offline changes are reconciled, not
replayed. The helper changes before the write to prevent repeated increases
on ambiguous command failure. Mismatched readback creates a notification;
transport exceptions stop the run and appear in its trace. Failed writes can
leave helper/device state inconsistent: check them before the next transition.
Manual changes during the brief read/write interval can race the write.

Disable the automation to stop automatic commands; disabling does not undo an
outstanding boost. Check helper state before re-enabling after manual recovery.

## Verification

- Owner confirmed reported volume **55** matched the screen.
- Read **43**, set the same **43**, received **43** back. Exact setting works;
  no intentional loudness increase was performed during that test.
- HA template API passed seven fan-state cases: auto idle, continuous low/high
  idle, heating/cooling, off, fan-only.
- Relative/clamp tests passed: 35+15=50, 40−15=25, 95+15=100, 10−15=0.
- Configuration API returned `result: ok`; complete readback matched the JSON.
- Live automation `on`, helper initially `off`; idle-path execution completed.
- Separate review raised a cached-response concern; direct response variables
  address it and their response shape was verified on live HA.
- **Still to test physically:** fan-start/stop cycle, manual adjustment between
  transitions, and restart recovery. Thermostat settings were not changed.

The JSON records the installed automation; a documentation merge does not
redeploy it or establish physical fan-cycle verification.
