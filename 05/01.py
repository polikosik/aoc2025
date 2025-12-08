import re

with open("input.txt") as f:
    part1, part2 = f.read().strip().split("\n\n")  # split on blank line

# parse ranges
ranges = []
for line in part1.splitlines():
    m = re.match(r"(\d+)-(\d+)", line)
    first, second = map(int, m.groups())
    ranges.append((first, second))

# parse numbers
numbers = [int(x) for x in part2.splitlines() if x]

global_sum = 0

for n in numbers:
    # check if n is inside ANY range
    for first, second in ranges:
        if first <= n <= second:
            global_sum += 1
            break  # no need to check other ranges for this n

print(global_sum)
