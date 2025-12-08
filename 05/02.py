import re

with open("input.txt") as f:
    part1, part2 = f.read().strip().split("\n\n")  # split on blank line

# parse ranges
ranges = []


for line in part1.splitlines():
    m = re.match(r"(\d+)-(\d+)", line)
    first, second = map(int, m.groups())
    ranges.append((first, second))

ranges.sort()

total = 0
cur_start, cur_end = ranges[0]

for start, end in ranges[1:]:
    if start > cur_end:
        total += cur_end - cur_start + 1
        cur_start = start
        cur_end = end
    else:
        if end > cur_end:
            cur_end = end


total += cur_end - cur_start + 1
print(total)