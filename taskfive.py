'''

#1


x == 3





# 2


from sys import argv
nameofprogram = argv

while True:

    try:

        filename = input('Enter filename\n')
        fh=open(filename)
        content=fh.read()
        print(content)
        fh.close()
        break
    except:
        print('Incorrect filename; please provide correct filename')




# 3


j=int(input("Enter 4 digit number"))
try:
    if len(str(j))!=4:
        raise ValueError
    else:
        print("Value accepted")

except ValueError:
    print("Invalid # of digits")



# 4.     Create a login page backend to ask user to enter the UserEmail and password.
# Make sure to ask Re-Type Password and if the password is incorrect give chance to enter it again
#  but it should not be more than 3 times.

email = 'ajit@mail.com'
password = 'password'
attemptsleft = 3

while True:
    try:
        e = input('Enter email\n')
        if e != email:
            raise ValueError('Unrecognized email')
        elif e == email:
            break
    except ValueError as ve:
        print(ve)


while True:
    try:
        if attemptsleft > 0:
            p = input('Enter password\n')
            if p != password:
                attemptsleft-=1
                raise ValueError('Incorrect password. ',attemptsleft,' tries remaining.')

            elif p == password:
                print('Login Successful')
                break
        else:
            print('# of Attempts exceeds limit. Security Lockout')
            break
    except ValueError as ve2:
        print(ve2)



# 5
# 6


from sys import argv
nameofprogram = argv

while True:

    try:

        filename = input('Enter filename\n')
        fh=open(filename)
        content=fh.readlines()
        for string in content:
            if len(string) % 2 == 0:
                print(string)
        fh.close()
        break
    except:
        print('Incorrect filename; please provide correct filename')

'''
