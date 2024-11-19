"""
Author: Sabrina Joseph
Date: 02-01-2024
Last Modified: 02-08-2024
Description: COP3502 - HW 2 - Blackjack
"""

from p1_random import P1Random

game_num = 1
rng = P1Random()
player_score = 0
dealer_score = 0
tie_score = 0
game_run = True

while game_run:
    # displaying round number
    print(f"START GAME #{game_num}")

    # automatically dealing a card to the player by generating a "random" number
    player_hand = 0
    card_num = rng.next_int(13) + 1

    # Ace
    if card_num == 1:
        print(f"\nYour card is a ACE!")
        player_hand += 1
    # Number cards
    elif 2 <= card_num <= 10:
        print(f"\nYour card is a {card_num}!")
        player_hand += card_num
    # Jack
    elif card_num == 11:
        print(f"\nYour card is a JACK!")
        player_hand += 10
    # Queen
    elif card_num == 12:
        print(f"\nYour card is a QUEEN!")
        player_hand += 10
    # King
    elif card_num == 13:
        print(f"\nYour card is a KING!")
        player_hand += 10

    # displaying hand value
    print(f"Your hand is: {player_hand}\n")

    # displaying menu options
    print("1. Get another card\n"
          "2. Hold hand\n"
          "3. Print statistics\n"
          "4. Exit")

    option = int(input("\nChoose an option: "))

    no_winner = True
    while no_winner:

        # If player were to choose option 1 from the menu
        if option == 1:
            card_num = rng.next_int(13) + 1

            # Ace
            if card_num == 1:
                print(f"\nYour card is a ACE!")
                player_hand += 1
            # Number cards
            elif 2 <= card_num <= 10:
                print(f"\nYour card is a {card_num}!")
                player_hand += card_num
            # Jack
            elif card_num == 11:
                print(f"\nYour card is a JACK!")
                player_hand += 10
            # Queen
            elif card_num == 12:
                print(f"\nYour card is a QUEEN!")
                player_hand += 10
            # King
            elif card_num == 13:
                print(f"\nYour card is a KING!")
                player_hand += 10

            # displaying hand value
            print(f"Your hand is: {player_hand}\n")

            # checking if the game requirements are met
            if player_hand == 21:
                player_score += 1
                game_num += 1
                print("\nBLACKJACK! You win!\n")
                player_hand = 0
                no_winner = False
            elif player_hand > 21:
                dealer_score += 1
                game_num += 1
                print("You exceeded 21! You lose.\n")
                no_winner = False
            else:
                # displaying menu options
                print("1. Get another card\n"
                      "2. Hold hand\n"
                      "3. Print statistics\n"
                      "4. Exit")
                option = int(input("\nChoose an option: "))

        # Option 2
        elif option == 2:
            dealer_hand = rng.next_int(11) + 16
            print(f"\nDealer's hand: {dealer_hand}")
            print(f"Your hand is: {player_hand}\n")

            # checking for who won
            if dealer_hand > 21:
                player_score += 1
                game_num += 1
                print("You win!\n")
                player_hand = 0

            elif dealer_hand == 21:
                dealer_score += 1
                game_num += 1
                print("Dealer wins!\n")
                player_hand = 0

            # Tie game
            elif player_hand == dealer_hand:
                tie_score += 1
                game_num += 1
                print("It's a tie! No one wins!\n")
                player_hand = 0

            # if the player's hand is closer to 21
            elif (abs(player_hand) - 21) > (abs(dealer_hand) - 21):
                player_score += 1
                game_num += 1
                print("You win!\n")
                player_hand = 0

            # if the dealer's hand is closer to 21
            elif (abs(player_hand) - 21) < (abs(dealer_hand) - 21):
                dealer_score += 1
                game_num += 1
                print("Dealer wins!\n")
                player_hand = 0

            no_winner = False

        # Option 3
        elif option == 3:
            print(f"\nNumber of Player wins: {player_score}\n"
                  f"Number of Dealer wins: {dealer_score}\n"
                  f"Number of tie games: {tie_score}\n"
                  f"Total # of games played is: {game_num - 1}\n"
                  f"Percentage of Player wins: {round(((player_score / (game_num-1)) * 100), 2)}%\n")
            # displaying menu options
            print("1. Get another card\n"
                  "2. Hold hand\n"
                  "3. Print statistics\n"
                  "4. Exit")
            option = int(input("\nChoose an option: "))

        # Option 4
        elif option == 4:
            no_winner = False
            game_run = False

        # Invalid Input
        else:
            print("\nInvalid input!\n"
                  "Please enter an integer value between 1 and 4.\n")
            # displaying menu options
            print("1. Get another card\n"
                  "2. Hold hand\n"
                  "3. Print statistics\n"
                  "4. Exit")
            option = int(input("\nChoose an option: "))
