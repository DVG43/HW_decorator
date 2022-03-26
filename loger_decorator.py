import os
from datetime import datetime


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