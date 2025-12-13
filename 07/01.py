with open("input.txt") as f:
    arr = [list(line.rstrip("\n")) for line in f]   # list of list-of-chars

H = len(arr)
W = len(arr[0])
        
#print(arr[2])
splits = 0
for row in range(0,H):
    for col in range(0,W):
        if arr[row][col] == ".":
            continue
        elif arr[row][col] == "S":
            arr[row+1][col] = "|"
        elif arr[row][col] == "|" and row + 1 < H and arr[row+1][col] == ".":
            arr[row+1][col] = "|"
        elif arr[row][col] == "|" and row + 1 < H and arr[row+1][col] == "^":
            arr[row+1][col-1] = "|"
            arr[row+1][col+1] = "|"
            splits += 1



for row in arr:
    print(row)

print(splits)