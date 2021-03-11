from random import randint
def win():
    print("you win")
def lose():
    print("you lose")
while True:
    player_choice=input("what do you pick?(rock,papaer,scissors)")
    player_choice.strip()
    random_move=randint(0,2)
    move=["rock","paper","scissors"]
    computer_choice = move[random_move]
    print("computer_choice",computer_choice)
    if computer_choice==player_choice:
        print("draw")
    elif player_choice == 'rock' and computer_choice== 'scissors':
        win()
    elif player_choice == 'paper' and computer_choice== 'scissors':
        lose()
    elif player_choice == 'scissors' and computer_choice == 'paper':
        win()
    elif player_choice == 'scissors' and Computer_choice== 'rock':
        lose()
    elif player_choice == 'paper' and computer_choce == 'rock':
        win()
    elif player_choice=="rock" and computer_choice=="papaer":
        lose()
    again=input("do you want to play again?(y or n)").strip()
    if again=="n":
        break
