import numpy as np

def compute_rsi(price, period=14):
    delta = np.diff(price)

    gain = np.maximum(delta, 0)
    loss = -np.minimum(delta, 0)

    avg_gain = np.convolve(gain, np.ones(period)/period, mode='same')
    avg_loss = np.convolve(loss, np.ones(period)/period, mode='same')

    rs = avg_gain / (avg_loss + 1e-8)
    rsi = 100 - (100 / (1 + rs))

    return rsi


def backtest_strategy(price, regimes, cost=0.0005):

    price = np.array(price)
    returns = np.diff(price) / price[:-1]

    regimes = regimes[-len(returns):]

    
    rsi = compute_rsi(price)

    position = 0
    equity = [1]
    trades = []

    cooldown = 30
    last_trade = -cooldown

    for i in range(50, len(returns)):

        # cooldown
        if i - last_trade < cooldown:
            if position == 1:
                equity.append(equity[-1] * (1 + returns[i] - cost))
            else:
                equity.append(equity[-1])
            continue

        # regime change
        if regimes[i] != regimes[i-1]:

           
            if regimes[i] == 1 and rsi[i] < 40 and position == 0:
                position = 1
                trades.append(("BUY", i))
                last_trade = i

           
            elif position == 1 and (rsi[i] > 60 or regimes[i] == 0):
                position = 0
                trades.append(("SELL", i))
                last_trade = i

        
        if position == 1:
            equity.append(equity[-1] * (1 + returns[i] - cost))
        else:
            equity.append(equity[-1])

    total_return = (equity[-1] - 1) * 100

    return equity, trades, total_return
