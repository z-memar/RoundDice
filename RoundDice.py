# Dice - count totals in user-defined number of rounds

import random

class Bin():
    def __init__(self, binIdentifier, counter):
        self.binIdentifier = binIdentifier
        self.counter = counter

    def reset(self):
       self.counter = 0

    def increment(self):
        self.counter = self.counter + 1 
       
    def show(self, nRoundsDone):
        if self.binIdentifier < 2:
            return
        else:
            print(self.binIdentifier, '*' * self.counter ,"(", round((self.counter/nRoundsDone)*100) , "%" , ")")
                               
def Run():
    binList = [ ]
    for i in range(0,13):
        binObj = Bin(i,0)
        binList.append(binObj)
    
    while True:
        #reset
        for i in range(0,13):
            binList[i].reset()

        nRounds = input('How many rounds do you want to do? (or Enter to exit): ')
        if nRounds == '':
            break
        nRounds = int(nRounds)

        for i in range(0,nRounds):
            dic1 = random.randrange(1,7)
            dic2 = random.randrange(1,7)
            sum_dics = dic1 + dic2
            binList[sum_dics].increment()
            
        print()
        print('After', nRounds, 'rounds:')
        for bin in binList:
            bin.show(nRounds)
        print()

    print('OK bye')
Run()
