my_list = ["a", "e", "i", "o", "u"]

def Vowel(x):
    if x in my_list:
        return True
    else:
        return False

x = input("Enter symbol: ")
print(Vowel(x))