# zad 1
#a, b , c = map(int, input().split())
#if c - b == b - a: print("ciag arytmetyczny", end=" ")
#if c / b == b / a: print("ciag geometryczny", end=" ")

#if a < b: print("rosnacy")
#if a > b: print("malejacy")

# zad 2
#suma = 0
#for i in range(104, 1000, 16):
#    suma += i
#print(suma)

# zad 3
#wielokr = 0
#ilosc = 0
#first = 0
#for i in range(99, 9, -1):
#    if i % 7 == 0:
#        wielokr = i
#        break
#for i in range(1000, wielokr):
#    if i % wielokr == 0:
#        first = i
#for i in range(first, 10000, wielokr):
#    ilosc += 1
#print(ilosc)

# zad 4
#ilosc = 0
#for i in range(10, 100):
#    if i // 10 >= 2 * (i % 10):
#        ilosc += 1
#print(ilosc)

# zad 5
#ilosc = 0
#suma = 0
#for i in range(100, 1000):
#    if (i % 100) * 100 > (i // 10) % 10 + (i % 10):
#        ilosc += 1
#        suma += i
#print(f"Ilosc: {ilosc}")
#print(f"Suma: {suma}")

# zad 6
#n = int(input())
#suma = 0
#i = 1
#while n > 0:
#    if i % 19 == 0:
#        suma += i
#        n -= 1
#    i = i + 1
#print(suma)

# zad 7
#n = int(input())
#suma = 0
#i = 999
#while n > 0:
#    if i % 37 == 0:
#        suma += i
#        n -= 1
#    i -= 1
#print(suma)

# zad 8
n = int(input())
suma = 0
for i in range(n):
    suma += (3 * i + 2) * ((-1) ** i)
print(suma)
