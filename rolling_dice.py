import random

repeating_text = 'To roll again type "roll"\nTo quit type "stop"'

def roll():
    print(random.randint(1,6))
    print(repeating_text)
    
print('To roll the dice type in "roll"')

roll_again = True
    
while roll_again == True:
    user_input = str(input())
    if user_input == 'roll':
        roll()
        repeating_text
    elif user_input == 'stop':
        roll_again = False