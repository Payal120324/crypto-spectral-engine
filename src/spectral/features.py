import numpy as np

def extract_features(freqs, power):
    half = len(freqs) // 2
    
    freqs = freqs[1:half]
    power = power[1:half]

    dominant_freq = freqs[np.argmax(power)]
    
    max_power = np.max(power)
    
    mean_power = np.mean(power)
    
    energy = np.sum(power)

    return {
    "dominant_frequency": float(dominant_freq),
    "max_power": float(max_power),
    "mean_power": float(mean_power),
    "energy": float(energy)

    }