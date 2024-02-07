# Телефонная книга

Консольное приложение "Телефонная книга"

Основные функции, использованные в приложении:

### main()
main() - функция, отвечающая за основную работу программы. В режиме бесконечного цикла выводит пользователю
    меню программы. При выборе пользователем пункта для взаимодействия - запускает логику этого взаимодействия

    :return: 0

### read_data()
read_data() - функция, принимающая на вход строку с именем файла, считывает из него данные
    и возвращает их в виде списка строк. Если возникает исключение/ошибка - функция отправляет сообщение об ошибке
    и возвращает пустой список

    :param file_name: str
    :return: list[str]

### check_phone_number() 
check_phone_number() - функция, принимающая на вход строку, проверяет, состоит ли эта строка
    только из цифр и символа +. В случае если строка состоит из цифр и +, функция возвращает True,
    в обратном случае - False

    :param phone: str
    :return: bool

### add_contact() - 
add_contact() - функция, принимающая название файла строкой, в который будет произведена запись.
    Функция запрашивает имя контакта и номер телефона. Номер телефона проверяется на корректность.
    Корректным считается любой номер, состоящий только из цифр и символа +
    Если телефон корректен - функция add_contact() добавляет новую запись в переданный файл.
    Запись производится в режиме добавления append, без перезаписи исходного файла

    :param file_name: str
    :return: None

### show_data()
show_data() - функция, принимающая аргументом список строк data для вывода на экран.
    Также дополнительный список founded (по умолчанию пуст, если не передал пользователь),
    который содержит индексы отдельных контактов, найденных ранее при поиске.
    Выводит каждый элемент списка в отдельной строке

    :param data: list[str]
    :param founded: list[str]
    :return: None

### find_data()
find_data() - функция, принимающая на вход список строк data, в котором будет произовдиться поиск.
    Функция запрашивает у пользователя ключевое слово (Имя/телефон) и ищет вхождения ключевого слова
    в списке строк data. В случае успешного поиска, возрващается список founded, который содержит индексы
    строк, в которых вхождение ключевого слова было успешным. В случае, если вхождений нет, функция сообщает об этом
    и возвращает пустой список

    :param data: list[str]
    :return: list[int]

### select_index()
select_index() - функция, которая принимает на вход список строк data и список founded индексов вхождений запроса
     пользователя при поиске. Функция возвращает финальный выбор пользователя для редактирования, удаления
    данных. Если список founded состоит из 1 элемента - он и будет возвращаемым числом. Если же в founded несколько
    элементов - функция финализирует выбор пользователя предлагая выбор из списка. В случае некорректного выбора,
    возращается значение -1

    :param data: list[str]
    :param founded: list[int]
    :return: int

### delete_data()
delete_data() - функция удаления элемента с индексом idx из списка данных data. Функция выводит сообщение
    об успешном/неуспешном удалении данных

    :param data: list[str]
    :param idx: int
    :return: None

### edit_data()
edit_data() - объемная функция для редактирования данных, принимающая список строк data для редактирования
    и индекс редактируемого элемента idx. Исходная строка под индексом idx из списка data разбивается на список
    из 2х элементов: наименования контакта и номера телефона. Выбор данных для корректировки (наименование или номер)
    осуществляется пользователем. Также, в случае редактирования телефона, дополнительно проверяет корректность ввода
    при помощи функции check_phone_number(). Функция edit_data() при завершении сообщает пользователю об
    успехе/провале операции или некорректно введенных данных

    :param data: list[str]
    :param idx: int
    :return: None

### export_contact()
export_contact() - принимает список строк data и индекс строки idx для экспорта в отдельный файл, имя которого
    запрашивается у пользователя. Файл открывается на дозапись в режиме "append"

    :param data: list[str]
    :param idx: int
    :return: None

### export_phonebook_to_xlsx()
export_phonebook_to_xlsx() - функция принимает список строк data, которые будут экспортированы в файл формата
    xlsx при помощи библиотеки pandas. Имя нового файла задается пользователем. Функция построчно разбивает
    строки по делителю " - ", добавляя наименования и номера контактов в отдельные списки. После чего, при помощи
    библиотеки pandas, реализует запись в xlsx-файл

    :param data: list[str]
    :return: None

### rewrite_file()
rewrite_file() - функция перезаписи файла. Принимает имя файла file_name для записи и список строк data,
    которые и будут записаны в указанный файл. Перед записью список data сортируется.
    Далее происходит запись в file_name в режиме 'write', перезаписывая предыдущее содержимое файла file_name

    :param file_name: str
    :param data: list[str]
    :return: None
