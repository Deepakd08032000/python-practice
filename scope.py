# m =10  #global
# def func1(n):
#     l=5   #local
#     global m
#     m=m+6
#     print(l , m)
#     print(n , "have")
# func1("this is me")    
# print(m)
# from re import X

x =89
def deepak():
    x =20
    def rohan():
        global x
        x =88
    print("before global" ,x)    
    rohan()
    print("after calling" , x)
deepak()  
print(x)  