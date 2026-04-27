# Snake & Ladder Game (2-Player, Terminal-Based)

A classic Snake & Ladder game for two players, playable directly in the terminal.

## Description

Two players take turns rolling a dice and moving along a board numbered from 1 to 100.
- Landing on a **ladder** bottom sends you up to the top.
- Landing on a **snake** head sends you down to its tail.
- The first player to land **exactly on 100** wins.

## Board Layout

| Type   | From | To |
|--------|------|----|
| Snake  | 16   | 6  |
| Snake  | 48   | 30 |
| Ladder | 3    | 22 |
| Ladder | 20   | 38 |

## Rules

- Players start at position **0** (before square 1).
- Each turn, a player rolls a dice (`random.randint(1, 6)`).
- If a roll would move a player **past 100**, they stay at their current position.
- Players can share the same cell without affecting each other.
- A player must land on **exactly 100** to win.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/Azo5340/Final_Project_CMPSC132.git
```
2. Navigate into the project folder:

```bash
cd Final_Project_CMPSC132
```
3. Run the game:
 - On **macOS / Linux**:

```bash
python3 snake_and_ladder.py
```
   - On **Windows**:

```bash
 python snake_and_ladder.py
```
> Requires Python 3.x — no additional libraries needed.

## Author for this project

Adam Ouareth




