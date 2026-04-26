def generate_signals(regimes):
    signals = []

    for r in regimes:
        if r == 1:
            signals.append("SELL / AVOID")  
        else:
            signals.append("BUY / HOLD")    

    return signals
