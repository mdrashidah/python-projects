user_id = input("Enter your user ID: ")
i = 0
while i < 3:
    password = input("Enter the password: ")
#password is written inside the loop because we want to check the password each time the loop runs
    if password == "ali@234": 
        #isme [i] is not used because we are checking the entire password string
        # If the password is correct, exit the loop
        print("Password is correct!")
        break
    else:
        print("Password is incorrect. Try again.")
    i += 1
    if i == 3:
        print("Password attempt limit reached.")
