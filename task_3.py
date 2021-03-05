def thesaurus(*args):
    dict_names = {}
    for idx in sorted(args):
        if idx[0] in dict_names:
            dict_names[idx[0]] += [idx]
        else:
            dict_names[idx[0]] = [idx]
    return dict_names


print(thesaurus("Дима", "Аля", "Кусик", "Танька", "Толик", "Даниил"))
