#with open("input.txt", 'r+') as f:
#    content = f.read()
#    f.seek(0, 0)
#    a = '.' * len(f.readlines())
#    f.seek(0, 0)
#    f.write(a + '\n' + content + '\n' + a)



with open("input.txt") as f:
    # 1) Pad each line with '.' on left and right
    raw_lines = [line.rstrip("\n") for line in f]
    lines = ['.' + line + '.' for line in raw_lines]

# 2) Add a '.' border row at the top and bottom
width = len(lines[0])
border = '.' * width
lines = [border] + lines + [border]

global_sum = 0
#while i < len(lines) - 1
for i in range(1, len(lines) - 1):
    l2 = lines[i]
    middle = list(l2)
    for char in range(1, len(l2)-1):
        
        if(l2[char] == '@'):
            atcount = 0
            for x in range(-1,2):
                for y in range(-1,2):
                    if lines[i + x][char + y] == '@':
                        atcount = atcount + 1
            if atcount <= 4:
                middle[char] = 'x'
                global_sum += 1          
    print(''.join(middle[1:-1]))
print(global_sum)
#            for j in range(0,3):
#                if lines[i]

    # process group of 3
    #print(l1, l2, l3)
    