d=int(input())
for i in range(d):
    d=input()
    if len(d)>10:
        print(d[0]+str(len(d)-2)+d[-1])
    else:  
        print(d)