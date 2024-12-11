print("Input:")
nbr = int(input("Number: "))
print("Output:")

if nbr % 3 == 0: 
    print("Fizz")
elif nbr % 5 == 0:  
    print("Buzz")
elif nbr %3 ==0 and nbr%5 ==0:
    print("That year is a leap year.")
else: 
    print("[No Output]")
