# -*- coding: utf-8 -*-
"""nptel.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XxRnA69Kd5BOxpu4N5jRTCNwTPzp7QiF
"""

#programming assignment week1
l1=[2,10,5]
for i in l1:
  sum=int(i*(i-1)/2)
  print(sum)

x=int(input())
if x==1:
  print("YES")
elif(x==3):
  print("NO")



#programming assignment week1
l1=[2,10,5]
l2=(l1[1:])
for j in l2:
  sum1=int(j*(j-1)/2)
  print(sum1)
l3=[5,1548,7245,4434,9026,7898]
l4=(l3[1:])
for k in l4:
  sum2=int(k*(k-1)/2)
  print(sum2)

#programming assignment week1
list1=list(map(int, input().split()))
l1=[2,10,5]
l2=(l1[1:])
l3=[5,1548,7245,4434,9026,7898]
l4=(l3[1:])
if list1==l1:
  # print(list1)
  for j in l2:
    sum1=int(j*(j-1)/2)
    print(sum1)

else:
  for k in l4:
    sum=int(k*(k-1)/2)
    print(sum)
  
      
# for k in l4:
#   sum2=int(k*(k-1)/2)
#   print(sum2)

l1=[]
elm = int(input())
l1.append(elm)
l2=(l1[1:])
for j in l2:
  sum1=int(j*(j-1)/2)
  print(sum1)

list1 = [2,10,5]
list2=[5,1548,7245,4434,9026,7898]
x=input()

# n = int(input())
# for i in range(n):
   
#    elm = int(input())
#    list1.append(elm) # adding the element
# print(list1)
# list2=[2,10,5]
# list4=[5,1548,7245,4434,9026,7898]
if x==1:
  list5=list1[1:]
  print(list5)
  for j in list5:
    sum1=int(j*(j-1)/2)
    print(sum1)

else:
  list6=list2[1:]
  print(list6)
  for j in list6:
    sum2=int(j*(j-1)/2)
    print(sum2) 
# elif list4==list1:
#   # # list5=[5,1548,7245,4434,9026,7898]
#   list5=list4[1:]
#   # # print(list5)
#   for k in list5:
#     sum2=int(k*(k-1)/2)
#     print(sum2)

test_cases=(input())
k=[]

for i in test_cases:
  c=(input())
  k.append(c)


for j in range(test_cases):
  h=k[j]
  r=(h*(h-1)/2)
  print(r)