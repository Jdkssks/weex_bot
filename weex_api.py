import requests

BASE_URL = "https://api-contract.weex.com/capi/v2/"

def get_all_contracts():
    try:
        r = requests.get(f"{BASE_URL}market/contracts", timeout=10)
        data = r.json().get("data", [])
        return [item["symbol"] for item in data]
    except Exception as e:
        print("get_all_contracts error:", e)
        return []

def get_position_leverage(api_key, api_secret, symbol):
    headers = {"API-KEY": api_key, "API-SECRET": api_secret}
    try:
        r = requests.get(f"{BASE_URL}position/leverage", headers=headers, timeout=10)
        return r.json()
    except Exception as e:
        print(f"get_position_leverage error ({symbol}):", e)
        return {}