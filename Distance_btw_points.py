#Distance between n points
import math

n=int(input("in what dimension do you want to calculate ? : "))
list1 = []
print("FIRST POINT")
for i in range(n):
    list1.append(float(input("Enter coordinate : ")))
list2 = []
print("SECOND POINT")
for j in range(n):
    list2.append(float(input("Enter coordinate : ")))
print(list1)
print(list2)
difference = []
zip_object = zip(list1, list2)
for list1_k, list2_k in zip_object:
    difference.append(list1_k-list2_k)
#print(difference)
f=0
f_list= []
for i in difference:
    f = i ** 2
    i = i + 1
    f_list.append(f)
#print(f_list)
sum_list = 0
for c in f_list:
    sum_list=sum_list +c

print("Distance between these points = ",math.sqrt(sum_list))
