# CAD (Fusion 360)

Organise by version: `cad/v0.1/`, `cad/v0.2/` ...

For each version, export:
- **STEP** (`.step`): the neutral 3D format anyone can open, and what CFD meshing starts from
- **STL / 3MF**: the files you actually print on the K2 Pro
- **Screenshot / render** (`.png`): so people can see the design without opening CAD
- Optionally the **Fusion archive** (`.f3d`)

Big files (`.stl`, `.step`, `.f3d`, `.3mf`) are stored with **Git LFS** (see `.gitattributes`). Run `git lfs install` once on your computer before committing them.

Tip: your live working model stays in Fusion's cloud with its own version history. Export here at each milestone so the repo shows the evolution.
