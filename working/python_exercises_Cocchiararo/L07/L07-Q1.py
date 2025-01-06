'''
Q1: The stock market
'''

import random
import numpy as np
import time
from numba import njit

# For using the probability in the figure, I define a matrix 
# where x is the actual state, y the state of the day after [Prob(bull -> bear) = 0.075]
prob = np.array([[0.9,  0.075, 0.025],# Bull
                 [0.15, 0.8,   0.05], # Bear
                 [0.25, 0.25,  0.5]]) # Stagnant
                 #Bull   #Bear #Stag    

# Three possibile states
# states = ['bull','bear','stagnant']
# states = [0,1,2]

def MC(ndays):
    state       = np.random.choice([0,1,2]) 
    counts_days = [0,0,0]
   
    for i in range(ndays):
        counts_days[state] += 1. #the first day is selected by random choise and I'm increasing by 1 the count corresponding to that status day
        state               = np.random.choice([0, 1, 2], p=prob[state])        
    
    return counts_days
@njit
def MC_numba(ndays):
    # I can not use random.choise with numba, so I try another way
    # to pick a random number 
    state = np.random.randint(0, 3)  
    counts_days = [0,0,0]

    for i in range(ndays):
        counts_days[state] += 1  

        r = np.random.rand() #between 0 and 1 
        # cumulative probabilities for the current state
        cumulative_prob = np.cumsum(prob[state])  

        # Now I can compare the random number with the cum prob instead of using random.choise
        if r < cumulative_prob[0]:
            state = 0
        elif r < cumulative_prob[1]:
            state = 1
        else:
            state = 2

    return counts_days

#I've to check that the fraction of days in each state converges 
time0         = time.time()
ndays         = 1000000
counts_python = MC(ndays)
fractions     = [count_each/ndays for count_each in counts_python]
print(fractions)
time1         = time.time()
print('Time with python:', time1-time0)

time2 = time.time()
counts_python = MC_numba(ndays)
time3 = time.time()

print('Time with numba:', time3-time2)