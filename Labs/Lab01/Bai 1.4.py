from datetime import datetime
class DateHandler:
    def format_date(date):
        return date.strftime("%d/%m/%Y")
    def get_days_between(date1, date2):
        d_betw = date2 - date1
        return d_betw.days

start_date = datetime(2010,9,15)
end_date = datetime(2023,7,1)
print("Start:\t\t\t", DateHandler.format_date(start_date))
print("End:\t\t\t", DateHandler.format_date(end_date))
print("Days between:\t", DateHandler.get_days_between(start_date, end_date))