import os

#f = open("input.txt")

wartosc = 50
licz = 0

with open("input.txt") as f:
	for x in f:
		linia = x
		rot = linia[0]
		skok = int(linia[1:])
		while skok >= 100:
			skok = skok - 100
		#print(linia)
		if rot == 'R':
			wartosc = wartosc + skok
			if wartosc >= 100:
				wartosc = wartosc - 100
		else:
			wartosc = wartosc - skok
			if wartosc < 0:
				wartosc = wartosc + 100
		#print(wartosc)
		if wartosc == 0:
			licz = licz + 1

print(wartosc) 
print(licz) 


f.close()


#02 - 4 = -2 + 100 = 98 