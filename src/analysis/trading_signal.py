def generate_signals(regimes):
    signals = []

    for r in regimes:
        if r == 1:
            signals.append("SELL / AVOID")   # volatile regime
        else:
            signals.append("BUY / HOLD")    # stable regime

    return signals