napis = input()
print("1.", napis[0], napis[-1])
print("\n")

L = list(napis)
print("2.", L[1:-1])
print("\n")

print("3.", napis[-1:-5:-1])
print(napis[:-5:-1])
print("\n")

suma = 0
k = 0
for i in range(len(napis)):
    suma += ord(napis[i])
    if napis[i] == "A" or napis[i] == "a":
        k += 1
print("4.", suma)
print("\n")

print("5.", napis.count('a'))
# ALBO TAK
print("5.", k)
print("\n")

ilosc = 0
for i in range(len(napis)):
    l = 0
    for j in range(i, len(napis)):
        if napis[i] == napis[j]:
            l += 1
        else:


