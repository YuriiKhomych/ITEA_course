countdigits = 0
countletters = 0
while True:
    userinput = input("Enter string")
    for element in userinput:
        if element.isdigit():
            countdigits +=1
        elif element.isalpha():
            countletter +=1
print(f"Letters in input: {countletters}, digits in input:{countdigits}")
