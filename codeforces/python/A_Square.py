import sys
input_data = sys.stdin.read().split()
if input_data:
    t = int(input_data[0])
    idx = 1
    
for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        c = int(input_data[idx+2])
        d = int(input_data[idx+3])
        idx += 4
        
        if a == b == c == d:
            print("YES")
        else:
            print("NO")