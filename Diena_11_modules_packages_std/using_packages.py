# # # Creating and using packages
# # # simply make subfolders
# # # moved .py there
# # # create __init__.py
# # # https://docs.python.org/3/reference/import.html
# # # https://stackoverflow.com/questions/12229580/python-importing-a-sub-package-or-sub-module
# # # https://realpython.com/lessons/subpackages/

# # import my_lib.my_tools
# # import my_lib.my_tools as mt
# # from my_lib.my_tools import tool_fun
# from my_lib.my_tools import tool_fun as tf
# print(f"Starting program in {__file__}")
# # import my_cool_lib.my_cool_mod
# import pkg.my_utils
# import pkg.my_utils as my_ut
# from pkg.my_utils import add
# from pkg.my_utils import add as my_add

# from  .. import some_mod # generally not recommended

import mat_lib
print(mat_lib.add(5,35)) # this works because I set PYTHONPATH for my utilities folder

# print(some_mod.mult(4,66))

# # import pkg.my_housing
# # import pkg as pk
# # import pkg.subp.sub_utils
# # import pkg.subp.sub_utils as sutils
# # # from pkg.subp.sub_utils import subadd # can use this thats fine
# # # from pkg.subp.sub_utils import * # avoid this, because of namespace pollution
# # from pkg.subp.sub_utils import (
# #     subadd,
# #     subprint,
# #     MAGIC_PI
# # )
# # sutils.subadd(555, 100)

# # my_lib.my_tools.tool_fun("My tools")
# # mt.tool_fun("tools again")
# # tool_fun("Here we have tools")
# tf("aha!")

# pkg.my_utils.add(30, 50)
# my_ut.add(30, 50)
# add(55,212)
# my_add(33,55)
# # gar = pkg.my_housing.Garage("Funny")

# # pk.my_utils.add(30, 60)

# # pkg.subp.sub_utils.subadd(100, 20)
# # sutils.subadd(50, 20)

# # subadd(30, 90)
# # subprint("Valdis")
# # print(MAGIC_PI)
# # my_cool_lib.my_cool_mod.add(555, 222)
