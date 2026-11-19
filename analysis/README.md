# Analysis

Python calculations used to size the drone and predict performance.

| Script | What it does |
|---|---|
| `sizing/top_speed_estimate.py` | First-order top speed estimate: where prop thrust (falling with speed) equals aero drag |

Run with Python 3:
```
python analysis/sizing/top_speed_estimate.py
```
Change the numbers at the top of the script to try different motors, props, batteries and body shapes. Copy interesting results into the iteration README.
