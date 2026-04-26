from src.data.loader import load_data
from src.preprocessing.smoothing import smooth_price
from src.spectral.fft import compute_fft
from src.spectral.rolling_fft import rolling_fft
from src.spectral.wavelet import compute_wavelet
from src.spectral.entropy import spectral_entropy
from src.spectral.features import extract_features
from src.analysis.regime_detection import detect_regimes

from src.visualization.spectrum_plot import plot_spectrum
from src.visualization.spectrogram import plot_spectrogram
from src.visualization.wavelet_plot import plot_wavelet
from src.visualization.regime_plot import plot_regimes
from src.visualization.price_regime_plot import plot_price_with_regimes
from src.analysis.trading_signal import generate_signals
from src.visualization.trading_plot import plot_trading_signals

df = load_data("data/btc.csv")
df = smooth_price(df)

signal = df['Smoothed'].dropna().values

signal = signal - signal.mean()
signal = signal / signal.std()


freqs, power = compute_fft(signal)
plot_spectrum(freqs, power)


spec = rolling_fft(signal)
plot_spectrogram(spec)


coeffs = compute_wavelet(signal)
plot_wavelet(coeffs)


half = len(power) // 2
entropy = spectral_entropy(power[1:half])
print("\nEntropy:", entropy)

features = extract_features(freqs, power)

print("\n--- Extracted Features ---")
print(f"Dominant Frequency: {features['dominant_frequency']:.6f}")
print(f"Approx Period: {1 / features['dominant_frequency']:.2f} samples")
print(f"Max Power: {features['max_power']:.2e}")
print(f"Mean Power: {features['mean_power']:.2e}")
print(f"Total Energy: {features['energy']:.2e}")


dom_freqs, regimes = detect_regimes(signal)


filtered = []
gap = 80
last = -gap

for i, r in enumerate(regimes):
    if r == 1 and (i - last) > gap:
        filtered.append(1)
        last = i
    else:
        filtered.append(0)


plot_regimes(dom_freqs, filtered_regimes)

plot_price_with_regimes(df, filtered_regimes)

signals = generate_signals(filtered_regimes)

print("\nLast 10 Signals:")
print(signals[-10:])

plot_trading_signals(df, filtered_regimes)