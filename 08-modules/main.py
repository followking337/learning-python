"""
    import [package].[module]
        [package].[module].[variable]

    from [package] import [module]
        [module].[variable]

    from [package].[module] import [variables, functions, ...]
        [variable]

    from [package].[module] import *
        [variable]

    Файл __init__
        --> Запускается при любом импорте пакета только 1 раз.
        --> Поиск модуля в файле __init__ при импорте, относительно файла __init__:
             . текущий каталог
             .. каталог выше

    Переменная __all__
        --> Указывает к каким переменным модуля будет доступ.
        --> Переменная __all__ прописывается в модуле источник:
            __all__ = ['variable', 'variable']
        -->  import производится только через * в модуле назначение:

"""

# import package1.file1
# import package1.file2
# print(package1.file1.b)
# print(package1.file2.d)

# from package1 import file1
# from package1 import file2
# print(file1.b)
# print(file2.d)

# from package1.file1 import a, b, c
# from package1.file2 import *
# print(a, b, c)
# print(d, h)

# import package1
# # 1й способ:
# print(package1.a, package1.d)
# 2й способ:
# print(package1.file1.a, package1.file2.d)
