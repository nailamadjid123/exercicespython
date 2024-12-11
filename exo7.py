print("Input:")
year = int(input("Please type in a year: "))
print("Output:")

if year % 400 == 0:  # Divisible par 400
    print("That year is a leap year.")
elif year % 100 == 0:  # Divisible par 100 mais pas par 400
    print("That year is not a leap year.")
elif year % 4 == 0:  # Divisible par 4 mais pas par 100
    print("That year is a leap year.")
else:  # Pas divisible par 4
    print("That year is not a leap year.")
