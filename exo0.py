question1=int(input("how many people need a ride ?"))
question2=int(input("How many people fit in one taxi? "))
z=question1 // question2
if question1 % question2 != 0:
    z=z+1
print("Number of taxis needed:",z)






