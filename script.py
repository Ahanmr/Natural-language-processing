import numpy as np
from math import floor
c=floor(np.random.rand()*1000)
print(c)
num=str(input("Enter 4 numbers:"))+str(c)
print(num)
lst=[]
for i in num:
    lst.append(i)
lst = list(map(int, lst))
lst1=np.array(lst)*np.array([8,7,6,5,4,3,2])
last_digit=sum(lst1)%11
print(last_digit)
