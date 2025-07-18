import pandas as pd
import pywhatkit
import datetime
import time

def send_common_message(excel_path, message):
    df = pd.read_excel(excel_path)

    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute + 2  # start 2 minutes later

    for index, row in df.iterrows():
        phone = f"+{row['Phone']}"

        # Handle time overflow
        if minute >= 60:
            minute -= 60
            hour = (hour + 1) % 24

        try:
            pywhatkit.sendwhatmsg(phone, message, hour, minute, wait_time=20, tab_close=True)
            print(f"Scheduled message to {phone} at {hour}:{minute}")
        except Exception as e:
            print(f"Error sending to {phone}: {e}")

        minute += 1  # Schedule next message 1 minute later

def send_personalized_messages(excel_path):
    df = pd.read_excel(excel_path)

    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute + 2  # start 2 minutes later

    for index, row in df.iterrows():
        phone = f"+{row['Phone']}"
        message = row['Message']

        # Handle time overflow
        if minute >= 60:
            minute -= 60
            hour = (hour + 1) % 24

        try:
            pywhatkit.sendwhatmsg(phone, message, hour, minute, wait_time=20, tab_close=True)
            print(f"Scheduled message to {phone} at {hour}:{minute}")
        except Exception as e:
            print(f"Error sending to {phone}: {e}")

        minute += 1  # Schedule next message 1 minute later
