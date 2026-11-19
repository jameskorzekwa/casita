# Grey Mopeka echo ambiguity — live containment

Status: containment superseded by full-reference guarded tracking, deployed
2026-11-05 UTC. Full-to-empty performance is **not yet validated**.

## Current live correction (supersedes containment below)

Owner confirmed the tank full. Raw direct echo was 79 mm, then settled at
81 mm at deployment, quality 100. The old decoder halved this to about
40 mm because its previous estimate was already wrong.

- Persisted `input_number.casita_grey_last_depth_mm`, initialized to the
  observed direct full echo of **81 mm**. No `initial` property: restore
  accepted depth across restarts rather than default to 40 mm.
- Fold considers raw / 1, 2, 3, 4, bounded to (0, 95] mm. It accepts an update
  only if exactly one candidate is within **5 mm** of the last accepted depth
  and echo quality is at least 33. Otherwise hold the previous depth.
  The 5 mm guard is an engineering threshold, not a manufacturer accuracy claim.
- `automation.casita_grey_persist_accepted_depth` saves numerical folded
  updates to that helper (entity ID may be slugified from its alias).
- `sensor.casita_grey_echo_status` reports tracking or held (ambiguous,
  low quality, no echo/disconnected). Added to Water card and labeled shared.
- Percentage now uses accepted folded depth directly, **not the old median**.
  This prevents the old incorrectly halved samples continuing to drive the
  gauge. The old median remains diagnostic only.
- Kept full calibration **76 mm**, capped percentage at 100. Did not calibrate
  full to the incorrect half-height. Both measured and combined read **100%**
  on live verification, folded/persisted depth **81 mm**, status tracking.
- Removed the display block at owner request. Estimate automation remains
  off and its displayed value is labeled paused/stale.
- No-echo no longer becomes zero via the percent template: accepted depth
  holds with status. This also prevents a false automatic dump inference.

Regression checks: direct full 79 and 2x/3x/4x echoes return 79; the observed
129/2 = 64.5 to 178 and 146 sequence holds 64.5 instead of dropping to 59.3
and 48.7; 146 from a 76 reference gives 73; 140 from 73 gives 70; zero echo
holds; multiple candidates hold. Ten checks passed locally.

Limitations: a rapid true change exceeding the guard can leave tracking held,
and a wrong echo inside the guard can still be accepted. This is not a promise
of universally correct echo interpretation. Inspect status during the next
normal drain. Never treat a held reading as a fresh measurement or rely on
this gauge alone for overflow protection. No drain or restart was required.

During an owner-confirmed fill, raw distance changed from 129 mm to 178 mm,
then settled near 146 mm. The nearest-candidate fold changed from division by
two to division by three. The gauge fell from 84% to 64%. The five-sample
median delayed but did not reject the incorrect interpretation. Neither the
pre-drop nor post-drop percentage is independently verified tank volume.

The estimate was not independent: its automation copied the Mopeka percent
into gallons on each update. It consequently reproduced the same false drop.

## Emergency containment

- Added `input_boolean.casita_grey_echo_uncertain`, enabled.
- Wrapped the state templates for `sensor.casita_grey_tank`,
  `sensor.casita_grey_tank_combined`, and `sensor.casita_grey_estimate` with:

  ```jinja
  {% if is_state('input_boolean.casita_grey_echo_uncertain', 'on') %}
    unknown
  {% else %}
    {# Existing state template, otherwise unchanged. #}
  {% endif %}
  ```

- Disabled `automation.casita_grey_estimate` with running actions stopped.
- Added an availability guard to all three templates: while the fault flag
  is on, availability is false; otherwise preserve existing availability.
  Returning the literal `unknown` alone did not clear the numeric sensors'
  previous state. Live readback after the availability fix confirms all three
  are **unavailable**, estimate automation is **off**, and full is **76 mm**.
- Added a warning card to the trailer Casita Status dashboard and a persistent
  notification. Historical pre-drop display (84%, 01:27 UTC) is explicitly
  labeled historical, not a current reading.
- Raw distance, fold and median remain available for diagnosis.
- Full calibration stays at 76 mm. No firmware, Garnet, or full-calibration
  changes were made. No drain requested.

The grey alerts cannot establish fullness while their input is unknown.
Do not rely on them to prevent overflow during the supervised fill.

## Remaining work

The root algorithm is still ambiguous. Do not clear the fault flag to make
the gauge numeric again without verification. A repaired decoder needs explicit
ambiguity handling, restart behavior, fill and drain tests, and validation
against known levels. Do not automatically reset volume on no echo or treat
local depth percentage as independently measured tank-volume percentage.

This document supersedes earlier claims that continuity folding reliably
distinguishes echo multiples. Repository publication/review/merge is separate
from the live containment deployment.
