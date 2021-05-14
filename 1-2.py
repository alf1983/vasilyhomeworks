def num_translate_adv(numeral):
    """ Translate from English to Russian numeral 1-10"""
    dictionary = {
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять"
    }
    translate = dictionary.get(numeral.lower(), False)
    if translate:
        if numeral.istitle(): # проверка
            return translate.title()
        else:
            return translate
    else:
        return None


numeral_input = input('Enter a number from 1 to 10 with a word: ')
print(num_translate_adv(numeral_input))
