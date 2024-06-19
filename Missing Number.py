nums = [0,1,2,4,3]

realXor = 0
expectedXor = 0

for i in range(len(nums)):
    realXor ^= nums[i]
    expectedXor ^= i

print(realXor ^ expectedXor ^ len(nums))