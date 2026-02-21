# COE 216 — Signals and Systems
## Homework 1 Report

**Course:** COE 216 Signals and Systems
**Semester:** 2025–2026 Spring
**Group Number:** 1

---

## Cover

| Name | Student ID |
|------|-----------|
| [Ad Soyad 1] | [Öğrenci No 1] |
| [Ad Soyad 2] | [Öğrenci No 2] |
| [Ad Soyad 3] | [Öğrenci No 3] |

---

## 1. Method / Mathematical Model

### 1.1 Fundamental Frequency (f₀) Calculation

The fundamental frequency f₀ is computed by summing the last two digits of each group member's student ID:

```
f₀ = 30 + 38 + 43 = 111 Hz
```

The three signal frequencies used in Task 1 are therefore:

| Signal | Formula | Value |
|--------|---------|-------|
| f₁ | f₀ | 111 Hz |
| f₂ | f₀ / 2 | 55.5 Hz |
| f₃ | 10 × f₀ | 1110 Hz |

---

### 1.2 Nyquist Criterion — Task 1

The **Nyquist–Shannon Sampling Theorem** states that to reconstruct a bandlimited signal without aliasing, the sampling frequency must satisfy:

$$f_s > 2 \cdot f_{max}$$

The highest frequency component in Task 1 is f₃ = 1110 Hz. Therefore:

$$f_s > 2 \times 1110 = 2220 \text{ Hz}$$

We chose **f_s = 44100 Hz** (CD-quality audio), which greatly exceeds the minimum requirement:

$$44100 \gg 2220 \text{ Hz} \quad \checkmark$$

This choice ensures no aliasing occurs for any of the three signals (f₁, f₂, f₃).

---

### 1.3 Nyquist Criterion — Task 2 (DTMF)

Standard DTMF uses frequencies up to **1633 Hz** (the highest column frequency). Applying the Nyquist criterion:

$$f_s > 2 \times 1633 = 3266 \text{ Hz}$$

We again selected **f_s = 44100 Hz**, which satisfies the requirement by a factor of more than 13×:

$$44100 \gg 3266 \text{ Hz} \quad \checkmark$$

---

### 1.4 DTMF Frequency Table

DTMF (Dual-Tone Multi-Frequency) encoding represents each key as the sum of one **row frequency** and one **column frequency**:

|          | **1209 Hz** | **1336 Hz** | **1477 Hz** | **1633 Hz** |
|----------|:-----------:|:-----------:|:-----------:|:-----------:|
| **697 Hz** | 1 | 2 | 3 | A |
| **770 Hz** | 4 | 5 | 6 | B |
| **852 Hz** | 7 | 8 | 9 | C |
| **941 Hz** | * | 0 | # | D |

Each DTMF tone is generated as:

$$x(t) = \sin(2\pi f_{row} t) + \sin(2\pi f_{col} t)$$

The signal is normalized by a factor of 0.5 to prevent clipping:

$$x_{norm}(t) = 0.5 \cdot x(t)$$

---

## 2. Results and Screenshots

### 2.1 Task 1 — Individual Signal Subplots

> **[Screenshot placeholder]**
> *Figure 1: Three subplots showing f₁ = 111 Hz, f₂ = 55.5 Hz, and f₃ = 1110 Hz — each displaying at least 4 full periods.*

---

### 2.2 Task 1 — Combined Signal

> **[Screenshot placeholder]**
> *Figure 2: Sum of all three signals: x(t) = sin(2πf₁t) + sin(2πf₂t) + sin(2πf₃t)*

---

### 2.3 Task 2 — GUI Interface

> **[Screenshot placeholder]**
> *Figure 3: DTMF signal generator GUI showing the 4×4 telephone keypad (left) and the signal/FFT graph area (right).*

---

### 2.4 Task 2 — Time-Domain + FFT Spectrum (Key Press Example)

> **[Screenshot placeholder]**
> *Figure 4: Example pressing key "5" (770 Hz + 1336 Hz). Top: time-domain waveform (first 20 ms). Bottom: FFT spectrum showing two dominant peaks at 770 Hz and 1336 Hz.*

---

## 3. GitHub Repository

**Repository URL:** [https://github.com/[username]/HW_1_GROUP1](https://github.com/[username]/HW_1_GROUP1)

### Installation

```bash
# Clone the repository
git clone https://github.com/[username]/HW_1_GROUP1.git
cd HW_1_GROUP1

# Install dependencies
pip install numpy matplotlib sounddevice

# Run Task 1
python task1.py

# Run Task 2
python task2.py
```

---

## 4. References

1. Oppenheim, A. V., & Schafer, R. W. (2010). *Discrete-Time Signal Processing* (3rd ed.). Prentice Hall.
2. NumPy Documentation — `numpy.fft`: https://numpy.org/doc/stable/reference/routines.fft.html
3. Matplotlib Documentation: https://matplotlib.org/stable/contents.html
4. SoundDevice Documentation: https://python-sounddevice.readthedocs.io/
5. Tkinter Documentation (Python Standard Library): https://docs.python.org/3/library/tkinter.html
6. ITU-T Recommendation Q.23 — *Technical Features of Push-Button Telephone Sets* (DTMF standard)

> *Note: If AI tools (e.g., ChatGPT, Claude) were used during development, list them here.*

---

## 5. Division of Labor

**[Ad Soyad 1] — Student ID: [No]**
[Bu üyenin katkılarını buraya yazın. Örneğin: Task 1 sinyal üretimi ve grafik kodlaması, Nyquist hesaplamalarının doğrulanması.]

**[Ad Soyad 2] — Student ID: [No]**
[Bu üyenin katkılarını buraya yazın. Örneğin: Task 2 DTMF GUI implementasyonu, ses çalma entegrasyonu, FFT eklentisi.]

**[Ad Soyad 3] — Student ID: [No]**
[Bu üyenin katkılarını buraya yazın. Örneğin: Rapor yazımı, matematiksel model bölümü, GitHub deposu oluşturma ve yönetimi.]
