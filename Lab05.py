#Matt Clark
#CS101 Lab
#6 October 2021


#ALGORITHM:
# Ask user for chips, wager and then run the program

#Error:
# Wager not less than 0 or more than 100




import random

def play_again():
    while True:
        playGame = input('Play again? (y / n): \n')
        if playGame == 'y' or playGame == 'Y':
            return True

        if playGame == 'n' or playGame == 'N':
            return False
        else: print('Must answer with "y" or "n"')

def get_wager(bank : int):
    while True:
        global wager
        
        wager = int(input('Enter your wager: \n'))
        if wager <= 0 or wager > bank:
            print('Your value must be greater than zero and less than the current chips in your bank')
        else:
            return wager

def get_slot_results():
    global reela
    global reelb
    global reelc
    
    reela = random.randint(1,10)
    reelb = random.randint(1,10)
    reelc = random.randint(1,10)

    results = [reela, reelb, reelc]
    return results

def get_matches(reela, reelb, reelc):
    global matches
    matches = 0
    if reela == reelb and reelb == reelc:
        matches = 3
    if reela == reelb and reelb != reelc:
        matches = 2
    else:
        matches = 0
    print(matches, ' matches.\n')
    return matches

def get_bank():
        global bank
        bank = int(input('How many chips would you like to start with? : \n'))
        if bank < 1 or bank > 100:
            print('Please enter a value between 1 and 100')
        else:
            return bank

def get_payout(wager, matches):
    payout = 0
    if matches == 3:
        payout = wager * 10
    if matches == 2:
        payout = wager * 3
    if matches == 0:
        payout = bank - wager
    return wager * -1

if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()

        while True: 
            
            wager = get_wager(bank)

            reela, reelb, reelc = get_slot_results()

            matches = get_matches(reela, reelb, reelc)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reela, reelb, reelc)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
    print("You lost all", 0, "in", 0, "spins")
    print("The most chips you had was", 0)
    playing = play_again()
