number_input = [1,2,3,6,9,14,19,22,37,39]
odd = 0
even = 0

for number in number_input:
    if number % 2:
        odd += 1
    else:
        even += 1
print(even, odd)
