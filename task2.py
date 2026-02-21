import tkinter as tk
from tkinter import ttk
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DTMFApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Group Assignment - DTMF Signal Generator")

        # DTMF frequency table: key -> (row_freq, col_freq)
        self.dtmf_freqs = {
            '1': (697, 1209), '2': (697, 1336), '3': (697, 1477), 'A': (697, 1633),
            '4': (770, 1209), '5': (770, 1336), '6': (770, 1477), 'B': (770, 1633),
            '7': (852, 1209), '8': (852, 1336), '9': (852, 1477), 'C': (852, 1633),
            '*': (941, 1209), '0': (941, 1336), '#': (941, 1477), 'D': (941, 1633)
        }

        self.fs = 44100   # sampling frequency (Hz)
        self.duration = 0.5  # seconds per keypress

        self.create_interface()

    def create_interface(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky="nsew")

        # Left: keypad
        keypad_frame = ttk.LabelFrame(main_frame, text="Telephone Keypad", padding="10")
        keypad_frame.grid(row=0, column=0, padx=10, sticky="n")

        keys = [
            ['1', '2', '3', 'A'],
            ['4', '5', '6', 'B'],
            ['7', '8', '9', 'C'],
            ['*', '0', '#', 'D']
        ]

        for r, row_keys in enumerate(keys):
            for c, key in enumerate(row_keys):
                btn = ttk.Button(keypad_frame, text=key, width=5,
                                 command=lambda k=key: self.play_tone(k))
                btn.grid(row=r, column=c, padx=5, pady=5)

        # Right: signal graphs (time domain + FFT)
        graph_frame = ttk.LabelFrame(main_frame, text="Signal Graph (Time + Frequency Domain)", padding="10")
        graph_frame.grid(row=0, column=1, padx=10, sticky="nsew")

        self.fig, (self.ax, self.ax_fft) = plt.subplots(2, 1, figsize=(6, 6))

        self.ax.set_title("Press a key...")
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel("Amplitude")
        self.ax.grid(True)

        self.ax_fft.set_title("FFT Spectrum")
        self.ax_fft.set_xlabel("Frequency (Hz)")
        self.ax_fft.set_ylabel("Amplitude")
        self.ax_fft.grid(True)

        self.fig.tight_layout(pad=2.0)

        self.canvas = FigureCanvasTkAgg(self.fig, master=graph_frame)
        self.canvas.get_tk_widget().pack()

    def generate_signal(self, f1, f2):
        t = np.linspace(0, self.duration, int(self.fs * self.duration), endpoint=False)
        signal = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)
        return t, signal * 0.5  # normalize to prevent clipping

    def play_tone(self, key):
        f1, f2 = self.dtmf_freqs[key]
        t, signal = self.generate_signal(f1, f2)

        sd.play(signal, self.fs)

        # Time-domain plot (first 20 ms)
        display_samples = int(0.02 * self.fs)
        self.ax.clear()
        self.ax.plot(t[:display_samples], signal[:display_samples], color='blue')
        self.ax.set_title(f"Key: {key} | {f1} Hz + {f2} Hz")
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel("Amplitude")
        self.ax.set_ylim(-1.5, 1.5)
        self.ax.grid(True)

        # FFT plot (0–2000 Hz)
        fft_vals = np.abs(np.fft.rfft(signal))
        fft_freqs = np.fft.rfftfreq(len(signal), d=1/self.fs)
        mask = fft_freqs <= 2000

        self.ax_fft.clear()
        self.ax_fft.plot(fft_freqs[mask], fft_vals[mask], color='red')
        self.ax_fft.axvline(x=f1, color='green', linestyle='--', linewidth=1.5, label=f'f_low = {f1} Hz')
        self.ax_fft.axvline(x=f2, color='orange', linestyle='--', linewidth=1.5, label=f'f_high = {f2} Hz')
        self.ax_fft.set_title(f"FFT Spectrum — Key: {key}")
        self.ax_fft.set_xlabel("Frequency (Hz)")
        self.ax_fft.set_ylabel("Amplitude")
        self.ax_fft.legend(fontsize=8)
        self.ax_fft.grid(True)

        self.fig.tight_layout(pad=2.0)
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = DTMFApp(root)

    def on_closing():
        sd.stop()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
