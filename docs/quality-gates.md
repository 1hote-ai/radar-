# Quality Gates

## MVP gates
A change can be merged into the MVP track only if:
- search still returns results from stored data
- currency conversion is deterministic
- API responses stay backward compatible
- web does not reimplement business logic
- worker jobs remain idempotent

## 2.0 gates
A change can move the project toward 2.0 only if:
- notifications reuse the same price snapshot model
- charts are derived from stored data
- mobile clients consume the same API contract
- accounts do not leak into the read path
- analytics stay event-based and optional

## Future gates
Any new subsystem must:
- plug in through a small interface
- avoid circular dependency with the core domain
- preserve migration safety
- keep the MVP runnable by itself
