num_output = []

for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        num_output.append("FizzBuzz")
    elif number % 3 == 0:
        num_output.append("Fizz")
    elif number % 5 == 0:
        num_output.append("Buzz")
    else:
        num_output.append(number)

print(num_output)