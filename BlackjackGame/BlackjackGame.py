import time
from Deck import Deck
from Card import Card

class BlackjackGame:
    deck = Deck()
    playAgain = 1
    playerWins = 0
    playerLosses = 0
    playerTies = 0

    while playAgain != -1:
        houseTotal = deck.draw_card().get_value(True) + deck.draw_card().get_value(True)
        playerTotal = deck.draw_card().get_value(True) + deck.draw_card().get_value(True)
        
        while houseTotal >= 21:
            houseTotal = deck.draw_card().get_value(True) + deck.draw_card().get_value(True)

        while playerTotal >= 21:
            playerTotal = deck.draw_card().get_value(True) + deck.draw_card().get_value(True)
        
        print("The House is showing: " + str(houseTotal))

        while playerTotal < 22:
            print("The Player's total is: " + str(playerTotal))
            time.sleep(1)
            choice = int(input("Would you like to hit or stand? \n\tEnter 1 for a hit or 0 for a stand: "))
            
            if choice == 0:
                break
            elif choice == 1:
                nextCard = deck.draw_card()
                print()
                print("The Player has been dealt " + str(nextCard.declare_card()))
                playerTotal += nextCard.get_value(True)
            else:
                print("Invalid option, try again");

        if playerTotal > 21:
            print("The Player has busted! You lose.")
            time.sleep(1)
            playerLosses += 1
        else:
            print("\nThe Player stands with " + str(playerTotal))
            print("The House will play next.\n")
            time.sleep(1)

            while houseTotal < 17:
                nextCard = deck.draw_card()

                print("The House takes another card")
                time.sleep(1)
                print("The House has been dealt " + str(nextCard.declare_card()))
                houseTotal += nextCard.get_value(True)

                if houseTotal >= 17 and houseTotal <= 21:
                    break
            
            print("The House stands with " + str(houseTotal))

            print()
            time.sleep(1)
            print("Game Results!")
            time.sleep(1)
            print()

            if houseTotal > 21:
                print("The House has busted! You win!")
                playerWins += 1
            elif houseTotal > playerTotal:
                print("The House wins! Sorry.")
                playerLosses += 1
            elif playerTotal > houseTotal:
                print("The Player wins! Congrats!")
                playerWins += 1
            else:
                print("The Player and House are tied")

        time.sleep(1)
        playAgain = int(input("Would you like to play again?\n\tEnter 1 to play again or -1 if you would like to quit: "))
        print()

    print("You have won", playerWins , "times")
    print("You have lost", playerLosses, "times")
    print("You have tied", playerTies, "times")
    print("Thanks for playing BlackJack!")


game = BlackjackGame()
