
"""


'But we're talking about practice right now' by Allen Iverson


"""
import random
# a few types
one = 1
one_float = 1.0
string = "string"
false = True
no = None
file = open("text.txt", "r")
b = list()
c = tuple()
s = {1,2,3}
se = frozenset((1,23))
dic = dict(zip([1,2,3], "abc"))
gen = (sum(i+i) for i in range(6))
byte = bytearray()
print(type(one),type(one_float),type(string), type(false), type(no), type(b), type(c), type(file), type(s),type(se), type(dic), type(gen), type(byte))

# get some input
First_Name = ''
Last_Name = ''
Phone_number = ''
Group = ''

INPUT_str = [First_Name, Last_Name, Phone_number,  Group]
for i in range(len(INPUT_str)):

    INPUT_str[i] = input("Write something: ")

print(INPUT_str)

a = 0
b = 0
c = 0
d = 0
INPUT_num = [a, b, c, d]

for i in range(len(INPUT_num)):

    if not i % 2 :

        INPUT_num[i] = int(input("Write something: "))

    else:

        INPUT_num[i] = float(input("Write something: "))

print(INPUT_num)

# time to have a look at the operators

plus = INPUT_num[0]+INPUT_num[2]
ne_plus = INPUT_num[0] - INPUT_num[2]
mult = INPUT_num[0]*INPUT_num[2]
div = INPUT_num[0]/INPUT_num[2]
flo = INPUT_num[0]//INPUT_num[2]
mod = INPUT_num[0]%INPUT_num[2]
exp = INPUT_num[0]**INPUT_num[2]
# print(plus,exp,mod,mult)
#assignment time
m = 3.1415
m +=INPUT_num[1]
print(m)
m -=INPUT_num[1]
print(m)

m *=INPUT_num[1]
print(m)

m **=INPUT_num[1]
m /=INPUT_num[1]
m //=INPUT_num[1]

k = random.randint(1,15)
print(k)

if k == 10:

    print("==")

elif k < 15:

    print("<")

elif k > 15:

    print(">")

elif k >= 15:

    print(">=")

elif k != 15:

    print("!=")

elif k <= 3:

    print("!=")

else:

    print('else')

# string time

print(f'k = {k}')
print('{} something {}'.format(1,2))
print('{1} something {0}'.format(1,2))
print('%d - int,  %0.2f - float' % (1,4.5))




"""

Thank you for attention

"""


