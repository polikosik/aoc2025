import os

wartosc = 50  # aktualna pozycja 0..99
licz = 0      # ile razy trafiliśmy w 0

with open("input.txt") as f:
    for linia in f:
        rot = linia[0]          # 'R' lub 'L'
        skok = int(linia[1:])   # liczba kliknięć
        dodatek = 0

        # 1. Pełne obroty po 100 kliknięć – każdy daje dokładnie jedno 0
        while skok >= 100:
            skok -= 100
            dodatek += 1

        # Teraz skok < 100 – sprawdzamy, czy OGON przechodzi przez 0

        if rot == 'R':
            # przy ruchu w prawo: s -> s+1, s+2, ..., s+skok
            # trafimy w 0, jeśli:
            #   - nie startujemy z 0
            #   - skok >= (100 - wartosc)   (dystans do 0 w prawo)
            if wartosc != 0 and skok >= 100 - wartosc:
                dodatek += 1

            # aktualizacja pozycji bez użycia %
            wartosc = wartosc + skok
            if wartosc >= 100:
                wartosc -= 100   # jedno zawinięcie, bo skok < 100

        else:  # rot == 'L'
            # przy ruchu w lewo: s -> s-1, s-2, ..., s-skok
            # trafimy w 0, jeśli:
            #   - nie startujemy z 0
            #   - skok >= wartosc           (dystans do 0 w lewo)
            if wartosc != 0 and skok >= wartosc:
                dodatek += 1

            # aktualizacja pozycji bez użycia %
            wartosc = wartosc - skok
            if wartosc < 0:
                wartosc += 100    # jedno zawinięcie, bo skok < 100

        licz += dodatek

print(wartosc)
print(licz)
