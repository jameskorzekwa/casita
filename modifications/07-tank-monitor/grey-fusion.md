# Grey tank level

Status: **recalibrated 2026-11-18** from a monitored full fill and drain; live
in trailer Home Assistant and mirrored at home. The sections after this one are
the 2026-11-05 history and are superseded where they conflict.

## Calibration from the 2026-11-18 fill and drain (current)

Every state change of all three grey sensors was recorded through the trailer
HA websocket from an empty tank, through an owner-confirmed full fill, to an
owner-confirmed drain ("basically empty"). Times are UTC.

| Sensor | Fill | At full | Drain | Verdict |
| --- | --- | --- | --- | --- |
| Grey 2 Garnet (outlet-pipe corner) | 0 → 8 (23:15:20) … 66 (23:25:48), one step at a time | **66** | 66 → 58 (23:36:59) … 0 (23:41:40), one step at a time | **Used. 66 = full, 0 = basically empty** |
| Grey 1 Garnet (opposite corner) | 0 throughout | **0** | 0 throughout | **Excluded: faulty** |
| Mopeka (outside) | No echo until 23:22, then 79–126 mm while Grey 2 rose 33 → 66, plus false deep echoes up to 194 mm | ~80 mm (owner-confirmed full reference 81 mm) | False echoes 137–108 mm, then ~80 mm while Grey 2 was 41, no echo from Grey 2 = 33 | **Excluded from the number; diagnostic only** |

Live rule ([`grey-fusion.jinja`](grey-fusion.jinja)): level =
Grey 2 raw / 66 × 100, clamped to 0–100. One sender step is 8–9 raw points,
about 12 % of the tank. 0 % means "basically empty": the owner saw only a small
residual when Grey 2 reached 0. If Grey 2 stops reporting, the level is
unavailable and the source sensor says why. `sensor.casita_grey_level_source`
gives the reason in words.

**Grey 1 fault.** The controller's own broadcast (captured at 23:35:45, full
tank) carried Grey 1 = `0x00` with Grey 2 = `0x42` (66) and black = `0x66`
(open, no sender). So the controller gets a valid "no water" reply from the
Grey 1 sender, not a wiring open; it is not a Home Assistant or integration
decoding fault (the grey fields are decoded the same way in 1.4.0 and 1.5.0).
The owner checked on 2026-11-18 that the strip is fully stuck to the tank with
no air gap. It last gave non-zero readings in the 2026-11-05 drain. Cause still
to find: failed sender or its signal connection.

**Mopeka.** During the fill and drain the fold guard locked onto a multiple of
the true depth (while filling it followed half of false 154 → 137 mm echoes down from 77 to 68 mm and
read the 80 mm full depth while half drained). Its reading is only meaningful
at full, where Grey 2 already reads 66. `sensor.casita_grey_level_folded` and
`sensor.casita_grey_echo_status` remain as diagnostics.

Raw evidence: `casita-grey-cal-20261118.jsonl` (kept off-repo with the agent's
working files; it contains raw HA attributes).

## Observed drain

Owner confirmed full with Garnet reading 66 and Mopeka direct echo 81 mm.
Garnet descended 66 → 58 → 50 → 41 → 33 → 25 → 16 → 8 → 0 without an
upward step during recording. Owner confirmed empty later, explicitly noting
the Garnet had reached zero minutes before water stopped draining. Mopeka
lost its echo while Garnet was still nonzero; the guarded Mopeka-only output
remained held at 95%. It cannot be used unconditionally as the primary gauge.

**Placement correction from owner, 2026-11-05 UTC:** the first Garnet sender
is on the same side as the outlet pipe, at the opposite corner. A second
Garnet sender is now attached at the outlet-pipe corner, right next to the
pipe, intended to improve low-level coverage. Earlier statements placing the
first Garnet at the inlet end were incorrect. The Mopeka's previously recorded
location is separate; this clarification does not relocate it.

The intended new sender address is Grey 2 (cut 2/GRY and 3/BLK per
manufacturer; tab cuts have not been independently inspected).
On first API inspection its entity was already enabled but **unknown**;
Grey 1 reported **0**. A numeric Grey 2 reading, low-level performance and
full/empty calibration remain unverified. The live fusion still uses Grey 1
plus gated Mopeka only; do not include uncalibrated Grey 2 automatically.

### Grey 2 diagnosis, 2026-11-05 UTC

**Resolved later the same session:** direct vendor BLE configuration enabled
Grey 2 for one sender, saved and read back with only its observed state byte
changed. Grey 2 now reports 33% in both raw broadcasts and HA. See
[verified procedure and evidence](garnet-direct-configuration.md).

Live HA Bluetooth advertisement subscription, explicitly matched to the
registered Garnet device, reported local name **Soul**, 14-byte manufacturer
payload, Grey 1=16, Grey 2=110, LPG=0, supply=13.5 V. Manufacturer standardized
BLE map (Soul 708-RBT manual v2.4, Appendix A, page 20) identifies byte 7 as
Grey 2 and code **110 as Disabled**. Byte 10 is the separate LPG value.
Thus the Grey 2 controller channel is disabled; LPG zero is not evidence
of the new sender being addressed as LPG. HA's Grey 2 entity is already enabled
and displays unknown for values above 100, hiding the specific diagnostic.

The integration assigns model 709-BTP7 based on manufacturer ID, so that HA
model string alone is not hardware-label verification. The live advertised
name Soul and owner's lack of a physical display warrant correcting the
earlier assumption of a BTP7 display after checking the actual controller label.
Both models use the same Grey 2 tab combination (2/GRY + 3/BLK).

The inspected upstream integration is passive monitoring and has no controller
channel-configuration option. Enabling the physical Grey 2 channel requires
the manufacturer's configuration interface, not another entity-registry change.
No controller settings were changed by this diagnosis. Manufacturer source:
https://www.garnetinstruments.com/wp-content/uploads/2026/07/SeeLeveL-Soul-708-RBT-Manual-v2.4.pdf

**Zero means below sender range, not empty.** Neither this test nor the blend establishes volume in gallons.
Changing drain flow and changing head mean elapsed time is not volume.

## Rule deployed

### Grey 2 low-end evidence (owner update 2026-11-05)

Owner reports the new outlet-adjacent Grey 2 sender reached 0 with only a
small amount of water remaining. Treat its zero as **near-empty**, not proof of
absolutely dry. HA history confirms Grey 1 reached 0 at 03:56:35 UTC while
Grey 2 still reported 33; Grey 2 subsequently reported 25, 16, 8 and reached
0 at 03:58:42 UTC. This establishes additional low-end coverage, not a volume
calibration. Grey 2 was disabled during the earlier confirmed-full test; its
highest numeric value in the inspected history is 33. No confirmed-full Grey 2
reference exists yet. Do not reuse Grey 1's full=66 or treat observed max=33 as
Grey 2 full. Adding Grey 2 to the numeric fusion remains pending calibration;
the two-sensor rule below is still the live rule.

[`grey-fusion.jinja`](grey-fusion.jinja) is the live state template for
`sensor.casita_grey_tank`. `sensor.casita_grey_tank_combined` is now a direct
alias of this value, with no fresh-water fallback.

1. Garnet anchors the range: `g = clamp(raw / full * 100, 0, 100)`.
   `input_number.casita_grey_garnet_full_pct` is 66, the confirmed-full endpoint.
   It is not a claim that the tank has linear geometry.
2. Garnet at zero returns zero with source **below Garnet range; not confirmed
   empty**. Garnet at/above the full reference returns 100.
3. At intermediate levels, Mopeka may contribute only if raw distance is
   numeric, quality ≥33, folded depth is numeric, full calibration is valid,
   and echo status is `tracking from full reference` (not held).
4. Normalize Mopeka accepted depth against its existing 76 mm full reference.
   Require agreement within one observed Garnet step: 9 raw points, or
   13.64 normalized points at full=66. Larger disagreements use Garnet alone.
5. Within that window, `level = 0.75*g + 0.25*m`, rounded to whole percent.
   Weighting is a **heuristic**, not fitted calibration or verified increased
   accuracy. It limits Mopeka influence to about 3.4 percentage points.
6. A missing/invalid Garnet reference makes the combined value unavailable;
   it does not silently fall back to the unreliable standalone Mopeka.

`sensor.casita_grey_level_source` uses the same template prefixed by
`{% set output='source' %}`. It is shared to home and shown on both dashboards.
Both numeric entities retain their existing IDs; the e-ink source ID does not
need a firmware change. Physical e-ink refresh was not visually verified.

Main template availability:

```jinja
{{ is_number(states('sensor.inside_fresh_water_tank_sensor_grey_tank'))
   and states('sensor.inside_fresh_water_tank_sensor_grey_tank')|float(0)>=0
   and states('input_number.casita_grey_garnet_full_pct')|float(0)>0 }}
```

Combined alias state: `{{ states('sensor.casita_grey_tank') | float(none) }}`;
availability: `{{ is_number(states('sensor.casita_grey_tank')) }}`.

The estimate automation stays off; its old value is labeled paused/stale.
Alerts retain the adjustable nearly-full threshold and the fixed 95% warning,
but now operate on this calibrated combined local-level scale. Notification
text no longer claims a numerical reading means water will back up. Threshold
meaning changed with the scale; no overflow guarantee is implied.

## Verification

Nine synthetic cases rendered through the actual HA Jinja template engine
before deployment (not injected into live sensor states):

| Case | Result |
| --- | --- |
| Garnet 0, held Mopeka 95% | 0 |
| Garnet 66, Mopeka depth 81 mm | 100 |
| Garnet 33, Mopeka depth 38 mm | 50 |
| Garnet 33, Mopeka depth 45.6 mm | 52 (HA rounding) |
| Garnet 50, Mopeka depth 72.3 mm | 76 (disagreement excluded) |
| Garnet 33, Mopeka held at 45.6 mm | 50 |
| Missing Garnet | None; availability guard false |
| Garnet 75 | 100 |
| Garnet 8, Mopeka held | 12 |

Live readback: both trailer entities and their home mirrors **0%**, source
**below Garnet range; not confirmed empty**, Garnet full helper **66**, old
estimate automation **off**. Owner has separately confirmed this dump empty.

Further fills/drains are needed to assess whether the bounded Mopeka
contribution improves the reading. Small non-monotonic variations remain
possible; this is not a guarantee of perfect accuracy or monotonicity.
