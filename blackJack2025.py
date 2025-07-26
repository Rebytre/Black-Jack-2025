#Blackjack
#BY: Rebytre
#A simple slightly dumbed-down version of Black Jack

# ---Imports--- #
import time
import random
import math

# ---Global Variables--- #
#(There are wayy more variables, but these need to be global)
actionsTaken = 0
bet = 0
coins = 100
hand = 1

# ---Lists--- #
deckOfCards = [2,3,4,5,6,7,8,9,10,"J","Q","K","A",2,3,4,5,6,7,8,9,10,"J","Q","K","A",2,3,4,5,6,7,8,9,10,"J","Q","K","A",2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
hands = [[],[]] #Dealer L, Player R#

# ---Functions--- #

# --Title Screen-- # X
#Pretty self explanatory, just the title screen
def titleScreen():
    time.sleep(1.5)
    print ('''\033[1m\033[0;31m
|¯¯¯|   |¯¯¯¯|    /¯¯¯¯¯| /¯¯¯\|¯¯¯|/¯¯¯/ |¯¯¯¯¯¯|  /¯¯¯¯¯| /¯¯¯¯\|¯¯¯|/¯¯¯/ 
|   ¯¯\ |    |_  /   !  ||   ( |   <°  |  /¯¯|   | /   !  ||    ( |       <° 
|__x__/°|______|/___/¯|_|\____\|___|\___\ \______|/___/¯|_| \____\|___|\___\ 
    \033[0m''')
    time.sleep(1)
    print ('''
    \n\033[1mBig Money INC. \033[0m
Please Enjoy!\n
    ''')
    time.sleep(5)
    for i in range(30): #(Clears the screen)
        print("\n")
    return "null"

# --Start-- # X
#Function for creating the starting hands
def start():
    for i in range(0,len(hands)): #For each hand
        for j in range (2): #How many cards it should give each hand
           drawnCard = cardPull()
           hands[i].append(drawnCard)

# --Place Bet-- # X
#Function for making the user place a valid bet.
def placeBet(coins):
    bet = 0
    betCheck = 0
    while bet == 0:
        try:
            bet = int(input(f"How many coins would you like to bet? (Current Purse: {coins} coins)    "))
            if bet > coins:
                bet = 0
                print ("NOT ENOUGH CURRENCY! TRY AGAIN!")
            elif bet < 0:
                bet = 0
                print ("INVALID INPUT")
        except ValueError:
            bet = 0
            print ("INVALID INPUT!")
    return bet

# --Show Hands (Hidden)-- # X
#Function for showing player/dealer hands.
#This is the hidden variation, meaning dealer has a hidden card.
def showHands():
    print ("\n")
    time.sleep(1)
    print ("Player's Hand: ",end="")
    for i in range(len(hands[1])):
        print (hands[1][i]," ",end="")
    print ("\n")
    print ("Dealer's Hand: ",end="")
    print (hands[0][0]," ","*")
    return "null"
    
# --Show Hands (Unhidden)-- # X
#Function for showing player/dealer hands.
#This is the unhidden variation, meaning there are no hidden cards.
def showHandsUnhidden():
    print ("\n")
    time.sleep(1)
    print ("Player's Hand: ",end="")
    for i in range(len(hands[1])):
        print (hands[1][i]," ",end="")
    print ("\n")
    print ("Dealer's Hand: ",end="")
    for i in range(len(hands[0])):
        print (hands[0][i]," ",end="")
    print ("\n")
    return "null"

# --Pulling A Card-- # X
#Function for pulling a card from the deck while removing that card from the deck.
def cardPull():
    cardInList = random.randrange(len(deckOfCards))
    pickedCard = deckOfCards[cardInList]
    deckOfCards.pop(cardInList)
    return pickedCard

# --Turn-- # X
#Function for turns in a round.
def turn(actionsTaken,hand,bet):
    null = ""
    action = 0
    hand = 1
    if actionsTaken == 0:   #Checks if this is the first round to allow doubling down
        while action == 0:
            try:
                action = int(input('''
Select an option:
1 - Draw
2 - Stand
3 - Surrender
4 - Double Down
                \n'''))
            except ValueError:
                print ("INVALID INPUT!")
                action = 0
            if action > 4 and action < 1:
                print ("INVALID INPUT!")
                action = 0        
        if action == 1:     #Returns
            actionsTaken = actionsTaken + 1
            return "drawnCard"
        elif action == 2:
            actionsTaken = actionsTaken + 1
            hand = 0
            return "stand"
        elif action == 3:
            actionsTaken = actionsTaken + 1
            return "surrender"
        elif action == 4:
            actionsTaken = actionsTaken + 1
            return "doubleDown"
    else:
        while action == 0:   #Incase it isn't the first turn within the round(doubling down is only on first turn)
            try:
                action = int(input('''
Select an option:
1 - Draw
2 - Stand
3 - Surrender
                \n'''))
            except ValueError:
                print ("INVALID INPUT!")
                action = 0
            if action > 3 and action < 1:
                print ("INVALID INPUT!")
                action = 0
        if action == 1:     #Returns
            actionsTaken = actionsTaken + 1
            return "drawnCard"
        elif action == 2:
            actionsTaken = actionsTaken + 1
            hand = 0
            return "stand"
        elif action == 3:
            actionsTaken = actionsTaken + 1
            return "surrender"
        
# --Bust Check-- # X
#Function for checking if a hand has busted.
def bustCheck(hand):
    handValue = 0
    for i in range(len(hands[hand])): #Adds all the card values together
        try:
            handValue = int(handValue + hands[hand][i])
        except TypeError:
            if hands[hand][i] == "J" or hands[hand][i] == "Q" or hands[hand][i] == "K":
                handValue = handValue + 10
            elif hands[hand][i] == "A":
                handValue = handValue + 11
    if handValue > 21:  #This part switches an Ace to a 1 in case the hand is over 21 if the ace counts as 11
        for i in range(len(hands[hand])):
            if hands[hand][i] == "A":
                handValue = handValue - 10
                hands[hand][i] = 1
                return "noBust"
        return "bust"
    return "noBust"
    
# --Hand Value Check-- # X
#Checks the value of a specified hand.
#Essentially bustCheck() but it returns handValue instead of "bust"/"noBust"
def handValueCheck(hand):
    handValue = 0   #Adds all the card values together
    for i in range(len(hands[hand])):
        try:
            handValue = int(handValue + hands[hand][i])
        except TypeError:
            if hands[hand][i] == "J" or hands[hand][i] == "Q" or hands[hand][i] == "K":
                handValue = handValue + 10
            elif hands[hand][i] == "A":
                handValue = handValue + 11
    if handValue > 21:      #This part switches an Ace to a 1 in case the hand is over 21 if the ace counts as 11
        for i in range(len(hands[hand])):
            if hands[hand][i] == "A":
                handValue = handValue - 10
                hands[hand][i] = 1
    return handValue

# --Dealer Turn-- #
#Function for what the dealer does during their turn.
def dealerTurn(hand):
    print ("Now the dealer goes.")
    showHandsUnhidden()
    hand = 0
    dealerHandValue = handValueCheck(hand)
    while dealerHandValue < 17:     #Makes the dealer pull more cards if handValue < 17
        print ("The dealer pulls a card...",end="")
        cardPulled = cardPull()
        hands[0].append(cardPulled)
        print (f"its a(n) {cardPulled}!")
        dealerHandValue = handValueCheck(hand)
    bustCheckVar = bustCheck(hand)      #Checks if dealer busts
    if bustCheckVar == "bust":
        showHandsUnhidden()
        print ("\033[1mDEALER BUST!\033[0m")
        print ("Dealer has busted. You win this round!")
        return "win"
    else:
        hand = 1        #Compares hands, and returns messages based on who wins.
        playerHandValue = handValueCheck(hand)
        if playerHandValue > dealerHandValue:
            print ("\033[1m WIN!!! \033[0m")
            return "win"
        elif playerHandValue == dealerHandValue:
            print ("\033[1m TIE!!! \033[0m")
            return "tie"
        elif playerHandValue < dealerHandValue:
            print ("\033[1m LOSS!!! \033[0m")
            return "loss"
    
# --Full Round-- #
#(I know, its a super long function) fullRound() essentially acts as a motherboard,
#combining most of the other functions to create the base game.
#It was easier to do this inside a function rather than leaving it outside the function.
def fullRound(coins,bet):
    #Function variables:
    actionsTaken = 0
    cardsPulled = 0
    bet = placeBet(coins)
    coins = coins - bet
    start()
    playerHandValue = handValueCheck(hand)
    if playerHandValue == 21:
        showHands()
        print ("\n\033[1mBLACK JACK!\033[0m\n")
        coins = coins + round(bet*2.5)
        return coins
    while actionsTaken < 4:
        showHands()#Where individual rounds start
        actionTaken = turn(actionsTaken,hand,bet) #Determines the outcome
        #Rest of the stuff is just checking what the result is, and what the consequence is.
        if actionTaken == "drawnCard":      #If player's action is to draw a card:
            cardsPulled = cardsPulled + 1
            cardPulled = cardPull()
            hands[1].append(cardPulled)
            print (f"You pulled a \033[1m{cardPulled}\033[0m!")
            actionsTaken = actionsTaken + 1
            bustCheckVar = bustCheck(hand)
            if bustCheckVar == "bust":
                print ("\n\033[1mBUST!\033[0m")
                bet = 0
                return coins
        elif actionTaken == "stand":        #If player's action is to stand:
            print ("You choose to stand")
            dealerTurnOutcome = dealerTurn(hand)
            if dealerTurnOutcome == "win":
                coins = coins + (bet*2)
                return coins
            elif dealerTurnOutcome == "tie":
                coins = coins + bet
                return coins
            elif dealerTurnOutcome == "loss":
                return coins
        elif actionTaken == "surrender":    #If player's action is to surrender:
            print ("You choose to surrender; half of your hand is returned.")
            coins = round(coins + (bet*0.5))
            return coins
        elif actionTaken == "doubleDown":       #If player's action is to double down:
            coins = coins - bet
            bet = bet * 2
            print ("Your bet has doubled, you pull 1 last card...")
            cardPulled = cardPull()
            hands[1].append(cardPulled)
            print (f"You pull a {cardPulled}!")
            bustCheckVar = bustCheck(hand)
            if bustCheckVar == "bust":
                print ("\n\033[1mBUST!\033[0m")
                bet = 0
                return coins               
            dealerTurnOutcome = dealerTurn(hand)
            if dealerTurnOutcome == "win":
                coins = coins + (bet*2)
                return coins
            elif dealerTurnOutcome == "tie":
                coins = coins + bet
                return coins
            elif dealerTurnOutcome == "loss":
                return coins
    if actionsTaken >= 4:
        dealerTurnOutcome = dealerTurn(hand)
        if dealerTurnOutcome == "win":
            coins = coins + (bet*2)
            return coins
        elif dealerTurnOutcome == "tie":
            coins = coins + bet
            return coins
        elif dealerTurnOutcome == "loss":
            return coins

# ---Main Program--- #
#Literally just the main program.
titleScreen() #Intro
foreverLoop = 0
while foreverLoop == 0: #To repeat the program until balance reaches 0 or balance < 0:
    coins = fullRound(coins,bet)
    deckOfCards = [2,3,4,5,6,7,8,9,10,"J","Q","K","A",2,3,4,5,6,7,8,9,10,"J","Q","K","A",2,3,4,5,6,7,8,9,10,"J","Q","K","A",2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
    hands = [[],[]]
    if coins == 0:
        print ("\n\033[1mYou are now broke. Get a job.\033[0m")
        foreverLoop = 1
    elif coins < 0 and coins > -1000:
        print ('''\n\033[1mYou are now in debt to BM INC.
You will now work off your debt under our supervision in the coal mines.\033[0m''')
        foreverLoop = 1
    elif coins <= -1000:
        print ('''\n\033[1mCongratulations player, you have reached an excess of $1,000,000 in coins worth of debt. 
As per your membership contract, your soul will now be extracted and sold off. 
BM INC. wishes you a pleasant labour filled eternity.
        ''')
        foreverLoop = 1
