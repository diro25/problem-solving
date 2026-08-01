import sys
import math

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    a = int(math.sqrt(n))
    
    while n % a != 0:
        a -= 1
        
    b = n // a
    print(a, b)

if __name__ == "__main__":
    main()