# Analysis

Python calculations used to size the drone and predict performance.

| Script | What it does |
|---|---|
| `sizing/top_speed_estimate.py` | First-order top speed estimate: where prop thrust (falling with speed) equals aero drag |

Run with Python 3:
```
python analysis/sizing/top_speed_estimate.py v0   # standard 5" quad
python analysis/sizing/top_speed_estimate.py v1   # printed rocket body
```

| Preset | Mass | CdA (m²) | Predicted top speed |
|---|---|---|---|
| v0 | 0.62 kg | 0.0120 | 178 km/h |
| v1 | 0.85 kg | 0.0018 | 218 km/h |

The model is optimistic. Real 5" quads usually top out around 150 to 170 km/h, so expect real numbers 10 to 20 % lower. Flight data will calibrate it.

Change the numbers at the top of the script to try different motors, props, batteries and body shapes. Copy interesting results into the iteration README.
