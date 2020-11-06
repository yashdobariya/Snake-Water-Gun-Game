

                        #   snack water gun Game

import random
list=["s","g","w"]

chance=10
no_of_chance=0
computer_points=0
human_points=0

print(" \t \t \t \t Snake,Water,Gun,Game\n")
print("s for snake\nw for water\ng for gun\n")

# making the game in while

while no_of_chance<chance:
    _input=input("snak,water,gun:\n")
    _random=random.choice(list)

    if _input==_random:
        print("Tie both 0 point to each \n ")

    elif _input=="s" and _random=="g":
        computer_points=computer_points+1
        print(f"your guess is {_input} and computer guess is {_random}")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_points} and you points is {human_points} \n")

    elif _input=="s" and _random=="w":
        human_points = human_points + 1
        print(f"your guess is {_input} and computer guess is {_random}")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_points} and you points is {human_points} \n")

    elif _input=="w" and _random=="s":
        computer_points = computer_points + 1
        print(f"your guess is {_input} and computer guess is {_random}")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_points} and you points is {human_points} \n")

    elif _input=="w" and _random=="g":
        human_points = human_points + 1
        print(f"your guess is {_input} and computer guess is {_random}")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_points} and you points is {human_points} \n")

    elif _input=="g" and _random=="s":
        human_points = human_points + 1
        print(f"your guess is {_input} and computer guess is {_random}")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_points} and you points is {human_points} \n")

    elif _input=="g" and _random=="w":
        computer_points = computer_points + 1
        print(f"your guess is {_input} and computer guess is {_random}")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_points} and you points is {human_points} \n")

    else:
        print("you have wrong input\n")

    no_of_chance = no_of_chance +1
    print(f"{chance-no_of_chance} is left out of {chance} \n ")

print("Game Over")

if computer_points==human_points:
    print("Tie")
if computer_points>human_points:
    print("Computer won and you loose")
elif computer_points<human_points:
    print("you won and computer loose")

print(f"your points is {human_points} and computer points is {computer_points} ")