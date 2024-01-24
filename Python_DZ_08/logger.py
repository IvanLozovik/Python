def show_all(file_name:str):
    try:
        with open(file_name, 'r',encoding='utf-8') as f:
            data = f.readlines()
            print("".join(data))
    except  FileNotFoundError:
        print('>>Ошибка: Пока нет ни одной записи \n')

def remove(file_name:str):
    last_name = input('Введите Фамилию: ')
    first_name = input('Введите Имя: ')
    patronymic = input('Введите Отчество: ')
    phone_number = input('Введите номер телефона: ')
    data = ""
    with open(file_name, 'r',encoding='utf-8') as f:
        data = f.readlines()
        s = f'{last_name}, {first_name}, {patronymic}, {phone_number}\n'
        data.remove(s)
    with open(file_name, 'w',encoding='utf-8') as f:
        f.writelines(data)
        
def modify(file_name:str):
   
    old_data = find_by_attribute(file_name, True)
    
    print("Введите новые данные:\n")
    last_name_ = input('Введите Фамилию: ')
    first_name_ = input('Введите Имя: ')
    patronymic_ = input('Введите Отчество: ')
    phone_number_ = input('Введите номер телефона: ')
    data = ""
    with open(file_name, 'r',encoding='utf-8') as f:
        data = f.readlines()
        i = data.index(old_data)
        data[i] = f'{last_name_}, {first_name_}, {patronymic_}, {phone_number_}\n'
        
    with open(file_name, 'w',encoding='utf-8') as f:\
        f.writelines(data)
        
        
def find_by_attribute(file_name:str,option: bool):
    c = input("Введите 1 для поиска по Фамилии, 2 для поиска по Имени: ")
        
    opt = 0
    if c == '1':
        opt = 0
    elif c == '2':
        opt = 1
        
    attr = input("Введите Имя/Фамилию для поиска: ")
    with open(file_name, 'r',encoding='utf-8') as f:
        data = f.readlines()
        data = list(filter(lambda x: x.split(', ')[opt] == attr,data))
        print(*list(zip(range(1,len(data)+1),data)))
        if option:
            id = input("Введите id нужного контакта для изменения данных: ")
        else:
            id = input("Введите id нужного контакта: ")
        return data[int(id)-1]


def add_new(file_name: str):
    # data = input('Введите Фамилию Имя Отчество и номер телефона через пробел: ')
    last_name = input('Введите Фамилию: ')
    first_name = input('Введите Имя: ')
    patronymic = input('Введите Отчество: ')
    phone_number = input('Введите номер телефона: ')

    with open(file_name, 'a', encoding='utf-8') as fd:
        fd.write(f'{last_name}, {first_name}, {patronymic}, {phone_number}\n')

def copy_data_to_file(file_name:str,option: bool):
    # show_all(file_name)
    with open(file_name, 'r',encoding='utf-8') as f:
        # option=True
        data = f.readlines()
        # data = list(filter(lambda x: x.split(', ')[opt] == attr,data))
        print(*list(zip(range(1,len(data)+1),data)))
        if option:
            id = input("Введите id контакта для копирования в файл : ")
        # else:
        #     id = input("Введите id контакта: ")
        data_new = data[int(id)-1]
        # return data[int(id)-1]
    file_name_new = input ('Введите имя файла: ')
    with open(file_name_new, 'a', encoding='utf-8') as fn:
        fn.write(data_new)
    print(f'Запись {data_new} скопирована в файл {file_name_new} ' )  