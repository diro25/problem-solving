n=12
sum=0
for i in range(n+1):
  if i%2==0:
    continue
  else:
    sum+=i
print(sum)