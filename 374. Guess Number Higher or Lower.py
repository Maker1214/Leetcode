# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1 , n
        g = (l + r) >> 1
        res = guess(g)
        while res:
            if res == 1:
                l = g + 1
            else:
                r = g - 1
            g = (l + r) >> 1
            res = guess(g)
        
        return g

# Python : 2nd 寫法
# class Solution:
#     def guessNumber(self, n: int) -> int:
#         l, r = 1 , n
#         while True:
#             m = (l + r) >> 1
#             res = guess(m)
#             if res == 1:
#                 l = m + 1
#             elif res == -1:
#                 r = m - 1
#             else:
#                 return m

# C code:
# /** 
#  * Forward declaration of guess API.
#  * @param  num   your guess
#  * @return 	     -1 if num is higher than the picked number
#  *			      1 if num is lower than the picked number
#  *               otherwise return 0
#  * int guess(int num);
#  */

# int guessNumber(int n){
# 	int l = 0, r = n;
#     int m = (l + r) / 2;
#     int res = guess(m);
#     while(res){
#         if (res == 1){
#             l = m + 1;
#         }
#         else{
#             r = m - 1;
#         }
#         m = l + (r - l) / 2;
#         res = guess(m);
#     }

#     return m;
# }


