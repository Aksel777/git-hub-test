# Задача №55. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию 
# человека)
# Использование функций. Ваша программа не должна быть линейной


############# READ ME #############


# 1) создать телефонный справочник:             +++
#         открыть файл в режиме добавления (а)  +++
# 2) Добавить контакт:                          +++
#         запросить информацию контакта         +++
#         подготовить нужный формат записи      +++
#         открыть файл в режиме добавления (а)  +++
#         записать данные контакта              +++
# 3) вывести данные на экран:                   +++
#         открыть файл в режим чтения           +++
#         вывести на экран информацию(r)        +++
# 4) Поиск данных:
#         запросить критерий поиска             
#         запросить данные поиска               +++
#         открыть файл в режиме чтения(r)       +++
#         сохранить даные в переменной          +++
#         осуществить поиск по файлу
#         вывести нужную инфу на экран
# 5) Удалить контакт:
#         запросить информацию контакта
#         открыть файл в режиме чтения(r)
#         удалить контакт
#         сохранить изменения
# 6) Перенести контакт:
#         запросить информацию контакта
#         открыть файл в режиме чтения(r)
#         открыть файл в режиме добавления (а) 
#         перенести контакт
#         сохранить изменения
# 6) Реализовать юзер интерфейс (UI):
#         вывести варианты меню                 +++
#         получение запроса пользователя        +++
#         реализация запроса пользователя       +++
#         выход из программы                    +++


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
    contact = create_contact()
    with open('phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write(contact)
        
def delete_contact():
    with open('phonebook.txt', 'r', encoding='UTF-8') as file: 
        contacts_list = file.read().split('\n\n')
    with open('phonebook.txt', 'w', encoding='UTF-8') as file: 
        name = input('Введите контакт: ')
    for contact in contacts_list:
        if name in contact:
            contacts_list.remove(contact)
            print("Контакт удален.")
        else:
            print("Контакт не найден.")
                
    print(contacts_list)                
# ############ В МОМЕНТЕ ПРОВЕРКИ КОДА нужные ЭЛЕМЕНТЫ УДАЛЯЕТ, НО,ПО ФАКТУ, УДАЛЯЕТ ВЕСЬ СПРАВОЧНИК 

def transfer_contact():
    with open('phonebook.txt', 'r', encoding='UTF-8') as file: 
        contacts_list = file.read().split('\n\n')
    f_new = open('new.txt', 'a')
    with open('new.txt', 'a', encoding='UTF-8') as f_new:
        number = input('Введите номер строки для копирования: ')
        for number in enumerate(contacts_list,1):
            if number in contacts_list[:]:
                f_new.write(contacts_list[number])
                print('copy done')
            else:
                print('not find')
    print(f_new)    
        
        
        
def show_info():
    with open('phonebook.txt', 'r', encoding='UTF-8') as file: 
        contacts_list = file.read().split('\n\n')    
    #   print(file.read().rstrip()) 
        for nn,contact in enumerate(contacts_list,1):
            print(nn, contact)   
            print(type(contact))      
def search_contact():
    var_search = input('Choice variant of search:\n '
                       '1. Name\n'
                       '2. surname\n'
                       '3. patronymic\n'
                       '4. phone\n'
                       '5. city\n'
                       'Enter:')
    
    while var_search not in ('1', '2', '3', '4',  '5'):
        print("incorrect")
        var_search = input("enter dote of menue: ")
        
    index_var = int(var_search)-1
    
    search = input('Enter data for reading: ')
    
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().split('\n\n')
        
    for contact_str in contacts_list:
        contact_lst = contact_str.replace('\n', ' ').split()
        if search in contact_lst[index_var]:
            print(contact_str)
            

    

def interface():
    with open('phonebook.txt', 'a', encoding='UTF-8') as file:
        print(file)
        
    command = '-1'
    while command != '6':
        print('Возможные действия:\n'
            '1. Добавить контакт\n'
            '2. Удалить контакт\n'
            '3. Копировать контакт\n'
            '4. Вывести на экран\n'
            '5. Поиск контакта\n'
            '6. Выход из программы')
        
        command = input("enter dote of menue: ")
        
        while command not in ('1','2','3','4','5','6'):
            print("incorrect")
            command = input("enter dote of menue: ")
            
        match command:
            case '1':
                add_contact(create_contact)
            case '2':
                delete_contact()
            case '3':  
                transfer_contact()
            case '4':  
                show_info()
            case '5':
                search_contact()
            case '6':
                print("good bye!")      
                
interface()      