from random import choice, randrange
def get_jokes(num, repeat = False):
    list_jokes = []
    for i in range(num):
        if repeat == True:
            list_jokes.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
        elif repeat == False and min(len(nouns), len(adverbs), len(adjectives)) >= num:
            list_jokes.append(f"{nouns.pop(randrange(len(nouns)))} {adverbs.pop(randrange(len(adverbs)))} "
                              f"{adjectives.pop(randrange(len(adjectives)))}")
        else:
            list_jokes.append("Не получится сделать такое количество шуток без повторов. "
                              "Пожалуйста, введите меньшее число, или разрешите повторы.")
            break
    return list_jokes



nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(get_jokes(12, False))





