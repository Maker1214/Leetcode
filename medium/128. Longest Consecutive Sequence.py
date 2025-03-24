# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
 

# Constraints:

# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9


nums = [0,3,7,2,5,8,4,6,0,1]

def longestConSeq() -> int:
    numSet = set(nums)
    longest = 0
    oldhead = set()

    for i in nums:
        length = 0
        # 代表 i 是連續數字序列的起頭，且後面還有下一個連續數字
        while(i not in oldhead and i - 1 not in numSet and i + length in numSet):
            length += 1
        # 若 nums 中有多個重複的數字序列起頭，例如 nums = [0,3,7,2,5,8,4,6,0,1] 中有兩個 0 為連續序列起頭，當檢查完第一個 0 後，不需要再重複檢查第二個 0
        if length:
            oldhead.add(i)
        longest = max(length, longest)
    
    return longest

if __name__ == "__main__":
    res = longestConSeq()
    print(f"res = {res}")
