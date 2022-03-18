from classes.TrieNode import TrieNode


class Trie():
    def __init__(self) -> None:
        self.__root = TrieNode()
        self.counter = 0

    def insert(self, word: str) -> None:
        itr = self.__root
        for i in range(0, len(word)):
            next_node = itr.children.get(word[i])
            if next_node is None:
                next_node = TrieNode()
                itr.children[word[i]] = next_node

            itr = next_node
            if i == len(word) - 1:
                itr.end = True

    def prefix_search_by_word(self, word):
        node = self.__root
        for char in word:
            if not node.children.get(char):
                return 0
            node = node.children.get(char)

        if not node.children:
            return -1

        self.get_word_suggestions(node, word)
        return 1

    def get_word_suggestions(self, node, word):
        if node.end:
            print(word)
            self.counter += 1

        for a, n in node.children.items():
            self.get_word_suggestions(n, word + a)

    def update_trie_by_word(self, lookup_word, new_word):
        found = True

        i = 0
        itr = self.__root
        prev = None
        while i < len(new_word):
            if lookup_word[i] == new_word[i] and itr.children.get(new_word[i]) is not None:
                i += 1
                prev = itr
                itr = itr.children[new_word[i]]
                continue
            else:

                break

        return None
