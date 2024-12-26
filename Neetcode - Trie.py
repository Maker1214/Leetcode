class TrieNode:
    def __init__(self):
        self.links = {} # use hashMap to record all children links below this parent node. All links are Node which includes two components(links and isEnd)
        self.isEnd = False # use this componebt to identify if this char is the latest char of the word or not
    
    def Add(self, word):
        curr = self

        for w in word:
            if w not in curr.links:
                curr.links[w] = TrieNode()            
            curr = curr.links[w]
            
            curr.isEnd = True
        
    def Search(self,word):
        curr = self

        for w in word:
            if w in curr.links:
                curr = curr.links[w]
        
        return curr.isEnd

    def SearchPrefix(self,word):
        curr = self

        for w in word:
            if w not in curr.links:
                return False
            curr = curr.links[w]
        
        return True
    

    def Remove(self,word):
        curr = self
        keyNodePair = []

        for w in word:
            keyNodePair.append((w, curr)) # take "oa" as an example. The pair is [('o', self), ('a', self.links['o'])]
            curr = curr.links[w]
        
        i = 0
        for childKey, parentNode in reversed(keyNodePair):
            childNode = parentNode.links[childKey]

            if i == 0: # the first childKey must be the last char of the word. 
                childNode.isEnd = False
            if len(childNode.links) == 0: # No element in this childNode and we can delete it
                del childNode
            else: # multi path
                return
            i += 1 # We only need to change isEnd once for a word
