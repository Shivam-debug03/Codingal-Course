city = input("Enter your city name")
temp = float(input("Enter today's temperature in C:"))

if temp > 35 :
    print("Warning : It is very hot outside")

if temp > 25 :
    print("Great day to go outside")
else:
    print("Grab a jacket before you go outside")

if temp > 35 :
    print("Weather: Scorching Outside")
elif temp > 25 :
    print("Weather: Warm and Sunny Outside")
elif temp > 15 :
    print("Weather: Breezy and Cool Outside")
else:
    print("Weather: Cold - stay Warm!")

import datetime
import calendar

now = datetime.datetime.now()
print("City:",city)
print("Time now:",now)

print(calendar.calendar(now.year))