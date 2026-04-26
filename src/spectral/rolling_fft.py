import numpy as np

def rolling_fft(signal, window_size=256):
    spectrogram = []

    for i in range(window_size, len(signal)):
        segment = signal[i-window_size:i]
        
        fft_vals = np.fft.fft(segment)
        power = np.log(np.abs(fft_vals) ** 2 + 1)
        
        spectrogram.append(power[:window_size//2])

    return np.array(spectrogram)