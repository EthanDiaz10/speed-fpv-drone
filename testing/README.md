# Testing

- `flight-logs/`: one file per session, named `YYYY-MM-DD_<version>_<what>.md`, plus Blackbox / GPS logs
- Always compare **predicted vs actual** (prediction comes from `analysis/` and `cfd/`)

## Flight log template
One short file per notable test: `YYYY-MM-DD_<version>.md`
```
Test / goal:
Result (top speed, flight time):
Lesson:
```
Raw Blackbox / GPS files go alongside it.

## Test ladder (don't skip steps)
1. Bench test: motors spin the right way, failsafe works, props off
2. Thrust stand (optional but great data)
3. Hover and low-speed handling
4. Progressively faster passes, logging GPS speed
5. Full speed runs
