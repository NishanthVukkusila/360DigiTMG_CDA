# -*- coding: utf-8 -*-
"""
Created on Sun May 21 20:03:49 2023

@author: Nishanth vukkusila
"""

#Module – 2 ASSIGNMENT

'''1.	Construct 2 lists containing all the available data types 
(integer, float, string, complex and Boolean) and do the following.
'''


# Construct 2 lists containing all the available data types (integer, float, string, complex and Boolean)

list1 = ['Nish', 360, 4.0, 360+4j, True]
list2 = [237, 'DigiTMG', 3+5j, False, 23.7]

# a.Create another list by concatenating the above 2 lists.
list3 = list1+list2
print("concatinated list:", list3)

# c.Print the list in reverse order.
list2 = [237, 'DigiTMG', 3+5j, False, 23.7]
list2.reverse()
print(list2)

# b.Find the frequency of each element in the concatenated list.
list1 = ['Nish','Nish', 360, 360, 360, 4.0, 360+4j, True]
print(list1.count(360), list1.count('Nish'))



#Create 2 Sets containing integers (numbers from 1 to 10 in one set and 5 to 15 in another set)

set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {5,6,7,8,9,10,11,12,13,14,15}

# a.Find the common elements in the above 2 Sets.
set3 = set1 & set2
print(set3)

#or 

set5 = set1.intersection(set2)
print(set5)

# b.Find the elements that are not common.
set4 = set1 - set2
print(set4)


# c.Remove element 7 from both Sets.
set1.remove(7)
set2.remove(7)

print(set1)
print(set2)


#Dictionary
# 3.	Create a data dictionary of 5 states having state name as key and number of covid-19 cases as values.
dict1={'Andhra':'10000','Assam':'1000', 'Bihar':'20000', 'Chattisgarh':'30000', 'karnataka':'45000'}


#a.	Print only state names from the dictionary.
dict1.keys()

#b.	Update another country and its covid-19 cases in the dictionary.
dict1['USA'] = '100000'
dict1

#1. A Write an equation that relates   399, 543, and 12345.
print(12345%543) #399




# b. When I divide 5 by 3, I got 1. But when I divide -5 by 3, I got -2 —How would you justify it?
#here the nearest lowest value is printed
print(5/3) #1.6666667 # here 1 is nearest lowest value
print(-5/3) #-1.666667 #since -2 is the lowest value it is printed

#2.  a=5, b=3, c=10. What will be the output of the following:
a = 5
b = 3
c = 10


a/=b #a = a/b
a

c*=5 #c= c*5
c

# 3. A. How to check the presence of an alphabet ‘s’ in the word “Data Science”.

print("s" in 'Data Science')

#B. How can you obtain 64 by using numbers 4 and 3
4**3 #64

#1.	What will be the output of the following (can/cannot):
Age1=5
print(Age1)

5age=55 #Syntaxerror - invalid decimal literal

# 2.What will be the output of the following (can/cannot):
Age_1=100 
print(Age_1) #100

age@1=100 #cant assign an expression here, this is because we cant use special chareters in variable name


# 3.	How can you delete variables in Python?
''' To delete variables in python del function can be used'''
deletion_of_variable = 'nothing'
print(deletion_of_variable)
del(deletion_of_variable)
deletion_of_variable
