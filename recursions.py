# def print2(str1):
#     print(str1)
#     print("this is" +str1)
# itrative
n = int(input("enter the number"))
def factorial_itrative(n):
    fact = 1
    for i in range(n):
        fact = fact*(i+1)
    return fact
    # print(fact)
print(factorial_itrative(n))
n = int(input("enter the number"))
def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n * factorial_recursive(n-1)  
print(factorial_recursive(n))        
    