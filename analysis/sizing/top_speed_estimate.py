"""
First-order top speed estimate for a speed quadcopter.

Idea: at top speed the props' thrust must hold up the drone's weight AND push
against aerodynamic drag. Prop thrust falls as airspeed rises, roughly reaching
zero near the prop's "pitch speed" (how far the prop would screw itself forward
through the air each second). Top speed is where available thrust = required thrust.

This is deliberately simple. It is the hand-calc baseline that later CFD and
real flight data will be compared against. Expect it to be off by 10-30 %.

Model:
    rpm         = Kv * V_battery * rpm_load_factor
    v_pitch     = rpm / 60 * prop_pitch
    T(v)        = n_motors * T_static * (1 - v / v_pitch)        (linear fall-off)
    D(v)        = 0.5 * rho * v^2 * CdA
    W_net       = m * g - body_lift                               (lift from wings/body)
    required(v) = sqrt(D^2 + W_net^2)
    top speed: T(v) = required(v)
"""

import math
import sys

# ---------- Inputs: change these to explore designs ----------
# Each preset is one design. Run:  python top_speed_estimate.py v1
# Shared electronics (see electronics/README.md): 2207 1900KV motors,
# 5.1" props, 6S battery. Only the body (mass, drag, lift) changes.
PRESETS = {
    "v0": dict(               # standard 5" quad, open X frame
        mass_kg=0.62,
        cd=1.0,                   # flat frame flying at a steep tilt: very draggy
        frontal_area_m2=0.0120,
        body_lift_fraction=0.0,
    ),
    "v1": dict(               # printed rocket body, same electronics
        mass_kg=0.85,
        cd=0.30,                  # slender body (CFD will refine in v2)
        frontal_area_m2=0.0060,   # fuselage + wings + motors seen from the front
        body_lift_fraction=0.0,
    ),
}
DEFAULT_PRESET = "v1"

n_motors = 4
motor_kv = 1900           # rpm per volt
cells = 6                 # LiPo cell count (6S)
volts_per_cell_loaded = 3.6   # voltage sags under heavy load
rpm_load_factor = 0.80    # loaded rpm vs no-load Kv*V (props slow the motor)
prop_pitch_in = 5.1       # prop pitch in inches
static_thrust_per_motor_g = 1600  # from motor thrust tables or a thrust stand
rho = 1.225               # air density, kg/m^3 (sea level, 15 C)
g = 9.81
# -------------------------------------------------------------

preset_name = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_PRESET
if preset_name not in PRESETS:
    sys.exit(f"Unknown preset '{preset_name}'. Choose from: {', '.join(PRESETS)}")
p = PRESETS[preset_name]
mass_kg = p["mass_kg"]
cd = p["cd"]
frontal_area_m2 = p["frontal_area_m2"]
body_lift_fraction = p["body_lift_fraction"]


def thrust_n(v, t_static_n, v_pitch):
    return max(0.0, n_motors * t_static_n * (1 - v / v_pitch))


def required_n(v):
    drag = 0.5 * rho * v**2 * cd * frontal_area_m2
    w_net = mass_kg * g * (1 - body_lift_fraction)
    return math.hypot(drag, w_net), drag


def main():
    volts = cells * volts_per_cell_loaded
    rpm = motor_kv * volts * rpm_load_factor
    v_pitch = rpm / 60 * prop_pitch_in * 0.0254
    t_static_n = static_thrust_per_motor_g / 1000 * g

    print(f"Preset             : {preset_name}  (mass {mass_kg} kg, CdA {cd*frontal_area_m2:.4f} m^2)")
    print(f"Battery under load : {volts:.1f} V ({cells}S)")
    print(f"Loaded motor speed : {rpm:,.0f} rpm")
    print(f"Prop pitch speed   : {v_pitch:.1f} m/s = {v_pitch*3.6:.0f} km/h  (hard ceiling in this model)")
    print(f"Thrust-to-weight   : {n_motors*t_static_n/(mass_kg*g):.1f} : 1 (static)")
    print()
    print(f"{'km/h':>6} {'thrust N':>9} {'drag N':>7} {'needed N':>9}")

    # Find top speed with a fine sweep
    top = None
    v = 0.0
    while v < v_pitch:
        if thrust_n(v, t_static_n, v_pitch) < required_n(v)[0]:
            top = v
            break
        v += 0.05

    # Print a readable table every 25 km/h
    for kmh in range(0, int(v_pitch * 3.6) + 1, 25):
        v = kmh / 3.6
        need, drag = required_n(v)
        print(f"{kmh:6d} {thrust_n(v, t_static_n, v_pitch):9.1f} {drag:7.1f} {need:9.1f}")

    print()
    if top is None:
        print("No crossing found below pitch speed (check inputs).")
        return
    need, drag = required_n(top)
    w_net = mass_kg * g * (1 - body_lift_fraction)
    print(f"Estimated top speed: {top*3.6:.0f} km/h  ({top/v_pitch:.0%} of pitch speed)")
    print(f"At top speed: drag {drag:.1f} N vs weight to support {w_net:.1f} N")
    tilt = math.degrees(math.atan2(drag, w_net))
    print(f"Thrust tilt at top speed: {tilt:.0f} deg forward of vertical "
          "(a rocket body should be level at this tilt)")
    if top > 0.8 * v_pitch:
        print("-> Mostly limited by pitch speed: more Kv, voltage or prop pitch raises the ceiling.")
    if w_net > drag:
        print("-> Holding up the weight costs more thrust than drag: body/wing lift or less mass helps a lot.")
    else:
        print("-> Drag dominates: aero work (smaller frontal area, lower Cd) pays off most.")


if __name__ == "__main__":
    main()
