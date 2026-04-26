import matplotlib.pyplot as plt

def plot_spectrum(freqs, power):
    plt.figure(figsize=(10, 5))
    
    half = len(freqs) // 2
    freqs = freqs[1:half]
    power = power[1:half]

    plt.plot(freqs, power)
    
    plt.yscale('log')   
    
    plt.title("Frequency Spectrum")
    plt.xlabel("Frequency")
    plt.ylabel("Power")
    
    plt.grid()
    plt.show()