import numpy as np

def compute_fft(signal):
    fft_vals = np.fft.fft(signal)
    power = np.abs(fft_vals) ** 2
    freqs = np.fft.fftfreq(len(signal))
    
    return freqs, power