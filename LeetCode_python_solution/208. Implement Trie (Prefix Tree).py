'''
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.

题意：Trie树
思路：Trie树中的每个节点都是TrieNode，包括属性children和is_word，
属性children为字典，key是当前对应的字母，value为TrieNode，存储当前节点的后代节点，
is_word表示当前节点是否存储了一个单词
'''
import collections
class TrieNode:
# Initialize your data structure here.
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node=self.root
        for letter in word:
            node=node.children[letter]
        node.is_word=True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node=self.root
        for letter in word:
            node=node.children.get(letter)
            if node is None:
                return False
        return node.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node=self.root
        for letter in prefix:
            node=node.children.get(letter)
            if node is None:
                return False
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('apple')
param_2 = obj.search('apple')
print(param_2)
param_3 = obj.startsWith('appb')
print(param_3)