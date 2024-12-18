# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

# Example 1:

# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
 

# Constraints:

# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 104 calls in total will be made to insert, search, and startsWith.

class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        
        curr.end = True        

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.child:
                return False
            curr = curr.child[c]
        
        return curr.end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.child:
                return False
            curr = curr.child[c]
        
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)




# c code
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

# 定義 TrieNode 節點結構
typedef struct TrieNode {
    struct TrieNode *children[26]; # 子節點指針陣列
    bool isEnd;                    # 是否為單詞結尾
} TrieNode;


# 創建一個新的 TrieNode 節點
TrieNode* createNode() {
    TrieNode *node = (TrieNode*)malloc(sizeof(TrieNode));
    for (int i = 0; i < 26; i++) {
        node->children[i] = NULL;
    }
    node->isEnd = false;
    return node;
}

# 定義 Trie 結構
typedef struct {
    TrieNode *root;
} Trie;

# 創建一個新的 Trie
Trie* trieCreate() {
    Trie *trie = (Trie*)malloc(sizeof(Trie));
    trie->root = createNode();
    return trie;
}

# 插入單詞
void trieInsert(Trie* obj, char *word) {
    TrieNode *node = obj->root;
    for (int i = 0; word[i] != '\0'; i++) {
        int index = word[i] - 'a'; // 計算字母在 children 中的位置
        if (node->children[index] == NULL) {
            node->children[index] = createNode(); // 如果不存在子節點，創建新節點
        }
        node = node->children[index];
    }
    node->isEnd = true; // 標記為單詞結尾
}

# 搜索完整單詞
bool trieSearch(Trie* obj, char *word) {
    TrieNode *node = obj->root;
    for (int i = 0; word[i] != '\0'; i++) {
        int index = word[i] - 'a';
        if (node->children[index] == NULL) {
            return false; // 子節點不存在，返回 false
        }
        node = node->children[index];
    }
    return node->isEnd; // 是否為單詞結尾
}

# 搜索前綴
bool trieStartsWith(Trie* obj, char *prefix) {
    TrieNode *node = obj->root;
    for (int i = 0; prefix[i] != '\0'; i++) {
        int index = prefix[i] - 'a';
        if (node->children[index] == NULL) {
            return false; // 子節點不存在，返回 false
        }
        node = node->children[index];
    }
    return true; // 遍歷到結尾，返回 true
}

# 釋放 Trie 節點記憶體
void freeNode(TrieNode* node) {
    for (int i = 0; i < 26; i++) {
        if (node->children[i] != NULL) {
            freeNode(node->children[i]);
        }
    }
    free(node);
}

# 釋放整個 Trie
void trieFree(Trie* obj) {
    freeNode(obj->root);
    free(obj);
}

# /**
#  * Your Trie struct will be instantiated and called as such:
#  * Trie* obj = trieCreate();
#  * trieInsert(obj, word);
 
#  * bool param_2 = trieSearch(obj, word);
 
#  * bool param_3 = trieStartsWith(obj, prefix);
 
#  * trieFree(obj);
# */