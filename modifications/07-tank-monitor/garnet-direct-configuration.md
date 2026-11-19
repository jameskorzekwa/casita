# Garnet Soul Grey 2 enablement over Bluetooth

Status: **applied and verified 2026-11-05 UTC**. Owner authorized direct
Bluetooth configuration because SeeLeveL Launch crashes opening Tanks.

## Home Assistant management now installed

Later on 2026-11-05, the owner requested a fork adding this management to HA.
`jameskorzekwa/garnet` version 1.5.0 was directly dev-installed on trailer HA
2026.11.0, preserving existing entity IDs. The device now has explicit Read,
staged sender selectors, Apply and save, and Discard controls plus meaningful
diagnostic states. Three consecutive reads and stage/discard/fourth read passed
on the physical controller. No physical setting was toggled for those tests.

The fork passed 95 tests plus 5 subtests, Ruff, hassfest, HACS validation and
independent review. [PR #1](https://github.com/jameskorzekwa/garnet/pull/1)
was subsequently **merged with owner approval** as
`a30712ceaf01f366d8b014f6b2ef204b2296245e`. Release **v1.5.0** was published
by passing CI and installed from its verified release ZIP on 2026-11-05.
The final build includes bounded read-only timeout recovery and passed 103
tests plus 11 subtests. All release files matched the loaded tested build;
two post-release configuration reads succeeded, with Grey2 still enabled.
HACS is absent, so this is a manual released-artifact installation, not
HACS-managed. Deployment and rollback evidence:
[deployment record](https://github.com/jameskorzekwa/garnet/blob/main/docs/deployment-20261105.md).

## Identity and cause

The registered Garnet device advertises local name Soul. Direct version query
returned `G708_REVK_L433_ver_7.0.4`. Prior documentation incorrectly assumed
the HA integration's inferred 709-BTP7 model proved a physical BTP7 display.

Grey 2's advertisement field (byte 7) contained 110: **Disabled**, per
Garnet's standardized BLE map, Appendix A of the Soul manual v2.4. The HA
entity was enabled but displayed unknown because its decoder accepts only
0–100 as level. LPG was a separate byte (10), containing zero. Sender tabs
2/GRY + 3/BLK correctly address Grey 2; the controller also needed enabling.

## Protocol evidence

Protocol recovered by static inspection of the manufacturer's Launch PC
download, without running its executables:

- https://www.garnetinstruments.com/wp-content/uploads/2026/01/LaunchApp_v1.03_1.zip
- SHA256: `0c648f924b993acd92ce48f4fe7372a25b7393aa7612c0d0513efc6f9e6a8b1d`
- Assemblies: G70xSystem.dll and ISerialMAUI.dll.
- Vendor manual: https://www.garnetinstruments.com/wp-content/uploads/2026/07/SeeLeveL-Soul-708-RBT-Manual-v2.4.pdf

GATT serial service: `0000a002-0000-1000-8000-00805f9b34fb`.
Commands: `0000c303-0000-1000-8000-00805f9b34fb`, write without response.
Replies: `0000c305-0000-1000-8000-00805f9b34fb`, notifications.
ASCII commands end with one carriage return; no application CRC is added.

Read-only commands:

```text
AT+VERSTR\r
AT+CFG?\r
```

The G708 response is `CFG=<base64>`. Do not use the separate SOUL/V1
`TKCONFIG` command format on this device.

The read configuration was 36 bytes: eight four-byte tank records, followed
by four output bytes. Grey 2 is tank index 4; its sender-state byte is offset
19. The only observed configuration change was **offset 19, 0 → 1** (disabled
to one sender). All other 35 returned bytes were preserved, including warning
and shutdown settings. No blind reconstruction from UI defaults was used.

Vendor write format: `AT+CFG=<base64(LE16 save-key + 40 config bytes)>\r`.
The vendor client's four extra fields are brightness, always-on display,
secondary display, C4P mode; the fresh-object defaults appended here were
`01 00 00 00`. This firmware returns only the first 36 configuration bytes,
so effects on any unreturned fields cannot be independently checked. The
vendor default save-key was accepted; no key search was performed.

## Applied sequence and verification

1. Confirmed version and re-read the unchanged baseline before writing.
2. Required the exact intended one-byte diff in the observed 36-byte block.
3. Sent the vendor-format write; controller returned **OK**.
4. Read configuration **before saving**: exact expected 36-byte block.
5. Sent `AT+SAVE=0\r`; controller returned **SETTINGS SAVED**.
6. A strict client initially expected OK for save and stopped on the different
   success text. No write was repeated; a separate read-only connection
   confirmed the expected configuration after disconnect/reconnect.
7. Advertisements changed Grey 2 from disabled code 110 to **33%**; Grey 1
   was **16%**, LPG **0%**, supply **13.5 V**. HA matched these raw values.

Power-cycle persistence was **not tested**. Save acknowledgment and readback
after reconnect were verified. No controller or HA restart was needed.

Initial BLE discoveries sometimes exposed only C300/read, missing serial
characteristics. These attempts stopped without commands. A later connection
exposed the complete profile. Do not invent an unlock write or assume this
observation proves the cause of the mobile app crash.

Temporary Python/Bleak diagnostics ran inside the trailer Terminal add-on
using its existing system Bluetooth bus. API/ingress credentials remained
in process; no credentials or private device addresses are recorded here.

Grey 2 is visible separately on the Maintenance Water card. Its empty/full
calibration and contribution to the combined gauge remain **pending**; a
33% raw reading next to the outlet is not independently measured volume.
