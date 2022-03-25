
import os
from datetime import datetime

#Написать декоратор - логгер. Он записывает в файл дату и время вызова функции, имя функции, аргументы, с которыми вызвалась и возвращаемое значение.

#Написать декоратор из п.1, но с параметром – путь к логам.

#Применить написанный логгер к приложению из любого предыдущего д/з


def loger_decorator(old_function):
	def new_function(*args, **kwars):
		current_datetime = datetime.now()
		print(current_datetime)
		name_function = f'имя функции {old_function.__name__}'
		print(name_function)
		arguments_function = f'с аргументами {args}'
		print(arguments_function)
		resultat = old_function(*args,**kwars)
		print(f'результат функции {resultat}')
		with open('log_file.txt', 'a', encoding="utf-8") as f:
	    	  path_to_file = os.path.abspath('log_file.txt')
	    	  f.write(f'{current_datetime} {name_function} {arguments_function} результат функции {resultat} '
					  f' путь к файлу {path_to_file}\n')
		return resultat
	return new_function

# with open('log_file.txt', 'a') as f:
# 	f.write(f'{some_pat}')

@ loger_decorator
def multiplier(a, b):
    return a + b

if __name__ == '__main__':
    aa = [1, 2, 4, 5]
    bb = ['d', 'c', 'd', 'e']
    x = multiplier(aa, bb)
    print(x)






