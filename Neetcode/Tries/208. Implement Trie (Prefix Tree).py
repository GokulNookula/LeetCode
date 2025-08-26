# OPTIMAL Solution
class TrieNode:
    # Initalizing a way to add nodes for the trie tree
    def __init__(self):
        # This will store all the children for
        # that node
        self.children = {}
        # This indicates if that child node
        # is the end of the word that was inserted or not
        self.endOfWord = False

class Trie:

    def __init__(self):
        # Creating an empty TrieNode
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        # Making a pointer to keep track of 
        # root node
        cur = self.root

        # Iterating through each character of the word
        for c in word:
            # Checking if that character is already
            # a child node inside the trie or not
            if c not in cur.children:
                # Creating a trie where the character
                # is the key which gives it's child nodes
                # like a, b, or c etc...
                cur.children[c] = TrieNode()
            # Else the character exists so we move
            # our cur pointer to that child node
            cur = cur.children[c]
        # Marking the end of the word for where we stopped cur pointer at
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        # Making a pointer to keep track of 
        # root node
        cur = self.root

        # Iterating through each character of the word
        for c in word:
            # Checking if that character is already
            # a child node inside the trie or not
            if c not in cur.children:
                # Since it is not we return false
                # as no such word exists yet in the trie
                return False
            # else if we found the character we move our
            # cur pointer to that children node pointer
            cur = cur.children[c]
        # Once we are done with the loop we check
        # if that word fully exists by looking at the end
        # character if it was marked as endOfWord like true or false
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        # Making a pointer to keep track of 
        # root node
        cur = self.root

        # Iterating through each character of the prefix 
        # aka part of the word
        for c in prefix:
            # Checking if that character is already
            # a child node inside the trie or not
            if c not in cur.children:
                # Since it is not we return false
                # as no such prefix exists yet in the trie
                return False
            # else if we found the character we move our
            # cur pointer to that children node pointer
            cur = cur.children[c]
        # We return true if we end the loop without touching
        # the if statement above as the cur pointer still
        # points to some child node that exists in the trie
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

'''Explained: Time Complexity: O(L) where L is the length of the input word or prefix
and Space Complexity: O(L * A)
A is the size of the alphabet (e.g., 26 for lowercase English letters)
'''
