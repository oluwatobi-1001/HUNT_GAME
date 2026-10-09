# 🏝️ Treasure Quest

A small text adventure game written in Python. You land on Treasure Island, make three choices, and try to find the treasure. One wrong choice and it's GAME OVER.

Built as part of my 100 Days of Coding journey.

## How the game works

1. You arrive at a crossroad and choose left or right.
2. If you go left, you reach a lake with an island in the middle. You choose to wait for a boat or swim.
3. If you wait, a boat takes you safely to the island, where there is a house with three doors: red, yellow and blue.
4. You pick a door. Only one door leads to the treasure.

### Game map

flowchart TD
    A[Crossroad] -->|left| B[Lake with an island]
    A -->|right| X1[Wrong path: GAME OVER]
    B -->|wait| C[House with 3 doors]
    B -->|swim| X2[Tried to swim across the lake: GAME OVER]
    C -->|yellow| W[You found the treasure: YOU WIN]
    C -->|red| X3[Dangerous room: GAME OVER]
    C -->|blue| X4[Room filled with water: GAME OVER]
    C -->|anything else| X5[Not an available door: GAME OVER]
### Outcomes

| Choice | Result |
|---|---|
| left, wait, yellow | 🏆 You win! |
| left, wait, red | 🔥 Dangerous room, game over |
| left, wait, blue | 🌊 Room filled with water, game over |
| left, wait, any other colour | Not one of the available doors, game over |
| left, swim (or anything except wait) | You tried to swim across the lake, game over |
| right (or anything except left) | You chose the wrong path, game over |

## Requirements

- Python 3
- No extra libraries needed

## How to run

1. Save the code as hunt.py.
2. Open a terminal in the folder that contains the file.
3. Run:

python hunt.py
## Example play-through (winning path)

Welcome to Treasure Island!
Your mission is to find the treasure.
You're at a crossroad. Where do you want to go?

Type 'left' or 'right': left

You come to a lake.
There is an island in the middle of the lake.
You wait for a boat.

Type 'wait' to wait for a boat or 'swim' to swim: wait

A boat arrives and takes you to the island.
You arrive at the island unharmed.

There is a house with 3 doors.
One red, one yellow and one blue.

Which colour do you choose? yellow

🎉 You found the treasure!
🏆 YOU WIN! CONGRATULATIONS!
## What I practised

- print() and input() for talking to the player
- .lower() so answers work in any letter case (Left, LEFT, left)
- if, elif and else to follow the player's choices
- Nested conditions: choices inside choices
- Writing multi-line text art with triple quotes

## Author

Oluwatobi Patience Oyelude
GitHub: [oluwatobi-1001](https://github.com/oluwatobi-1001)
