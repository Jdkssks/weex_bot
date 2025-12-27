def check_margin(balance, used_margin, max_ratio):
    if used_margin / balance > max_ratio:
        print("⚠️ 超過最大保證金比例，暫停開倉")
        return False
    return True

def check_leverage(leverage, max_leverage):
    if leverage > max_leverage:
        print(f"⚠️ 槓桿 {leverage} 超過上限 {max_leverage}")
        return False
    return True