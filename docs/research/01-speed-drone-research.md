# Speed Drone Research: Records, Reference Builds, Physics and Roadmap

*Research notes for a 3D-printed high-speed FPV quadcopter. Written November 2026. Records move fast in this category, so re-check the Guinness listing before quoting any number.*

---

## 1. Summary

- The current **ratified Guinness record** for "fastest ground speed by a battery-powered remote-controlled quadcopter" is **657.59 km/h (408.6 mph)**, set by Luke and Mike Bell's **Peregreen V4** on 11 Dec 2025 in Cape Town. Unofficial runs in 2026 (Blackbird, Quantum Systems' Apex Recordhunter) claim around 685 to 700 km/h but were not certified as of the sources below.
- The record went from **360 km/h (2022)** to **658 km/h (2025)** in three years, mostly through aerodynamic bodies, very high power (16 kW on Peregreen 3), and careful prop and thermal engineering. Every top team iterated through 3 or 4 versions and crashed or burned some of them.
- A realistic plan for this project: **v1 at about 200 km/h**, **v2 at 250 to 300 km/h**, **v3 at 350+ km/h** (the 2022 world-record level and the Red Bull F1 chase drone's level). Going past that is a stretch goal, not a v1 goal.
- The rocket layout in the inspiration images is the right one: one long, smooth body that points into the wind at speed, with four motors on short arms or wings.

## 2. The inspiration images

| Image | What it shows | What to take from it |
|---|---|---|
| White rocket with 4 motors on short black wings | Hobby-scale rocket-layout quad | Simple, printable shape. Good model for a v1. |
| Red Bull Drone 1 (Dutch Drone Gods) | Bullet body, 4 arms, camera in the nose. Filmed F1 cars at up to 350 km/h | Proof that this layout can be stable, steerable and carry a camera at 350 km/h. |
| Black record-style drone with tapered motor pods | Peregreen-style record build | Shows where a v3+ goes: motor nacelles faired into the wing, everything smoothed. |

## 3. Record history (Guinness category above)

| Date | Drone / team | Speed | Notes |
|---|---|---|---|
| Jul 2017 | DRL RacerX | 263 km/h (163.5 mph) | First notable record. |
| 8 Nov 2022 | XLR V3, Ryan Lademann (USA) | 360.5 km/h (224 mph) | Only 490 g. |
| 2023 | Peregreen 1, Bells | 397 km/h | Not ratified. Weighed 1.05 kg, 5.2 kW peak. |
| Apr 2024 | Peregreen 2, Bells | 480.2 km/h | 1.85 kg, 8.9 kW. Touched 510 km/h peak. |
| 28 Feb 2025 | Fastboy 2, Samuele Gobbi (Switzerland) | 557.6 km/h | Student build. |
| 22 Jun 2025 | Peregreen 3, Bells + Dubai Police | 580 km/h | 2.77 kg, 16.2 kW. Later 585 km/h unratified. |
| 8 Dec 2025 | Blackbird, Benjamin Biggs (Australia) | 626.4 km/h | 599 upwind / 655 downwind. |
| **11 Dec 2025** | **Peregreen V4, Bells** | **657.59 km/h** | **Current ratified record**, three days after losing it. |
| 2026 (unofficial) | Blackbird; Apex Recordhunter | ~685 to ~699 km/h | Not certified in sources. |

**How Guinness measures it:** two passes in opposite directions at a level altitude, each timed over at least 100 m, and the two speeds averaged. The opposite passes cancel out wind. Note how big the wind effect is: Blackbird was 599 km/h upwind and 655 km/h downwind on the same day. Use the same two-way method for our own speed claims, so the numbers mean something.

## 4. Reference builds in detail

### Peregreen series (Luke and Mike Bell, South Africa)

The best-documented iteration story in this category, and a good model for how to show a process.

- **Peregreen 1 → 2 → 3 → V4:** weight went 1.05 → 1.85 → 2.77 kg and peak power 5.2 → 8.9 → 16.2 kW. They did not make it lighter to go faster. They made it more powerful and more aerodynamic, and accepted the weight.
- **Props:** high-pitch APC props so RPM stays low and blade tips stay below the speed of sound. Takeoff is "miserable", like starting a car in seventh gear. V4 went from 7x5 to about 6 inch props and never exceeded 40,000 RPM (printed spinners were bench tested to 70,000 RPM).
- **Motors (V4):** compared AOS Supernova 3220, AMX 2826 and T-Motor 3120 on a homemade thrust stand (strain gauges, Arduino, thermal camera). The AOS made the most thrust, but they chose the T-Motor 3120 for lower temperature and wear, rewound from 800 KV to 900 KV.
- **Heat (Peregreen 3):** the printed chassis **caught fire** during a test flight. They oven-tested materials: PLA and PETG melted, carbon-fibre nylon survived above 175 °C. They switched to water cooling (50 ml chamber, small pump) so the body needed no air inlets.
- **Flight profile (Peregreen 3):** about 300 km/h after 20 s, top speed at about 40 s, about 5.5 km covered. Full throttle empties the battery in 23 s.
- **Materials (V4):** printed as one continuous body on a Bambu H2D in PETG, PA6-CF and TPU (soft TPU nose tip for landings). Sanded and polished. CFD done with AirShaper.
- **Roles:** Mike on aerodynamics and drivetrain, Luke on battery and cooling.

### Red Bull Drone 1 (Dutch Drone Gods + Red Bull Advanced Technologies)

- Top speed 350 km/h, 0 to 300 km/h in about 2 to 4 s (sources differ), under 1 kg, rotors up to 42,000 RPM, about 3 minutes of flight, 4K60 camera in the nose.
- Body in carbon, glass fibre and 3D-printed polymer; the team used printing for both prototypes and final parts.
- Electronics are "pretty standard, off-the-shelf", plus a motor from a supplier that handled higher RPM.
- Design philosophy: **aerodynamics matter more than weight**, and run every part below its limits.
- First full lap (Sept 2023) reached 310 km/h. Their pilot said "the speed was never the problem," the corners were. They redesigned after that lap.

### XLR V3 (Ryan Lademann, 2022)

- 360 km/h at only 490 g. Shows that the first ~350 km/h is reachable with a small, light drone and a clean body, without multi-kW custom drivetrains. This is the most relevant benchmark for our v3.

## 5. The physics, for a beginner

### 5.1 Drag decides top speed

Top speed is where **thrust along the flight path = drag**. Drag is

> **D = ½ · ρ · v² · CdA**

- ρ = air density (about 1.2 kg/m³ at sea level)
- v = airspeed in m/s
- CdA = drag coefficient × frontal area, the one number that describes how "slippery" the drone is. A normal 5" FPV quad is very roughly 0.01 m² or worse. A good rocket-layout body might reach 0.002 to 0.004 m². **This is the number OpenFOAM will help us measure and reduce.**

The power needed to push through the air is drag × speed, so **power grows with the cube of speed**:

> **P = D · v = ½ · ρ · v³ · CdA**

Estimates (sea level, assuming 60% of battery power ends up as useful thrust work):

| Speed | CdA 0.002 m² | CdA 0.003 m² | CdA 0.004 m² |
|---|---|---|---|
| 200 km/h | 340 W | 510 W | 690 W |
| 250 km/h | 670 W | 1.0 kW | 1.3 kW |
| 300 km/h | 1.2 kW | 1.7 kW | 2.3 kW |
| 360 km/h | 2.0 kW | 3.0 kW | 4.0 kW |

Two lessons from this table:

1. Going from 300 to 360 km/h (20% faster) needs about **73% more power**.
2. Cutting CdA by a third is worth as much as a third more power, and usually costs nothing in weight or battery. That is why every record team invested in aero.

### 5.2 Pitch speed: the prop has to "screw" through the air faster than the drone

A prop moves forward one pitch length per revolution in ideal conditions:

> **pitch speed (m/s) = RPM / 60 × pitch (m)**

At speed, the prop needs to be about 20 to 40% faster than the airspeed to still make thrust. For 300 km/h (83 m/s), allowing 30% slip:

| Prop pitch | RPM needed | Blade tip speed, 6" prop |
|---|---|---|
| 5" | ~51,000 | Mach 1.2 ❌ |
| 6" | ~43,000 | Mach 1.0 ❌ |
| 7" | ~37,000 | Mach 0.88 ⚠️ |
| 8" | ~32,000 | Mach 0.78 ✅ |

Tip speed includes forward speed (the tip moves in a helix). Once tips approach Mach 0.8 to 0.9 they lose efficiency fast and get very loud. That is exactly why the Peregreen team used high-pitch props at modest RPM. **High pitch / low RPM is the core trick for speed quads**, and the price is weak thrust at low speed (slow takeoff).

### 5.3 Matching motor KV and battery voltage

> **unloaded RPM ≈ KV × battery voltage**, and loaded RPM is roughly 80 to 85% of that.

Example: to get about 37,000 RPM loaded on 6S (about 22 V under load) you need roughly 2,000 KV. On 8S (about 29 V) roughly 1,550 KV. Higher voltage means lower current for the same power, so less heat in wires, ESCs and the battery. That is why record builds go to 8S and above.

### 5.4 Weight and attitude

In the rocket layout the body points forward and the motors tilt the thrust mostly backward. Some thrust still has to hold the drone up (or small wings can help, like in the white rocket image). At 300 km/h with 12 N of drag and an 8 N (800 g) drone, total thrust needed is about √(12² + 8²) ≈ 15 N. Weight matters less than drag at top speed but matters a lot for acceleration, and acceleration matters because the battery only lasts tens of seconds at full power.

### 5.5 Heat

At 1 to 3 kW, even 85% efficient motors and ESCs dump hundreds of watts of heat into a closed plastic shell. Peregreen 3's chassis caught fire. Plan for heat from v2 onward: airflow paths, heat-resistant filament near motors and ESCs, and temperature logging.

## 6. Recommended roadmap

Each version has one main question to answer, so each one is a clear chapter in the portfolio.

### v0: Learn to fly and build (about 150 km/h)
- **Goal:** learn the basics without designing anything new yet.
- Build a standard 5" freestyle quad from parts or a kit: solder the ESC, flight controller, receiver and video, set up **Betaflight**, add a GPS module.
- Before the first flight, practise in an FPV simulator (Liftoff, Uncrashed or VelociDrone).
- Learn to read **Blackbox** flight logs. Fly a GPS-logged speed run as a baseline.
- **Portfolio output:** build log, wiring diagram, first speed log.

### v1: First rocket body (target about 200 km/h)
- **Question:** can I make a printed rocket-layout quad that is stable and controllable?
- Reuse v0 electronics (6S, 5" or 6" props, ~2,000 to 2,400 KV) inside a simple printed rocket body in Fusion 360.
- Print in PETG (or PLA for quick fit checks). Focus on centre of gravity, motor tilt angle, battery access and a crash-replaceable nose.
- Expect to rebuild the nose and arms several times. That is the point.
- **Portfolio output:** CAD revisions, why each change was made, stable flight video, first two-way speed result.

### v2: Aero and drivetrain optimisation (target 250 to 300 km/h)
- **Question:** how much speed does real engineering buy?
- **OpenFOAM:** run v1's shape and estimate CdA. Try 3 or 4 shapes (nose, tail taper, arm cross-section, motor fairings) and compare. Validate against flight data (speed vs. power from Blackbox).
- **Thrust stand:** build a cheap one (load cell + HX711 + Arduino + current sensor) and test 2 or 3 motor/prop combos. This is exactly what the Peregreen team did and is great portfolio content.
- Move to higher-pitch props and consider 8S.
- Print hot zones in carbon-fibre nylon (PA-CF / PA6-CF) or PETG-CF. The K2 Pro's enclosed, heated chamber and hardened nozzle are suited to these.
- **Portfolio output:** CFD comparison, thrust-stand data, predicted vs. measured top speed.

### v3: Record-class (target 350+ km/h)
- **Question:** can I reach the 2022 world-record level / Red Bull Drone 1 level?
- Custom motor pods and fairings, thermal management, higher power (roughly 3 kW+), telemetry for temperatures and current.
- Formal two-way, 100 m timed runs with GPS logs, matching the Guinness method.
- **Portfolio output:** full engineering report across all versions.

### Stretch
Beyond ~400 km/h the teams that succeed spend years and many kW. Treat it as an open-ended goal once v3 works.

## 7. Starter component class (v0 / v1)

Not a shopping list yet, just the class of parts to look at. Prices move, so we will pick exact parts in a separate step.

| Part | Class to look for |
|---|---|
| Flight controller | F7 or H7 running Betaflight, with Blackbox logging |
| ESC | 4-in-1, 6S rated (8S rated if you want to grow into v2), 55 A+ per channel |
| Motors | 2207 to 2306 size, ~1,900 to 2,400 KV for 6S |
| Props | 5" to 6" racing props, then high-pitch props for speed runs |
| Battery | 6S LiPo, 1,100 to 1,800 mAh, high discharge rating |
| Video | Digital (DJI O4 / Walksnail) for clearer picture at speed |
| Radio | ELRS transmitter and receiver |
| GPS | Small GPS module for speed logging and failsafe return |
| Tools | Temperature-controlled soldering iron, smoke stopper, multimeter, LiPo charger with balance port, fireproof LiPo bag |

## 8. Safety

- **Energy:** a 1 kg drone at 300 km/h carries about 3.5 kJ, around seven times a 9 mm pistol bullet. Fly speed runs only over empty land with nobody downrange, and with a spotter.
- **LiPo batteries:** charge on a non-flammable surface in a LiPo bag, never unattended, always balance charge, store at storage voltage (~3.8 V/cell), retire any puffed or damaged pack.
- **Bench work:** take props off whenever the drone is powered on the bench. Use a smoke stopper on first power-up.
- **Failsafe:** set and test failsafe (disarm or GPS rescue) before every new build's first flight.
- **Printed parts and heat:** PLA softens around 55 to 60 °C and PETG around 75 to 80 °C. Do not use them next to motors or ESCs at high power.

## 9. Legal (assuming you fly in the US)

Check the current FAA pages before flying; the rules change.

- **Recreational flying** (49 U.S.C. 44809): pass the free **TRUST** test, register drones over 250 g, comply with **Remote ID** (built in, broadcast module, or fly at an FAA-recognised identification area, a FRIA), stay at or below 400 ft, keep visual line of sight. FPV goggles mean you need a **visual observer** next to you.
- **Part 107** (commercial / Remote Pilot certificate) has a **100 mph (161 km/h) speed limit**. Recreational rules have no set speed limit, but you must follow a community-based organisation's safety guidelines. High-speed runs are best done at an **AMA field or FRIA** with permission.
- **Radio:** DJI and Walksnail digital systems operate under FCC Part 15 rules. Many analog video transmitters need an amateur radio (Technician) licence in the US.
- Talk to a local FPV club early. They will know where you can legally fly fast.

## 10. Documenting the iterations (for the portfolio)

- One folder per version (`v0/`, `v1/`, ...) with CAD exports, a short design note, flight logs and photos.
- For each change, record **what changed, why, what you expected, and what actually happened**. Failures are the most interesting part.
- Keep the same test method across versions (two-way GPS runs, same thrust stand) so results are comparable.
- Keep a single "results over time" table that shows speed, CdA estimate, weight and power for each version.

## Sources

- DroneXL, "Luke Maximo Bell's Peregreen V4 goes 408 mph" (Jan 2026): https://dronexl.co/2026/01/04/luke-bells-peregreen-v4-new-fastest-drone/
- Tom's Hardware, "Fully 3D printed drone capable of flying at 408 mph..." (Jan 2026): https://www.tomshardware.com/3d-printing/fully-3d-printed-drone-capable-of-flying-at-408-mph-is-the-fastest-in-the-world-father-son-duo-reclaim-guinness-world-record-title-with-diy-quadcopter
- New Atlas, "World's fastest drone hits 408 mph": https://newatlas.com/drones/luke-mike-bell-peregreen-v4-guinness-speed/
- heise online, "Peregreen 3: Fastest electric DIY quadcopter drone flies 585 km/h": https://heise.de/-10908286
- AeroCorner, "Fastest Drones in the World: 2026 Speed Records": https://aerocorner.com/blog/fastest-drones/
- sUAS News, "World's fastest filming FPV drone: How it was built" (Feb 2024): https://suasnews.com/2024/02/worlds-fastest-filming-fv-drone-how-it-was-built
- Newsshooter, "World's fastest camera drone: 300 km/h in just 4 seconds" (Feb 2024): https://www.newsshooter.com/2024/02/27/worlds-fastest-camera-drone-300-km-h-in-just-4-seconds-with-a-top-speed-of-over-350-km-h/
- Red Bull, "World's fastest filming drone build": https://www.redbull.com/int-en/worlds-fastest-filming-drone-build
- Elektor, "World's Fastest Drone Reclaims Guinness Record at 657.59 km/h": https://www.elektormagazine.com/news/worlds-fastest-drone-guinness

*Physics tables are back-of-envelope estimates made for this document, not measured values. They will be replaced with CFD and flight data as the project goes on.*
