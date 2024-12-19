# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

# Example:

# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Outputx
# [null,null,null,null,false,true,true,true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
 

# Constraints:

# 1 <= word.length <= 25
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
# There will be at most 2 dots in word for search queries.
# At most 104 calls will be made to addWord and search.

class TrieNode:
    def __init__(self):
        self.links = {}
        self.isEnd = False

class WordDictionary:
    def __init__(self): 
        self.root = TrieNode()    

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.links:
                curr.links[c] = TrieNode()
            curr = curr.links[c]
        curr.isEnd = True
        
    def search(self, word: str) -> bool:

        def dfs(curr, word):
            for idx, c in enumerate(word):
                if c == '.':
                    for link in curr.links.values():
                        if dfs(link, word[idx + 1:]):
                            return True
                    return False
                else:
                    if c not in curr.links:
                        return False
                    curr = curr.links[c]            
            return curr.isEnd

        return dfs(self.root, word)
                


            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)