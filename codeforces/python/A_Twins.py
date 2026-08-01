import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    coins = [int(x) for x in input_data[1:]]
    
    total_sum = sum(coins)
    coins.sort(reverse=True)
    
    my_sum = 0
    coin_count = 0
    
    for coin in coins:
        my_sum += coin
        coin_count += 1
        if my_sum > (total_sum - my_sum):
            break
            
    print(coin_count)

if __name__ == "__main__":
    main()