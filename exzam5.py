# Напишите функцию, которая считает сумму цифр любого целого положительного числа
# вход: 459
# выход: 18


N = int(input("Введите число="))
sum = 0
while N > 0:
    d = N % 10
    N = N // 10
    sum += d
print("Сумма всех чисел в числе=", sum)