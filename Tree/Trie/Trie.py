class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.end_symbol = '*'

    def suffixTrie(self,string):
        for i in range(len(string)):
            self.insert(i,string)

    def insert(self, index, string):
        node = self.root
        for i in range(index, len(string)):
            letter = string[i]
            if letter not in node.children:
                #creating a hashtable actually
                #empty dict children for new letter going to be added on the node
                new_node = TrieNode()
                #adding a key==letter to the hashtable of the previous node
                #and asigning the value of new key as new_node containg a fresh hashtable/dictionary
                node.children[letter] = new_node
            #asigning the dictionary of letter to node for again checking inside that in the next iteration
            node = node.children[letter]
        #giving an end symbol to the dictionary of last letter
        #showing there is a complete word exists
        node.children[self.end_symbol] = None

    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return self.end_symbol in node.children
    
trie = Trie()
trie.suffixTrie("neel")
print(trie.contains("eel"))