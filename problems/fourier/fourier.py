# All import modules are declared here
# ----------------------------------------
# pandas - for manipulating excel sheets
# scipy - for Fourier transform, to store the generated audio file
# matplotlib - for visualizing the waveforms
# numpy - for Fourier transform, signal generation, etc.
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.io.wavfile import write
from scipy.fft import fft, fftfreq

# Reads the data frame from the excel sheet from local directory.
df = pd.read_excel('sample.xlsx')
print(df)

# Signal Parameters
SIGNAL_FREQ = 2 # Hertz (Hz)
SAMPLE_RATE = 44100 # Hertz (Hz)
DURATION = 5 # Seconds

# Noise Characteristics
NOISE_POWER_REDUCTION = 0.3 #au

# Normaliztion Parameters
SINT16BIT_MAX_P = 32767

# Defining Sine wave generation function
def generate_sine_wave(freq, sample_rate, duration) :

    # X axis definition
    x_axis = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x_axis * freq

    # Y axis definition
    # 2 pi because np.sin takes in radians.
    y_axis = np.sin((2 * np.pi) * frequencies)

    return x_axis, y_axis


# Generating the actual sine wave
x, y = generate_sine_wave(SIGNAL_FREQ, SAMPLE_RATE, DURATION)
#plt.plot(x, y)
#plt.show()

# Mixing audio signals
_, nice_tone = generate_sine_wave(400, SAMPLE_RATE, DURATION) # Medium pitch sound
_, noise_tone = generate_sine_wave(4000, SAMPLE_RATE, DURATION) # High pitch sound
noise_tone = noise_tone * NOISE_POWER_REDUCTION

mixed_signal = nice_tone + noise_tone

# Normalization
normalized_tone = np.int16((mixed_signal / mixed_signal.max()) * SINT16BIT_MAX_P)
plt.plot(normalized_tone[:1000])
plt.show()

# To store the generated audio file
write("sample_audio.wav", SAMPLE_RATE, normalized_tone)

# Fast Fourier Transform
N = SAMPLE_RATE * DURATION

yf = fft(normalized_tone)
xf = fftfreq(N, 1 / SAMPLE_RATE)

plt.plot(xf, np.abs(yf))
plt.show()
