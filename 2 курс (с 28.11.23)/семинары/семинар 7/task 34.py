# ВИННИ ПУХ И СТИХИ
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его 
# кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.

# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе 
# стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.

# Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки. В ответе
# напишите Парам пам-пам, если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
# Если фраза только одна, то ритм определить не получится и необходимо вывести: Количество фраз 
# должно быть больше одной!.

# Пример
# На входе:

# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# На выходе:

# Парам пам-пам


# def syllable(stroka):
# stroka = 'со-лнце-гре-ет ве-сной'
# list_1 = stroka.split()
# size = len(list_1)
# print(list_1)
# print(size)
# count = 0
# for el in list_1:
#     for i in el:
#         if i in "аеёиоуыэюяaeiouy":
#             count+=1
#     print(count, end='\n')
# if size < 2:
#     print("Количество фраз должно быть больше одной!")
# elif count%size==0:
#     print("Парам пам-пам")
# else:
#     print("Пам парам")
    


def word(words):
    str = words.lower().split()
    print(str)
    print(len(str))
    f = lambda x: sum(1 for i in x if i in 'аоуыэеёиюя')
    tmp = f(str[0])
    if len(str) < 2:
        return "Количество фраз должно быть больше одной!"
    if all([f(i) == tmp for i in str]):
        return 'Парам пам-пам'
    return 'Пам парам'


print(word("со-лнце-гре-ет"))




def rifma(poem):
    phrases_list = poem.lower().split()
    sum_vowels = lambda phrase: sum(1 for symbol in phrase if symbol in 'аеёиоуыэюя')
    tmp = sum_vowels(phrases_list[0]) #4
    if all([sum_vowels(phrase) == tmp for phrase in phrases_list[1:]]):
        return 'Парам пам-пам'
    return 'Пам парам'


print(rifma("пара-ра-рам рам-пам-папам па-ра-па-дам"))




def rifma(poem):
    phrases_list = poem.lower().split() #
    sum_vowels = lambda phrase: len(list(filter(lambda symbol: symbol in 'аеёиоуыэюя', phrase)))
    vowels_0 = sum_vowels(phrases_list[0]) # 4
    if all(map(lambda phrase:sum_vowels(phrase) == vowels_0, phrases_list[1:])):
        return 'Парам пам-пам'
    return 'Пам парам'
print(rifma("пара-ра-рам рам-пам-папам па-ра-па-дам"))






def sum_vowels(phrase):
    vowLet = "аеёиоуыэюя"
    cnt=0
    for let in phrase:
        if let in vowLet:
            cnt += 1
    return cnt

def check_rifm(poem):
    vowel_0 = sum_vowels(poem[0])
    for phrase in poem[1:]:
        if sum_vowels(phrase) != vowel_0:
            return "Пам парам"
    return "Парам пам-пам"


check_rifm('пара-ра-рам рам-пам-папам па-ра-па-дам')


text = input("Введите стихотворение Винни-Пуха: ").split()
print(check_rifm(text))








def cntVowLet(str):
    cnt=0
    for let in str:
        if let in vowLet:
            cnt += 1
    return cnt

vowLet = "а,е,ё,и,о,у,ы,э,ю,я".split(",")

inStr=input("Введите стихотворение Винни-Пуха: ")
res = set(map(cntVowLet, inStr.split()))

if len(res) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")