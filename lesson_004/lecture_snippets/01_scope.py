# распаковка параметров (аргументов)
def vector_module(x, y, z):
    return (x ** 2 + y ** 2 + z ** 2) ** .5


# # распаковка позиционных параметров
# some_list = [2, 3, 4]
# res = vector_module(*some_list)
# # x, y, z = some_list
# # print(vector_module(2, 3, 4))
# print(res)
#
# some_dict = {'x': 2, 'y': 3, 'z': 4}
# res = vector_module(**some_dict)
# # vector_module(x=2, y=3, z=4)
# print(res)

# some_list = [2, 3]
# some_dict = dict(z=4)
# res = vector_module(*some_list, **some_dict)
# vector_module(2, 3, z=4)
some_list = [3, 4]
res = vector_module(2, *some_list)
print(res)
