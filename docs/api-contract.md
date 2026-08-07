# API Contract

## Read endpoints
- `GET /health`
- `GET /services`
- `GET /services/{slug}`
- `GET /services/{slug}/prices`
- `GET /countries`
- `GET /currencies`
- `GET /analytics/summary` (future)

## Write endpoints
- `POST /watchlist` (2.0+)
- `POST /notifications/test` (2.0+)
- `POST /auth/login` (2.0+)
- `POST /auth/register` (2.0+)

## Contract rules
- Responses must be stable and versionable.
- Read endpoints must return stored snapshots, not live scrapes.
- Public clients must never depend on internal parsing models.
- Future endpoints should be additive, not breaking.
