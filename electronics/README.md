# Electronics

The v0 parts are chosen so they move straight into the v1 rocket body. Only the frame changes between v0 and v1.

## Bill of materials (v0 and v1)

Prices are approximate (US, Nov 2026). Check before buying.

| Part | Model | Qty | Mass (g) | Price (USD) | Link | Why this one |
|---|---|---|---|---|---|---|
| Frame (v0 only) | TBS Source One V5, 5" | 1 | 110 | 35 | [RDQ](https://www.racedayquads.com/search?q=source+one+v5) | Cheap, open-source and easy to repair. Replaced by the printed body in v1 |
| Motors | T-Motor Velox V2207.5 V2, 1950KV | 4 | 33 each | 22 each | [RDQ](https://racedayquads.com/products/t-motor-velox-v2-2207-5-1950kv-motor-royal-blue) | Proven 6S 5" motor. 1950KV on 6S gives the pitch speed needed for about 200 km/h |
| Props | HQProp 5.1x5.1x3 | 4 + spares | 4.5 each | 4 per set | [RDQ](https://www.racedayquads.com/search?q=hqprop+5.1x5.1x3) | Common, cheap, durable. Higher-pitch props come later for speed runs |
| Flight controller | Foxeer F722 V4 X8, 30x30 | 1 | 8 | 50 | [RDQ](https://www.racedayquads.com/products/foxeer-f722-v4-x8-4-8s-30x30-dual-bec-barometer-flight-controller-mpu6000) | F7 running Betaflight, Blackbox flash, rated 4 to 8S |
| ESC (4-in-1) | Foxeer Reaper F4 65A, 3 to 8S, 30x30 | 1 | 16 | 80 | [RDQ](https://racedayquads.com/collections/all-electronics/products/foxeer-reaper-f4-128k-32bit-65a-3-8s-30x30-4in1-esc) | 65 A per motor with headroom, and 8S rated so it carries into v2. Same brand as the FC, so the cable plugs straight in |
| Battery | CNHL Black Series 6S 1300mAh 100C | 3 | 215 each | 35 each | [RDQ](https://www.racedayquads.com/search?q=cnhl+6s+1300) | Standard 6S 5" size. Its 35 x 38 mm cross-section sets the fuselage diameter |
| Video (air unit) | DJI O4 Air Unit | 1 | 9 | 90 | [DJI](https://www.dji.com/o4-air-unit) | Clear digital picture at speed, records onboard video, very light |
| Goggles | DJI Goggles N3 | 1 | | 230 | [DJI](https://www.dji.com/goggles-n3) | Cheapest goggles that work with the O4 |
| Radio | RadioMaster Pocket, ELRS | 1 | | 65 | [RDQ](https://www.racedayquads.com/search?q=radiomaster+pocket+elrs) | Low cost, ELRS built in, good beginner radio |
| Receiver | RadioMaster RP2, ELRS nano | 1 | 2 | 20 | [RDQ](https://www.racedayquads.com/search?q=radiomaster+rp2) | Tiny, long range, matches the radio |
| GPS | Matek M10Q-5883 | 1 | 10 | 40 | [RDQ](https://www.racedayquads.com/search?q=matek+m10q) | Logs ground speed in Blackbox and enables GPS Rescue |

Flying weight: about 560 g on the v0 frame, about 850 g in the v1 printed body (see `analysis/sizing/top_speed_estimate.py`).

## Tools and safety kit

| Item | Model | Price (USD) | Why |
|---|---|---|---|
| Soldering iron | Pinecil V2 | 30 | Temperature controlled, enough power for battery leads |
| Smoke stopper | Any XT60 smoke stopper | 10 | Stops a wiring mistake from burning the ESC on first power-up |
| Charger | ToolkitRC M7AC | 70 | Balance charges 6S, runs from the wall |
| LiPo bag | Any fireproof LiPo bag | 15 | Charge and store batteries inside it |
| Multimeter | Any basic meter | 20 | Check for shorts before plugging in a battery |

Rough total: about $960. That is about $520 for the parts that fly, $295 for goggles and radio, and $145 for tools. The goggles, radio and tools are one-off costs reused for every version.

## Notes

- The 1950KV motors are matched to 6S. Moving to 8S in v2 means new motors, but the FC and ESC stay.
- Keep antennas (O4, receiver) and the GPS away from carbon-fibre parts. Carbon blocks radio signals.

## Also store here

- Wiring diagram (a photo of a hand sketch is fine to start)
- Betaflight config backup (`diff all` output) for each version
