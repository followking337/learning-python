import import_st_library3
import import_st_library3  # импортируется только 1 раз
print('----------------------------------')
print(import_st_library3.my_num1)
import_st_library3.my_num1 = 20
print(import_st_library3.my_num1)
print('----------------------------------')
import import_st_library3  # после очередного импорта переменная не перезатирается
print(import_st_library3.my_num1)
print('----------------------------------')
import importlib
importlib.reload(import_st_library3)  # в случае если хотим перезагрузить модуль
print(import_st_library3.my_num1)
