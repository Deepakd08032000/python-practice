# def function_name_print(a ,b ,c ,d):
    # print(a ,b,c,d)
def funargs(*args):
    for item in args:
        print(item)
     
har = ["deepak" , "rohan" , "skillaf" , "aa" , "ddd"]
print(funargs(*har))
# print(function_name_print("deepak" , "rohan" , "skillaf" , "aa"))   