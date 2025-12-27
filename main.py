import time
from config import API_KEY, API_SECRET, MAX_LEVERAGE, MAX_MARGIN_RATIO
from weex_api import get_all_contracts
from strategy import combined_strategy
from risk import check_margin, check_leverage

def main_loop():
    symbols = get_all_contracts()
    if not symbols:
        print("⚠️ 無法取得交易對")
        return

    # 範例歷史價格
    prices_dict = {symbol: [100, 101, 102, 99, 100] for symbol in symbols}

    while True:
        for symbol in symbols:
            try:
                action = combined_strategy(prices_dict[symbol])
                print(f"[{symbol}] 策略建議: {action}")

                balance = 1000
                used_margin = 400
                if not check_margin(balance, used_margin, MAX_MARGIN_RATIO):
                    continue

                leverage = 50
                if not check_leverage(leverage, MAX_LEVERAGE):
                    continue

                print(f"[{symbol}] 執行 {action} 合約交易")

            except Exception as e:
                print(f"[{symbol}] 主循環錯誤:", e)

        time.sleep(30)

if __name__ == "__main__":
    print("🔹 Weex Bot Worker 已啟動 (多策略 + 所有交易對)")
    main_loop()