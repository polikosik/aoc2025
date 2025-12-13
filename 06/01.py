import re

rows = []
operators = []

with open("input.txt") as f:
    lines = [ln.rstrip() for ln in f if ln.strip()]

    for ln in lines:
        nums = re.findall(r"\d+", ln)
        if nums:
            rows.append([int(x) for x in nums])
        else:
            opr = re.findall(r"[+*]", ln)
            if opr:
                operators.append(opr)

global_sum = 0
#print(len(rows[0]))
for c in range(0,len(rows[0])): #c = 0 
    col = [r[c] for r in rows]
    opr = operators[0][c]
    wynik = col[0]
    if opr == "+":
        for i in range(1, len(col)):
            wynik = wynik + col[i]
    if opr == "*":
        for i in range(1, len(col)):
            wynik = wynik * col[i]
    print(wynik)
    global_sum += wynik

print(global_sum)

#print(col)
#print(operators[0][0])