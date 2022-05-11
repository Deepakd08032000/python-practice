var1 = 60
var2 = 56
var3 = int(input())
if var3>var2:
    # IndentationError
    print("greter")
elif var1>var2:
    print("between")    
else:
    print("smaller")

list1 = {1,2,3,4}
if 2 in list1:
    print("yes")