208. Implement Trie (Prefix Tree)
Medium

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings.
There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before),
and false otherwise.

boolean startsWith(String prefix) Returns true if there is a previously inserted string word that
has the prefix prefix, and false otherwise.

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

1. 澄清:
   edges cases

2. 易错点:
    when move to next, remeber to move to node.word[w], not node[w]

3. 思路
   3.1 define a node class, which has word dictionary as base structure and also isword boolean check


4.1.algorithm: o(n) time
class Node:
    def __init__(self):
        self.word = {}
        self.isword = False
class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.word:
                node.word[w]= Node()
            node = node.word[w]

        node.isword = True

    def search(self, word):
        node = self.root
        for w in word:
            if w not in node.word:
                return False
            node = node.word[w]

        return node.isword

    def startsWith(self, prefix):
        node = self.root
        for w in prefix:
            if w not in node.word:
                return False
            node = node.word[w]

        return True
