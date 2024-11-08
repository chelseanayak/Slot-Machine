import random
import time

characters = ['Diamond', 'Ruby', 'Cherry', 'Sakura', 'Moon']

balance = 1000
min_bet = 10

character_odds = {
    'Diamond': 8,
    'Ruby': 5,
    'Cherry': 4,
    'Sakura': 3,
    'Moon': 2
}

def spin_slot_machine(winning_characters=None):
    if winning_characters:
        result = winning_characters
    else:
        result = [random.choice(characters) for _ in range(3)]
    print(f"DEBUG: Spin result: {result}")
    return result

def calculate_winnings(result, bets):
    total_winnings = 0
    for character, bet in bets.items():
        if all(c == character for c in result):
            total_winnings += bet * character_odds[character]
            print(f"DEBUG: Winning character: {character}, Bet: {bet}, Multiplier: {character_odds[character]}")
    if total_winnings == 0:
        print("DEBUG: No winning match for this round.")
    return total_winnings

def display_slot_machine(result):
    print("Slot Machine:")
    for _ in range(3):
        print(" | ".join(random.choice(characters) for _ in range(3)))
        time.sleep(1)
    print("Slot Machine Result:", result)

# Main game loop
while balance > 0:
    print("\nWelcome to the Slot Machine!")
    print(f"Your current balance: {balance}")
    print("Characters to choose from:")
    for index, character in enumerate(characters, 1):
        print(f"{index}. {character}")

    bets = {}
    while True:
        try:
            choice = int(input("Choose a character to bet on (1-5, 0 to stop selecting characters): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 0:
            break
        if choice < 1 or choice > 5:
            print("Invalid choice. Please select a valid character.")
            continue

        character = characters[choice - 1]

        try:
            bet = int(input(f"Place a bet on {character}: "))
        except ValueError:
            print("Please enter a valid bet amount.")
            continue

        if bet < min_bet:
            print(f"Minimum bet amount not met for {character}. Please try again.")
            continue
        if bet > balance:
            print("Insufficient balance. Please place a lower bet.")
            continue

        bets[character] = bet

    if not bets:
        print("No bets placed. Thanks for playing!")
        break

    balance -= sum(bets.values())

    winning_characters = [
        ['Diamond', 'Diamond', 'Diamond'],
        ['Ruby', 'Ruby', 'Ruby'],
        ['Cherry', 'Sakura', 'Moon']
    ]

    result = random.choice(winning_characters)

    display_slot_machine(result)
    winnings = calculate_winnings(result, bets)
    balance += winnings

    if winnings > 0:
        print(f"Congratulations! You won {winnings}!")
    else:
        print("Sorry, you lost.")

print("Out of funds. Thanks for playing!")
