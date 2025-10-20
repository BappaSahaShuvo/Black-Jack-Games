import random
import os


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def show_logo():
    logo = r"""
    ██████╗ ██╗      █████╗  ██████╗██╗  ██╗      █████╗  ██████╗██╗  ██╗
    ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██╔══██╗██╔════╝██║ ██╔╝
    ██████╔╝██║     ███████║██║     █████╔╝█████╗███████║██║     █████╔╝ 
    ██╔══██╗██║     ██╔══██║██║     ██╔═██╗╚════╝██╔══██║██║     ██╔═██╗ 
    ██████╔╝███████╗██║  ██║╚██████╗██║  ██╗     ██║  ██║╚██████╗██║  ██╗
    ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                           🃏 BLACKJACK GAME 🃏
    """

    cards_demo = r"""
        ╔═════╗ ╔═════╗ ╔═════╗ ╔═════╗
        ║A    ║ ║K    ║ ║Q    ║ ║J    ║
        ║  ♠  ║ ║  ♥  ║ ║  ♦  ║ ║  ♣  ║
        ║    A║ ║    K║ ║    Q║ ║    J║
        ╚═════╝ ╚═════╝ ╚═════╝ ╚═════╝
    """

    print(logo)
    print(cards_demo)
    print("Welcome to the Ultimate Blackjack Experience!\n")

def deal_Cards():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate(cards):
    """Calculate the score from a list of cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    """Compare scores and return the result"""
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose. Opponent has Blackjack 😭"
    elif user_score == 0:
        return "Win with a Blackjack 😍"
    elif user_score > 21:
        return "You went over. You lose 😢"
    elif computer_score > 21:
        return "Opponent went over. You win ☺️"
    elif user_score > computer_score:
        return "You win 😎"
    else:
        return "You lose 😨"


def play_game():
    user_Cards = []
    computer_Cards = []
    is_game_over = False

    for _ in range(2):
        user_Cards.append(deal_Cards())
        computer_Cards.append(deal_Cards())

    while not is_game_over:
        user_score = calculate(user_Cards)
        computer_score = calculate(computer_Cards)

        print(f"Your cards: {user_Cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_Cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_Cards.append(deal_Cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_Cards.append(deal_Cards())
        computer_score = calculate(computer_Cards)

    print(f"\nYour final hand: {user_Cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_Cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play Blackjack? (y/n): ").lower() == "y":
    clear_screen()
    show_logo()
    play_game()
