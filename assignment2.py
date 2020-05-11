'''
Ajit Matharu Assignment 2


#1

num = int(input('Enter int'))

if num % 3 == 0 and num % 5 != 0:
    print('Consultadd')

elif num % 5 == 0 and num % 3 != 0:
    print('c')

elif num % 3 == 0 and num % 5 == 0:
    print('consultadd python training')



#2

selection = int(input('Select 1 - Addition, 2 - Subtraction, 3 - Division, 4 - Multiplication, 5 - Average'))

if selection == 1 or selection == 2 or selection==3 or selection==4:

    first = float(input('Enter first value'))
    second = float(input('Enter second value'))

    if selection == 1:
        ans = first + second

    elif selection == 2:
        ans = first - second

    elif selection == 3:
        ans = first/second

    elif selection == 4:
        ans = first*second

elif selection == 5:

    first = float(input('Enter first value'))
    second = float(input('Enter second value'))

    ans = (first+second)/2


print(ans)

if ans < 0:
    print('NEGATIVE')



#3

a=10
b=20
c=30

avg = (a+b+c)/3

print('Avg: ',avg)

if avg > a and avg > b and avg > c:

    print('Avg is higher than a, b, and c')

elif avg > a and avg > b:

    print('Avg is higher than a, b, and c')

elif avg > a and avg > c:

    print('Avg is higher than a and c')

elif avg > b and avg > c:

    print('avg is higher than b and c')

elif avg > a:

    print('avg just higher than a')

elif avg > b:

    print('avg just higher than b')

elif avg > c:

    print('avg just higher than c')


#4

x = 1

while x > 0:

    x = float(input('Enter value'))

    if x < 0:
        break
    elif x > 0:
        print('Good going')


print("It's over")



#5

x = 2000

while x < 3201:

    if x % 7 == 0 and x % 5 != 0:

        print(x)

    x+=1



#6

1) error

2) 0, 1, 2, 3

3) 0, 1, 2, 3, 4


#7

x = 0

while x < 7:

    if x != 3 and x != 6:

        print(x)

    x+=1

    continue



#8

letters = 0
numbers = 0

string = input('Enter string\n')

for x in string:

    if x in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]:

        letters+=1

    elif x in ['1','2','3','4','5','6','7','8','9']:

        numbers+=1

print('Letters: ',letters)
print('Numbers: ',numbers)



#9

answer = 43

number = -1000

#number = int(input('Guess the lucky number'))

while number != answer:

    number = int(input('Guess the lucky number'))

    if number != answer:

        cont = input('Guess again? y or any other key to exit')

        if cont == 'y':

            continue

        else:
            break


#10

luckynum = 43

count = 1

guesses = []

while count < 6:

    guess = int(input('Enter guess'))

    guesses.append(guess)

    if luckynum == guess:

        print('Good guess!')

    else:
        print('Try again!')

    count+=1

print('Game over')


#11

luckynum = 43

count = 1

guesses = []

while count < 6:

    guess = int(input('Enter guess'))

    guesses.append(guess)

    if luckynum == guess:

        print('Good guess!')

        break

    else:
        print('Try again!')

    count+=1

print('Game over')

if guess != luckynum:
    print('Sorry, not very successful')

'''
