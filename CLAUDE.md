# CLAUDE.md

This file provides context to Claude Code when working in this repository.

## Project Overview

This is a collection of BBC micro:bit projects written in MicroPython. The codebase contains hardware control scripts for NeoPixel LEDs, radio communication, motor-driven robotics, and sensor data logging — all targeting the BBC micro:bit microcontroller.

## Repository Structure

```
Micro-bit/
├── HalloweenCostume2018/    # NeoPixel LED costume project
│   └── halloween_costume_sampson_2018.py
├── Misc/                    # Standalone utility scripts
│   ├── hello.py             # Display and digital I/O
│   ├── blink_led.py         # Analog output (PWM)
│   ├── pinOn.py             # Digital pin control
│   ├── radio.py             # Wireless communication
│   ├── test_plotter.py      # Temperature data logger
│   ├── neopixels.py         # NeoPixel chase animation
│   └── MotorDriver.py       # Radio-controlled robot
├── PushupChallenge2019/     # Pre-compiled .hex firmware files
│   ├── microbit-Pushup_Player.hex
│   ├── microbit-Pushup_Receiver.hex
│   ├── microbit-Pushup_Player_BDayParty.hex
│   └── microbit-Pushup_Receiver_BDayParty.hex
├── mu_installation_instructions.txt
├── README.md
├── LICENSE                  # GPLv3
└── CLAUDE.md                # This file
```

## Language and Platform

- **Language:** MicroPython (Python 3 subset for microcontrollers)
- **Target hardware:** BBC micro:bit (v1 and v2)
- **Editor:** Mu editor (codewith.mu) is the recommended tool for flashing code

## Key Libraries

All scripts use the `microbit` module. Additional libraries:

- `neopixel` — RGB LED strip control (WS2812B)
- `radio` — Wireless inter-device communication (channel 19 is used throughout)
- `random` — Random number generation for LED effects

These are built into the micro:bit MicroPython runtime and do not require installation.

## Conventions

- Scripts are self-contained single-file programs (no imports between project files)
- Each script runs in an infinite `while True:` loop after setup
- Pin assignments are defined as module-level globals
- Radio projects use **channel 19** and **power level 7** as defaults
- NeoPixel brightness is capped at **200** (out of 255)
- `.hex` files in `PushupChallenge2019/` are pre-compiled firmware — do not edit directly

## Common Patterns

- `display.scroll()` and `display.show()` for LED matrix output
- `button_a.is_pressed()` / `button_b.is_pressed()` for input
- `pin0.write_digital()` / `pin0.write_analog()` for GPIO control
- `radio.send()` / `radio.receive()` for wireless messaging
- `accelerometer.get_x()` for tilt-based input
- `sleep()` for timing delays (milliseconds)

## Working with This Codebase

- There are no tests, build steps, or package dependencies — scripts are flashed directly to hardware
- The `.hex` files are large binary blobs; changes to the pushup challenge require the original source and a micro:bit compiler toolchain
- When adding new scripts, place them in `Misc/` unless they belong to a dedicated project
- Follow the existing style: module-level globals with underscore prefix (e.g., `_mainDelayTime`), PascalCase for functions
