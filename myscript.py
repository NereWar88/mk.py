### Основн. математические операторы
# + Сложение
# - Вычитание
# * Умножение
# / Деление (прямой слеш)

# Операции выполняются по очереди (по приоритету)
# Очередность // приоритет можно изменить с помощью скобок

# print('Пример')
# print(((5+30)*20)/15)

### Переменные
## переменная обозначает именованное место для хранения данных

# fred = 200
# miha = fred
# print(miha)

# print('Пример')
# number_of_coins = 250
# print(number_of_coins)

## имена переменных не могут начинаться с цифры
# found_coins = 20
# magic_coins = 10
# stolen_coins = 3
# print (found_coins + magic_coins * 365 - stolen_coins * 52)

### Строки
# Строка - исп. для вывода текста
# В списках, кортежах и словарях можно хранить наборы значений

# fred = 'Почему у горилл большие ноздри? Потому что у них толстые пальцы!'
# print(fred)

## Строку можно записать в одинарных '---' или двойных "---" кавычках
## Если нужно ввести текст, занимающий несколько строк, поставьте в начале и в конце три одинарные кавычки

# print('Пример')
# fred = '''Что едят на полдник динозавры? 
# ТиРекс-кекс!'''
# print(fred)

### Single Quote // Double Quoute
# \ - символ экранирования, если нужно записать строку в двойных или одинарных кавычках
# print('Пример')
# single_quote_str = '"Тут что-то не так, не будь я д\'Артаньян", - подумал он.'
# double_quote_str = "\"Тут что-то не так, не будь я д'Артаньян\", - подумал он."
# print(single_quote_str)
# print(double_quote_str)

### Переменные внутри строк
## Исп. %s для печатати строк, содержащих значения переменных
# print('Пример:')
# myscore = 1000
# message = 'Мой счет: %s очков' // ЕСТЬ ВОПРОСЫ // 
# print(message % myscore)
## Исп. %s для можно подставлять различные переменные
# print('Пример:')
# joke_text = '%s: приспособление для поиска мебели в темноте'
# bodypart1 = 'Коленка'
# bodypart2 = 'Лодыжка'
# print(joke_text % bodypart1)
# print(joke_text % bodypart2)
## Исп. нескольких %s меток в одной строке
# print('Пример:')
# nums = 'Что сказало число %s числу %s? Славный поясок!'
# print(nums % (0, 8))
## Если исп. несколько меток, то значения для подстановки указываются в скобках


### Умножение строк
print('Пример:')
print(10*'a')