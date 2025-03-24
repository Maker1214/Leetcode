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
nums = [1,1]
k = 1

# 方法1 : time complexcity is O(nlogn)
# res = []
# freq, times = {}, {}
# # 取得每個數字出現的次數
# for i in nums:
#     freq[i] = freq.get(i, 0) + 1
# # print(f"freq : {freq}")

# # 將出現出現次數的數字包進同一個 list 中，並用出現次數當作新字典的 key
# for f in freq:
#     times[freq[f]] = times.get(freq[f], []) + [f]
# # print(f"times : {times}")

# # 將新字典依照 key (出現次數)由大到小排序, the time complexcity of sorted is O(nlogn)
# sorted_times = sorted(times.keys(), reverse = True)
# # print(f"sorted_times : {sorted_times}")

# round = 0

# # 取得出現次數前 K 名的數字
# while k - len(res) > 0:
#     res += times[sorted_times[round]]
#     round += 1
#     # print(f"k : {k}, round : {round}")
    
# print(res)


# 方法2 : 將新字典依照 key (出現次數)由大到小排序，採用 bucket sort，the time complexcity of bucket sort is O(n)
def searchTopKFreq():
    times = [[] for c in range(len(nums) + 1)] # 數字最多出現len(nums)次，最少出現1次，(index[0]不會放次數)
    freq = {}
    res = []

    for i in nums:
        freq[i] = freq.get(i, 0) + 1

    for n, v in freq.items():
        times[v].append(n)

    for j in range(len(times) - 1, 0, -1):
        if times[j]: 
            res += times[j]
        if len(res) == k: return res

if __name__ == "__main__":
    result = searchTopKFreq()
    print(f"result = {result}")












