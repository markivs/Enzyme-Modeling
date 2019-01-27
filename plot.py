import random as random
import numpy as np
import sys
import matplotlib.pyplot as plt
from click._compat import raw_input
from nltk.tag import sequential

primerLength = 10

# creates DNA sequence of specified length with random base pairs
def randDNASeq(length):
    # variable to store DNA sequence
    DNA = ['']*length
    # possible base pairs
    basePairs = ['A', 'G', 'C', 'T']
    for i in range(len(DNA)):
        # randomly chooses a base to put into DNA at index
        DNA[i] = random.choice(basePairs)
    # return resulting sequence
    return DNA

# searches DNA sequence sequentially - checks every index for possible primer
def seqentialSearch(DNA):
    steps = 0
    primerOccurences = 0
    # search starts at 0 and increments after each iteration
    for i in range(len(DNA)):
        
        if(DNA[i] == 'A'): # check for primer, increase primer count
            primerOccurences+=1
        elif (primerOccurences > 0): # if primer is not found, reset primer count and increment steps
            primerOccurences = 0
            steps += 1
        if(primerOccurences == primerLength): # once primer is found, return number of steps
            return ['Sequential Search', steps, 'blue']
    return -1 # otherwise return -1

def randSearch(DNA):
    i = 0
    steps = 0
    found = False
    primerOccurences = 0
    while found == False: # loop until primer is found
        if(DNA[i] == 'A'): # if potenital primer is found
            primerOccurences+=1 #increase primer count
            if(primerOccurences >= primerLength): # check if primer has been found
                found = True # inform loop using variable
                print('Found') # print result for debugging
        else:
            steps += 1 # otherwise increase step number
            i = int(random.uniform(0, len(DNA)-1)) #select another random index
            if (primerOccurences > 0): # reset primer count
                primerOccurences = 0
        if(i < len(DNA)-1): # increase index of search
            i+=1
    return ['Random Search', steps, 'red'] #return result

#get user input
trials = int(raw_input("Enter number of trials: "))
DNAsize = int(raw_input("Enter size of DNA: "))

#store runs to provide framework for algorithm testing
stepListLen = 2
barWidth = 1.0
barIndex = 1
randomRuns = []
sequentialRuns = []

for trialNum in range(stepListLen): # two for loops to test number of trials and length of DNA
    
    for i in range(trials):

        DNA = randDNASeq(DNAsize) # create random DNA seq
        
        insertIndex = int(random.uniform(0, len(DNA))) # insert primers at random index
        for j in range(primerLength):
            DNA.insert(insertIndex, 'A')
        
        stepList = [randSearch(DNA), seqentialSearch(DNA)] # store results of each algorithm
        print(stepList)
        name = stepList[trialNum][0] # store prefered results based on trial
        step = stepList[trialNum][1]
        clr = stepList[trialNum][2]
        if(trialNum == 0): # store results (to be averaged)
            randomRuns.append(step)
        elif(trialNum == 1):
            sequentialRuns.append(step)
        if(i == 0): # plot legend if first index
            plt.bar((trialNum+1/barWidth)*barIndex, step, barWidth/2, label = name, color = clr)
        else: # otherwise ignore legend
            plt.bar((trialNum+1/barWidth)*barIndex, step, barWidth/2, color = clr)
        barIndex += 1
        
# plot lines representing average        
plt.hlines(np.mean(randomRuns), 0, trials*stepListLen*2 , color = 'red')
plt.hlines(np.mean(sequentialRuns), 0, trials*stepListLen*2 , color = 'blue')

#create graph based on data
plt.title('Histogram of Avg # of steps for DNA search algorithms')
plt.xlabel(' Algorithm ')
plt.ylabel(' Number of Steps ')
plt.legend(loc = 'lower left')
plt.grid(True)
plt.show()

