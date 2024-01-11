nums = [1,2,3,1]
ans = []
x = nums.count(max(nums,key = nums.count))
print(x)
if x > 1:
    ans = True
else:
    ans = False
print(ans)

