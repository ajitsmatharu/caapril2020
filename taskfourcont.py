# TASK 4 PROBLEMS 10-14
'''
 #10.     Write a program which can filter() to make a list whose elements are even number between 1 and 20 ( both included)

j = list(filter(lambda x:x%2==0,range(1,21)))
print(j)

# 11.     Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]
# Hints: Use map() to generate a list.
#               Use filter() to filter elements of a list
#             Use lambda to define anonymous functions



j = filter(lambda x:x%2==0, range(1,11))
k = map(lambda x:x**2, list(j))
print(list(k))



#12 write a function to compute 5/0

def fiveo(x,y):

    try:
        print(x/y)

    except:
        print('invalid denominator')

fiveo(5,0)



#13
#
# 13.     Flatten the list [[1,2,3],[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
# Goal : Turn [1,2,3,4,5,6,7] to 1234567

from functools import reduce
x = [[1,2,3],[4,5],[6,7,8]]

def add(x,y):
    return (x+y)


flat = reduce(add, x)
print(flat)


#14 output of the following?
# (i) def foo():
#     try:
#         return 1
#     finally:
#         return 2
# k = foo()
# print(k)
#
# (ii) def a():
#     try:
#         f(x, 4)
#     finally:
#         print('after f')
#     print('after f?')
# a()

# i) output: 2
# ii) f is not defined

'''
