import datetime
import pytz
from google.oauth2 import service_account
from googleapiclient.discovery import build
import os
import json
import base64




SCOPES = ["https://www.googleapis.com/auth/calendar"]


# Set your calendar ID (usually your own Gmail or primary)
CALENDAR_ID = "puskaru202@gmail.com"  # or use full email if using a test calendar

#Load credentials from env var (no file needed)
encoded = os.getenv("GOOGLE_CREDS_BASE64")
if not encoded:
    raise RuntimeError("GOOGLE_CREDS_BASE64 env variable is missing.")

service_json = json.loads(base64.b64decode(encoded).decode("utf-8"))
credentials = service_account.Credentials.from_service_account_info(service_json, scopes=SCOPES)

service = build("calendar", "v3", credentials=credentials)


def get_available_slots(date_str):
    """Returns available hourly slots on a given day."""
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    start = date.replace(hour=9, minute=0)
    end = date.replace(hour=18, minute=0)

    start_iso = start.isoformat() + "Z"
    end_iso = end.isoformat() + "Z"

    events_result = service.events().list(
        calendarId=CALENDAR_ID,
        timeMin=start_iso,
        timeMax=end_iso,
        singleEvents=True,
        orderBy="startTime",
    ).execute()
    events = events_result.get("items", [])

    booked_hours = []
    for event in events:
        start_time = event["start"]["dateTime"]
        booked = datetime.datetime.fromisoformat(start_time[:-1]).hour
        booked_hours.append(booked)

    available = [f"{h}:00" for h in range(9, 18) if h not in booked_hours]
    return available


def book_slot(date_str, hour, reason):
    """Books an event on the calendar."""
    start_time = f"{date_str}T{hour:02}:00:00"
    end_time = f"{date_str}T{hour + 1:02}:00:00"

    event = {
        "summary": f"Meeting - {reason}",
        "start": {"dateTime": start_time, "timeZone": "Asia/Kolkata"},
        "end": {"dateTime": end_time, "timeZone": "Asia/Kolkata"},
    }

    created_event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
    return f" Your appointment is booked on {date_str} at {hour}:00 for '{reason}'."
