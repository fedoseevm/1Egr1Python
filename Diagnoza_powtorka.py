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

# Zad 2
b = int(input())
def czy_zlozona(b):
    for i in range(2, int(b ** 0.5) + 1):
        if b % i == 0:
            return "Zlożona"
    return "Pierwsza"
print(f"Zadanie 2: {czy_zlozona(a)}")
print("\n")

# Zad 3
l, m = map(int, input().split())
def czy_wzglednie_pierwsze(l, m):
    while m > 0:
        l, m = m, l % m
    if l == 1:
        return "Względnie pierwsze"
    return "Nie Względnie piersze"
print(f"Zadanie 3: {czy_wzglednie_pierwsze(l, m)}")
print("\n")

# Zad 4
slowo = input()
def szyfr_cezara(slowo):
    szyfr = ""
    for i in range(len(slowo)):
        szyfr += chr(65 + (ord(slowo[i]) - 65 + 3) % 26)
    return szyfr
print(f"zadanie 4: {szyfr_cezara(slowo)}")
print("\n")

# Zad 5
a, b = map(int, input().split("/"))
c, d = map(int, input().split("/"))

def dodawanie_ulamkow(a, b, c, d):
    wynik = (f"{a}/{b} + {c}/{d} = ")
    nww = b * d // gcd(b, d)
    a, b = a * (nww // b) + c * (nww // d), nww
    a, b = a // gcd(a, b), b // gcd(a, b)
    if a < b:
        wynik += (f"{a}/{b}")
    else:
        iloczyn = a // b
        a -= iloczyn * b
        if a == 0:
            wynik += (f"{iloczyn}")
        else:
            wynik += (f"{iloczyn}({a}/{b})")
    return wynik

print(f"zadanie 5: {dodawanie_ulamkow(a, b, c, d)}")
print("\n")
