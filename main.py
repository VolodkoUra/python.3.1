"""Дана следующая строка: ‘Сидел барсук в своей норе и ел картошечку пюре’

1. Создайте данную строку
2. Получите ее длину
3. Проведите операцию сложения со строкой ‘.’
4. Проверьте, входит ли подстрока ‘ре’ в заданную строку
5. Посчитайте количество вхождений подстроки ‘ре’
6. Получите предпоследний символ строки
7. Получите все символы с нечетными индексами
8. Определите, сколько слов в строке
"""
def power():
    s = "Сидел барсук, в своей норе и ел картошечку пюре"
    print("Длинна строки s = ", len(s))
    s1 = "."
    result = s + s1
    print(result)
    t = s.count("ре")
    print(t)
    print(s[-2])
    print(s[1::2])

    k = s.split()
    print(k)
    print("Количество слов в строке: ", len(k))


if __name__ == '__main__':
    power()

