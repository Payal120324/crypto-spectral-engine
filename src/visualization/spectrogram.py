import matplotlib.pyplot as plt
import numpy as np

def plot_spectrogram(spec):
    plt.figure(figsize=(10, 6))
    
    plt.imshow(spec.T, aspect='auto', origin='lower', cmap='viridis')
    plt.clim(vmin=np.percentile(spec, 5), vmax=np.percentile(spec, 95))
    
    plt.title("Spectrogram (Rolling FFT)")
    plt.xlabel("Time")
    plt.ylabel("Frequency")
    
    plt.colorbar(label="Power")
    plt.show()