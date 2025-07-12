#user_id and password are written inside the loop because we want to check the user_id and password each time the loop runs
print("PRIVATE___FOLDER")
print("ENTER_CORRECT_PASSWORD_TO ACCESS_DATA")

user_id = input("Enter your user ID: ")
i = 0
while i < 3:
    if user_id=="748192" :
            print("entered user_id is correct")
        

    else:
        print("incorrect user_id")
        break
    i += 1
    if i == 3:
        print("user_id attempt limit reached.")
        break

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
            break
    i += 1
    if i == 3:
        print("Password attempt limit reached.")
    break
