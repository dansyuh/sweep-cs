from random import randint
from datetime import date

grid = []
positions = {}

for it in range(0, 3):
    grid.append(["⬛️"] * 3)


def print_grid():
    for column in grid:
        print(" ".join(column))


def random_x():
    return randint(0, len(grid) - 1)


def random_y():
    return randint(0, len(grid[0]) - 1)


bomb1 = random_x()
bomb2 = random_y()

score = 0

print("""
💣 MINESWEEPER 💣

⛏️= IS GOOD
💣 = IS BAD
""")

for turn in range(4):
    x = int(input("What row you would like to select?\n"))
    y = int(input("What column would you like to select?\n"))

    if x > 3 or y > 3:
        continue

    if grid[x -1][y - 1] == "⛏️":
        print("You have already chosen this slot!")
        continue

    if bomb1 == x and bomb2 == y:
        grid[x - 1][y - 1] = "💣"
        print_grid()
        print("You loose! You hit the bomb! 💣")
        break

    if score == 3:
        print("""
        👑 YOU WIN! Congratulations you won the game!
        """)

        for it in positions:
            print(" ".join(it))
        break

    if score > 1:
        print(f"You need {3 - score} more misses to win!")

    grid[x - 1][y - 1] = "⛏️"
    positions[str(score)] = {
        "move": f"{x}, {y}",
    }

    score = score + 1
    print_grid()
    print(positions)
