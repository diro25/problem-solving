n=input()
luck_count=0
for digit in n:
  if digit=='4'or digit=='7':
    luck_count+=1
if luck_count==4 or luck_count==7:
  print("YES")
else:
  print("NO")
        
  

