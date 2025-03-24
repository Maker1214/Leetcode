# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

# Example 1:

# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.
# Example 2:

# Input: n = 1, bad = 1
# Output: 1
 

# Constraints:

# 1 <= bad <= n <= 231 - 1

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        L, R = 1, n

        while L <= R:
            M = L + ((R - L) >> 1)
            V = isBadVersion(M)

            if V:
                res = M
                R = M - 1
            else:
                L = M + 1
        
        return res


# C code
# // The API isBadVersion is defined for you.
# // bool isBadVersion(int version);

# int firstBadVersion(int n) {
#     int L = 1, R = n, M, res, V = true;

#     while (L <= R){
#         M = L + ((R - L) >> 1);
#         V = isBadVersion(M);

#         if (V){
#             R = M - 1;
#             res = M;
#         }
#         else{
#             L = M + 1;
#         }
#     }
#     return res;
# }