from classes.Trie import Trie


class PhoneBook():
    def __init__(self) -> None:
        self.__store = {}
        self.__first_name_trie = Trie()
        self.__number_trie = Trie()
        self.__last_name_trie = Trie()

    def _validate_contact(self, first_name, last_name, number):
        if not isinstance(first_name, str) or not isinstance(last_name, str) or not isinstance(number, str):
            print("Not valid string contact")
            return "Not valid string contact"
        return None

    def add_contact(self, first_name, last_name, number):
        error = self._validate_contact(first_name, last_name, number)
        if error is None:
            self.__store[first_name] = number
            self.__first_name_trie.insert(first_name)
            self.__last_name_trie.insert(last_name)
            self.__number_trie.insert(number)
        else:
            print("\nvalidation error occured. not creating contact", error)

    def update_contact_by_number(self, lookup_number, new_number):
        self.__number_trie.update_trie_by_word(lookup_number, new_number)

    def search_contact_by_number(self, lookup_number):
        found = False
        for name, number in self.__store.items():
            if lookup_number == number:
                print("\nResults = 1")
                print("\nname: ", name, " number: ", number)
                found = True
                break

        if found is False:
            print("\nNumber not found in phonebook")

    # TODO search contact by last name
    def search_contact_by_first_name(self, lookup_name):
        if self.__store.get(lookup_name) is not None:
            print("\nResults = 1")
            print("\nname: ", lookup_name,
                  " number: ", self.__store[lookup_name])
        else:
            print("\nname not found in phonebook")

    def prefix_search_contact_by_first_name(self, lookup_name):
        self.__first_name_trie.prefix_search_by_word(lookup_name)
        print("\nResults Found = ", self.__first_name_trie.counter)

    def prefix_search_contact_by_last_name(self, lookup_name):
        self.__last_name_trie.prefix_search_by_word(lookup_name)
        print("\nResults Found = ", self.__last_name_trie.counter)

    def prefix_search_contact_by_number(self, lookup_number):
        self.__number_trie.prefix_search_by_word(lookup_number)
        print("\nResults Found = ", self.__number_trie.counter)
