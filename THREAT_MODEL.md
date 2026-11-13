# Threat model (draft)

Chain under analysis: **Vehicle OBD-II port -> ELM327 dongle -> Bluetooth/Wi-Fi link -> host/app -> dashboard**

## Assets
Vehicle bus integrity, driver safety, vehicle data/location privacy, host device.

## Initial STRIDE table (to be validated with real tests)
| Category | Example threat | Status |
|---|---|---|
| Spoofing | Rogue device pairs with the dongle (default PIN 1234/0000) | To test |
| Tampering | Unauthenticated client sends commands to the CAN bus through the dongle | To test |
| Repudiation | No logging of who connected/sent what | Mitigation: audit log |
| Information disclosure | Unencrypted telemetry over the air | To test |
| Denial of service | Bus flooding via the adapter | Out of scope for testing on the car |
| Elevation of privilege | Dongle as pivot from wireless to the vehicle network | To analyse |

Experiments must only be performed on owned hardware, never on a moving vehicle.
