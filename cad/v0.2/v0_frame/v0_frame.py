"""
v0 printed 5" X frame, built with the Fusion 360 API.

Run it in Fusion: Utilities > Scripts and Add-ins (Shift+S). See README.md.
Each run creates a new design. To try a change, edit the numbers in PARAMETERS
below and run the script again.

You can also run it with plain Python (no Fusion) to print the clearance check:
    python v0_frame.py

Axes: X points forward (camera end), Y points left, Z points up.
All numbers are millimetres.
"""

import math
import traceback

# ---------------------------------------------------------------------------
# PARAMETERS: change these to iterate on the design
# ---------------------------------------------------------------------------
PARAMETERS = {
    # Overall layout
    "wheelbase": 225.0,        # motor to motor, measured diagonally
    "arm_angle": 45.0,         # arm angle from the forward axis (45 = true X)
    "prop_dia": 129.5,         # HQProp 5.1 inch

    # Bottom plate (centre and arms are one printed part)
    "plate_length": 80.0,      # centre section, front to back
    "plate_width": 40.0,       # centre section, left to right
    "bottom_thk": 5.0,         # thicker than carbon (printed parts are weaker)
    "arm_width": 16.0,
    "motor_pad_dia": 32.0,

    # Motor mount: Emax ECO II 2207
    "motor_hole_spacing": 16.0,  # 16 x 16 mm square pattern
    "motor_hole_dia": 3.2,       # M3 clearance
    "motor_center_hole": 8.0,    # clearance for the shaft and clip
    "motor_dia": 27.9,           # reference only
    "motor_height": 19.0,        # mount face to top of bell, reference only

    # FC / ESC stack: SpeedyBee F7 V3, 30.5 x 30.5 mm
    "stack_spacing": 30.5,
    "stack_hole_dia": 3.2,

    # Standoffs and top plate
    "standoff_height": 25.0,
    "standoff_dia": 6.0,
    "standoff_inset": 5.0,     # from the plate edges
    "top_thk": 3.0,
    "strap_slot_length": 22.0,  # for a 20 mm battery strap
    "strap_slot_width": 3.0,
    "strap_slot_x": 25.0,       # slot distance from the centre, front and back

    # Camera mount: DJI O4 Air Unit camera. Check its width with calipers.
    "cam_width": 14.0,
    "cam_wall": 3.0,
    "cam_mount_length": 14.0,
    "cam_mount_height": 22.0,
    "cam_base_thk": 2.0,
    "cam_pivot_height": 12.0,  # above the bottom plate
    "cam_pivot_hole": 2.2,     # M2 screw

    # Battery: CNHL 6S 1300mAh, reference only
    "battery_length": 75.0,
    "battery_width": 35.0,
    "battery_height": 38.0,

    # Printer: Creality K2 Pro
    "bed_size": 300.0,
}


# ---------------------------------------------------------------------------
# Layout maths (plain Python, no Fusion needed)
# ---------------------------------------------------------------------------
def motor_positions(p):
    """Return the (x, y) centre of each motor and the angle of its arm."""
    r = p["wheelbase"] / 2
    a = math.radians(p["arm_angle"])
    angles = [a, -a, math.pi - a, math.pi + a]  # front left, front right, rear left, rear right
    return [(r * math.cos(t), r * math.sin(t), t) for t in angles]


def clearance_report(p):
    """Check prop and print bed clearances. Returns (lines, warnings)."""
    r = p["wheelbase"] / 2
    a = math.radians(p["arm_angle"])
    prop_r = p["prop_dia"] / 2
    mx, my = r * math.cos(a), r * math.sin(a)

    def gap_to_box(half_x, half_y):
        # Distance from the motor centre to the nearest point of a centred box, minus prop radius.
        dx = max(mx - half_x, 0)
        dy = max(my - half_y, 0)
        return math.hypot(dx, dy) - prop_r

    checks = [
        ("Prop to prop, left to right", 2 * my - p["prop_dia"], 5.0),
        ("Prop to prop, front to back", 2 * mx - p["prop_dia"], 5.0),
        ("Prop to top plate", gap_to_box(p["plate_length"] / 2, p["plate_width"] / 2), 5.0),
        ("Prop to battery (seen from above)",
         gap_to_box(p["battery_length"] / 2, p["battery_width"] / 2), 5.0),
    ]

    # Footprint of the bottom plate, for the print bed check
    reach_x = mx + p["motor_pad_dia"] / 2
    reach_y = my + p["motor_pad_dia"] / 2
    size_x, size_y = 2 * max(reach_x, p["plate_length"] / 2), 2 * max(reach_y, p["plate_width"] / 2)
    checks.append(("Print bed margin (bottom plate)", p["bed_size"] - max(size_x, size_y), 10.0))

    lines, warnings = [], []
    for name, value, minimum in checks:
        ok = value >= minimum
        lines.append("{:<36} {:6.1f} mm  {}".format(name, value, "ok" if ok else "TOO SMALL"))
        if not ok:
            warnings.append(name)
    lines.append("Bottom plate footprint: {:.0f} x {:.0f} mm".format(size_x, size_y))
    return lines, warnings


# ---------------------------------------------------------------------------
# Fusion 360 part (only runs inside Fusion)
# ---------------------------------------------------------------------------
try:
    import adsk.core
    import adsk.fusion
except ImportError:
    adsk = None


def cm(v_mm):
    """Fusion's API works in centimetres."""
    return v_mm / 10.0


def new_component(root, name):
    occ = root.occurrences.addNewComponent(adsk.core.Matrix3D.create())
    occ.component.name = name
    return occ.component


def xy_plane_at(comp, z):
    """XY plane raised to height z."""
    if z == 0:
        return comp.xYConstructionPlane
    plane_input = comp.constructionPlanes.createInput()
    plane_input.setByOffset(comp.xYConstructionPlane, adsk.core.ValueInput.createByReal(cm(z)))
    return comp.constructionPlanes.add(plane_input)


def sketch_point(sketch, x, y, z):
    """Turn a model point (mm) into a point on the sketch."""
    pt = sketch.modelToSketchSpace(adsk.core.Point3D.create(cm(x), cm(y), cm(z)))
    pt.z = 0
    return pt


def draw_polygon(sketch, points, z):
    """Closed shape through a list of (x, y) points at height z."""
    lines = sketch.sketchCurves.sketchLines
    pts = [sketch_point(sketch, x, y, z) for x, y in points]
    first = prev = None
    for i in range(len(pts)):
        start = prev.endSketchPoint if prev else pts[0]
        end = first.startSketchPoint if (i == len(pts) - 1) else pts[i + 1]
        line = lines.addByTwoPoints(start, end)
        if first is None:
            first = line
        prev = line


def draw_rect(sketch, cx, cy, length, width, z, angle=0.0):
    """Rectangle centred on (cx, cy), long side along `angle` (radians)."""
    c, s = math.cos(angle), math.sin(angle)
    corners = []
    for dx, dy in [(-1, -1), (1, -1), (1, 1), (-1, 1)]:
        lx, ly = dx * length / 2, dy * width / 2
        corners.append((cx + lx * c - ly * s, cy + lx * s + ly * c))
    draw_polygon(sketch, corners, z)


def draw_circle(sketch, x, y, z, dia):
    sketch.sketchCurves.sketchCircles.addByCenterRadius(sketch_point(sketch, x, y, z), cm(dia / 2))


def all_profiles(sketch):
    profiles = adsk.core.ObjectCollection.create()
    for prof in sketch.profiles:
        profiles.add(prof)
    return profiles


def extrude(comp, profiles, distance, operation, bodies=None):
    """Extrude upwards (+Z for XY sketches). `bodies` limits a join or cut to those bodies."""
    extrudes = comp.features.extrudeFeatures
    ext_input = extrudes.createInput(profiles, operation)
    ext_input.setDistanceExtent(False, adsk.core.ValueInput.createByReal(cm(distance)))
    if bodies:
        ext_input.participantBodies = bodies
    return extrudes.add(ext_input)


NEW = None
JOIN = None
CUT = None


def build_bottom_plate(root, p):
    comp = new_component(root, "Bottom plate")
    plane = comp.xYConstructionPlane
    t = p["bottom_thk"]

    # Centre section
    sk = comp.sketches.add(plane)
    sk.name = "Centre"
    draw_rect(sk, 0, 0, p["plate_length"], p["plate_width"], 0)
    body = extrude(comp, sk.profiles.item(0), t, NEW).bodies.item(0)
    body.name = "Bottom plate"

    # Arms, one sketch each so the shapes don't overlap in a sketch
    motors = motor_positions(p)
    for i, (x, y, ang) in enumerate(motors):
        sk = comp.sketches.add(plane)
        sk.name = "Arm {}".format(i + 1)
        draw_rect(sk, x / 2, y / 2, p["wheelbase"] / 2, p["arm_width"], 0, ang)
        extrude(comp, sk.profiles.item(0), t, JOIN, [body])

    # Round motor pads at the arm tips
    sk = comp.sketches.add(plane)
    sk.name = "Motor pads"
    for x, y, _ in motors:
        draw_circle(sk, x, y, 0, p["motor_pad_dia"])
    extrude(comp, all_profiles(sk), t, JOIN, [body])

    # Holes
    sk = comp.sketches.add(plane)
    sk.name = "Holes"
    half = p["motor_hole_spacing"] / 2
    for x, y, ang in motors:
        draw_circle(sk, x, y, 0, p["motor_center_hole"])
        for dx, dy in [(-half, -half), (half, -half), (half, half), (-half, half)]:
            hx = x + dx * math.cos(ang) - dy * math.sin(ang)
            hy = y + dx * math.sin(ang) + dy * math.cos(ang)
            draw_circle(sk, hx, hy, 0, p["motor_hole_dia"])
    for x, y in stack_holes(p):
        draw_circle(sk, x, y, 0, p["stack_hole_dia"])
    for x, y in standoff_positions(p):
        draw_circle(sk, x, y, 0, 3.2)
    for x, y in cam_screw_positions(p):
        draw_circle(sk, x, y, 0, 3.2)
    extrude(comp, all_profiles(sk), t, CUT, [body])


def build_top_plate(root, p):
    comp = new_component(root, "Top plate")
    z = p["bottom_thk"] + p["standoff_height"]
    plane = xy_plane_at(comp, z)

    sk = comp.sketches.add(plane)
    sk.name = "Outline"
    draw_rect(sk, 0, 0, p["plate_length"], p["plate_width"], z)
    body = extrude(comp, sk.profiles.item(0), p["top_thk"], NEW).bodies.item(0)
    body.name = "Top plate"

    sk = comp.sketches.add(plane)
    sk.name = "Holes and strap slots"
    for x, y in standoff_positions(p):
        draw_circle(sk, x, y, z, 3.2)
    for x in (p["strap_slot_x"], -p["strap_slot_x"]):
        draw_rect(sk, x, 0, p["strap_slot_width"], p["strap_slot_length"], z)
    extrude(comp, all_profiles(sk), p["top_thk"], CUT, [body])


def build_standoffs(root, p):
    comp = new_component(root, "Standoffs")
    z = p["bottom_thk"]
    sk = comp.sketches.add(xy_plane_at(comp, z))
    sk.name = "Standoffs"
    for x, y in standoff_positions(p):
        draw_circle(sk, x, y, z, p["standoff_dia"])
        draw_circle(sk, x, y, z, 3.2)
    # Keep only the rings (profiles with an outer and an inner loop)
    rings = adsk.core.ObjectCollection.create()
    for prof in sk.profiles:
        if prof.profileLoops.count == 2:
            rings.add(prof)
    extrude(comp, rings, p["standoff_height"], NEW)


def build_camera_mount(root, p):
    comp = new_component(root, "Camera mount")
    z = p["bottom_thk"]
    plane = xy_plane_at(comp, z)
    x_front = p["plate_length"] / 2
    x_mid = x_front - p["cam_mount_length"] / 2
    inner = p["cam_width"] / 2
    outer = inner + p["cam_wall"]

    # Base
    sk = comp.sketches.add(plane)
    sk.name = "Base"
    draw_rect(sk, x_mid, 0, p["cam_mount_length"], 2 * outer, z)
    body = extrude(comp, sk.profiles.item(0), p["cam_base_thk"], NEW).bodies.item(0)
    body.name = "Camera mount"

    # Two side walls
    for side in (1, -1):
        sk = comp.sketches.add(plane)
        sk.name = "Side wall"
        draw_rect(sk, x_mid, side * (inner + outer) / 2, p["cam_mount_length"], p["cam_wall"], z)
        extrude(comp, sk.profiles.item(0), p["cam_mount_height"], JOIN, [body])

    # Screw holes through the base
    sk = comp.sketches.add(plane)
    sk.name = "Base holes"
    for x, y in cam_screw_positions(p):
        draw_circle(sk, x, y, z, 3.2)
    extrude(comp, all_profiles(sk), p["cam_base_thk"], CUT, [body])

    # Pivot hole through both walls (sketch on the XZ plane, cut both ways)
    sk = comp.sketches.add(comp.xZConstructionPlane)
    sk.name = "Pivot hole"
    draw_circle(sk, x_mid, 0, z + p["cam_pivot_height"], p["cam_pivot_hole"])
    extrudes = comp.features.extrudeFeatures
    ext_input = extrudes.createInput(sk.profiles.item(0), CUT)
    ext_input.setSymmetricExtent(adsk.core.ValueInput.createByReal(cm(2 * outer + 10)), True)
    ext_input.participantBodies = [body]
    extrudes.add(ext_input)


def build_reference_parts(root, p):
    """Motors, props, stack and battery as simple shapes, to check fit. Not printed."""
    comp = new_component(root, "Reference parts (not printed)")
    z0 = p["bottom_thk"]
    motors = motor_positions(p)

    sk = comp.sketches.add(xy_plane_at(comp, z0))
    sk.name = "Motors"
    for x, y, _ in motors:
        draw_circle(sk, x, y, z0, p["motor_dia"])
    for b in extrude(comp, all_profiles(sk), p["motor_height"], NEW).bodies:
        b.name = "Motor"

    z_prop = z0 + p["motor_height"]
    sk = comp.sketches.add(xy_plane_at(comp, z_prop))
    sk.name = "Props"
    for x, y, _ in motors:
        draw_circle(sk, x, y, z_prop, p["prop_dia"])
    for b in extrude(comp, all_profiles(sk), 6.0, NEW).bodies:
        b.name = "Prop disc"
        set_opacity(b, 0.25)

    z_stack = z0 + 5.0
    sk = comp.sketches.add(xy_plane_at(comp, z_stack))
    sk.name = "Stack"
    draw_rect(sk, 0, 0, 36.0, 36.0, z_stack)
    extrude(comp, sk.profiles.item(0), 15.0, NEW).bodies.item(0).name = "FC ESC stack"

    z_bat = z0 + p["standoff_height"] + p["top_thk"]
    sk = comp.sketches.add(xy_plane_at(comp, z_bat))
    sk.name = "Battery"
    draw_rect(sk, 0, 0, p["battery_length"], p["battery_width"], z_bat)
    extrude(comp, sk.profiles.item(0), p["battery_height"], NEW).bodies.item(0).name = "Battery"


def set_opacity(body, value):
    try:
        body.opacity = value
    except Exception:
        pass  # older Fusion versions: not important


def stack_holes(p):
    h = p["stack_spacing"] / 2
    return [(h, h), (h, -h), (-h, h), (-h, -h)]


def standoff_positions(p):
    x = p["plate_length"] / 2 - p["standoff_inset"]
    y = p["plate_width"] / 2 - p["standoff_inset"]
    return [(x, y), (x, -y), (-x, y), (-x, -y)]


def cam_screw_positions(p):
    x_front = p["plate_length"] / 2
    x_mid = x_front - p["cam_mount_length"] / 2
    return [(x_mid - 3.5, 0.0), (x_mid + 3.5, 0.0)]


def run(context):
    global NEW, JOIN, CUT
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        NEW = adsk.fusion.FeatureOperations.NewBodyFeatureOperation
        JOIN = adsk.fusion.FeatureOperations.JoinFeatureOperation
        CUT = adsk.fusion.FeatureOperations.CutFeatureOperation

        app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
        design = adsk.fusion.Design.cast(app.activeProduct)
        design.designType = adsk.fusion.DesignTypes.ParametricDesignType
        root = design.rootComponent

        p = PARAMETERS
        steps = [
            ("bottom plate", build_bottom_plate),
            ("top plate", build_top_plate),
            ("standoffs", build_standoffs),
            ("camera mount", build_camera_mount),
            ("reference parts", build_reference_parts),
        ]
        for name, build in steps:
            try:
                build(root, p)
            except Exception:
                ui.messageBox("Failed while building the {}.\n\n{}".format(name, traceback.format_exc()))
                return

        app.activeViewport.fit()
        lines, warnings = clearance_report(p)
        title = "v0 frame built" if not warnings else "v0 frame built, check clearances"
        ui.messageBox("\n".join(lines), title)
    except Exception:
        if ui:
            ui.messageBox("Failed:\n{}".format(traceback.format_exc()))


if __name__ == "__main__":
    report, problems = clearance_report(PARAMETERS)
    print("\n".join(report))
