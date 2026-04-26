import numpy as np

def spectral_entropy(power_spectrum):
    """
    power_spectrum: 1D array (use positive freqs only)
    returns: entropy value (float)
    """
    ps = np.array(power_spectrum, dtype=float)

    
    ps = np.abs(ps)
    total = ps.sum()

    if total == 0:
        return 0.0

    
    p = ps / total

   
    p = p + 1e-12

    entropy = -np.sum(p * np.log(p))
    return entropy
