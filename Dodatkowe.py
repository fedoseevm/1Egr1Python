n = int(input())
liczba1 = 0
liczba2 = 0
czy_pierwsza = True
for i in range(3, n + 1):
    for j in range(2, int(n ** 0.5) + 1):
        if i % j == 0:
            czy_pierwsza = False
            break
    if czy_pierwsza:
        i = liczba1
        exit()
liczba2 = n - liczba1
print(f"liczba {n} skada sie z liczb {liczba1} i {liczba2}")
