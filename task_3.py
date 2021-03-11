from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Даниил', 'Вячеслав', 'Алевтина'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б',
]


combination = (val for val in zip_longest(tutors, klasses))
print(type(combination))
print(*combination, sep=", ")





