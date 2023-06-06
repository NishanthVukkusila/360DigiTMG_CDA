#MODULE – 3 ASSIGNMENT
#Conditional Statements

'''Take a variable ‘age’ which is of positive value and check the following:
a.	If the age is less than 10, print “Children”.
b.	If the age is more than 60, print ‘senior citizens’.
c.	 If it is between 10 and 60, print ‘normal citizen’.
'''

age = 3
age = 30
age = 300


if age <10:
    print("Children")
elif age >10 and age < 60:
    print('normal citizen')
else:
    print('senior citizen');
    

'''2.Find the final train ticket price with the following conditions. 
a.	If male and ‘sr.citizen’, 70% of the fare is applicable
b.	If female and ‘sr.citizen’, 50% of the fare is applicable.
c.	If a female and a normal citizen, 70% of the fare is applicable.
d.	If a male and a normal citizen, 100% of the fare is applicable.
'''

is_male = True
age = 5
age = 60

if is_male == True and age >= 60:
    print("70% of the fare is applicable")
elif is_male == False and age >= 60:
    print("50% of the fare is applicable")
elif is_male == False and age < 60:
    print("70% of the fare is applicable")
else:
    print("100% fare is applicable")


'''3.Check whether the given number is positive and divisible by 5 or not.'''

num = int(input("enter your number: "))

if num >= 0 and num % 5 == 0:
    print("entered number is positive and divisible by 5")
elif num != 0 and num %5 !=0:
    print(' entered  nunber is a negative and not divisible by 5')
else:
    print("number is negative")
    
'''1.	A) list1 = [1, 5.5, (10+20j), ’data science’]. Print default functions and parameters exist in list1.
'''
list1 = [1, 5.5, (10+20j), 'data science']

dir(list1)

'''B) How do we create a sequence of numbers in Python?
C) Read the input from the keyboard and print a sequence of numbers up to that number.
'''

# Generating a sequence from 0 to 99
sequence = list(range(100))
print(sequence)  

#step size can also be given
sequence = list(range(0,100,20))
print(sequence)  

#using for loop
sequence = []
for i in range(1, 6):
    sequence.append(i)
print(sequence)  # [1, 2, 3, 4, 5]

'''2.	Create 2 lists: One list contains 10 numbers (list1 = [0, 1, 2, 3....9]) and another 
list contains words of those 10 numbers (list2 = ['zero', 'one', 'two', ...., 'nine']).
a.	Create a dictionary such that list2 are keys and list1 are values.
'''
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

dictionary = dict(zip(list2, list1))
print(dictionary)

'''3.	Consider list1 [3, 4, 5, 6, 7, 8]. Create a new list2 such that Add 10 to the even number and 
multiply with 5 if it is an odd number in the list1.'''

list1 = [3, 4, 5, 6, 7, 8]
list2 = []

for num in list1:
    if num % 2 == 0:  # even number
        new_num = num + 10
    else:  # odd number
        new_num = num * 5
    
    list2.append(new_num)

print(list2)


'''Write a simple user-defined function that greets a person in such a way that:
i) It should accept both the name of a person and the message you want to deliver.
ii) If no message is provided, it should greet a default message ‘How are you’.
'''
def greet_person(name, message='How are you?'):
    print(f"Hello, {name}! {message}")

# Example usage
greet_person('nishanth', 'Hope you have a great day!')
greet_person('nishanth')


 



