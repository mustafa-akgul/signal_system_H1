import numpy as np
import matplotlib.pyplot as plt

def main():
    # f0: sum of last two digits of each group member's student ID (30+38+43)
    f0 = 111  # Hz
    f1 = f0        # 111 Hz
    f2 = f0 / 2    # 55.5 Hz
    f3 = 10 * f0   # 1110 Hz

    # fs > 2 * f_max = 2 * 1110 = 2220 Hz (Nyquist)
    fs = 44100  # Hz

    # Time vectors — 4 periods each
    t1 = np.arange(0, 4 * (1/f1), 1/fs)
    t2 = np.arange(0, 4 * (1/f2), 1/fs)
    t3 = np.arange(0, 4 * (1/f3), 1/fs)

    y1 = np.sin(2 * np.pi * f1 * t1)
    y2 = np.sin(2 * np.pi * f2 * t2)
    y3 = np.sin(2 * np.pi * f3 * t3)

    # Figure 1: Individual signals
    plt.figure(figsize=(10, 8))
    plt.subplots_adjust(hspace=0.5)

    plt.subplot(3, 1, 1)
    plt.plot(t1, y1)
    plt.title(f'Signal 1: f1 = {f1} Hz')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    plt.subplot(3, 1, 2)
    plt.plot(t2, y2, color='orange')
    plt.title(f'Signal 2: f2 = {f2} Hz')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    plt.subplot(3, 1, 3)
    plt.plot(t3, y3, color='green')
    plt.title(f'Signal 3: f3 = {f3} Hz')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    # Figure 2: Combined signal (duration of slowest signal f2)
    t_sum = np.arange(0, 4 * (1/f2), 1/fs)
    y_sum = (np.sin(2 * np.pi * f1 * t_sum) +
             np.sin(2 * np.pi * f2 * t_sum) +
             np.sin(2 * np.pi * f3 * t_sum))

    plt.figure(figsize=(10, 4))
    plt.plot(t_sum, y_sum, color='red')
    plt.title('Combined Signal: f1 + f2 + f3')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    plt.show()

if __name__ == "__main__":
    main()
