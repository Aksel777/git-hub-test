def input_name():
    return input("enter name: ")
def input_surname():
    return input("enter surname: ")
def input_patronymic():
    return input("enter patronymic: ")
def input_phone():
    return input("enter phone number: ")
def input_address():
    return input("enter address: ")
def create_contact():
    name = input_name()
    surname = input_surname()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    
    return f'{name} {surname} {patronymic} {phone}\n{address}\n\n'

def add_contact(contact):
    # contact = create_contact()
    with open('phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write(contact)