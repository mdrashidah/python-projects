print("follow the traffic light rules  " + "and drive safely \n")

light = input("displayed traffic light signal colour: \n")

if light == "red":
    print("stop the vehicle" + " and wait for the green light")

elif light == "yellow":
    print("get ready to move" + " and wait for the green light")

elif light == "green":
    print("you can move now" + " and drive safely")

else:
    print("please enter a valid traffic light command")