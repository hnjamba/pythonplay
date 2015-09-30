'''
Created on Aug 12, 2015

@author: hnjamba
'''

'''
print range(7)
print range(2, 7)
print range(2, 20, 3)

for i in range(2, 20, 2):
    print i
    
'''

'''
for year in range(1980, 2020):
    yearRemainder = year % 4
    
    if yearRemainder == 0:
        print "The year {} ... is a leap year. February has 29 days" . format(year)
    else:
        print "The year {} ... is not a leap year. February was same" . format(year)
'''        


'''
cats = ['Manx', 'Calico', 'Bluebay']

for cat in cats:
    print "The cat is name {}".format(cat)
'''


numbers = [5, 2, 0, 12, 22, 36, 0, 15]
for number in numbers:
    if number == 0:
        print "Skipping number {}".format(number)
        continue
    
    dividedNo = 100.0 // number
    remainderNo = 100.0 % number
    print "100.0 divided by {} is equal to {} and remains {}".format(number, dividedNo, remainderNo)


'''
personAge = raw_input("Enter your age : ")
while not personAge.isdigit():
    print "Entry {} is not a valid age".format(personAge)
    personAge = raw_input("Enter your age : ")
    
print "Age has been set to {}".format(personAge)
'''

'''
while True:
    text = raw_input("Enter some text for e's or enter q to quit : ")
    if text == 'q':
        break
    print text.count('e')
'''



