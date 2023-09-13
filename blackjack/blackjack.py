import random

def deal_card():
    return random.randint(1, 11)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def blackjack():
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    
    print("Your cards:", user_cards)
    print("Computer's first card:", computer_cards[0])
    
    while calculate_score(user_cards) != 0 and calculate_score(computer_cards) != 0:
        should_continue = input("Type 'y' to get another card, 'n' to pass: ")
        if should_continue == 'y':
            user_cards.append(deal_card())
            print("Your cards:", user_cards)
        else:
            break

    while calculate_score(computer_cards) < 17:
        computer_cards.append(deal_card())

    print("Your final hand:", user_cards)
    print("Computer's final hand:", computer_cards)

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your final score: {user_score}")
    print(f"Computer's final score: {computer_score}")

    if user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Computer went over. You win!"
    elif user_score == computer_score:
        return "It's a draw!"
    elif user_score == 0 or user_score > computer_score:
        return "You win!"
    else:
        return "Computer wins!"

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    print(blackjack())
