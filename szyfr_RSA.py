# Algorytm RSA
# szyfr RSA
#from hashlib import md5, sha256
#user = kamilek
#pass = nigeria123
#print(md5(b"lorem").hexdigest())
#print(md5(b"Iorem").hexdigest())
#print(md5(b"Lorem").hexdigest())

#x*a + y*b  = NWD(a, b)
#x*7 + y*11 = NWD(7,11) = 1
#8*7 - 5*11

# biore 2 duze liczby pierwsze
p = 13
q = 11

# szukam f = (p - 1) * (q - 1) tzw Funkcja Eulera
F = (p - 1) * (q - 1)

# Obliczam modul n = p * q
n = p * q

# wyznaczamy klucz publiczny e, ma on byc wzglednie perwszy z F
# algorytm Euklidesa...
# NWD(e, F) = 1
#np NWD(143, 7) = 1
# wyznaczamy klucz prywatny d, ma on byc wzglednie perwszy z n
NWD(d, n = 1)
