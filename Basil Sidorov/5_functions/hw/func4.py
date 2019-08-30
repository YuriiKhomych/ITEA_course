def my_sum(x, y):
    return x + y


print(my_sum(1, 2))


# print(sum(my_sum))

def my_sum2(num1, *args):
    number = num1
    for num in args:
        total = number + num
    return number
