# Speed FPV Drone

A 3D-printed, rocket-style FPV quadcopter built to go as fast as possible, designed, analysed, printed, and flown by me as a learning and portfolio project.

> **Status:** 🟡 v0.1 concept / research phase
> **Follow the journey:** [Build log](docs/build-log.md) · [Iterations](iterations/) · [Decisions](docs/decisions/)

<!-- Add a hero image here once you have a render or photo, e.g. ![v0.1 render](media/renders/v0.1.png) -->

---

## Why this project

Purpose-built speed drones (the Red Bull chase drone, the Peregreen record drones) have pushed quadcopters past 300 to 500+ km/h by treating the drone like a small aircraft: a long, smooth fuselage, motors pushed out on short wings, and the whole thing flying nearly horizontal. I want to understand *why* those designs work by building my own, and to document every step, including the parts that don't work.

This repo is the record of that process. It is meant to show **how** the design evolved, not just the final model.

## Goals

| Phase | Target | What success looks like |
|---|---|---|
| v0.x | Learn + first flight | A printed airframe that hovers, flies stably, and survives a crash or two |
| v1 | **250 to 300 km/h** | GPS-verified top speed in this range, with CFD and sizing calcs that predicted it |
| v2+ | Push toward record territory | Each version beats the last, with data showing why |

## Tools

| Area | Tool |
|---|---|
| CAD | Autodesk Fusion 360 |
| Aero analysis / CFD | OpenFOAM (plus hand calcs in Python) |
| Printing | Creality K2 Pro |
| Flight controller firmware | Betaflight (likely) |
| Data / sizing | Python (`analysis/`) |

## Repo layout

```
docs/
  build-log.md         Dated diary of everything I do, try, break, and learn
  decisions/           One short note per big design decision (what, why, alternatives)
  research/            Reference designs, records, papers, notes
  GITHUB_GUIDE.md      How I use Git/GitHub for this project
iterations/            One folder per design version (v0.1, v0.2 ...) with what changed and why
cad/                   Fusion 360 exports (STEP / STL / 3MF), organised by version
cfd/                   OpenFOAM cases and results
analysis/              Python sizing and performance calculations
electronics/           Parts list (BOM), wiring, flight controller config
testing/               Flight logs, test plans, results
media/                 Photos, renders, videos
```

## How the design process works

1. **Research** → write it up in `docs/research/`
2. **Decide** → record the choice in `docs/decisions/`
3. **Design** → model in Fusion, export to `cad/<version>/`
4. **Analyse** → run sizing (`analysis/`) and CFD (`cfd/`)
5. **Build + test** → print, assemble, fly, log in `testing/`
6. **Reflect** → write up the iteration in `iterations/<version>/README.md`, then start the next one

Every step gets a line in the [build log](docs/build-log.md).

## Safety

High-speed drones carry real kinetic energy (a 1 kg drone at 300 km/h has roughly 3.5 kJ, comparable to a rifle round). All speed runs are flown in open, unpopulated areas, following local drone regulations (registration, line-of-sight / spotter rules), with failsafes configured and tested first.

## Credits / inspiration

Reference designs and their creators are credited in [docs/research/reference-designs.md](docs/research/reference-designs.md). This project is my own design, inspired by but not copied from them.
