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


nums = [100,4,200,1,3,2]

def longestConSeq() -> int:
    temp = [0] * 219
    output, curr = 0, 0

    for i in nums:
        temp[i + 109] = 1
    
    for n in temp:
        if n:
            curr += 1
        else:
            curr = 0
        output = max(output, curr)

    return output


if __name__ == "__main__":
    res = longestConSeq()
    print(f"res = {res}")
