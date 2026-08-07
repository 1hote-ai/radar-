# Radar

Monorepo scaffold for a regional subscription price tracker.

## Goals
- MVP: search subscriptions, compare regional prices, convert currencies, and show results fast from stored data.
- 2.0+: Telegram notifications, charts, mobile app, plan comparison, user accounts, and analytics.
- Long-term: keep architecture modular so new price sources, products, and channels can be added without rewriting core logic.

## Repo layout
- `apps/web` — Next.js web app
- `apps/api` — FastAPI backend
- `apps/worker` — background jobs for sync and notifications
- `packages/shared` — shared types and utilities
- `docs/` — architecture, roadmap, and product vision
- `infrastructure/` — Docker and deployment helpers

## Development principle
The first version should optimize for:
1. quick search
2. cached data access
3. clean domain boundaries
4. small reusable modules
5. future expansion without breaking the MVP
