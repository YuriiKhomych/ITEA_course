#Write a function `is_member()` that takes a value
#i.e. a number, string, etc) x and a list of values a,
#and returns True if x is a member of a, False otherwise.
#(Note that this is exactly what the `in` operator does, but
#for the sake of the exercise you should pretend Python
#did not have this operator.)

def is_member(some_element, some_array):
    for element in some_array:
        if element == some_element:
            return True
        else:
            return False

