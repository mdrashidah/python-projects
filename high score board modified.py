import random
import time

tim_e = time.localtime()
tim__e = time.strftime(" %d/%m/%Y,\n %H:%M %p", tim_e)
print(tim__e)

def game():
    
    time.sleep(2)
    print("welcome to your score board of the game to check if you have the highest score from your previous game and current score"+"\n","let's check it out")
    time.sleep(5)
    score = random.randint(0,1000)
    
    with open ("hiscore_ofgame.txt") as f:
        hiscore_ofgame = f.read()
        if hiscore_ofgame != "":
            hiscore_ofgame = int(hiscore_ofgame)
        else:
            hiscore_ofgame = 0
            #agar empty haa to fir hi-score 0 haa
            
    print(f"your current score is : {score} ")

    
    time.sleep(2)
    print(f"your last high score was : {hiscore_ofgame} ")
    time.sleep(2)
    print("let's check it out")
    time.sleep(2)


    if score > hiscore_ofgame:
        with open("hiscore_ofgame.txt", "w") as f:
            f.write(str(score))
        print("Hey congratulations buddy, you have broken the high score")
    else:
        print("Oh! no! You are away from the high score")

    return score
game()