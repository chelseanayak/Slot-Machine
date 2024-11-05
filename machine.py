import numpy as np
import random
import time

# Define characters for the slot machine and their unique multipliers
symbols = {
    'Sun': 10,
    'Moon': 8,
    'Star': 6,
    'Comet': 4,
    'Meteor': 5,
    'Galaxy': 12
}

# Set the initial player balance
balance = 1000
min_bet = 10

# Function to perform a spin
def spin_reels():
    return [random.choice(list(symbols.keys())) for _ in range(3)]

# Calculate the payout based on the spin result and total bet
def calculate_payout(result, bet):
    payout = 0
    message = "No win this time!"

    # Special reward conditions
    if result[0] == result[1] == result[2]:
        # Triple match for jackpot
        payout = bet * symbols[result[0]]
        message = f"Jackpot! Triple {result[0]} matched!"

    elif len(set(result)) == 2:
        # Two symbols match for a minor win
        payout = bet * 3
        message = "Nice! Two of a kind. You get a minor win!"

    elif 'Sun' in result and 'Galaxy' in result:
        # Bonus win if Sun and Galaxy appear together
        payout = bet * 5
        message = "Special Bonus! Sun and Galaxy aligned!"

    return payout, message

# Display the spin animation and final result
def display_reels(result):
    print("Spinning the reels...")
    for _ in range(3):
        print(" | ".join(random.choice(list(symbols.keys())) for _ in range(3)))
        time.sleep(0.5)
    print("Final Result:", " | ".join(result))

# Main game loop
while balance >= min_bet:
    print(f"\nWelcome to Galactic Fortune! Current balance: ${balance}")
    print("Characters:", ", ".join(symbols.keys()))

    try:
        bet = int(input(f"Enter your total bet for this spin (minimum ${min_bet}, or 0 to exit): "))
        if bet == 0:
            print("Exiting game. Thanks for playing!")
            break
        if bet < min_bet or bet > balance:
            print(f"Invalid bet. Please enter an amount between ${min_bet} and ${balance}.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Deduct bet from balance
    balance -= bet

    # Spin and show results
    spin_result = spin_reels()
    display_reels(spin_result)

    # Calculate winnings and update balance
    winnings, message = calculate_payout(spin_result, bet)
    balance += winnings

    # Display result message
    print(message)
    if winnings > 0:
        print(f"You won ${winnings}!")
    else:
        print("Better luck next time!")

# End of the game
print("Game over! You're out of funds. Thanks for playing Galactic Fortune!")
