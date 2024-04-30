import random

def roll():
    # Simulates the rolling of two dice and returns their sum.
    return random.randint(1,6) + random.randint(1,6)

def play():
    # Simulates a game of Craps

    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    sum_result = dice_1 + dice_2

    if sum_result == 7 or sum_result == 11:
        print(f"The sum of dice is {dice_1} + {dice_2} = {sum_result}")
        print("You won!")
    elif sum_result == 2 or sum_result == 3 or sum_result == 12:
        print(f"The sum of dice is {dice_1} + {dice_2} = {sum_result}")
        print("You lost!")
    else:
        goal_number = sum_result
        print(f"You got {goal_number}. So the goal number is {goal_number} and you need to roll till you get {goal_number} again.")
        while True:
            playing_question = input("Continue playing? y/n ")
            if playing_question.lower() == 'y':
                sum_result = roll()
                if sum_result != goal_number:
                    print(f"You got {sum_result}. Roll again till you get {goal_number}.")
                elif sum_result == goal_number:
                    print(f"You got {goal_number} again and won, congratulations!")
                    break
                elif sum_result == 7:
                    print(f"You got 7 and lost.")
                    break
            elif playing_question.lower() == 'n':
                print("Ok, then we don't play anymore.")
                break
            else:
                print("You didn't choose 'y' or 'n'")
