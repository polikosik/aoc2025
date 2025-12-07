
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

    while first <= second: 
        first_char = str(first)

        for i in range(1, int(int(len(first_char))/2)+ 1): # 123123
            block = first_char[:i]              # 123 i=3
            #print(first_char)
            #print(block)                        #
            #print(block * int((len(first_char)/len(block))) )     # 123 * 6/3 = 123* 2
            if block * int((len(first_char)/len(block)))  == first_char:     # 
                #print("kutas")
                #print(first)
                global_sum = global_sum + first
                break

        first = first + 1
         # 1212
#        if len(first_char) % 2 == 0:
#            half = int(len(first_char) / 2)
#
#            flag = 1
#            for i in range(0,half):
#                if first_char[i] != first_char[half + i]:
#                    flag = 0
#            if flag == 1:
#                print(first_char)
#                global_sum = global_sum + first
#        
#        first = first + 1

print(global_sum)

f.close()