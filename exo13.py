while True:
   
    user_input = input("Please type in a string: ")
    
    # End the loop if the input is an empty string
    if user_input == "":
        break
   
    print(user_input)
    print("-" * len(user_input))
