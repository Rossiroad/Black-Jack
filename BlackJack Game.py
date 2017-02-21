import random
wins = 0
losses = 0
draws = 0
played = 0
play = True
go = "y"
blackjack = 0
def displaystats():
    print("wins:",wins,"losses:",losses,"draws:",draws,"Blackjacks:",blackjack)
          
username = input(str("Welcome to Black Jack, please enter in your username"))
while play == True:
    go = "y"
    totalcards = 0
    card1 = random.randint(1,10)
    card2 = random.randint(1,10)
    card3 = 0
    card4 = 0
    card5 = 0
    bankrupt = False
    BANKERupt = False #A brilliant pun for a variable name even though hes called the dealer and now the banker.

    print()
    print()
    print("--------------------------------------------------------------------------------")
    print()
    print("lets start the next round!")
    print(username,"goes first")
    print("Your first card is",card1,"and your second card is",card2)
    dealercard = random.randint(1,10)
    print("The dealers face up card is:",dealercard)

    if card1 == 1:
        card1 = int(input("You have an ace! do you want it to equal 1 or 11?"))
        if card1 == 1:
            print("thank you, you have selected one")
        elif card1 == 11:
            print("thanks, you've selected 11")
        else:
            print("you havent selected a valid option, therefore we will select one for you randomly")
            card1 = random.randint(1,2)
            if card1 == 2:
                card1 = 11
                print("your card now equals 11")
            else:
                print("your card now equals 1")

    if card2 == 1:
        card2 = int(input("You have an ace! do you want it to equal 1 or 11?"))
        if card2 == 1:
            print("thank you, you have selected one")
        elif card2 == 11:
            print("thanks, you've selected 11")
        else:
            print("you havent selected a valid option, therefore we will select one for you randomly")
            card2 = random.randint(1,2)
            if card2 == 2:
                card2 = 11
                print("your card now equals 11")
            else:
                print("your card now equals 1")


    again = input("would you like to draw another card? (enter anything for yes and n for no)")
    if again == "y":
        card3 = random.randint(1,10)
        print("your 3rd card is",card3)
        if card3 == 1:
            card3 = int(input("You have an ace! do you want it to equal 1 or 11?"))
            if card3 == 1:
                print("thank you, you have selected one")
            elif card3 == 11:
                print("thanks, you've selected 11")
            else:
                print("you havent selected a valid option, therefore we will select one for you randomly")
                card3 = random.randint(1,2)
                if card3 == 2:
                    card3 = 11
                    print("your card now equals 11")
                else:
                    print("your card now equals 1")
        totalcards = card1 + card2 + card3
        if totalcards < 21: 
                    again = input("would you like to draw another card? (enter y for yes and n for no)")
                    if again == "y":
                            card4 = random.randint(1,10)
                            print("your 4th card is",card4)
                            print("You cannot draw anymore cards")
                            if card4 == 1:
                                card4 = int(input("You have an ace! do you want it to equal 1 or 11?"))
                                if card4 == 1:
                                    print("thank you, you have selected one")
                                elif card4 == 11:
                                    print("thanks, you've selected 11")
                                else:
                                    print("you havent selected a valid option, therefore we will select one for you randomly")
                                    card4 = random.randint(1,2)
                                    if card4 == 2:
                                        card4 = 11
                                        print("your card now equals 11")
                                    else:
                                        print("your card now equals 1")
                    else:
                        print("You will hold on to your cards")
            
    else:
        print("you will hold onto your cards")

    totalcards = card1 + card2 + card3 + card4
    if totalcards > 21:
        print("you've gone bankrupt and have lost the game")
        losses = losses + 1
        displaystats()
        bankrupt = True
    else:
        print("the total value of your cards came up to",totalcards)
        if totalcards == 21:
            print("you got black jack! congratulations")
            blackjack = blackjack + 1
        else:
            print("")
    
    if bankrupt == False:
        print("dealers turn")
        dealercard = dealercard + random.randint(1,11)
        while dealercard < 17:
            dealercard = dealercard + random.randint(1,11)
            print("The dealer drew a card")
        print("the dealer's score is",dealercard)
        if dealercard > 21:
            BANKERupt = True
        else:
            print()
        if BANKERupt == False:
            if dealercard > totalcards:
                print("The dealer won, sorry")
                losses = losses + 1
                displaystats()
            elif dealercard < totalcards:
                print("You won, congratulations!")
                wins = wins + 1
                displaystats()
            else:
                print("Sorry, it looks like you had the same score")
                draws = draws + 1
                displaystats()
        else:
            print("the dealer went bankrupt!!!!")
            wins = wins + 1
            displaystats()

    print("would you like to play again? answer with the letter y for yes and n for no.")
    while go == "y":
        play = input("y or n?")
        print(play)
        if play == "y":
            print("good choice!")
            go = "n"
            play = True
        elif play == "n":
            print("you will stop playing, come back soon!")
            go = "n"
            play = False
        else:
            print("enter in y or n")

plays = wins + losses + draws
if wins != 0:
    score = round(wins / plays * 100 * wins + draws * 5)
    if blackjack != 0:
        for loop in range(blackjack):
            score = round(score * 1.164)
    else:
        print("")
else:
    score = plays + draws * 5
    
wins = str(wins)
losses = str(losses)
draws = str(draws)
score = str(score)
blackjack = str(blackjack)

print("username:",username)
displaystats()
print("overall score:",score)
scores = open("player_scores.txt","a")
scores.write("\n" + "username: " + username + "\n")
scores.write("wins:" + wins + " losses:" + losses + " draws:" + draws + " blackjacks:" + blackjack + "\n")
scores.write("overall score:" + score + "\n")
scores.close()

        
    
    


    
        




