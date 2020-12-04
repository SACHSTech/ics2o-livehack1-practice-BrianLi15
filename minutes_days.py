input_minute = int(input("Enter amount of minutes: "))
number_days = input_minute // 1440
number_hours = (input_minute - (number_days * 1440)) // 60
number_minutes = input_minute - (number_days * 1440) - (number_hours * 60)
print("Amount of days: " + str(number_days))
print("Amount of hours: " + str(number_hours))
print("Amount of minutes: " + str(number_minutes))
