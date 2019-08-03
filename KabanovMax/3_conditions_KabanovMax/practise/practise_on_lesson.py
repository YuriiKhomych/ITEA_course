a = 5
b = 4
c = a > b
print(c)
a < b
#true
new_string = ""
c = 6
d = 7
print(a > b and c > d)
#false
print(a > b or c > d)
#true
print(not (a > b or c > d))
#false

#true or true =
#true or true =
#true or true =
#true or true =

#true and true = ?
#true and true = ?
#true and true = ?
#true and true = ?

my_string = "abcd"
print(my_string)
#"a" in my_string = true
#"abd" in my_string = false
#"b" in my_string = true
#"d" in my_string = true

my_students = ("Anya", "Nikita", "Max")
print(my_students)
#"Anya" in my_students = true

print(not "Anya" in my_students)

not {}
#always negative

the_same_students = my_students
the_same_students is my_students
#true

the_same_students is not my_students
#False

my_new_students = ("Anya", "Nikita", "Max")

the_same_students is my_new_students
#False but in contex is True

my_max = "Max"
my_new_max = "Max"
#True cuz definition is not changible, string is changible that why it false

# for if make definitions and define them aas true

students = []
# empty false
if students:
	print("Students in here!")
elif "Oleg" in students:
	print("Oleg is here!")
else:
	print("Students not here!")
# will be else cos false for first two options

students = ["Max"]
# empty false
if "Oleg" in students:
	print("Oleg is here!")
if students:
	print("Students in here!")
else:
	print("Students not here!")

students = ["Max", "Oleg"]
lost_students = ["Yurii"]

if students:
	print("Students in here!")
	if "Oleg" in students:
		print("Oleg is here!")
	elif "Max" in students:
		print("Max is here!")
else:
	if lost_students:
		print(f"{lost_students}")

print(f"Final program, students not found) {students}")

a = 1
b = 2

try:
	a + b
except ValueError as error:
	print("Something broken", error)
print("final code")
# all good no need in except

a = 1
b = '2'
c = 3

try:
	result = a + b
except Exception as error:
	print("Something broken", error)
	result = a + int(b)
else:
	result += c
finally:
	print(result)
# finally works always even if other do

print(f"Result {result}")



