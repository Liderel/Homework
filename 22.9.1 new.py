#функция проверки вводимых значений
def InputCheck(value, isCollection):
    value = value.strip()
    checkValue = value
    if isCollection:
        checkValue = value.replace(' ', '')
    result = checkValue.isdigit()
    if not result:
        print('---------------------------')
        if value == '':
            print('Введена пустая строка.')
        elif isCollection:
            print('Введены символы помимо чисел и пробела.')
        else:
            print('Введены символы помимо чисел.')
    return result;

#функция сортировка пузырьком
def sort(collection):
    length = len(collection)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if collection[j] > collection[j + 1]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]

#функция алгоритма двоичного поиска из курса.
def binary_search(num, user_number, left, right):
    if left > right:
        return -1
    middle = (right + left) // 2
    if num[middle] == user_number:
        return middle
    elif user_number < num[middle]:
        return binary_search(num, user_number, left, middle - 1)
    else:
        return binary_search(num, user_number, middle + 1, right)


#Ввод чисел через пробел. Если условия ввода не соответствуют цикл будет повторяться.
numbers = input("Введите числа: ")
while not InputCheck(numbers, True):
    numbers = input("Попробуйте снова: ")
num = numbers.split()
num = [int(i) for i in num]
print('---------------------------')

#Ввод числа от пользователя. Если условия ввода не соответствуют цикл будет повторяться
user_number = input('Введите число пользователя: ')
while not InputCheck(user_number, False):
    user_number = input("Попробуйте снова: ")
user_number = int(user_number)


#Вывод списков
print('---------------------------')
print("Несортированный список: " + str(num))
print('---------------------------')
sort(num)
print("Сортированный список: " + str(num))
print('---------------------------')


#поиск
Index = binary_search(num, user_number, 0, len(num) - 1)
if Index == -1:
    print('Введенное число не найдено')
else:
    LeftIndex = Index - 1
    RightIndex = Index + 1
    print('Номер позиции введенного числа:' + str(Index))
    if LeftIndex < 0:
        print('Номер позиции элемента, который меньше введенного числа: отсутствует')
    else:
        print('Номер позиции элемента, который меньше введенного числа: ' + str(LeftIndex))
    if RightIndex > len(num) - 1:
        print('Номер позиции элемента, который больше введенного числа: отсутствует')
    else:
        print('Номер позиции элемента, который больше введенного числа: ' + str(RightIndex))
