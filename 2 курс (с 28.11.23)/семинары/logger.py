from date_create import *

def add_contact(contact):
    # contact = create_contact()
    with open('phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write(contact)
def show_info():
    with open('phonebook.txt', 'r', encoding='UTF-8') as file: 
        contacts_list = file.read().split('\n\n')    
    #   print(file.read().rstrip()) 
        for nn,contact in enumerate(contacts_list,1):
            print(nn, contact)         
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