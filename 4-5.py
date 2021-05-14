from random import randrange, shuffle


def get_jokes(count_of_jokes, unique_words = True):
    count_of_jokes = int(count_of_jokes)
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    if unique_words:
        if count_of_jokes > 4:
            return print("To many unique jokes!")  # проверка на максимальное использование уникальных слов
        shuffle(nouns)
        shuffle(adverbs)
        shuffle(adjectives)
        for jokes in range(0, count_of_jokes):
            print(f'{nouns.pop()} {adverbs.pop()} {adjectives.pop()}')
        return
    else:
        for jokes in range(0, count_of_jokes):
            rand_index_nouns = randrange(len(nouns))
            rand_index_adv = randrange(len(nouns))
            rand_index_adj = randrange(len(nouns))
            print(f'{nouns[rand_index_nouns]} {adverbs[rand_index_adv]} {adjectives[rand_index_adj]}')


get_jokes(8, False)
