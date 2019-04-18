import re
from app.Top_Stats.Get_Class_Schedule_URL import get_term_url
from app.Top_Stats.Get_Departments import value

from datetime import datetime

url = get_term_url(datetime.today())
print(url)

results = value(url)

for item in results.values():
    for classes in item:
        if classes != "[CROSSLISTED COURSES]":
            print(classes.replace("-", " "))

