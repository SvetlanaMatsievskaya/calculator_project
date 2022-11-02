# модуль вычислений
import cmath


def Calculation(data):
    value_a, operation, value_b = data
    if operation == '+':
        return summation(value_a, value_b)
    if operation == '-':
        return substraction(value_a, value_b)
    if operation == '*':
        return multiplication(value_a, value_b)
    if (operation == '/') and (value_b != 0):
        return division(value_a, value_b)
    else:
        return 'Ошибка деления на 0!'


def summation(value_a, value_b):
    return value_a + value_b


def substraction(value_a, value_b):
    return value_a - value_b


def multiplication(value_a, value_b):
    return value_a * value_b


def division(value_a, value_b):
    return value_a / value_b
