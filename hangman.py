#rules
print('RULES: \n1.One player chooses the word\n2.Second player guesses\n3.You have 5 lives, to quit guess "END"')

#functions

def replace_letter(letter):
        index_of = [i for i, d in enumerate(chosen_word) if d == letter]
        for index in index_of:
            second_word[index] = player_guess
        return second_word


#choose a word

chosen_word = [letter for letter in input('Choose a word: ')]

second_word = ['_' for letter in chosen_word]

lives = 5

while lives != 0:
    #general
    if '_' not in second_word:
        print('YOU WIN!')
        break
    print('================')
    print('\nWord:', end = ' ')
    for letter in second_word:
        print(letter, end = ' ')
    
    print('\n')
    print('Your lives:', lives)
    player_guess = str(input('Guess a letter: '))
    if player_guess == 'END':
        break
    if len(player_guess) > 1:
        print('You can only choose one letter!')
        
    #guesses
    if player_guess in chosen_word:
        print('Good job!')
        replace_letter(player_guess)
        
            
    elif player_guess not in chosen_word:
        print('Incorrect guess, -1 life.\n')
        lives -= 1
        
if lives == 0:
    print('YOU LOST!')
    
        

