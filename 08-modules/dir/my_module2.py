import sys
from pprint import pprint
sys.path.append('/Volumes/GoogleDrive/Mi unidad/Aprendizaje/Data Scientist/Egoroff/Modules')
pprint(sys.path)  # поскольку path это список, можем добавить другие пути к модулям.
print('----------------------------------')
# import import_st_library
# print(import_st_library.factorial(10))
# print(import_st_library.pi, import_st_library.e)
# ----------------------------------
from import_st_library import my_num1, my_str
print(my_num1, my_str)
# ----------------------------------
# import import_st_library2
# print(import_st_library2.factorial(10))
# print(import_st_library2.pi, import_st_library2.e)
# ----------------------------------
# from import_st_library2 import my_num1, my_str
# print(my_num1, my_str)
