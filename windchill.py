celsius = float(input("Enter your temperature in celsius: "))
wind_speed = float(input("Enter your windspeed: "))
windchill = 13.12 + (0.6215 * celsius) - (11.37 * wind_speed**0.16) + (0.3965 * celsius * wind_speed**0.16)
print("This is the windchill: %.2f" % (windchill))