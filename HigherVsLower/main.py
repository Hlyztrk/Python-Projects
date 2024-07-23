from data import data
import random
from art import logo,vs
import os
score = 0
continue_playing = True

random.shuffle(data)# Reorganize the order of items in the list

while continue_playing: # Continue playing until user guess it wrong
    for i in range(len(data)): # Start looping from the first index of data list
        print(logo) # Print the logo imported from art.py
        print(f"Your current score is : {score}") # Print the current score
        print(f"Compare A: {data[i]['name']}, {data[i]['description']}, from {data[i]['country']}") 
        A = data[i]['follower_count']
        print(vs)
        print(f"Against B: {data[i+1]['name']}, {data[i+1]['description']}, from {data[i+1]['country']}")
        B = data[i + 1]['follower_count']
        answer = input("Who has more followers? Type 'A' or 'B' : ").capitalize()
        if A > B and answer == 'A' or B > A and answer == 'B':
            i += 1
            score += 1
            os.system('clear')
        else:
            print(f"Sorry you lost, your final score is {score}")
            if A > B:
                print(f"{data[i]['name']}({A}) has more followers than {data[i + 1]['name']}({B})")
            elif B > A:
                print(f"{data[i + 1]['name']}({B}) has more followers than {data[i]['name']}({A})")
            continue_playing = False
            break
    
    