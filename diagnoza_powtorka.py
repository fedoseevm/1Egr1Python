# WSTEP
print("WSTEP")
# Zad 1
from cmath import sqrt
import random
def suma_cyfr_trzycyfrowych():
    suma = 0
    for i in range(100, 1000):
        suma += i
    return suma
print(f"Zadanie 1: {suma_cyfr_trzycyfrowych()}")
print("\n")

# Zad 2
def zad_2():
    suma = 0
    ilosc = 0
    for i in range(10, 100):
        if i % 6 == 0:
            suma += i
            ilosc += 1
    return suma, ilosc
print(f"Zadanie 2: {zad_2()}")
print("\n")

# Zad 3
def zad_3():
    l = []
    for i in range(5):
        l.append(random.randint(1000, 10000))
    return max(l)
print(f"Zadanie 3: {zad_3()}")
print("\n")

# Zad 4
def zad_4(x):
    suma = 0
    while x > 0:
        suma += x % 10
        x =x // 10
    return suma
n = random.randint(10, 10000)
print(f"Zadanie 4: liczba losowa: {n}; Suma cyfr: {zad_4(n)}")
print("\n")

# Zad 5
x = int (input())
def zad_5(n):
    min_cyfra = n
    while n > 0:
        if (min_cyfra > n % 10):
            min_cyfra = n % 10
        n //= 10
    return min_cyfra
print(f"Zadanie 5: liczba: {x}; Najmniejsza cyfra: {zad_5(x)}")
print("\n")
print("\n")
print("\n")



# ALGORYTMY
print("ALGORYTMY")
# Zad 1
a = int(input())
def czy_pierwsza(a):
    #flaga = True
    for i in range(2, int(sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True
print(f"Zadanie 1: {czy_pierwsza(a)}")
print("\n")
