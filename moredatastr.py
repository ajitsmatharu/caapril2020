'''

x = [2,3,32.24,5j+1,'mystring','abc',42,'d',242,2492]
y = [1,2,3,4,5]

print(y[:])


x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]

# Access list [1, 2, 3, 4]
# x[5][:4]

# Access list [600,  700]
# [600,700]

# Access list [100, 300, 500, 600, 800]
# x[::2]

# Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
# x[::-1]

# Access list [10]
# x[5][5][0]

# Access list [ ]

# x[0:0]

#4

>>> x = range(1000)
>>> x
range(0, 1000)
>>> x
range(0, 1000)
>>> for i in x:
...
...
  File "<stdin>", line 3

    ^

IndentationError: expected an indented block
>>> y = []
>>> for j in x:
...     y.append(j)

Python 2.7.10 (default, Feb 22 2019, 21:55:15)
[GCC 4.2.1 Compatible Apple LLVM 10.0.1 (clang-1001.0.37.14)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> x = xrange(1000)
>>> x
xrange(1000)
>>> for j in x:
...
...
  File "<stdin>", line 3


    ^
IndentationError: expected an indented block
>>> y = []
>>> for j in x:
...     y.append(j)
...
Python 2.7.10 (default, Feb 22 2019, 21:55:15)
[GCC 4.2.1 Compatible Apple LLVM 10.0.1 (clang-1001.0.37.14)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> x = xrange(1000)
>>> x
xrange(1000)
>>> for j in x:
...
...
  File "<stdin>", line 3


    ^
IndentationError: expected an indented block
>>> y = []
>>> for j in x:
...     y.append(j)
...
Python 2.7.10 (default, Feb 22 2019, 21:55:15)
[GCC 4.2.1 Compatible Apple LLVM 10.0.1 (clang-1001.0.37.14)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> x = xrange(1000)
>>> x
xrange(1000)
>>> for j in x:
...
...
  File "<stdin>", line 3



#5

Tuples are beneficial in that they cannot be mutated after creation.

#6

x = []
for j in range(1100):
    if j % 3 == 0 and j % 2 ==0:
        x.append(j)

print(x)


#7

vlist = []
index = 0
input = input('Enter string')


revstring = input[::-1]

for j in revstring:

    if j in ['a','e','o','i','u']:
        vlist.append((j,index,))

    index+=1

print(vlist)



#8 print even words of string "hello my name is abcde"

string = input('Enter string\n')
string = string+' '

#hello my name is abcde

wordlist = []
evenwordlist = []

fi = 0
li = 0

for j in string:

    if j != ' ':

        li+=1

    elif j == ' ':

        li+=1

        word = string[fi:li-1]

        wordlist.append(word)

        fi = li

for word in wordlist:
    if len(word) % 2 == 0:
        evenwordlist.append(word)

print(" ".join(evenwordlist))



#9 script to produce pairs of numbers whose sum are the originally entered integer

int = int(input('Enter integer')) #1,2,3,4,5,6,7

addens = []

a = 0
b = int


for j in range(int+1):

    for k in range(int+1):

        if j + k == int:

            a,b = j,k

            if a<=b:

                addens.append((a,b,))



print(addens)

#9 example 2

int = int(input('Enter integer')) #1,2,3,4,5,6,7

addens = []

j = 0
k = int

while j<=k:

    addens.append((j,k,))

    j+=1
    k-=1

print(addens)



#10

evens = []
odds = []

while len(evens) < 5 or len(odds) < 5:

    num = int(input('Enter int between 1 and 50 (inclusive)'))

    if num < 0 or num > 50:
        print('Out of range')
        pass
    elif num % 2 == 0 and len(evens) <= 4:
        evens.append(num)
    elif num % 2 != 0 and len(odds) <=4:
        odds.append(num)

print('Evens: ',evens,'Sum: ',(sum(evens)),'Max: ',(max(evens)))
print('Odds: ',odds,'Sum: ',(sum(odds)),'Max: ',(max(odds)))



#11.     Write a program to find out the occurrence of a specific word from an alphanumeric statement. Example: 12abcbacbaba344ab


string = input('Enter string\n') #24f24fg2ug24f
charset = set()
dict = {}

for l in string:
    if l.isalpha():
        charset.add(l)


for e in charset:
    dict.update({e:0})

for l in string:

    if l.isalpha():

        dict[l] = dict[l]+1
    else:
        pass

print(dict)


#12 print another tuple of evens from given tuple


x = (1,2,3,4,5,6,7,8,9,10)

evens = ()

for j in x:
    if j % 2 == 0:
        evens = evens+(j,)

print(evens)

'''
