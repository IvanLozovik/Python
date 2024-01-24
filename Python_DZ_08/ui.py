from logger import show_all, add_new, remove, modify, find_by_attribute, copy_data_to_file

def interface ():
    file_name = 'phonebook.txt'
    flag_exit = False
    while not flag_exit:
        print('1 - Показать все записи')
        print('2 - Добавить запись')
        print('3 - Удалить запись')
        print('4 - Изменить запись')
        print('5 - Поиск записи по Имени/Фамилии')
        print('6 - Скопировать запись в другой файл')
        answer = input('Введите номер операции или (x) для выхода: ')
        print()
        if answer == '1':
            show_all(file_name=file_name)
        elif answer == '2':
            add_new(file_name)
        elif answer == '3':
            remove(file_name)
        elif answer == '4':
            modify(file_name=file_name)
        elif answer == '5':
            print(find_by_attribute(file_name,False))
        elif answer == '6':
            print(copy_data_to_file(file_name, True))
        elif answer == 'x':
            flag_exit = True