# Architecture

## Product shape
Radar is a monorepo with three core runtime surfaces:
- `apps/web` for search and comparison UI
- `apps/api` for domain APIs and read-heavy endpoints
- `apps/worker` for scheduled sync, notifications, and derived data

## Domain boundaries
Keep the core domain small:
- services
- countries
- prices
- users
- watchlists
- notifications
- analytics events

## Data flow
1. Worker refreshes cached source data on a schedule.
2. API serves requests from PostgreSQL and Redis.
3. Web reads the API and never owns business rules.
4. New data sources are added through adapters, not by rewriting the core.

## Expansion rules
- UI features stay in the web app.
- Read APIs stay stateless.
- Long-running jobs stay in workers.
- Shared DTOs and validation live in `packages/shared`.
- New channels such as Telegram or mobile apps consume the same API contract.
