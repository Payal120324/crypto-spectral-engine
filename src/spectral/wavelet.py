import pywt
import numpy as np

def compute_wavelet(signal):
    scales = np.arange(1, 128)
    
    coeffs, freqs = pywt.cwt(signal, scales, 'morl')

    coeffs = np.abs(coeffs)

    coeffs = np.log(coeffs + 1)

    return coeffs