t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    odd = sum(1 for v in arr if v % 2)
    even = n - odd

    possible = False

    for k in range(1, min(odd, x) + 1, 2):   
        if x - k <= even:
            possible = True
            break

    print("Yes" if possible else "No")