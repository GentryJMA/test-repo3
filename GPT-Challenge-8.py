#Rock Paper Scissors, no help from GPT

import random

computer_choice = ''
user_choice = ''
win = 'You Win!'
lose = 'You Lose!'
replay_input = ''

#Function for the inputs from user, and computer. Also shows input prompt.

def inputs():
    global user_choice
    global computer_choice
    
    user_choice = input('Rock, Paper, Scissors? ')
    user_choice = user_choice.lower()
    
    computer_choice = random.choice(('rock', 'paper', 'scissors'))
    print('Computers Choice is: ' + computer_choice)

#Function for main game logic. Decides which combination of inputs is a loss, tie, or win.

def main_logic():
    
    global replay_input

    if user_choice != computer_choice:

        if user_choice == 'rock' and computer_choice == 'scissors':
            print(win)
            replay_input = input('Would you like to play again? (Yes/No)')
            replay_input = replay_input.lower()
            if replay_input == 'yes':
                inputs()
                main_logic()
            else:
                print('Thanks for playing!')
        
        else:
            if user_choice == 'scissors' and computer_choice == "paper":
                print(win)
                replay_input = input('Would you like to play again? (Yes/No)')
                replay_input = replay_input.lower()
                if replay_input == 'yes':
                    inputs()
                    main_logic()
                else:
                    print('Thanks for playing!')
            else:
                if user_choice == 'paper' and computer_choice == 'rock':
                    print(win)
                    replay_input = input('Would you like to play again? (Yes/No)')
                    replay_input = replay_input.lower()
                    if replay_input == 'yes':
                        inputs()
                        main_logic()
                    else:
                        print('Thanks for playing!')
                else:
                    if user_choice == 'rock' and computer_choice == 'paper':
                        print(lose)
                        replay_input = input('Would you like to play again? (Yes/No)')
                        replay_input = replay_input.lower()
                        if replay_input == 'yes':
                            inputs()
                            main_logic()
                        else:
                            print('Thanks for playing!')
                        
                    else:
                        if user_choice == 'scissors' and computer_choice == 'rock':
                            print(lose)
                            replay_input = input('Would you like to play again? (Yes/No)')
                            replay_input = replay_input.lower()
                            if replay_input == 'yes':
                                inputs()
                                main_logic()
                            else:
                                print('Thanks for playing!')
                        
                        else:
                            if user_choice == 'paper'and computer_choice == 'rock':
                                print(lose)
                                replay_input = input('Would you like to play again? (Yes/No)')
                                replay_input = replay_input.lower()
                                if replay_input == 'yes':
                                    inputs()
                                    main_logic()
                                else:
                                    print('Thanks for playing!')
                        
                            else:
                                if user_choice == 'paper'and computer_choice == 'scissors':
                                    print(lose)
                                    replay_input = input('Would you like to play again? (Yes/No)')
                                    replay_input = replay_input.lower()
                                    if replay_input == 'yes':
                                        inputs()
                                        main_logic()
                                    else:
                                        print('Thanks for playing!')



    else:
        print('Tie')
        replay_input = input('Would you like to play again? (Yes/No)')
        if replay_input == 'yes':
            inputs()
            main_logic()
        else:
            print('Thanks for playing!')
                        

inputs()
main_logic()
      
        

