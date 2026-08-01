x=int(input())
full_Step=x//5
remaining_Step=x%5
if remaining_Step==0:
    print(full_Step)
else:
    print(full_Step+1)
