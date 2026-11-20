# 0002 — Motor spacing and 30° motor tilt for v1

**Date:** 2026-11-20
**Status:** Proposed (test in flight on v1)

## Context
In the rocket layout the fuselage should point straight into the airflow at top speed. The quad still has to tilt its thrust forward to fly fast, so the motors must be mounted at an angle to the body. Prop size (5.1") also sets how far apart the motors must be.

## Decision
- Motors 200 mm apart left to right and 145 mm front to back. These are the smallest values that keep each prop clear of the body and of the other props.
- Motors tilted 30° forward relative to the body.

The sizing script (`v1` preset) predicts the thrust is tilted about 26° forward at top speed. 30° rounds this up, because the script underestimates drag (it ignores prop drag and the motors themselves).

## Alternatives considered
- **0° tilt (normal quad):** the body would fly nose-down at a steep angle, which throws away the point of a slender body.
- **45° tilt:** body level only at much higher speeds than v1 can reach. Hover would be very nose-up.

## Consequences
- In hover the body sits 30° nose-up. Take-offs from a short stand or by hand launch.
- Print the motor pods with the tilt angle as a parameter, and make 20°, 30° and 40° versions to compare in flight.
