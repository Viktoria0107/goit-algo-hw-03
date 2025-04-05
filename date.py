from datetime import datetime

def get_days_from_today(date):
    try:
        date_new = datetime.strptime(date, "%Y.%m.%d").date()
        date_now = datetime.today().date()
        days = date_now - date_new
        return days
    except ValueError:
        raise ValueError("Format is expected YYYY.MM.DD")

# print(get_days_from_today("2025.04.21"))        
# print(get_days_from_today("2025.03.27"))  
print(get_days_from_today("20.02.2025"))  
