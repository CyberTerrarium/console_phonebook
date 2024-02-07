import phonebook_functions as pb

def main():
    """
    main() - функция, отвечающая за основную работу программы. В режиме бесконечного цикла выводит пользователю
    меню программы. При выборе пользователем пункта для взаимодействия - запускает логику этого взаимодействия
    :return: 0
    """
    file_name = "phonebook.txt"
    flag = True
    while flag:
        print("1 - Показать все записи\n"
              "2 - Добавить новую запись\n"
              "3 - Найти запись\n"
              "4 - Редактировать запись\n"
              "5 - Удалить запись\n"
              "6 - Экспортировать контакт в другой файл\n"
              "7 - Экспортировать телефонную книгу в Excel\n"
              "0 - выход\n")
        user_input = input("Выберите действие: ")
        if user_input == '0':
            flag = False
        elif user_input == '1':
            data = pb.read_data(file_name)
            pb.show_data(data)
        elif user_input == '2':
            pb.add_contact(file_name)
        elif user_input == '3':
            data = pb.read_data(file_name)
            founded = pb.find_data(data)
            if len(founded) > 0:
                pb.show_data(data, founded)
        elif user_input == '4':
            data = pb.read_data(file_name)
            founded = pb.find_data(data)
            if len(founded) > 0:
                idx = pb.select_index(data, founded)
                if idx > -1:
                    pb.edit_data(data, idx)
                    pb.rewrite_file(file_name, data)
        elif user_input == '5':
            data = pb.read_data(file_name)
            founded = pb.find_data(data)
            if len(founded) > 0:
                idx = pb.select_index(data, founded)
                if idx > -1:
                    pb.delete_data(data, idx)
                    pb.rewrite_file(file_name, data)
        elif user_input == '6':
            data = pb.read_data(file_name)
            founded = pb.find_data(data)
            if len(founded) > 0:
                idx = pb.select_index(data, founded)
                if idx > -1:
                    pb.export_contact(data, idx)
        elif user_input == '7':
            data = pb.read_data(file_name)
            if len(data) > 0:
                pb.export_phonebook_to_xlsx(data)
            else:
                print("Телефонная книга пока не содержит записей\n"
                      "Нажмите \"2\", чтобы добавить новую запись\n")


if __name__ == "__main__":
    main()