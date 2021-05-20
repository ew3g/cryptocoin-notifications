from datetime import datetime, timezone
import pytz

def get_now_datetime_formatted(desired_timezone, format):
    now_utc_time = datetime.now(timezone.utc)
    default_timezone = pytz.timezone(desired_timezone)
    return now_utc_time.astimezone(default_timezone).strftime(format)