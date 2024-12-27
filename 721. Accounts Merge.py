# Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. 
# 
# Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

 

# Example 1:

# Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Explanation:
# The first and second John's are the same person as they have the common email "johnsmith@mail.com".
# The third John and Mary are different people as none of their email addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
# Example 2:

# Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
# Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
 

# Constraints:

# 1 <= accounts.length <= 1000
# 2 <= accounts[i].length <= 10
# 1 <= accounts[i][j].length <= 30
# accounts[i][0] consists of English letters.
# accounts[i][j] (for j > 0) is a valid email.

class UnionFind:
    def __init__(self, n: int):
        self.parent = [-1] * n
        self.rank = [0] * n
    
    def findRoot(self, x: int) -> int:
        if self.parent[x] == -1:
            return x
        self.parent[x] = self.findRoot(self.parent[x])
        return self.parent[x]
    
    def unionVertices(self, x: int, y: int):
        xRoot, yRoot = self.findRoot(x), self.findRoot(y)

        if xRoot == yRoot:
            return
        
        if self.rank[xRoot] < self.rank[yRoot]:
            self.parent[xRoot] = yRoot
        elif self.rank[yRoot] < self.rank[xRoot]:
            self.parent[yRoot] = xRoot
        else:
            self.parent[yRoot] = xRoot
            self.rank[xRoot] += 1

# class Solution:
#     def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
#         email2Account, res = {}, {}
#         n = len(accounts)
#         uf = UnionFind(n)
#         visitedName = set()
#         output = []
        

#         for idx, account in enumerate(accounts):
#             for email in list(set(account[1:])):
#                 if email not in email2Account or account[0] not in visitedName:
#                     email2Account[email] = idx
#                     res[idx] = res.get(idx, []) + [email]                            
#                 else: # this email exists, need to union it with the existed idx
#                     uf.unionVertices(email2Account[email], idx)
#             visitedName.add(account[0])

#         # Add the mails of non-parent Node into the list of the parent's Node
#         # Also add the name into the corresponding list
#         for key in res:
#             root = uf.findRoot(key)
#             if root != key: # this node has parent
#                 res[root] = res.get(root, []) + res[key]
#             else:
#                 res[root] = [accounts[root][0]] + res[root]

#         # sort the list from the 1st element, except for the name
#         for key, val in res.items():
#             if uf.findRoot(key) == key:
#                 temp = val[1:]
#                 temp.sort()
#                 output.append([val[0]] + temp)

#         return output

# Time : O(N)
class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        email2Account, emailGroup, res = {}, {}, []
        uf = UnionFind(len(accounts))
        
        for idx, account in enumerate(accounts):
            for emails in list(set(account[1:])):
                if emails not in email2Account:
                    email2Account[emails] = idx                         
                else: # this email exists, need to union it with the existed idx
                    uf.unionVertices(email2Account[emails], idx)        

        # Add the mails of non-parent Node into the list of the parent's Node
        for e, i in email2Account.items():
            root = uf.findRoot(i)
            emailGroup[root] = emailGroup.get(root, []) + [e]
        
        # Sort the email address and add the name into the this sorted list
        for index, email in emailGroup.items():
            res.append([accounts[index][0]] + sorted(email))
        
        return res

            
obj = Solution()
#accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
#accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
accounts = [["Ethan","Ethan1@m.co","Ethan2@m.co","Ethan0@m.co"],["David","David1@m.co","David2@m.co","David0@m.co"],["Lily","Lily0@m.co","Lily0@m.co","Lily4@m.co"],["Gabe","Gabe1@m.co","Gabe4@m.co","Gabe0@m.co"],["Ethan","Ethan2@m.co","Ethan1@m.co","Ethan0@m.co"]]
obj.accountsMerge(accounts)

        
        
