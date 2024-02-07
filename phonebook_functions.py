import pandas as pd

def read_data(file_name:str):
    """
    read_data() - функция, принимающая на вход строку с именем файла, считывает из него данные
    и возвращает их в виде списка строк. Если возникает исключение/ошибка - функция отправляет сообщение об ошибке
    и возвращает пустой список
    :param file_name: str
    :return: list[str]
    """
    try:
        with open(file_name, 'r', encoding="utf-8") as file:
            return file.readlines()
    except Exception:
        print("Файл не существует или не поддерживается\n")
        return []


def check_phone_number(phone:str):
    """
    check_phone_number() - функция, принимающая на вход строку, проверяет, состоит ли эта строка
    только из цифр и символа +. В случае если строка состоит из цифр и +, функция возвращает True,
    в обратном случае - False
    :param phone: str
    :return: bool
    """
    for letter in phone:
        if letter not in "+1234567890":
            return False
    return True


def add_contact(file_name:str):
    """
    add_contact() - функция, принимающая название файла строкой, в который будет произведена запись.
    Функция запрашивает имя контакта и номер телефона. Номер телефона проверяется на корректность.
    Корректным считается любой номер, состоящий только из цифр и символа +
    Если телефон корректен - функция add_contact() добавляет новую запись в переданный файл.
    Запись производится в режиме добавления append, без перезаписи исходного файла
    :param file_name: str
    :return: None
    """
    contact_name = input("Введите имя контакта: ")
    contact_phone = input("Введите номер телефона контакта: ")
    if check_phone_number(contact_phone):
        with open(file_name, 'a', encoding="utf-8") as file:
            file.write(f"{contact_name} - {contact_phone}\n")
    else:
        print("Номер телефона может состоять только из цифр\n")


def show_data(data:list[str], founded:list[int]=[]):
    """
    show_data() - функция, принимающая аргументом список строк data для вывода на экран.
    Также дополнительный список founded (по умолчанию пуст, если не передал пользователь),
    который содержит индексы отдельных контактов, найденных ранее при поиске.
    Выводит каждый элемент списка в отдельной строке
    :param data: list[str]
    :param founded: list[str]
    :return: None
    """
    if len(founded) == 0:
        for idx, line in enumerate(data):
            print(f"{idx + 1}. {line}")
    else:
        for i, idx in enumerate(founded):
            print(f"{i + 1}. {data[idx]}")


def find_data(data:list[str]):
    """
    find_data() - функция, принимающая на вход список строк data, в котором будет произовдиться поиск.
    Функция запрашивает у пользователя ключевое слово (Имя/телефон) и ищет вхождения ключевого слова
    в списке строк data. В случае успешного поиска, возрващается список founded, который содержит индексы
    строк, в которых вхождение ключевого слова было успешным. В случае, если вхождений нет, функция сообщает об этом
    и возвращает пустой список
    :param data: list[str]
    :return: list[int]
    """
    user_input = input("Введите ключевое слово для поиска: ")
    founded = []
    for idx, line in enumerate(data):
        if user_input.lower() in line.lower():
            founded.append(idx)
    if len(founded) == 0:
        print("Запись не найдена\n")
    return founded


def select_index(data:list[str], founded:list[int]):
    """
    select_index() - функция, которая принимает на вход список строк data и список founded индексов вхождений запроса
     пользователя при поиске. Функция возвращает финальный выбор пользователя для редактирования, удаления
    данных. Если список founded состоит из 1 элемента - он и будет возвращаемым числом. Если же в founded несколько
    элементов - функция финализирует выбор пользователя предлагая выбор из списка. В случае некорректного выбора,
    возращается значение -1
    :param data: list[str]
    :param founded: list[int]
    :return: int
    """
    if len(founded) == 1:
        return founded[0]
    else:
        show_data(data, founded)
        try:
            user_choice = int(input("Введите порядковый номер контакта для продолжения: ")) - 1
            if user_choice < len(founded):
                return user_choice
        except Exception as err:
            pass
        print("Некорректный ввод\n")
        return -1


def delete_data(data:list[str], idx:int):
    """
    delete_data() - функция удаления элемента с индексом idx из списка данных data. Функция выводит сообщение
    об успешном/неуспешном удалении данных
    :param data: list[str]
    :param idx: int
    :return: None
    """
    try:
        print(f"{data.pop(idx)} Запись удалена\n")
    except Exception:
        print("Номер указан некорректно\n")


def edit_data(data:list[str], idx:int):
    """
    edit_data() - объемная функция для редактирования данных, принимающая список строк data для редактирования
    и индекс редактируемого элемента idx. Исходная строка под индексом idx из списка data разбивается на список
    из 2х элементов: наименования контакта и номера телефона. Выбор данных для корректировки (наименование или номер)
    осуществляется пользователем. Также, в случае редактирования телефона, дополнительно проверяет корректность ввода
    при помощи функции check_phone_number(). Функция edit_data() при завершении сообщает пользователю об
    успехе/провале операции или некорректно введенных данных
    :param data: list[str]
    :param idx: int
    :return: None
    """
    try:
        contact = data[idx].split(" - ")
    except Exception:
        print("Номер указан некорректно\n")
        return
    else:
        print("1 - Корректировка имени контакта")
        print("2 - Корректировка номера телефона контакта")
        user_choice = input("Выберите действие: ")
        if user_choice == '1':
            contact[0] = input("Введите новое имя: ")
        elif user_choice == '2':
            contact[1] = input("Введите новый номер: ")
            if not check_phone_number(contact[1]):
                print("Номер телефона может состоять только из цифр\n")
                return
        else:
            print("Некорректный выбор\n")
            return
        data[idx] = f"{contact[0]} - {contact[1]}"
        print("Контакт успешно обновлен\n")


def export_contact(data:list[str], idx:int):
    """
    export_contact() - принимает список строк data и индекс строки idx для экспорта в отдельный файл, имя которого
    запрашивается у пользователя. Файл открывается на дозапись в режиме "append"
    :param data: list[str]
    :param idx: int
    :return: None
    """
    new_file_name = input("Введите имя файла для экспортируемого контакта: ")
    if len(new_file_name):
        new_file_name = "export_phonebook"
    new_file_name = f"{new_file_name}.txt"
    with open(new_file_name, 'a', encoding="utf-8") as export_file:
        export_file.write(f"{data[idx]}")
        print("Импорт успешно осуществлен")


def export_phonebook_to_xlsx(data:list[str]):
    """
    export_phonebook_to_xlsx() - функция принимает список строк data, которые будут экспортированы в файл формата
    xlsx при помощи библиотеки pandas. Имя нового файла задается пользователем. Функция построчно разбивает
    строки по делителю " - ", добавляя наименования и номера контактов в отдельные списки. После чего, при помощи
    библиотеки pandas, реализует запись в xlsx-файл
    :param data: list[str]
    :return: None
    """
    new_file_name = input("Введите имя файла для экспорта контактов: ")
    if not len(new_file_name):
        new_file_name = "default_file_name"
    new_file_name = f"{new_file_name}.xlsx"
    names = []
    phones = []
    for line in data:
        tmp = line.split(" - ")
        names.append(tmp[0])
        phones.append(tmp[1][:-1])
    df = pd.DataFrame({"Имя контакта": names, "Номер телефона": phones})
    df.to_excel(new_file_name)
    print(f"Контакты успешно экспортированы в {new_file_name}\n")


def rewrite_file(file_name:str, data:list[str]):
    """
    rewrite_file() - функция перезаписи файла. Принимает имя файла file_name для записи и список строк data,
    которые и будут записаны в указанный файл. Перед записью список data сортируется.
    Далее происходит запись в file_name в режиме 'write', перезаписывая предыдущее содержимое файла file_name
    :param file_name: str
    :param data: list[str]
    :return: None
    """
    data.sort()
    with open(file_name, 'w', encoding="utf-8") as file:
        file.writelines(data)

