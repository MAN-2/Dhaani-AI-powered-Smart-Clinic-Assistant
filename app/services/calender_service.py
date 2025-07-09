import os
from datetime import datetime, timedelta
import pytz
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
env_path = os.path.join(os.path.dirname(__file__), os.pardir, ".env")
load_dotenv(dotenv_path=env_path)

def get_calendar_service():
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON")  # Your JSON key path

    credentials = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    return build('calendar', 'v3', credentials=credentials)
# Google Calendar API scope
SCOPES = ['https://www.googleapis.com/auth/calendar']

SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(__file__), '..', 'credentials.json') #path to credential json


def add_event_to_calendar(doctor_name: str, patient_email: str, reason: str, date: str, time: str) -> str:
    try:
        service = get_calendar_service()

        tz = pytz.timezone("Asia/Kolkata")
        start_dt = tz.localize(datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M"))
        end_dt = start_dt + timedelta(hours=1)

        event = {
            'summary': f'Appointment with Dr. {doctor_name}',
            'description': reason,
            'start': {
                'dateTime': start_dt.isoformat(),
                'timeZone': 'Asia/Kolkata',
            },
            'end': {
                'dateTime': end_dt.isoformat(),
                'timeZone': 'Asia/Kolkata',
            },
        }

        created_event = service.events().insert(calendarId='primary', body=event).execute()

        # Fallback to  Google Calendar "event viewer" URL manually
        start_fmt = start_dt.strftime("%Y%m%dT%H%M%S")
        end_fmt = end_dt.strftime("%Y%m%dT%H%M%S")

        calendar_url = (
            "https://calendar.google.com/calendar/render"
            f"?action=TEMPLATE"
            f"&text=Appointment+with+Dr.+{doctor_name.replace(' ', '+')}"
            f"&details={reason.replace(' ', '+')}"
            f"&dates={start_fmt}/{end_fmt}"
            f"&ctz=Asia/Kolkata"
        )

        return calendar_url

    except Exception as e:
        return f"❌ Failed to add to calendar: {e}"
