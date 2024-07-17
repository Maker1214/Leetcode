# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


# [1,2,5,3,6,7,4,8,10,11]
nums = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]
k = 10
res = []

freq, times = {}, {}

for i in nums:
    freq[i] = freq.get(i, 0) + 1
# print(f"freq : {freq}")

for f in freq:
    times[freq[f]] = times.get(freq[f], []) + [f]
# print(f"times : {times}")
sorted_times = sorted(times.keys(), reverse = True)
# print(f"sorted_times : {sorted_times}")

round = 0

while k - len(res) > 0:
    res += times[sorted_times[round]]
    round += 1
    # print(f"k : {k}, round : {round}")
    
print(res)







