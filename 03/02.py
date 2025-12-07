
global_sum = 0
with open("input.txt") as f:
    for x in f: 
        i = 0
        final = ['0'] * 12
        linijka = x.strip()
        pos = 0
        while i < 12:
            remaining_after = 12 - (i + 1)
            for j in range(pos, len(linijka) - remaining_after): # 7; 15 - 7 = 8
                if int(linijka[j]) > int(final[i]):
                    final[i] = linijka[j]
                    pos = j + 1
            i = i + 1
        global_sum = global_sum + int(''.join(final))
        print(int(''.join(final)))


print(global_sum)               