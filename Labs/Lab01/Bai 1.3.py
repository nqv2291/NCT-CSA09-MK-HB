from datetime import datetime
now = datetime.now()
class Customdate:
    def get_date(dt):
        return dt.strftime("%d/%m/%Y")
    def get_time(dt):
        return dt.strftime("%H:%M:%S")

print(Customdate.get_date(now))
print(Customdate.get_time(now))