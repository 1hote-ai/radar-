# Worker

Background jobs for Radar.

Responsibilities:
- refresh price snapshots
- refresh currency rates
- evaluate watchlists
- emit notification events
- derive analytics from stored data

Jobs must be idempotent and safe to rerun.
