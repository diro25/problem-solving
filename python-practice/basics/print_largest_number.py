n=int(input())
nums=list(map(int,input().split()))
max_val=nums[0]
max_num=0
for i,num in enumerate(nums):
    if num>max_val:
        max_val=num
        max_num=i
print(max_num)