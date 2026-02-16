# Micro-bit

A collection of BBC micro:bit projects written in MicroPython. These projects span interactive wearables, radio-controlled robotics, fitness games, and basic hardware tutorials — all designed for hands-on learning with the micro:bit platform.

## Table of Contents

- [Overview](#overview)
- [Projects](#projects)
  - [Halloween Costume 2018](#halloween-costume-2018)
  - [Pushup Challenge 2019](#pushup-challenge-2019)
  - [Miscellaneous Scripts](#miscellaneous-scripts)
- [Hardware Requirements](#hardware-requirements)
- [Getting Started](#getting-started)
- [Mu Editor Installation](#mu-editor-installation)
- [License](#license)

## Overview

This repository contains MicroPython scripts and pre-compiled firmware for the [BBC micro:bit](https://microbit.org/) microcontroller. The projects demonstrate a range of capabilities including NeoPixel LED control, radio communication between devices, motor control for robotics, accelerometer-based input, and temperature sensing.

All Python scripts are written for MicroPython and are intended to be flashed onto the micro:bit using the [Mu editor](https://codewith.mu/) or any compatible tool.

## Projects

### Halloween Costume 2018

**Directory:** `HalloweenCostume2018/`

An interactive Halloween costume powered by the micro:bit with multiple NeoPixel LED strips. The costume displays animated lighting effects across the body.

**File:** `halloween_costume_sampson_2018.py`

**Features:**
- Controls four independent NeoPixel strips:
  - **Circle** (pin2) — 16 RGB LEDs with random color patterns and a chase animation
  - **Left Arm** (pin14) — 5 LEDs cycling in red
  - **Right Arm** (pin0) — 5 LEDs cycling in green
  - **Temple** (pin1) — 1 LED blinking blue
- Button A and Button B adjust animation speed (250ms increments, minimum 500ms delay)
- A circular chase animation triggers every 5 minutes on the main NeoPixel ring
- Random LED selection and color generation for organic-looking effects
- LED brightness capped at 200 (out of 255) for safety
- Startup sequence displays "Boo!" and a skull image
- Test mode flag (`_isTest`) for debugging

**Wiring:**

| Strip      | Pin   | LED Count |
|------------|-------|-----------|
| Right Arm  | pin0  | 5         |
| Temple     | pin1  | 1         |
| Circle     | pin2  | 16        |
| Left Arm   | pin14 | 5         |

---

### Pushup Challenge 2019

**Directory:** `PushupChallenge2019/`

A multiplayer fitness game that uses the micro:bit's accelerometer to count pushups and transmits the count wirelessly to a receiver device. Includes standard and birthday party themed variants.

**Firmware Files (pre-compiled Intel HEX):**

| File | Description |
|------|-------------|
| `microbit-Pushup_Player.hex` | Player device — detects and counts pushups via accelerometer |
| `microbit-Pushup_Receiver.hex` | Receiver device — displays pushup counts from player devices |
| `microbit-Pushup_Player_BDayParty.hex` | Player device with birthday party theme |
| `microbit-Pushup_Receiver_BDayParty.hex` | Receiver device with birthday party theme |

**How it works:**
1. Flash the Player `.hex` file onto one micro:bit and the Receiver `.hex` file onto another
2. The Player micro:bit uses its accelerometer to detect pushup motions
3. Pushup counts are transmitted wirelessly via the micro:bit radio to the Receiver
4. The Receiver displays the count in real time

**To flash:** Drag and drop the `.hex` file onto the micro:bit's USB drive, or use the Mu editor.

---

### Miscellaneous Scripts

**Directory:** `Misc/`

A collection of standalone MicroPython scripts demonstrating various micro:bit capabilities.

#### `hello.py` — Display and Digital Output
Scrolls "Hi, Val" on the LED matrix and toggles pin0 on/off every 500ms. A simple starter example for learning basic I/O.

#### `blink_led.py` — Analog Output (PWM)
Writes alternating analog values (1000 and 500) to pin0 with 1-second delays. Demonstrates Pulse Width Modulation for controlling LED brightness or motor speed.

#### `pinOn.py` — Digital Pin Control with Display Feedback
Sets pin0 HIGH for 10 seconds (displays a checkmark) then LOW for 5 seconds (displays an X). Useful for testing relay circuits or external components.

#### `radio.py` — Wireless Communication
Demonstrates inter-micro:bit radio communication on channel 19 at maximum power (level 7). Supports sending messages triggered by:
- Button A, Button B, or both buttons simultaneously
- Pin0 touch input

The receiver displays incoming messages on the LED matrix. The main loop alternates between sending and receiving.

#### `test_plotter.py` — Temperature Data Logger
Reads the micro:bit's built-in temperature sensor 100 times at 500ms intervals. Each reading is displayed on the LED matrix and printed to serial output. Designed for use with the Mu editor's built-in plotter for real-time graphing.

#### `neopixels.py` — Rainbow Chase Animation
Drives a 16-LED NeoPixel strip on pin0 with a rainbow chase effect. Each LED lights up with a random RGB color while the previous one turns off, creating a smooth chasing pattern at 200ms per frame.

#### `MotorDriver.py` — Radio-Controlled Robot
A full robot control system with dual motor management and multiple input methods.

**Motor Wiring:**

| Motor       | Pin 1 | Pin 2 |
|-------------|-------|-------|
| Right Wheel | pin8  | pin12 |
| Left Wheel  | pin0  | pin16 |

**Movement Commands:**
- **Forward** — Both wheels forward
- **Reverse** — Both wheels reverse
- **Right Turn** — Left wheel forward, right wheel coast
- **Left Turn** — Right wheel forward, left wheel coast
- **Coast** — Both wheels idle
- **Brake** — Both wheels stop

**Control Methods:**
- **Radio remote control** (channel 19) — One micro:bit sends commands, another receives and drives the motors
- **Accelerometer steering** — Tilt the controller micro:bit left/right (threshold: 500) to steer
- **Button controls** — Button B = forward, Button A = brake, A+B = reverse

Visual feedback is shown on the LED matrix with directional arrow images.

## Hardware Requirements

- One or more [BBC micro:bit](https://microbit.org/) boards (v1 or v2)
- USB cable for flashing code
- **For LED projects:** NeoPixel RGB LED strips (WS2812B compatible)
- **For robot project:** Dual DC motors with an H-bridge motor driver
- **For radio projects:** Two micro:bit boards (one sender, one receiver)
- Jumper wires and a breadboard (optional, for prototyping)

## Getting Started

1. **Install the Mu editor** — See [Mu Editor Installation](#mu-editor-installation) below or visit [codewith.mu](https://codewith.mu/)
2. **Connect your micro:bit** via USB
3. **Open a script** from this repository in Mu
4. **Click "Flash"** to upload the code to your micro:bit
5. For `.hex` files (PushupChallenge), drag and drop them directly onto the micro:bit USB drive

## Mu Editor Installation

The [Mu editor](https://codewith.mu/) is the recommended editor for writing and flashing MicroPython to the micro:bit. See `mu_installation_instructions.txt` for Raspberry Pi-specific installation instructions.

**On Raspberry Pi:**

Binary install:
```bash
chmod +x <mu-file-path>
./<mu-file-path>
```

Debian package install:
```bash
sudo dpkg -i <mu.deb-file-path>
sudo apt-get -f install
```

**On other platforms:** Download from [codewith.mu/en/download](https://codewith.mu/en/download).

## License

This project is licensed under the **GNU General Public License v3.0** — see the [LICENSE](LICENSE) file for details.
