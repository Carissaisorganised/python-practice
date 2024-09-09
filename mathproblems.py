#Division is decimal by default 

print(5 / 2)

#Double slash rounds down 

print(5 // 2)

#CAREFUL: most lanaguages round towards 0 by 
#default so negative numbers will round down 
print(-3 // 2)

#A workaround for rounding towards zero is to 
#use decimal division and then convert to int. 
print(int(-3 / 2))

#Modding is similar to most langauages 
print(10 % 3)

#Except for negative values 
print(-10 % 3)

#To be consistent with other languages modules 
import math 
print(math.fmod(-10,3))

#more math helpers 
print(math.floor(3 / 2))
print(math.ceil(3 / 2))
print(math.sqrt(2))
print(math.pow(2,3))

#Max/Min Int 

float("inf")
float("-inf")

#Python numbers are infinate so they never overflow
import math 
print(math.pow(2, 200))

#but still less than infinity 
print(math.pow(2, 200) < float("inf"))