<a name="_e8l72fvkn31n"></a>**COE 216 \
SIGNALS AND SYSTEMS**
======================================
# <a name="_99ve033wqgjy"></a>**2025-2026 SPRING SEMESTER**
#
# <a name="_1wpn4uz0tyoc"></a><a name="_hqt5xe7i3gth"></a>**Homework 1**
# **This assignment defines two tasks.**
#
# <a name="_kz4egf62wj62"></a>**TASK 1: Sampling and Visualization of Sinusoidal Signals**
### <a name="_6cvplo7tuoiu"></a>**1. Assignment Format and Groups**
- This assignment will be done in groups **of 3** (or 2).
- **Submission Format:** Save your report as **HW\_1\_GROUP#.pdf . ( Replace the # symbol with the group number)**
- **Submission Channel:** The assignment will be uploaded via the BLACKBOARD system.
- **Code Sharing:** Code should be shared via GitHub, and the relevant repository link should be included in the report. A single report and a single code repository (GitHub) will be created for each group.
### <a name="_jswqv0pdp4pf"></a>**2. Parameter Determination**
Each group will determine its own baseline frequency <b>(f0 <sub>)</sub> based</b> on the school numbers of the students in the group:

- **Method:** Take the last two digits of each student's school number (as a two-digit number) and add those digits together.
- **Example:**
  - Student 1 (No: ... **21** ): 21
  - Student 2 (No: ... **05** ): 05
  - Student 3 (No: ... **14** ): 14

<b>f <sub>0</sub> Value:</b> 21 + 5 + 14 = 40 Hz
###
### <a name="_6h1s787esv4e"></a><a name="_kly7mkmsn4ic"></a>**3. Application and Graphics Requirements**
calculated <b>(f<sub>0</sub>) value</b> , generate the signal at the following three different frequencies:

1. **f1 = f0**
1. **f2 = f0 / 2**
1. **f3 = 10 \* f0**

**Technical Regulations:**

- **Visualization:** The three signals should be displayed in three separate subplots , one below the other, within the same window .
- **Time Window:** Each graph should display **at least 3 full periods of its signal** . (Tip: The time axis of the graphs should be dynamically adjusted according to the frequency value).
- The signal obtained by sum of three signals should be shown in a separate graph
- **Sampling and Nyquist:** To ensure accurate representation of signals in a computer environment, select your sampling frequency according to the Nyquist criterion. Specifically, to avoid distortion in signals with frequencies **f3 = 10 \* f0, justify your chosen sampling frequency value in the report.**
### <a name="_lhnilps41hff"></a>**4. Reporting**
**Your report should consist of the following sections:**

1. **Cover:** Information about the group members
1. **Method:** Your choice of sampling frequency and explanation of Nyquist's theorem.
1. **Graphs:** Screenshots of the 3 graphs obtained.
1. **GitHub Link:** The link to your active repository where your code is located.
1. **REFERENCES:** List the tools/resources you used while completing this assignment (AI tools, internet resources, books, etc. used should be listed here).
1. **DIVISION OF LABOR:** The contributions each team member makes while completing this assignment (coding, report writing, mathematical calculations, etc.)

**should be stated briefly and clearly in separate paragraphs** .


### <a name="_p7fr6v7bbjvn"></a>**Important Reminder:**
The main objective of this assignment is for you to practically see that analog signals can only be represented digitally on a computer by sampling , and to understand the importance of sampling frequency in this process.


**
# **TASK 2:**
# **DTMF (Dual-Tone Multi-Frequency) Signal Synthesis and Interactive Interface Design**
### **1. Purpose of the Assignment**
The aim of this assignment is to understand how sinusoidal signals are combined to create meaningful information (telephone keypad tones), to apply the principle of signal acquisition, and to gain skills in developing user-interactive (GUI/Web) software.
### **2. What is DTMF? (Short Research Assignment)**
DTMF is a system where each key on a telephone keypad represents the sum of two different sinusoidal signals, one from a "low" and the other from a "high" frequency group ( <i>x(t) = sin(2pi f <sub>low</sub> t) + sin(2pi f <sub>high</sub> t)</i> ). Your reports are expected to include the standard DTMF frequency table (row and column frequencies).
### **3. Application Requirements**
Students will develop software with the following features:

- **Platform Selection:** Code should be developed using **Python** (with Tkinter, PyQt, or CustomTkinter libraries) or **modern web technologies** (HTML/JS - using the Web Audio API).
- **Interactive Interface:** A phone keypad (numpad) design should be created where the user can see and click the 0-9, \*, #, A, B, C, D keys.
- **Signal Generation and Graphics:**  When a key is pressed, the two frequencies specific to that key should be added together to generate the corresponding signal.
  - The generated signal should be visualized in real-time in a graphical window (in the time domain).
- **Sound Synthesis:** The generated DTMF signal should be clearly audible from the computer's speakers.
### **4. Reporting**
### The report should include the following headings:
1. **Cover:** Group members' full names and student numbers.
1. **Mathematical Model:** DTMF frequency table and rationale for choosing the sampling frequency used.
1. **Screenshots:** A graph of the developed interface and a sample signal generated when a key is pressed.
1. **GitHub Link:** The active link containing the code (and installation instructions, if needed).
1. **REFERENCES:** List the tools/resources you used while completing this assignment (AI tools used, internet resources, library documents, books, etc.).
1. **DIVISION OF LABOR:** Each team member's contributions (interface design, mathematical modeling, audio engine coding, etc.) should be briefly and clearly described in separate paragraphs.

### **5. TIPS FOR SOUND PRODUCTION**
When generating DTMF signals digitally and transmitting them to the loudspeaker, the following technical details should be considered:
#### <b>A. Sampling Frequency (f <sub>s</sub>) and Duration</b>
For digital audio production, a standard sampling rate should be selected (f <sub>s</sub> = 8000 or 44100 Hz). A T value of approximately **0.2 - 0.5 seconds** per keypress is sufficient.

- Sample size calculation: N = f <sub>s</sub> \* T
#### **B. Steps for Those Using Python**
In Python, sound generation is typically done by creating a NumPy array and sending it to a sound library:

1. **Signal Generation:** Two separate frequencies are generated and added together using the numpy.sin() function.
1. **Normalization:** The amplitude of the collected signal can be increased to 2 (1+1). To avoid "clipping" (hissing/distortion) on the sound card, you need to normalize the signal to the [-1, 1] range or multiply the amplitude by 0.5.
1. **Libraries:** sounddevice: This is the most common and stable one. It is played using the `sd.play(signal, fs)` command.
   1. scipy.io.wavfile: if you want to save the signal you generate as a .wav file.
#### **C. Steps for those using the Web (JavaScript)**
Those developing a browser-based application can use **the Web Audio API** . For voice synthesis, they can examine the Web Audio API (OscillatorNode), and for graphics, the Canvas API or Chart.js libraries.

1. **AudioContext:** An AudioContext object is created for audio processing.
1. **Oscillator Nodes:** Two oscillator nodes are created for each key (one for low frequency, one for high frequency).
1. **Gain Node:** To control the sound level and prevent sudden cuts and clicking noises, the output must be connected via a Gain Node.
#### **D. Spectrum Observation (Optional/Plus Points)**
Showing both the time-domain graph of the signal you generated and its frequency-domain counterpart (using the Fast Fourier Transform) will greatly assist in proving the accuracy of the assignment (the existence of two dominant frequencies).
### <a name="_wycm66n7m3d5"></a><a name="_1mn84tugzvi"></a>**Homework/Report Submission Rules**
Name your report as **HW\_1\_GROUP#.pdf** and upload it via **Blackboard** . (You will use your Group number **instead of the # symbol** ).
