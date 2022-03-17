from classes.PhoneBook import PhoneBook


def main():

    phonebook = PhoneBook()
    phonebook.add_contact("Sagnik", 5)
    phonebook.add_contact("Sagnika", 56)
    # phonebook.prefix_search_contact_by_name_key_press("Sagnik")
    # phonebook.prefix_search_contact_by_name_key_press("Sagnk")
    # phonebook.search_contact_by_number(5)
    phonebook.prefix_search_contact_by_name("Sagnk")

    return None


main()
