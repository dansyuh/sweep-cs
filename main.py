from random import randint

grid = []

print("Simplified MineSweeper - CS Class Project")

for it in range(0, 3):
    grid.append(["⬛️"] * 3)


def print_grid():
    for column in grid:
        print(" ".join(column))


def random_x():
    return randint(0, len(grid) - 1)


def random_y():
    return randint(0, len(grid[0]) - 1)


randomX = random_x()
randomY = random_y()

score = 0

for turn in range(4):
    x = int(input("What row you would like to select?\n"))
    y = int(input("What column would you like to select?\n"))

    if x > 3 or y > 3:
        continue

    if grid[x - 1][y - 1] == "⛏️":
        print("You have already selected this slot, please input a new entry.")
        continue

    if randomX == x and randomY == y:
        grid[x - 1][y - 1] = "💣"
        print_grid()
        print("You loose! You hit the bomb! 💣")
        break

    if score == 3:
        print("You win! You did not hit the bomb! 👑")
        break

    if score > 1:
        print(f"You need {3 - score} more misses to win!")

    grid[x - 1][y - 1] = "⛏️"
    score = score + 1

    print_grid()
