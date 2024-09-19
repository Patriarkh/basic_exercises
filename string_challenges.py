# Вывести последнюю букву в слове
word = 'Архангельск'
last_letter = word[-1]
print(last_letter)


# Вывести количество букв "а" в слове
word = 'Архангельск'
count = 0
for letter in word.lower():
    if letter == 'а':
        count += 1
print(count)


# Вывести количество гласных букв в слове
word = 'Архангельск'
spis = 0
glasnye = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
for letter in word.lower():
    if letter in glasnye:
        spis += 1
print(spis)



# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words_in_sentence = 0
for words in sentence.split():
    words_in_sentence += 1
print(words_in_sentence)


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
first_letter = sentence.split()
for word in first_letter:
    print(word[0])



    
    


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
split_sentence = sentence.split()

for words in split_sentence:
    length_of_words = len(words)
    print(length_of_words)


