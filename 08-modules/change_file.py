import import_st_library3  # переменные образуються в пространстве имен модуля в Special Variables
from import_st_library3 import *  # переменные копируються в пространство имен актуального модуля
from importlib import reload
print('------------------------------')

print('\nМеняем не изменяемый объект:')
print('\tmy_str до изменений:')
print(import_st_library3.my_str, id(import_st_library3.my_str), '--> from import_st_library3 scope')
print(my_str, id(my_str), '--> from change_file scope')
print('------------------------------')
print('\tmy_str после изменений:')
import_st_library3.my_str = 'hello'
my_str = 'hi'
print(import_st_library3.my_str, id(import_st_library3.my_str), '--> from import_st_library3 scope')
print(my_str, id(my_str), '--> from change_file scope')
print('------------------------------')

# print('\nМеняем изменяемый объект на прямую:')
# print('\tmy_list до изменений:')
# print(import_st_library3.my_list, id(import_st_library3.my_list), '--> from import_st_library3 scope')
# print(my_list, id(my_list), '--> from change_file scope')
# print('------------------------------')
# print('\tmy_list после изменений:')
# import_st_library3.my_list = [4, 5, 6, 7]
# my_list = [11, 99]
# print(import_st_library3.my_list, id(import_st_library3.my_list), '--> from import_st_library3 scope')
# print(my_list, id(my_list), '--> from change_file scope')
# print('------------------------------')

print('\nПерезапускаем модуль:')
# reload(import_st_library3)
print('------------------------------')

print('\nМеняем изменяемый объект косвенно:')
print('\tmy_list до изменений:')
print(import_st_library3.my_list, id(import_st_library3.my_list), '--> from import_st_library3 scope')
print(my_list, id(my_list), '--> from change_file scope')
print('------------------------------')
print('\tmy_list после изменений:')
import_st_library3.my_list[0] = 1000
my_list[1] = 300
print(import_st_library3.my_list, id(import_st_library3.my_list), '--> from import_st_library3 scope')
print(my_list, id(my_list), '--> from change_file scope')
print('------------------------------')
