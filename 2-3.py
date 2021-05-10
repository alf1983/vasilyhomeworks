sentence_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
index = 0
while index < len(sentence_list):
    if sentence_list[index].isdigit():
        if len(sentence_list[index]) < 2:
            sentence_list[index] = '0' + sentence_list[index]
        sentence_list.insert(index, '"')
        sentence_list.insert(index + 2, '"')
        index += 3
    elif any(map(str.isdigit, sentence_list[index])):
        if len(sentence_list[index]) < 3:
            sing = sentence_list[index][0]
            degrees = '0' + sentence_list[index][1]
            sentence_list[index] = sing + degrees
        sentence_list.insert(index, '"')
        sentence_list.insert(index + 2, '"')
        index += 3
    else:
        # sentence_list[index] += " "
        index += 1
print(sentence_list)
quotes = 1
sentence = ''
index = 0
while index < len(sentence_list) - 1:
    if sentence_list[index] != '"':
        if sentence_list[index + 1] != '"':
            sentence += sentence_list[index] + ' '
        else:
            sentence += sentence_list[index]
    else:
        if quotes % 2 == 0:
            sentence += sentence_list[index] + " "
        else:
            sentence += " " + sentence_list[index]
        quotes += 1
    index += 1
sentence += sentence_list[index]
# print(dir(sentence)) можно использовать replace но это не честно
print(sentence)
