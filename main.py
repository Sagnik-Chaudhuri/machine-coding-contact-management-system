from classes.PhoneBook import PhoneBook


def main():

    # print("Hello World")

    phonebook = PhoneBook()
    phonebook.add_contact("abcd", "asca", "55")
    phonebook.add_contact("as", "asd", "56")
    phonebook.add_contact("asd", "asdac", "567")
    phonebook.add_contact("asdf", "asda", "5612")
    # phonebook.search_contact_by_number("55")
    # phonebook.search_contact_by_first_name("a")

    phonebook.prefix_search_contact_by_last_name("as")
    # phonebook.prefix_search_contact_by_number("5")


main()
