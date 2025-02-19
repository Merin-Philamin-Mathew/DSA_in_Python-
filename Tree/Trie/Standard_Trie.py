class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        #a root node with an empty dict is created in the first initialization itelf
        self.root = TrieNode()
        self.end_symbol = '*'

    def insert(self, string):
        node = self.root
        for letter in string:
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

    def _collect_all_words(self, node, prefix, results):
        if self.end_symbol in node.children:
            results.append(prefix)
        
        for letter, next_node in node.children.items():
            if letter!=self.end_symbol:
                self._collect_all_words(next_node, prefix+letter, results)
    
    def autofill(self,prefix):
        node = self.root
        results = []
        # checking whether the prefix is existing 
        for letter in prefix:
            if letter not in node.children:
                return results
            node = node.children[letter]
        self._collect_all_words(node, prefix, results)
        return results
        

    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return self.end_symbol in node.children
    
trie = Trie()
trie.insert('neel')
trie.insert('night')
trie.insert('eight')
trie.insert('neat')
print(trie.contains("eel"))
print(trie.contains("night"))

print(trie.autofill("n"))  # ['neel', 'neat', 'night']
print(trie.autofill("ne"))  # ['neel', 'neat']
print(trie.autofill("e"))  # ['eight']