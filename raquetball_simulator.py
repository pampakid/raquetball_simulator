# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 01:47:14 2017

@author: Pampa Kid
"""

# Import randint
from random import randint

# Ask user for probabilities
p1 = float(input('Enter the probability of winning a point when serving: '))
p2 = float(input('Enter the probability of winning a point when the opponent serves: '))

# Raquetball function
def raquetball(p1, p2):
    won = 0         # Counter of won games
    lost = 0        # Counter of lost games
    for n in range(10000):
        serve = randint(0, 1)
        player = 0
        opponent = 0
        while (player < 21):                # Loop stops when player reaches 21 pts
            if (serve == 1):
                rand1 = randint(1, 10)
                if (rand1 <= (p1*10)):      # If player serves AND wins
                    player += 1
                    serve = 1
                else:
                    serve = 0
            if (serve == 0):
                rand2 = randint(1, 10)      # If opponent serves AND player wins
                if (rand2 <= (p2*10)):
                    serve = 1
                else:
                    opponent += 1
                    serve = 0
        if (player > opponent):             # If player > opponent, player won the game
            won += 1
        else:
            lost += 1
    #result = won/10000
    return (won/10000)
    # Print probability of winning
print('\nYou have a ', (raquetball(p1, p2)*100), '% chance of winning the game.')        # 82.74%