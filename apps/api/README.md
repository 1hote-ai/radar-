# API

FastAPI backend for Radar.

Responsibilities:
- serve read-heavy subscription price data
- expose search and comparison endpoints
- manage exchange-rate caching
- keep worker-side jobs isolated

The API should remain stateless except for persistence and cache access.
