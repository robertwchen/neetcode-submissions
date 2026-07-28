class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        self.prefixes = {}
    
    # hashmap stores key == postfix , value == prefix

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word: 
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True
        return
        
        # what 
    # at some node or root
    def search(self, word: str) -> bool:
        # try to find the word with dfs
        def dfs(word, node, i):
            if i > len(word): 
                return False

            if i == len(word):
                return node.end_of_word
            
            c = word[i]

            if c == '.':
                for c in node.children:
                    if dfs(word, node.children[c], i + 1):
                        return True
                
            elif c in node.children:
                if dfs(word, node.children[c], i + 1):
                    return True

            return False
        return dfs(word, self.root, 0)
            
             

            
            

            
            





        
