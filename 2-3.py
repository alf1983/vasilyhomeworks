def thesaurus_adv(*args):
    name_book = {}
    # args = list(args)
    # args.sort()
    for _name in args:
        first_name, surname = _name.split(" ")
        # оставил свой вариант но с setdefault (решение увидел на разборе ДЗ) конечно красивее
        if name_book.get(surname[0].upper()) is None:
            name_book[surname[0].upper()] = {}
        if name_book[surname[0].upper()].get(first_name[0].upper()):
            name_book[surname[0].upper()][first_name[0].upper()].append(_name)
        else:
            name_book[surname[0].upper()][first_name[0].upper()] = [_name]
    # раздумья о сортировке
    # list_of_keys_surname = list(name_book.keys())
    # list_of_keys_surname.sort()
    # name_book_sorted = {}
    # # print(name_book)
    # for key_surname in list_of_keys_surname:
    #     list_of_keys_first_name = list(name_book[key_surname])
    #     list_of_keys_first_name.sort()
    #     # print(list_of_keys_first_name)
    #     for key_first_name in list_of_keys_first_name:
    #         name_book_sorted[key_surname][key_first_name] = \
    #             name_book.get(key_surname, "buy").get(key_first_name, "hello")
    return name_book


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
