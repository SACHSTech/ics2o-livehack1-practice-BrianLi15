input_hours = int(input("Enter amount of hours: "))
days = input_hours//24
remaining_hours = input_hours - (days * 24) 
print("Amount of days: " + str(days))
print("Amount of hours: " + str(remaining_hours))
