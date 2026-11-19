# 0001 — Rocket-style fuselage with motors on short wings

**Date:** 2026-11-19
**Status:** Proposed (confirm once v0.1 is modelled)

## Context
A normal FPV quad has to tilt steeply to fly fast, which puts its flat body broadside into the airflow and makes drag explode at high speed.

## Decision
Use a slender fuselage (battery, electronics, camera inside) with the motors mounted on short wings or arms, oriented so that at top speed the fuselage is close to aligned with the airflow.

## Alternatives considered
- **Standard X-frame racing quad:** cheap and proven, but drag-limited to roughly 200 km/h class speeds.
- **Fixed-wing plane:** faster per watt, but not a quadcopter, so it misses the point of the project.

## Consequences
- Need to choose the motor tilt angle relative to the fuselage (design variable for CFD)
- Hover and slow flight will be awkward; take-off and landing need thought
- More complex to print: long fuselage needs splitting into sections

*Template for future decisions: copy this file, bump the number, keep it short.*
