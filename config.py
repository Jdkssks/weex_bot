import os

API_KEY = os.environ.get("API_KEY")
API_SECRET = os.environ.get("API_SECRET")

if not API_KEY or not API_SECRET:
    raise ValueError("請先在 Render Environment Variables 設定 API_KEY / API_SECRET")

MAX_LEVERAGE = int(os.environ.get("MAX_LEVERAGE", 100))
MAX_MARGIN_RATIO = float(os.environ.get("MAX_MARGIN_RATIO", 0.5))