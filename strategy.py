# ----------------- 指標函數 -----------------
def moving_average(prices, period=5):
    if len(prices) < period:
        return sum(prices) / len(prices)
    return sum(prices[-period:]) / period

def rsi(prices, period=14):
    gains = 0
    losses = 0
    for i in range(1, len(prices)):
        diff = prices[i] - prices[i-1]
        if diff > 0:
            gains += diff
        else:
            losses -= diff
    rs = gains / (losses + 1e-6)
    return 100 - (100 / (1 + rs))

# ----------------- 交易策略 -----------------
def moving_average_strategy(prices, period=5):
    ma = moving_average(prices, period)
    latest = prices[-1]
    return "BUY" if latest > ma else "SELL"

def rsi_strategy(prices, period=14):
    val = rsi(prices, period)
    if val > 70:
        return "SELL"
    elif val < 30:
        return "BUY"
    return "HOLD"

def breakout_strategy(prices, period=5):
    recent_high = max(prices[-period:])
    recent_low = min(prices[-period:])
    latest = prices[-1]
    if latest > recent_high:
        return "BUY"
    elif latest < recent_low:
        return "SELL"
    return "HOLD"

def combined_strategy(prices):
    strategies = [
        moving_average_strategy,
        rsi_strategy,
        breakout_strategy
    ]
    signals = [strat(prices) for strat in strategies]
    if signals.count("BUY") > signals.count("SELL"):
        return "BUY"
    elif signals.count("SELL") > signals.count("BUY"):
        return "SELL"
    return "HOLD"