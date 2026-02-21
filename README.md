# COE 216 — Signals and Systems | Homework 1

**Course:** COE 216 Signals and Systems · 2025–2026 Spring · Group 9

> Sinusoidal signal sampling, Nyquist criterion, and DTMF tone synthesis with an interactive GUI.

---

## Tasks

### Task 1 — Signal Sampling & Visualization
Generates three sinusoidal signals derived from the group's fundamental frequency (f₀ = 111 Hz) and visualizes them both individually and as a combined waveform.

| Signal | Frequency |
|--------|-----------|
| f₁ | 111 Hz |
| f₂ | 55.5 Hz |
| f₃ | 1110 Hz |

Sampling frequency: **f_s = 44100 Hz** (Nyquist minimum: 2220 Hz)

### Task 2 — DTMF Signal Generator
Interactive 4×4 telephone keypad that synthesizes and plays the correct dual-tone signal for each key in real time. Displays both the time-domain waveform and the FFT frequency spectrum on keypress.

![GUI Preview](figures/active%20program.png)

---

## Setup

```bash
git clone https://github.com/mustafa-akgul/signal_system_H1.git
cd signal_system_H1
pip install numpy matplotlib sounddevice
```

```bash
python task1.py   # Signal sampling & visualization
python task2.py   # DTMF interactive GUI
```

---

## Group Members

| Name | Student ID |
|------|-----------|
| Mustafa Talha Akgül | 230611043 |
| Ahmet Akın | 230611038 |
| Berivan Demir | 230611038 |
