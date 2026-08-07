# Domain Model

## Core entities

### Service
Represents a digital subscription product such as Spotify, Netflix, Discord Nitro, or Telegram Premium.

Key fields:
- id
- name
- slug
- category
- official_url
- source_priority

### Country
Represents a region used for price comparison.

Key fields:
- id
- code
- name
- currency_code
- flag_emoji

### PriceSnapshot
Represents one captured price for one service in one country.

Key fields:
- id
- service_id
- country_code
- local_price
- local_currency
- billing_period
- tax_included
- source_type
- source_url
- captured_at
- checksum

### ExchangeRate
Represents a cached currency conversion value.

Key fields:
- base_currency
- quote_currency
- rate
- fetched_at
- provider

### User
Represents a future account holder.

Key fields:
- id
- email
- preferred_currency
- created_at

### WatchlistItem
Represents a price alert rule.

Key fields:
- id
- user_id
- service_id
- target_price
- alert_mode
- created_at

### AnalyticsEvent
Represents product usage telemetry.

Key fields:
- id
- event_name
- actor_id
- payload
- created_at

## Rules
- UI must not depend on source parsing details.
- All price reads should come from stored snapshots.
- All new channels should consume the same service and price contracts.
- New data sources should be added as adapters, not ad-hoc code.
