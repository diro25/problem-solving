n=int(input())
s=input().strip().lower()

if len(set(s)) == 26:
    print("YES")
else:
    print("NO")
