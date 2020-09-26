from datetime import *

# Get Today's Date
today = date.today()
print("Today: " + today.strftime('%A %d, %b %Y'))
print()

name = input("Please, enter your name")
print()
dob_str = input("What is your Date of Birth? dd/mm/yyyy")
print()
# Convert user input into a date
dob_data = dob_str.split("/")
dobDay = int(dob_data[0])
dobMonth = int(dob_data[1])
dobYear = int(dob_data[2])
dob = date(dobYear, dobMonth, dobDay)

# Calculate number of days lived
numberOfDays = (today - dob).days

# Convert this into whole years to display the age
age = numberOfDays // 365
print("You are " + str(age) + " years old.")
print()

# Retrieve the day of the week (Monday to Sunday) corresponding to the DoB.
day = dob.strftime("%A")
print("You were born on a " + day + ".")
print()

print("You have spent " + str(numberOfDays) + " days on Earth.")
print()

# Calculating the number of days until next birthday
thisYear = today.year

nextBirthday = date(thisYear, dobMonth, dobDay)
if today < nextBirthday:
    gap = (nextBirthday - today).days
    print("Your birthday is in " + str(gap) + " days.")
elif today == nextBirthday:
    print("Today is your birthday! Wishing you a very Happy Birthday," + name + "!")
    print()
else:
    nextBirthday = date(thisYear + 1, dobMonth, dobDay)
    gap = (nextBirthday - today).days
    print("Your birthday is in " + str(gap) + " days.")

if dobMonth == 12:
    astroSign = 'Sagittarius' if (dobDay < 22) else 'Capricorn'
elif dobMonth == 1:
    astroSign = 'Capricorn' if (dobDay < 20) else 'Aquarius'
elif dobMonth == 2:
    astroSign = 'Aquarius' if (dobDay < 19) else 'Pisces'
elif dobMonth == 3:
    astroSign = 'Pisces' if (dobDay < 21) else 'Aries'
elif dobMonth == 4:
    astroSign = 'Aries' if (dobDay < 20) else 'Taurus'
elif dobMonth == 5:
    astroSign = 'Taurus' if (dobDay < 21) else 'Gemini'
elif dobMonth == 6:
    astroSign = 'Gemini' if (dobDay < 21) else 'Cancer'
elif dobMonth == 7:
    astroSign = 'Cancer' if (dobDay < 23) else 'Leo'
elif dobMonth == 8:
    astroSign = 'Leo' if (dobDay < 23) else 'Virgo'
elif dobMonth == 9:
    astroSign = 'Virgo' if (dobDay < 23) else 'Libra'
elif dobMonth == 10:
    astroSign = 'Libra' if (dobDay < 23) else 'Scorpio'
elif dobMonth == 11:
    astroSign = 'Scorpio' if (dobDay < 22) else 'Sagittarius'

print()
print("Your Zodiac Sign is", astroSign)

