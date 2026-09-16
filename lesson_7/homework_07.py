# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1
        '''ДОВЕЛОСЬ ТРОХИ ЗМIНИТИ КОД ТА ЗРОБИТИ НЕСКIНЧЕННИЙ ЛУП ЧЕРЕЗ While True
        ТОМУ-ЩО Я НЕ ЗРОЗУМIВ ЩО ВIД МЕНЕ ХОЧУТЬ, АЛЕ ФУНКЦIЯ ПОВИННА ПРАЦЮВАТИ
        НЕ ТIЛЬКИ З ЗАДАНОЮ ТРIЙКОЮ АЛЕ Й З IНШИМИ ЧИСЛАМИ'''
multiplication_table(5)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def summa(number1, number2):
    return number1 + number2
    '''ЧИМ ВАМ НЕ ПОДОБАЄТЬСЯ ФУНКЦІЯ sum В БІБЛІОТЕЦІ ПІТОНА?'''
print(summa(5, 6))
# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def serednie_arifmet(list1):
    return sum(list1) // len(list1)
a = [5, 12, 68]
print(serednie_arifmet(a))
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def tipa_reverse(string):
    string = string[::-1]
    return string
print(tipa_reverse("Hello, world!"))
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def the_longest(list1):
    list1.sort(key=len)
    return list1[-1]
print(the_longest(['hello', 'python', 'bye', 'unemployment', 'happy']))
# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    index = str1.find(str2)
    return index

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# Завдання 6.1: если число уникальных символов строки >10 - писать тру, в ином случае фолс
# Так же в этом дз прошлый раз я сдал код который не проверяет символы на уникальность но тут я исправил
string = input('Enter a string:\n ')
def unique_symb_check(set1):
    set1 = set(set1)
    if len(set1) > 10:
        print('True')
    else:
        print('False')
unique_symb_check(string)
# task 8
#Завдання 6.2: проверка на присутствие буквы h/H в строке
need_H = input('Введи слово с буквой h/H или sudo rm -rf System32\n')
def h_symbol_check(line):

    while True:
        if 'h' in line or 'H' in line:
            print('Маладец')
            break
        else:
            line = input('Неправильно еще раз: \n')
            continue
h_symbol_check(need_H)
# task 9
# Завдання 6.3: вывести из списка все данные формата str
list1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
def find_str(list_of_something):
    result = list_of_something = [x for x in list_of_something if type(x) is str]
    return result
print(find_str(list1))
# task 10
# Завдання 6.4: вывести суму всех даных парных чисел из листа
created_list = [x for x in range(50)]
def sum_of_evens(list_of_numbers):
    list_of_numbers = [x for x in list_of_numbers if x % 2 == 0]
    return sum(list_of_numbers)
print(sum_of_evens(created_list)) # Должно выводить 600

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""