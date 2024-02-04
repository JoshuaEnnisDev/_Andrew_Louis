from random import randint


while True:
    # simulate drawing two cards
    player_cards = randint(1, 20)
    dealer_cards = randint(1, 20)

    print(f"Player's hand: {player_cards}")

    # ask if they want to hit or stand
    choice = int(input("Do you want to (1) hit or (2) stand?"))

    if choice == 1:
        draw = randint(1, 10)
        print(f"Player draws a {draw}")
        player_cards += draw

    print(f"Player's hand: {player_cards}")
    print(f"Dealer's hand: {dealer_cards}")

    # Decide who wins
    if player_cards > 21:
        print("Player Busts!")
    elif dealer_cards > player_cards:
        print("Dealer Wins!")
    elif player_cards > dealer_cards:
        print("Player wins!")
    elif player_cards == dealer_cards:
        print("It's a draw")
    print("######################################")
    print("######################################")
