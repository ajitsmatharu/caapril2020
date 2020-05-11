#1
'''

def revstring(str):
    print(str[::-1])

#2



def upperlower(str):

    uppers = 0
    lowers = 0

    for x in str:
        if x in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
            uppers+=1
        elif x in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
            lowers+=1

    print('Upper chars: ',uppers,'Lower chars: ',lowers,)

str = input('Enter string\n')
upperlower(str)




#3

def uniqueelements(list):
    newset = set(list)
    newlist = []
    for x in newset:
        newlist.append(x)
    print(newlist)

uniqueelements([1,1,1,1,2,2,2,3,4,5,5,5,6,7])


#4

def hyphenwords(str): #this-is-my
    x = str.split('-')
    x.sort()

    print('-'.join(x))


string = input('Enter string\n')
hyphenwords(string)




#5 sequence of lines as input and prints them after capitalizing all

def caplines():

    x = '0'
    lines = []
    caplines = []

    while x != '1':

        x = input('Enter line. Enter 1 if done.\n')
        if x != '1':
            lines.append(x)

    for j in lines:
        q = j.upper()
        caplines.append(q)

    for j in caplines:
        print(j)

caplines()


#6


def intsum():

    a = input('Enter int 1\n')
    b = input('Enter int 2\n')

    a = int(a)
    b = int(b)
    sum = a+b

    print(sum)

intsum()



#7

def biggerstring(str1,str2):
    x = len(str1)
    y = len(str2)
    if x > y:
        print(str1)
    elif y > x:
        print(str2)
    elif x == y:
        print(str1)
        print(str2)

one = input('Enter string one\n')
two = input('Enter string two\n')
biggerstring(one,two)



#8
def tuponetwenty():
    tup = ()
    for x in range(1,21):
        tup = tup + ((x**2),)
    print(tup)

tuponetwenty()


#9
def shownumbers(limit):

    for x in range(0,limit+1):
        if x%2==0:
            print(x,'EVEN')
        elif x%2!=0:
            print(x,'ODD')
shownumbers(10)

'''
