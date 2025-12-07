
f = open("input.txt")
import re
#with open("input.txt") as f:


dataset = f.read().split(",")

global_sum = 0

for pair in dataset:
    
    first = int(re.findall(r'(\d+)-', pair)[0])
    second = int(re.findall(r'-(\d+)', pair)[0])
    #print(first)
    #first_char = str(first)
    #print(len(first_char))

    while first < second:
        first_char = str(first)
        if len(first_char) % 2 == 0:
            half = int(len(first_char) / 2)

            flag = 1
            for i in range(0,half):
                if first_char[i] != first_char[half + i]:
                    flag = 0
            if flag == 1:
                print(first_char)
                global_sum = global_sum + first
        
        first = first + 1

print(global_sum)

f.close()