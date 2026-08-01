t=int(input())
for i in range(t):
  a,b=map(int,input().split())
  list1=list(map(int,input().split()))
  list1.sort(reverse=True)
  coin=0
  power=0
  for x in list1:
    if x*2**power>=b:
      coin+=1
    else:
      power+=1
  print(coin)