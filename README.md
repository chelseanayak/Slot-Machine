# 🎰 Slot Machine Game (Python)

This is a simple **console-based Slot Machine game** written in **Python**.  
The player starts with a fixed balance, places bets on characters, spins the slot machine, and wins rewards based on matching results.

---

## 📌 Features

- 🎲 Random slot machine spins  
- 💰 Betting system with minimum bet limit  
- 🧮 Different payout multipliers for each character  
- 🖥️ Animated slot display using time delays  
- 🧪 Debug messages for learning and testing  

---

## 🎭 Characters & Multipliers

| Character | Multiplier |
|---------|------------|
| Diamond | 8× |
| Ruby   | 5× |
| Cherry | 4× |
| Sakura | 3× |
| Moon   | 2× |

---

## ⚙️ How the Game Works

1. Player starts with **1000 balance**
2. Minimum bet per character is **10**
3. Player can bet on **multiple characters in one round**
4. The slot machine spins **3 symbols**
5. **Winning Condition:**
   - All 3 symbols must be the same as the character you bet on
6. Winnings = `Bet × Character Multiplier`
7. Game continues until:
   - Player runs out of balance  
   - OR chooses not to place any bet

---

## ▶️ How to Run the Game

### Prerequisites
- Python 3.x installed on your system

### Run Command
```bash
python slot_machine.py



output
Welcome to the Slot Machine!
Your current balance: 1000
Slot Machine Result: ['Diamond', 'Diamond', 'Diamond']
Congratulations! You won 160!
