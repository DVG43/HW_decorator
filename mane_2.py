import os
from loger_decorator import loger_decorator

@ loger_decorator
def get_data_dishes(file_neme):
      dishes_list = []
      with open(file_neme,encoding='UTF-8') as file:
            for line in file:
                  dishes_list.append(line.strip())
                  dish_qantity = int(file.readline().strip())
                  for ingradients in range(dish_qantity):
                        file.readline()
                  file.readline()
      return dishes_list

# достаем из файла инградиенты
@ loger_decorator
def get_data_ingrediens(file_neme):
      ingredients_list = []
      with open(file_neme,encoding='UTF-8') as file:
            for line in file:
                  list_ingr = []
                  ingredients_list.append(list_ingr)
                  dish_qantity = int(file.readline().strip())
                  for ingradients in range(dish_qantity):
                        ingradients = file.readline().strip()
                        list_ingr.append(ingradients)
                  file.readline()
      return ingredients_list

@ loger_decorator
def make_dict_from_str(str_name):
      new_str = str_name.split("|")
      new_dickt = {'ingredient_name': new_str[0], 'quantity': new_str[1], 'measure': new_str[2]}
      return new_dickt

@ loger_decorator
def make_list_of_dict(list_list):
      new_list_of_dict = []
      for element_list in list_list:
            new_element_list = []
            for element_str in element_list:
                 new_element_list.append(make_dict_from_str(element_str))
            new_list_of_dict.append(new_element_list)
      return new_list_of_dict


list_of_list = get_data_ingrediens("starting_file.txt")
new_list_of_list = make_list_of_dict(list_of_list)
dishes_name_list_for = get_data_dishes("starting_file.txt")
cook_book = dict(zip(dishes_name_list_for, new_list_of_list))

print(cook_book)


@ loger_decorator
def make_key_new_dict(name_in_dict, some_dict):
      list_of_ingradient = some_dict[name_in_dict]
      new_list_of_neme_ingradient = []
      for name_of_ingradient in  list_of_ingradient:
            aaa = name_of_ingradient['ingredient_name']
            new_list_of_neme_ingradient.append(aaa)
      return new_list_of_neme_ingradient


@ loger_decorator
def make_value_new_dict(name_in_dict, some_dict):
      list_of_ingradient = some_dict[name_in_dict]
      new_list_of_ingradient = []
      for name_of_ingradient in  list_of_ingradient:
            aaa = name_of_ingradient ['measure']
            bbb = int(name_of_ingradient ['quantity']) * persons
            ingradient_dict = {'measure': aaa , 'quantity': bbb  }
            new_list_of_ingradient.append(ingradient_dict)
      return new_list_of_ingradient


@ loger_decorator
def get_shop_list_by_dishes (whishes_list, book):
# Проверка правильости блюда по переменной dishes_name_lis - цикл по списку ввода.
      total_list_ingredients = []
      total_list_megering = []
      qvontat_dish = []
      for dish_name in whishes_list:
            if dish_name in dishes_name_list_for:
                  total_list_ingredients += (make_key_new_dict(dish_name, book))
                  total_list_megering += (make_value_new_dict(dish_name, book,))
            else:
                  print (f'Блюда {dish_name} нет в кухонной книге')

      for qvontat in total_list_ingredients:
            qvontat_dish.append(total_list_ingredients.count(qvontat))

      total_list_megering_new = []
      indeks = 0
      for member in total_list_megering:
            aaaa = member['measure']
            #print(qvontat_dish[indeks])
            bbbb = int(member['quantity']) * qvontat_dish[indeks]
            cccc = {'measure': aaaa, 'quantity': bbbb}
            total_list_megering_new.append(cccc)
            indeks += 1

      new_dict_of_dish_for_persons = dict(zip(total_list_ingredients, total_list_megering_new))
      return new_dict_of_dish_for_persons

whishes_list = ['Омлет', 'Фахитос']
persons = 3
print (get_shop_list_by_dishes (whishes_list, cook_book))

