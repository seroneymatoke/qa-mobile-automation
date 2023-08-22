from datetime import date



# now = datetime.datetime.now()
#         # print(now.year, now.month, now.day, now.hour, now.minute, now.second)
# today = date.today()
# print("Today's date:", today)


# Textual month, day and year	
d2 = date.today().strftime("%b %d, %Y")
print("d2 =", d2)