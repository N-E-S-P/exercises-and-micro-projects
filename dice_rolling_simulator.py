import random


def dice_rolling_simulator():
    print("Result:", random.randint(1, 6))

    try_again = input("Wanna try again? ")

    if try_again.lower() == "y" or try_again.lower() == "yes":
        return dice_rolling_simulator()
    elif try_again.lower() == "n" or try_again.lower() == "no":
        return "Sad dice. :("
    else:
        return "I did not understand. Retry."


print(dice_rolling_simulator())
