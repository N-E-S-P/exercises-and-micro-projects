import re

print('''
    THE SMART CALCULATOR
    --------------------
    Greetings, human friend! :) Please enter your input to make me perform calculations.
    
    Enter 'q' to quit
''')

number = 0
status = True


def smart_calculator():
    global status
    global number
    if number == 0:
        user_input = input("Input: ")
    else:
        user_input = input(str(number))
    if user_input == "q":
        print("Goodbye, human friend. :)")
        status = False
    else:
        user_input = re.sub('[a-zA-Z ,.:()&]', '', user_input)
        if number == 0:
            number = eval(user_input)
        else:
            number = eval(str(number) + user_input)


while status:
    smart_calculator()

