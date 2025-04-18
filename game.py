#snake water gun game 
import random
options = ['snake','water','gun']

def whowins(player_choice, system_choice):
    if player_choice == system_choice:
        print("Both chose same option.Tie!!")

    elif(player_choice == 'snake' and system_choice == 'water') or \
          (player_choice == 'water' and system_choice == 'gun') or \
          (player_choice == 'gun' and system_choice == 'snake'):
        print("You won!yay!!")
    else:
        print("Computer won!")

def play():
    while True:
        player_choice = input("Choose your option from 'snake, water, gun' or exit to end the game: ").lower()
        if player_choice == 'exit':
            print("Thanks for playing!")
            break
        if player_choice not in options:
            print("Oops!looks like you have choosen something wrong.")
            continue
        system_choice = random.choice(options)
        print(f"Computer chose: {system_choice}")
        print(f"You chose: {player_choice}")
        final_result = whowins(player_choice, system_choice)

play()