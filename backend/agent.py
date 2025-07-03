from dotenv import load_dotenv
import os
import re
from datetime import datetime, timedelta
import google.generativeai as genai
from calender_tools import get_available_slots, book_slot

#  Load environment variables
load_dotenv()

#  Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

#  Extract ISO date from text (supports 'today' and 'tomorrow')
def extract_date(text):
    text = text.lower()
    today = datetime.now().date()

    if "today" in text:
        return today.strftime("%Y-%m-%d")
    elif "tomorrow" in text:
        return (today + timedelta(days=1)).strftime("%Y-%m-%d")

    match = re.search(r"\d{4}-\d{2}-\d{2}", text)
    return match.group() if match else None

#  Extract hour from time string like "4PM"
def extract_time(text):
    match = re.search(r"(\d{1,2})\s*(am|pm)", text.lower())
    if match:
        hour = int(match.group(1))
        if "pm" in match.group(2) and hour != 12:
            hour += 12
        return hour
    return None

#  Extract reason like "for onboarding"
def extract_reason(text):
    if "for" in text.lower():
        return text.split("for")[-1].strip()
    return "General Meeting"

#  Main agent handler
def run_agent(message: str) -> str:
    message_lower = message.lower()

    if "availability" in message_lower or "available" in message_lower or "free" in message_lower:
        date = extract_date(message)
        if date:
            slots = get_available_slots(date)
            if slots:
                return f"🗓 Available slots on {date}: {', '.join(slots)}"
            else:
                return f" No slots available on {date}."
        else:
            return " Please mention the date in YYYY-MM-DD format, or use 'today' or 'tomorrow'."

    elif "book" in message_lower or "schedule" in message_lower:
        date = extract_date(message)
        hour = extract_time(message)
        reason = extract_reason(message)

        if not date or hour is None:
            return " Please provide both a valid date (YYYY-MM-DD, or 'tomorrow') and time (e.g. 3PM)."

        return book_slot(date, hour, reason)

    # Fallback to Gemini Chat
    try:
        chat = model.start_chat()
        response = chat.send_message(message)
        return f" Gemini says:\n\n{response.text}"
    except Exception as e:
        return (
        "I'm here to help with booking appointments. "
        "If you have general questions, I might not always respond accurately. "
        "Try asking about calendar availability or scheduling a meeting!"
    )
