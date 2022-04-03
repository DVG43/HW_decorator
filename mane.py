

from datetime import datetime
from loger_decorator import parametrized_decor
from loger_decorator import loger_decorator

#Написать декоратор - логгер. Он записывает в файл дату и время вызова функции, имя функции, аргументы, с которыми вызвалась и возвращаемое значение.

#Написать декоратор из п.1, но с параметром – путь к логам.

#Применить написанный логгер к приложению из любого предыдущего д/з


# @parametrized_decor(parameter='Log_files/')
@ loger_decorator
def multiplier(a, b):
    return a + b


#if __name__ != '__main__':
    aa = [1, 2, 4, 5]
    bb = ['d', 'c', 'd', 'e']
    x = multiplier(aa, bb)
    print(x)






