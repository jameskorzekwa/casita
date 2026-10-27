# Agent Guide: Casita Repository

This repository is the maintained record for James's 2026 Casita Liberty 17 Deluxe travel trailer. Read it before answering any Casita question, and record new facts and changes here (not in the older Google Docs).

## Where things are

| Need | Read |
| --- | --- |
| Equipment, model numbers, breakers, weights, tow vehicle | `docs/trailer.md` |
| Every modification and its status | `modifications/README.md`, then `modifications/NN-*/README.md` |
| 120 V wiring as built (shore-only breaker box + TS-30) | `modifications/03-whole-panel-inverter/` |
| Battery bank, fuses, busbars, cables | `modifications/01-second-battery/README.md` |
| A/C soft start | `modifications/02-ac-soft-start/README.md` |
| Battery monitor / ESPHome / Home Assistant | `modifications/04-battery-monitor-esp32/` |
| Tank levels (propane L06, grey L02, fresh SeeLeveL) / ESPHome | `modifications/07-tank-monitor/` (designed, not built; mod 09 merged into it) |
| Overall plan, research and decisions | `docs/off-grid-upgrade-plan.md` |
| Manuals | `manuals/README.md` (index). Every PDF has a same-name `.md` text version; search the `.md` files, then check the PDF for diagrams and safety-critical values |

## Rules

- **The repository is public.** Never add ownership documents (build sheet, title, registration, warranty registrations), the VIN, home address, phone numbers, home network details (IPs, MACs, SSIDs), or credentials. ESPHome secrets stay in `secrets.yaml`, which is git-ignored; only `secrets.example.yaml` with placeholders is committed.
- **Mark certainty.** Distinguish what was confirmed (from a label, measurement or test) from what is assumed or "to confirm", and give the date when something was built or tested.
- **New manuals:** put the PDF in `manuals/<system>/` as `manufacturer-model-document-type.pdf`, add a `.md` text version beside it (extract embedded text; OCR image-only pages), and add both to `manuals/README.md`.
- **New modifications:** a new numbered folder under `modifications/` with a README (status line, parts with links, wiring/diagrams, steps, tests, safety notes, revisions), plus a row in `modifications/README.md` and the root `README.md`.
- **Diagrams:** SVG in the modification's `images/` folder, with a `<title>` and `<desc>`. Render-check them before committing.
- Live equipment (the `casita-battery-monitor` ESPHome device) is managed through the trailer's own Home Assistant and its ESPHome Device Builder, not the home Home Assistant; this repo holds the source configuration and documentation. The trailer's entities are mirrored into the home Home Assistant (with an `rv_` / `RV ` prefix) by the Remote Home-Assistant integration over Tailscale; that mirror is read/control only, so firmware, add-on and integration changes still happen on the trailer. Keep the committed YAML identical to the Device Builder copy apart from secrets.
