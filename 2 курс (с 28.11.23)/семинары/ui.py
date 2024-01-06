from logger import *

def interface():
    with open('phonebook.txt', 'a', encoding='UTF-8') as file:
        print(file)
        
    command = '-1'
    while command != '4':
        print('Возможные действия:\n'
            '1. Добавить контакт\n'
            '2. Вывести на экран\n'
            '3. Поиск контакта\n'
            '4. Выход из программы')
        
        command = input("enter dote of menue: ")
        
        while command not in ('1', '2', '3', '4'):
            print("incorrect")
            command = input("enter dote of menue: ")
            
        match command:
            case '1':
                add_contact(create_contact)
            case '2':
                show_info()
            case '3':
                search_contact()
            case '4':
                print("good bye!")      
                
interface()      