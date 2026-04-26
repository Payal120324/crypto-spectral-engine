import numpy as np

def spectral_entropy(power_spectrum):
    """
    power_spectrum: 1D array (use positive freqs only)
    returns: entropy value (float)
    """
    ps = np.array(power_spectrum, dtype=float)

    # keep positive values only
    ps = np.abs(ps)
    total = ps.sum()

    if total == 0:
        return 0.0

    # normalize to probability distribution
    p = ps / total

    # avoid log(0)
    p = p + 1e-12

    entropy = -np.sum(p * np.log(p))
    return entropy