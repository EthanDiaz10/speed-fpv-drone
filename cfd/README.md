# CFD (OpenFOAM)

Each case lives in `cfd/cases/<version>-<description>/`, e.g. `v0.2-fuselage-100ms/`.

Commit only the **case setup** (`0/`, `constant/` except the mesh, `system/`) plus a short `README.md` and summary plots. Solver output (time folders, `processor*/`, meshes) is ignored by `.gitignore` because it gets huge.

Each case README should say:
- Geometry (which CAD export), flow speed, angle of attack
- Mesh size and quality checks
- Result: drag force, Cd, frontal area, and a pressure/velocity picture
- How it compares to the hand calculation in `analysis/`

Suggested starting point: OpenFOAM's `simpleFoam` motorBike tutorial, which is the same kind of problem (external aero around a body).
