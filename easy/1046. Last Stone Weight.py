# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.

# Return the weight of the last remaining stone. If there are no stones left, return 0.

 

# Example 1:

# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
# Example 2:

# Input: stones = [1]
# Output: 1
 

# Constraints:

# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000？?

import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        newStones = [-s for s in stones]
        heapq.heapify(newStones)

        while len(newStones) > 1:
            h1 = heapq.heappop(newStones)
            h2 = heapq.heappop(newStones)

            if h1 != h2:
                heapq.heappush(newStones, h1 - h2)        
        return 0 if len(newStones) == 0 else -newStones[0]
        



q = Solution()
print(q.lastStoneWeight([2,7,4,1,8,1]))