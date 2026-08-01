import sys
n=int(sys.stdin.readline())
database={}
for _ in range(n):
    name=sys.stdin.readline().strip()
    if name not in database:
      print("OK")
      database[name]=1
    else:
      count=database[name]
      new_name=f"{name}{count}"
      print(new_name)
      database[name]+=1

  