import datetime

date_current = datetime.datetime.now()

date_past = datetime.datetime(1970,1,1)

x = (date_current - date_past).total_seconds()
y = date_past.strftime("%S")

print("Seconds since January 1, 1970: ", x, "or", "{:.2e}".format(x), "in scientific notation")

# print(int(x))
# print("{:.3e}".format(x))
print(date_current.strftime("%B"), date_current.day, date_current.year)