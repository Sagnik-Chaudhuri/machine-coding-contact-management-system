from classes.Trie import Trie


class PhoneBook():
    def __init__(self) -> None:
        self.store = {}
        self.trie = Trie()

    def add_contact(self, name, number):
        self.store[name] = number
        self.trie.insert(name)

    def prefix_search_contact_by_name_key_press(self, name):
        self.trie.get_words_after_each_key_press(name)

    def prefix_search_contact_by_name(self, name):
        self.trie.get_words(name)

    def search_contact_by_number(self, lookup_number):
        found = False
        for name, number in self.store.items():
            if lookup_number == number:
                print("\nname", name, " number", number)
                found = True
                break
        if found is False:
            print("\nNumber not found in phonebook")
