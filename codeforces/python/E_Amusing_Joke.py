import sys

def main():
    input_data = sys.stdin.read().split()
    if len(input_data) < 3:
        return
    
    guest_name = input_data[0]
    host_name = input_data[1]
    pile = input_data[2]
    
    combined = guest_name + host_name
    
    if sorted(combined) == sorted(pile):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()