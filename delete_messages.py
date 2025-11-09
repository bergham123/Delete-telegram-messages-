import os
import requests
import time

# --- CONFIGURATION ---
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Set your message ID range
START_ID = 200
END_ID = 250

url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/deleteMessage"

for msg_id in range(START_ID, END_ID + 1):
    params = {"chat_id": TELEGRAM_CHAT_ID, "message_id": msg_id}
    response = requests.post(url, params=params)

    if response.ok:
        print(f"✅ Deleted message {msg_id}")
    else:
        print(f"❌ Failed to delete {msg_id}: {response.text}")

    time.sleep(0.5)  # avoid hitting Telegram rate limits
