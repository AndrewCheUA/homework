import sys

def get_birthdays_per_week(users):
    from datetime import datetime, timedelta
    from collections import defaultdict
    current_date = datetime.today()

    last_monday = current_date - timedelta(days=current_date.weekday())
    current_week = defaultdict(list)
    for item in users:
        for x,y in item.items():
            if isinstance(y,datetime):
                x = y.date() - last_monday.date()
                if x.days < 6 and x.days > 0:
                    name = item.get("name")
                    birthdate = item.get("birthday")
                    current_week[birthdate.strftime('%A')].append(name)
                elif x.days < 0 and x.days > -3:
                    name = item.get("name")
                    name = item.get("name")
                    current_week[last_monday.strftime('%A')].append(name)
                    

    for day in current_week:
        names = current_week.get(day)
        n_list = ", ".join(names)
        print(f"{day}: {n_list}")
        
if __name__ == "__main__":
    users = sys.argv[1]
    get_birthdays_per_week(users)