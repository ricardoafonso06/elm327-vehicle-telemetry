# elm327-vehicle-telemetry

Read-only vehicle telemetry over an ELM327 adapter, built around a **simulator-first** workflow
and a **security-oriented** view of the OBD-II attack surface.

> **Status:** early development. Primary target vehicle: Audi A4 Avant (B9) 2.0 TDI S tronic, 2018.

## Goals
- Real-time dashboard of standard OBD-II data (SAE J1979) for any compliant vehicle.
- Extended, vehicle-specific data (UDS over ISO-TP) as a research track for the Audi.
- An ELM327 simulator so everything is testable without a car (and in CI).
- Threat model and analysis of the cheap-dongle to CAN bus chain (see [THREAT_MODEL.md](THREAT_MODEL.md)).

## Design principles
- **Read-only**: the project never writes to ECUs.
- **Data, not code, per vehicle**: profiles live in `vehicles/*.yaml`.
- **Containers where they help**: API, simulator, dashboards. Hardware access stays on the host.

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev,api]"
pytest
```

## Layout
See [docs/architecture.md](docs/architecture.md).

## Safety and legal
Do not interact with the dashboard while driving. Use only on vehicles you own or are authorised to test.
