'''
Ajit Matharu


#1

list_one = [1,2.4,'a',4,67,355,5j+1,90,24,3.423]


#2

y = [1,2,3,4,5]

b = y[:-1]

print(b)



#3

list_two = [3,2,5,6,8]

sum = 0
multiply = 1

for j in list_two:

    sum = sum + j
    multiply = multiply*j

print(sum,multiply)



#4

list_three = [224,2452,63,2,2,73,5,362,3]

print(min(list_three))
print(max(list_three))



#5

list_four = [24,245,27,24,52,536,357,242,35,467,47,34]

for j in list_four:

    if j % 2 == 0:

        list_four.remove(j)

print(list_four)


#6

b = []
c = []


for j in range(1,31):

    b.append(j**2)

print(b)

c.append(b[0])
c.append(b[-5])
c.append(b[-4])
c.append(b[-3])
c.append(b[-2])
c.append(b[-1])

print(c)



#7

x = [1,3,5,7,9,10]
z = [2,4,6,8]

x.pop(-1)

for j in z:
    x.append(j)

print(x)




#8

a={1:10,2:20}
b={3:30,4:40}

a.update(b)

print(a)

'''

#9

num = int(input('Enter int'))
#num_list = []
dict = {}

for j in range(1,num+1):
#    num_list.append(j)

#for j in num_list:

    dict.update({j:j**2})

print(dict)


'''
#10

entry = input('Enter list\n')
x = ''
list = []
tup = ()
temptup = ()
length = len(entry)
#print(length)
s = 0

for j in entry:
    if (j in ['1','2','3','4','5','6','7','8','9','0']):

        x = x+j

        s+=1

        #print(s)

        #print('x=',x)

    elif (j == ','):

        #print('APPEND ',x)

        list.append(x)

        temptup = (x,)
        #print('TEMPTUP ',temptup)
        tup = tup+temptup
        temptup = ()
        s+=1

        x = ''

        #print(s)



list.append(x)
temptup = (x,)
tup = tup+temptup

print(list)
print(tup)

'''
