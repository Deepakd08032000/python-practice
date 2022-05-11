from sys import float_repr_style


list2 = {int , float , "deepak" , 1,2,3,4,5,5,6,7,7,899,99}
for item in list2:
    if str(item).isnumeric() and item<6:
        print(item)
        