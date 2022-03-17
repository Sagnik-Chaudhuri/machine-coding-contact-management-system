from string import ascii_letters
from classes.TrieNode import TrieNode


class Trie():

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        length = len(word)
        itr = self.root
        for i in range(0, length):
            nextNode = itr.children.get(word[i])
            if nextNode is None:
                nextNode = TrieNode()
                itr.children[word[i]] = nextNode

            itr = nextNode
            if i == length - 1:
                itr.end = True

    def get_words_after_each_key_press(self, word):
        prevNode = self.root
        prefix = ""
        length = len(word)
        i = 0
        while (i < length):
            prefix += word[i]
            last_char = prefix[i]
            currNode = prevNode.children.get(last_char)

            if currNode is None:
                print('\nNo results Found for ', prefix)
                i += 1
                break

            print('\nsuggestions for: ', prefix, ' are: ')
            self.display_words_util(currNode, prefix)

            prevNode = currNode
            i += 1

        while (i < length):
            prefix += word[i]
            print("no results found for ", prefix)

    def display_words_util(self, currNode, prefix):
        if currNode.end is True:
            print(prefix)

        for char in ascii_letters:
            nextNode = currNode.children.get(char)
            if nextNode is not None:
                # print("prefix: ", prefix[-1], "char", char)
                self.display_words_util(nextNode, prefix + char + "")

    def get_words(self, word):
        node = self.root
        for char in word:
            if not node.children.get(char):
                return 0
            node = node.children.get(char)

        if not node.children:
            return -1

        self.name_suggestions(node, word)
        return 1

    def name_suggestions(self, node, word):
        if node.end:
            print(word)

        for a, n in node.children.items():
            self.name_suggestions(n, word + a)
