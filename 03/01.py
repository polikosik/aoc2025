
global_sum = 0
with open("input.txt") as f:
    for x in f:
        maxa = x[0]
        maxb = x[1]
        suma = int(maxa) + int(maxb)
        
        #print(suma)
        for i in range(0, len(x)):
            for j in range(i+1, len(x)):
                if int(x[i] + x[j]) > suma:
                    suma = int(x[i] + x[j])

        global_sum = global_sum + suma

print(global_sum)    
            