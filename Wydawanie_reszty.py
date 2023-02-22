# wydawanie reszty
x = int(input())
N = [200, 100, 50, 20, 10, 5, 2, 1]
reszta = []
for i in N:
    ilosc = x // i
    if ilosc > 0:
        x = x - ilosc * i
        #print(f"{i}zl razy {ilosc}")
        for j in range(ilosc):
            reszta.append(i)
for i in reszta:
    print(i)
