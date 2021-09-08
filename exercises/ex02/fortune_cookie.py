"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730319741"

from random import randint

print("Your fortune cookie says... ")

int = randint(0, 3)
if int == 0:
    print("A golden egg of oportunity falls into your lap this month. ")
else:
    if int == 1: 
        print("Be careful or you could fall for some tricks today. ")
    else: 
        if int == 2:
            print("Every wise man started out by asking many questions. ")
        else:
            if int == 3:
                print("Fear and desire - two sides of the same coin. ")
print("Now, go spread positive vibes! ")