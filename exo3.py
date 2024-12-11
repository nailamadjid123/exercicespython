
WEEKDAYS=["Monday","Tuesday", "Wednesday","Thursday", "Friday"]

montant=int(input("Total amount:"))
items=int(input("Number of items:"))
day=str(input("Day of the week:"))


if day in WEEKDAYS:
    montant -=montant*0.1
else:
     montant-=montant*0.2


if items>5:
    montant-=montant*0.5

print("Total price after discount:",montant,"dinars")    