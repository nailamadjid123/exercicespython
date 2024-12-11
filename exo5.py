print("Runner 1:")
name=str(input("Name:"))
time=float(input("Time (in seconds):"))
print("Runner 2:")
name2=str(input("Name:"))
time2=float(input("Time (in seconds):"))

if time<time2:
    print("The faster runner is",name)
elif time>time2:
    print("The faster runner is",name2)
else:
    print(name,"and",name2,"have the same time") 