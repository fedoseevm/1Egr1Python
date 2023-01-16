a, b, c, d = map(int, input().split())

if a == c:
    if b >= d:  # 3 8 3 6
        print(d - c)
    else:       # 3 6 3 8
        print(b - a)
elif a < c:     # 3 6 7 9
    if b == c:
        print(0)
    elif b < c:
        print("NIE")
    else:
        if b >= d:
            print(d - c)
        else:
            print(b - c)
elif a > c:
    if d == a:
        print(0)
    elif d < a:
        print("Nie")
    else:
        if d >= b:
            print(b - a)
        else:
            print(d - c)
