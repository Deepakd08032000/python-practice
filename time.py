# from mimetypes import init
import time
# time module
initial = time.time()
print(initial)

k= 0
while(k<5):
    print("this is don")
    # time.sleep(2)
    k = k+1  
    
print("while loop ran in time" , time.time() - initial, "seconds")  
initial2 = time.time()  
for i in range(5):
       print("this is deepak dhakad")
print("while loop ran in time" , time.time() - initial, "seconds")    
localtime = time.asctime()
print(localtime)