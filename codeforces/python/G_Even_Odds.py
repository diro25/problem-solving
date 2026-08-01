n, k = map(int, input().split())
count_odds = (n + 1) // 2

if k <= count_odds:   
   print(2 * k - 1)
else:
    print(2 * (k - count_odds))