
import random
from dice import Dice
def ludo():
    player1=0
    player2=0
    player3=0
    target=100
    while True:
        dice=[1,2,3,4,5,6]
        output1=(random.choice(dice))
        print(output1)
        print("player1:   ",Dice[output1-1])
        player1+=output1
        output2=(random.choice(dice))
        print("player2:  ",Dice[output2-1])
        player2+=output2
        print(output2)
        output3=(random.choice(dice))
        print("player3" ,Dice[output3-1])
        player3+=output3
        print(output3)
        if player1>=target:
            print("player1 is winner")
            if player2>player3:
                print("player2 is place 2")
            else:
                print("player3 is place 2")
            if player2<player3:
                print("third-place is player 2")
            else:
                print("third-place is player 2")
            break
        elif player2>=target:
            print("player2 is winner")
            if player1>player3:
                print("second-place player1")
            else:
                print("second-place player3")
            if player3<player1:
                print("third-place player3")
            else:
                print("third-place player1")
            break
        elif player3>=100:
            print("player3 is winner")
            if player2>player1:
                print("second-place player 2")
            else:
                print("second-place is player1")
            if player1<player2:
                print("third-place is player1")
            else:
                print("third-place player 2")
            break
        

        
ludo()





    
        




