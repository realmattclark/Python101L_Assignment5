#Matt Clark
#CS101 Lab
#6 October 2021

import random

def play_again():
    while True:
        playGame = input('Play again? (y / n): \n')
        if playGame == 'y' or playGame == 'Y':
            return True

        if playGame == 'n' or playGame == 'N':
            return False
        else: print('Must answer with "y" or "n"')

def wager():
    while True:
        global wager
        
        wager = int(input('Enter your wager: \n'))
        if wager <= 0 or wager > bank['money']:
            print('Your value must be greater than zero and less than the current chips in your bank')
        else:
            return wager

def slot_results():
    global reel1
    global reel2
    global reel3
    reel1 = random.randint(1,10)
    reel2 = random.randint(1,10)
    reel3 = random.randint(1,10)

    results = [reel1, reel2, reel3]
    print(reel1, reel2, reel3)
    return results

def get_matches(reel1, reel2, reel3):
    global matches
    matches = 0
    if reel1 == reel2 and reel2 == reel3:
        matches = 3
    if reel1 == reel2 and reel2 != reel3:
        matches = 2
    else:
        matches = 0
    print(matches, 'matches.\n')
    return matches

def get_bank():
    while True:
        chips = int(input('How many chips would you like to start with? : \n'))
        if chips < 1 or chips > 100:
            print('Please enter a value between 1 and 100')
        else:
            bank['money'] = chips
            return chips

def payout(matches, payout):
    payout = 0
    if matches == 3:
        payout = (wager * 10) - wager
    if matches == 2:
        payout = (wager * 3) - wager
    if matches == 0:
        payout = bank - wager
    return payout

bank = {'money' : 0}
print('Welcome to the slot machine!')
get_bank()
while True:
    wager()
    slot_results()
    get_matches(reel1, reel2, reel3)
    outcome = payout(wager, matches)
    bank['money'] += outcome
    print('Current bank balance :', bank['money'])
    if bank['money'] > 0:
        if play_again() == False:
            print('Thank you for playing!')
            quit()
        else:
            continue
    else:
        print('You do not have any more money to play with. Thank you!')
        quit()
