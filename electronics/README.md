# Electronics

The v0 parts are chosen so they move straight into the v1 rocket body. Only the frame changes between v0 and v1.

## Bill of materials (v0 and v1)

Prices are approximate (US, Nov 2026). Check before buying.

| Part | Model | Qty | Mass (g) | Price (USD) | Link | Why this one |
|---|---|---|---|---|---|---|
| Frame (v0 only) | Printed 5" X frame, PETG-CF or PA-CF | 1 + spare arms | 140 | 10 (filament) | Printed on the K2 Pro | No frame to buy. Designing it in Fusion 360 is a good warm-up for the v1 body. Replaced by the printed rocket body in v1 |
| Motors | Emax ECO II 2207, 1900KV | 4 | 33 each | 14 each | [RDQ](https://www.racedayquads.com/search?q=emax+eco+ii+2207) | Budget 6S 5" motor. 1900KV on 6S gives the pitch speed needed for about 200 km/h |
| Props | HQProp 5.1x5.1x3, bulk pack | 4 + spares | 4.5 each | 3 per set | [RDQ](https://www.racedayquads.com/search?q=hqprop+5.1x5.1x3) | Common, cheap, durable. Higher-pitch props come later for speed runs |
| FC + ESC stack | SpeedyBee F7 V3 stack (F722 FC + 50A 4-in-1 ESC), 30x30 | 1 | 24 | 85 | [RDQ](https://www.racedayquads.com/products/speedybee-v3-f722-3-6s-30x30-stack-combo-f722-fc-50a-32bit-4in1-esc) | F7 running Betaflight with Blackbox logging. Sold as a matched pair, and set up from a phone app, which is easy for a first build |
| Battery | CNHL Black Series 6S 1300mAh 100C | 2 | 215 each | 35 each | [RDQ](https://www.racedayquads.com/search?q=cnhl+6s+1300) | Standard 6S 5" size. Its 35 x 38 mm cross-section sets the fuselage diameter |
| Video (air unit) | DJI O4 Air Unit | 1 | 9 | 90 | [DJI](https://www.dji.com/o4-air-unit) | Clear digital picture at speed, records onboard video, very light |
| Goggles | DJI Goggles N3 | 1 | | 230 | [DJI](https://www.dji.com/goggles-n3) | Cheapest goggles that work with the O4 |
| Radio | RadioMaster Pocket, ELRS | 1 | | 65 | [RDQ](https://www.racedayquads.com/search?q=radiomaster+pocket+elrs) | Low cost, ELRS built in, good beginner radio |
| Receiver | RadioMaster RP2, ELRS nano | 1 | 2 | 20 | [RDQ](https://www.racedayquads.com/search?q=radiomaster+rp2) | Tiny, long range, matches the radio |
| GPS | HGLRC M100 Mini (M10) | 1 | 6 | 20 | [RDQ](https://www.racedayquads.com/search?q=hglrc+m100+mini) | Logs ground speed in Blackbox and enables GPS Rescue |

Flying weight: about 590 g on the v0 frame, about 850 g in the v1 printed body (see `analysis/sizing/top_speed_estimate.py`).

## Tools and safety kit

| Item | Model | Price (USD) | Why |
|---|---|---|---|
| Soldering iron | Pinecil V2 | 30 | Temperature controlled, enough power for battery leads |
| Smoke stopper | Any XT60 smoke stopper | 10 | Stops a wiring mistake from burning the ESC on first power-up |
| Charger | ToolkitRC M6AC | 40 | Balance charges 6S, runs from the wall |
| LiPo bag | Any fireproof LiPo bag | 15 | Charge and store batteries inside it |
| Multimeter | Any basic meter | 20 | Check for shorts before plugging in a battery |

Rough total: about $770. That is about $360 for the parts that fly, $295 for goggles and radio, and $115 for tools. The goggles, radio and tools are one-off costs reused for every version.

## Notes

- Budget first: the speed comes mostly from the printed body, so the electronics only need to be good enough.
- All frames and bodies are printed, not bought. Printed arms break more easily than carbon ones, so print spares. They cost very little.
- Everything is matched to 6S. Moving to 8S in v2 means a new motor set and an 8S stack (for example Foxeer F722 V4 X8 + Reaper 65A, about $130). v0 and v1 don't need them, so that cost waits until v2.
- Keep antennas (O4, receiver) and the GPS away from carbon-fibre parts. Carbon blocks radio signals.

## Also store here

- Wiring diagram (a photo of a hand sketch is fine to start)
- Betaflight config backup (`diff all` output) for each version
