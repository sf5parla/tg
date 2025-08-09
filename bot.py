import requests
import time
from telegram import Bot

# --- CONFIG ---
API_KEY = "b950fd33e3766ea52609"  # AdbluMedia public API key
BOT_TOKEN = "8428599112:AAH_wE0fRWO519IuhQTjfsm8TPIXwS9P2NM"
CHAT_ID = "YOUR_TELEGRAM_USER_ID"  # Get from @userinfobot in Telegram
API_URL = f"https://api.adblumedia.com/v1/leads?api_key={API_KEY}"  # Change if needed

bot = Bot(token=BOT_TOKEN)
last_lead_id = None

def get_leads():
    try:
        r = requests.get(API_URL, timeout=10)
        if r.status_code == 200:
            return r.json()
    except Exception as e:
        print("Error:", e)
    return []

while True:
    leads = get_leads()
    if leads:
        newest = leads[0]  # Assuming latest lead is first
        if last_lead_id != newest.get("lead_id"):
            last_lead_id = newest.get("lead_id")
            msg = (
                f"🎯 *New Lead!*\n"
                f"Offer: {newest.get('offer', 'Unknown')}\n"
                f"Status: {newest.get('status', 'N/A')}\n"
                f"Payout: ${newest.get('payout', 0)}\n"
                f"Date: {newest.get('date', 'N/A')}"
            )
            bot.send_message(chat_id=CHAT_ID, text=msg, parse_mode="Markdown")
    time.sleep(60)  # Check every 60 sec
