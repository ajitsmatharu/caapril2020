x = int(input('Enter x'))
y = int(input('Enter y'))
try:
    print(x+y)
except ValueError:
    print('syntax error')
