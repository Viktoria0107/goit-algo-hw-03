from datetime import datetime

def get_days_from_today(date):
    try:
        date_new = datetime.strptime(date, "%Y.%m.%d").date()
        date_now = datetime.today().date()
        days = date_now - date_new
        return days
    except ValueError:
        raise ValueError("Format is expected YYYY.MM.DD")

