# Xantrex Freedom X 2000 Inverter and Bluetooth Remote Panel to Home Assistant

> **Status: inverter installed (October 2026); Home Assistant integration written and installed on the trailer's Home Assistant, first live connection to the panel still pending.** The physical installation (what the Freedom X replaced, how it is wired to the TS-30 and the battery bank, where the remote panel is mounted) is **not yet documented** - see [To document](#to-document).

Related: [whole-panel inverter / TS-30](../03-whole-panel-inverter/README.md) · [battery monitor to Home Assistant](../04-battery-monitor-esp32/README.md) · [trailer equipment](../../docs/trailer.md) · manuals: [Freedom X owner's guide](../../manuals/electrical/xantrex-freedom-x-owners-guide.pdf), [Freedom X data sheet](../../manuals/electrical/xantrex-freedom-x-datasheet.pdf), [Freedom X/XC remote panel owner's guide](../../manuals/electrical/xantrex-freedom-x-remote-panel-owners-guide.pdf)

## What it does and why

The factory Renogy 2000 W inverter has no data interface. The Xantrex Freedom X 2000 (part 817-2000) is a 2000 W true-sine inverter with a built-in 30 A AC transfer relay, and its optional **Freedom X Bluetooth Remote Panel** (part 808-0817-02) exposes the inverter's live readings and settings over Bluetooth Low Energy to the Xantrex phone app.

Xantrex publishes no protocol, so a Home Assistant integration was written for it: [`jameskorzekwa/ha-xantrex-freedom`](https://github.com/jameskorzekwa/ha-xantrex-freedom). The trailer's Home Assistant (Raspberry Pi 4, built-in Bluetooth) polls the panel directly, and the entities are mirrored to the home Home Assistant like everything else in the trailer (see [mod 04](../04-battery-monitor-esp32/README.md#mirroring-to-the-home-home-assistant)).

## Parts

| Part | Qty | Notes | Link |
| --- | ---: | --- | --- |
| Xantrex Freedom X 2000, 12 V, 120 V (817-2000) | 1 | 2000 W continuous at 40 °C, 4000 W surge for 5 s, 2200 W for 30 s. Built-in 30 A transfer relay (85-140 V AC input). LBCO adjustable 10.0-12.8 V. Peak efficiency 91 %. 14.6 × 10.8 × 3.9 in. Values from the data sheet; label `-P` suffix and GFCI option to confirm | [Amazon](https://www.amazon.com/dp/B074TDSRF1) |
| Xantrex Freedom X Bluetooth Remote Panel (808-0817-02) | 1 | Comes with a 25 ft 6-conductor RJ12 cable; plugs into the inverter's Remote port. Powered by the inverter, so it only advertises while the inverter has DC power. BLE address `B8:3D:F6:B6:30:A5`, advertised name `ID` + serial | [Xantrex](https://xantrex.com/products/accessories/freedom-x-bluetooth-remote-panel/) |

The owner's guide says: with the remote panel connected, leave the inverter's own Power button in Standby (up), so the panel's Power button controls the inverter.

## Home Assistant integration

### How it works

- The panel is a plain BLE GATT peripheral: service `0x1910`, characteristics `0x2A01` to `0x2A0E`, no pairing or authentication. The field layout was taken from the Xantrex app (`com.xantrex.app` 1.6.1, a Capacitor app that ships its TypeScript source maps). `0x2A03`/`0x2A04` are the live status, `0x2A0D`/`0x2A0E` the settings; settings are changed by reading the block, changing the bytes of one setting and writing the whole block back, exactly as the app does.
- The integration connects, reads every block (about a second), and disconnects, every 30 s by default (10-600 s in the integration options). The panel accepts one Bluetooth connection at a time, so the phone app still works between polls; while the app is connected, Home Assistant polls fail until it disconnects.
- Entities: AC input and output voltage/frequency/current/power, load %, battery voltage, signed battery current and power, heat sink temperature, working mode (standby / line / battery / fault / power saving), a `Problem` binary sensor with the decoded fault list, individual overload / over-temperature / battery-low sensors, and controls for the inverter on/off, power-saving mode, audible alarm, ignition control, transfer mode, shutdown recovery, low-battery cut-off voltage/delay/recovery, power save timer and utility under-voltage level. The lead-acid "battery capacity" estimate is hidden because the battery type is LiFePO4 (the Renogy/INA228 monitor from mod 04 is the real state of charge).
- The config entry's **Download diagnostics** includes the raw bytes of every characteristic, which is what to attach if a value looks wrong.

### Installation on the trailer's Home Assistant (done 2026-10-18)

1. HACS → custom repository `jameskorzekwa/ha-xantrex-freedom` (integration) → download; Home Assistant restarted. Installed version: 0.1.1.
2. Settings → Devices & services: the panel is discovered automatically when it advertises (service `0x1910`), or add **Xantrex Freedom X/XC** manually and pick it from the list. The confirm step connects once and reads the model and serial number.
3. At home the mirrored entities get the usual `rv_` prefix; set display precision by hand for the new voltage/current sensors as in mod 04.

Lesson learned on 2026-10-18: version 0.1.0 declared a Bluetooth `local_name` matcher of `ID*`. Home Assistant refuses wildcard patterns in the first three characters, and the error took down the **whole** `bluetooth` component on the trailer (and with it ESPHome and the battery monitor) for about five minutes until 0.1.1 removed the matcher. Any integration's bad manifest matcher can do this; check the core log after installing Bluetooth integrations.

### Access notes

- The trailer's Home Assistant is only reachable over Tailscale on port 80 (HA itself). The **Terminal & SSH** add-on was installed on 2026-10-18 with bee2's key for future deployments, but its port 22 is not reachable from bee2 (Tailscale ACL or similar); everything so far was done through the Home Assistant WebSocket/REST API and HACS.

## To document

- What happened to the Renogy inverter and how the Freedom X is wired: DC cables and fuse (the data sheet's full-load DC current is 192 A), AC output to the TS-30 "INVERTER" leads (or whether the Freedom X's built-in transfer relay now replaces the TS-30), ground/neutral bonding, and whether the two former inverted outlets are affected. Update [mod 03](../03-whole-panel-inverter/README.md) and the as-built diagram accordingly.
- Where the remote panel is mounted and the cable route.
- First live readings from Home Assistant, and confirmation of the three protocol details the app leaves ambiguous: the units of the output power limit (raw × 100 W or watts), whether the inverter on/off switch works, and the LiFePO4 battery-type setting.

## Testing

- 2026-10-18: Bluetooth advertisement seen by both the trailer's Pi (RSSI −66 to −79 dBm) and the home Home Assistant through an ESPHome Bluetooth proxy (−89 dBm). The first connection from Home Assistant has not happened yet: the panel stopped advertising later the same afternoon (inverter likely powered down or the phone app connected).

## Safety notes

- The Freedom X's settings (low battery cut-off, output voltage/frequency, ignition control) are writable from Home Assistant. A wrong LBCO or output voltage can damage the battery or appliances; the integration only exposes the ranges the Xantrex app allows, but treat the controls with the same care as the app.
- Turning the inverter to Standby does not disconnect DC or AC input power; shore power still passes through to the output.

## Revisions

| Date | Change |
| --- | --- |
| 2026-10-18 | Inverter reported installed. Protocol reverse-engineered from the Xantrex app; integration `ha-xantrex-freedom` 0.1.1 published and installed on the trailer's Home Assistant via HACS. Manuals added. Physical install and first live connection still to document |
