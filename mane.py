#from typing import Callable
from datetime import datetime

#Написать декоратор - логгер. Он записывает в файл дату и время вызова функции, имя функции, аргументы, с которыми вызвалась и возвращаемое значение.

#Написать декоратор из п.1, но с параметром – путь к логам.

#Применить написанный логгер к приложению из любого предыдущего д/з


def loger_decorator(old_function):
	def new_function(*args, **kwars):
		current_datetime = datetime.now()
		print(current_datetime)
		print(f'имя функции {old_function.__name__}')
		print(f'с аргументами {args} и {kwars}')
		resultat = old_function(*args,**kwars)
		print(f'результат функции {resultat}')
		return resultat
	return new_function

@ loger_decorator
def multiplier(a, b):
   return a + b

if __name__ == '__main__':
	aa = [1,2,4,5]
	bb = ['d','c','d','e']
	x = multiplier(aa, bb)
	print(x)






