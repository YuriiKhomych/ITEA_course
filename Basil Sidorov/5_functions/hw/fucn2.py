def len(string):
    count = 0
    for element in string:
        count+= 1
    return count
word = input("Enter word here: ")

print("Input lenght is: " len(word))