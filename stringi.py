# stringi
s = input()
L = list(s)     # list() - przetwarza slowo w liste
print(s, L)
L.sort()
print(s, L)
s = "-".join(L) # slkeje elementy listy w jeden wyraz
print(s, L)

# sprawdz czy podane slowo jest palindromem

slowo = input()
L = list(slowo)
R = L.copy
#R = list(slowo)
R.reverse()
if L == R:
    print("pallindrom")
else:
    print("nie jest")
