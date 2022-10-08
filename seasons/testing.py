import re
from datetime import date

today = date(2025, 1, 1)

num = "2024-01-01"
if re.search(r"^(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$", num):

    year, mm, dd = num.split("-")
    dob = date(int(year), int(mm), int(dd))
    time = abs(dob - today)
    print(time.days)

else:
    raise ValueError