# 1.    Write a program that calculates and prints the value according to the given formula:
# Q= Square root of [(2*C*D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
'''
print('ONE')
print('')

def calculate1(val):
    d = (val.split(','))
    j = []

    for d in d:
        j.append(float(d))

    c = 50
    h = 30

    for x in j:

        q = [(2*c*x)/h]

        print(q)

val = input('Enter CSVs for eval\n')
calculate1(val)
'''


#5

class time():
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self,hours,minutes):
        self.hours = self.hours + hours
        self.minutes = self.minutes + minutes

    def displayTime(self):
        print('Hours:',self.hours,'Minutes:',self.minutes)

    def displayMinutes(self):
        total_min = self.hours*60 + self.minutes
        print('Total Min: ',total_min)

#6

class person():
    def __init__(self, age):
        if age > 0:
            self.age = age
        else:
            print('age out of bounds, setting age to 0')
            self.age = 0

    def yearsPassed(self,years):
        self.age = self.age + years

    def displayAge(self):
        print('Age:',self.age)

    def amIold(self):
        if self.age > 18:
            print(self.age,'You are old')
        elif self.age > 12 and self.age < 19:
            print(self.age,'You are a teenager')
        else:
            print(self.age,'You are young')
