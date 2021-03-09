# Write your code here
import random

moves = ['rock', 'paper', 'scissors']


# if 'scissors' in user_move:
#     print('Sorry, but the computer chose rock')
# if 'rock' in user_move:
#     print('Sorry, but the computer chose paper')
# if 'paper' in user_move:
#     print('Sorry, but the computer chose scissors')

user_name = input('Enter your name: ')
print(f'Hello, {user_name}')


opened_file = open('rating.txt', 'r')
for line in opened_file:
    #global score
    s = line.split()
    if user_name in s[0]:
        #print(user_name)
        score = int(s[1])
        #print(s[1])
        break
    else:
        score = 0

option_input = input()
print("Okay, let's start")

if not option_input:
    lose_conditions = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    while True:
        #print('Wie hoch', score)
        user_move = input()
        computer_move = (random.choice(moves))
        if user_move == '!exit':
            print('Bye!')
            break
        if user_move == '!rating':
            print(f'Your rating: {score}')
        if user_move not in moves:
            print('Invalid input')
            continue
        if (user_move, computer_move) in lose_conditions.items():
            print(f'Sorry, but the computer chose {computer_move}')
            continue
        if user_move == computer_move:
            print(f'There is a draw {computer_move}')
            score += 50
            continue
        else:
            print(f'Well done. The computer chose {computer_move} and failed')
            score += 100
            continue

else:
    option_input = "rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire".split(",")

    while True:
        user_move = input()  # this input is a the players input

        if user_move == '!exit':
            print('Bye!')
            break
        if user_move == '!rating':
            print(f'Your rating: {score}')
            continue
        if user_move not in option_input:
            print('Invalid input')
            continue
        new = option_input[option_input.index(user_move):]
        for i in range(option_input.index(user_move)):
            new.append(option_input[i])

        new.remove(user_move)
        defeat = new[0: (len(new) // 2)]
        #print(defeat)
        win = new[(len(new) // 2):]
        #print(win)
        computer_move = (random.choice(option_input))
        if (computer_move) in defeat:
            print(f'Sorry, but the computer chose {computer_move}')
            continue
        if user_move == computer_move:
            print(f'There is a draw {computer_move}')
            score += 50
            continue
        else:
            print(f'Well done. The computer chose {computer_move} and failed')
            score += 100
            continue