import matplotlib.pyplot as plt

def plot_wavelet(coeffs):
    plt.figure(figsize=(10, 6))
    
    plt.imshow(coeffs, aspect='auto', origin='lower', cmap='viridis')
    
    plt.title("Wavelet Transform")
    plt.xlabel("Time")
    plt.ylabel("Scale")
    
    plt.colorbar(label="Magnitude")
    plt.show()