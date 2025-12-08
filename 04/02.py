def step(board):
    # board: list of strings without borders, only '.' and '@'

    # 1) add padding left/right
    padded = ['.' + row + '.' for row in board]

    # 2) add top/bottom border
    width = len(padded[0])
    border = '.' * width
    padded = [border] + padded + [border]

    new_rows = []
    removed = 0

    # 3) apply your neighbor rule
    for i in range(1, len(padded) - 1):
        l2 = padded[i]
        middle = list(l2)

        for char in range(1, len(l2) - 1):
            if l2[char] == '@':
                atcount = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if padded[i + x][char + y] == '@':
                            atcount += 1

                # your working rule: include self, <= 4
                if atcount <= 4:
                    middle[char] = 'x'
                    removed += 1

        # remove the horizontal border for the "core" row
        new_rows.append(''.join(middle[1:-1]))

    # 4) build next board: all 'x' become '.'
    next_board = [row.replace('x', '.') for row in new_rows]

    return next_board, removed, new_rows   # new_rows still has 'x' for printing


# --- main ---

with open("input.txt") as f:
    board = [line.rstrip("\n") for line in f]  # no borders here

total_removed = 0

while True:
    board, removed, view = step(board)

    if removed == 0:
        break

    total_removed += removed

print(total_removed)
