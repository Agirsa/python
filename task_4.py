# не считать за решение, посмотрела разбор на уроке
def thesaurus(*args):
    dict_names = {}
    for idx in args:
        name, surname = idx.split(" ")
        val = dict_names.setdefault(surname[0], {name[0]: idx})
        n_val = val.setdefault(name[0], [idx])
        if idx not in n_val:
            n_val.append(idx)
    return dict_names


print(thesaurus("Дима Сидоренко", "Аля Серебрякова", "Кусик Сидоренко", "Танька Киселева"))
