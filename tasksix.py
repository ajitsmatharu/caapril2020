# TASK SIX: HIGHER ORDER FUNCTIONS, GENERATORS, LIST COMPREHENSION AND DECORATOR

# 1.    Write a program to Python find the values which is not divisible by 3
# but is should be a multiple of 7. Make sure to use only higher order function.
print('ONE')

x = filter(lambda x:x%3!=0 and x%7==0, range(100))
print(list(x))



# 2.     Write a program in Python to  multiple the element of list by itself using
#traditional function and pass the function to map to complete the operation.

print('TWO')

def funcone(x):
    return x**2

j = list(map(funcone, [1,2,3,4,5]))
print(j)



# 3.     Write a program to Python find out the character in a string which is uppercase using list comprehension.

print('THREE')

str = 'thiS IS a STRinG'

x = [char for char in str if char.isupper()]
print(x)



# 4.     Write a program to construct a dictionary from the two lists containing the names of students
# and their corresponding subjects. The dictionary should maps the students with their respective subjects.
#Let’s see how to do this using for loops and dictionary comprehension. HINT-Use Zip function also

print('FOUR')

Student = ['Smit', 'Jaya', 'Rayyan']
capital = ['CSE', 'Networking', 'Operating System']

dict = {}

index = 0

for x in Student:
    dict.update({(Student[index]):(capital[index])})
    index+=1

print(dict)





# 5.     Learn More about Yield, next and Generators
# 6.     Write a program in Python using generators to reverse the string. Input String = “Consultadd Training”

print('SIX')

str='Consultadd Training'

x = (str[::-1])
print(x)


# 7.     Write any example on decorators.
# 8.     Learn about What is FRONT END and its Technologies and Tools
# Make sure to mention at least 5 top notch technologies of Frontend.
# Also mentioned the name of companies using those 5 technologies individually
