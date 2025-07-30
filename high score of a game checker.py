import random
import time

tim_e = time.localtime()
tim__e = time.strftime(" %d/%m/%Y,\n %H:%M", tim_e)
print(tim__e)

def game():
    
    time.sleep(2)
    print("welcome to your score board of the game to check if you have the highest score from your previous game and current score"+"\n","let's check it out")
    time.sleep(5)
    score = random.randint(0,1000)
    
    with open ("hiscore_of_game.txt") as f:
        hiscore_of_game = f.read()
        if hiscore_of_game != "":
            hiscore_of_game = int(hiscore_of_game)
        else:
            hiscore_of_game = 0
            #agar empty haa to fir hi-score 0 haa
            
    print(f"your current score is : {score} ")

    
    time.sleep(2)
    print(f"your last high score was : {hiscore_of_game} ")
    time.sleep(2)
    print("let's check it out")
    time.sleep(2)
        
    if score > hiscore_of_game:
            print("Hey congractulations buddy,you have broken the high score")
    else:
            print("Oh! no! shit, you have AWAY from the high score")
    with open ("hiscore_of_game.txt", "w") as f:
        f.write(str(score))

    return score

game()