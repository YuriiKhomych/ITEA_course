rate = int(input())
favourite_colors = ["blue", "grey"]
favourite_models = ["X", "GTR", "S"]
favourite_brands = ["Tesla", "Nissan"]
print("choose brand?")
branad = str(input())
    if brand in favourite_brands: print("Good choice!")
        rate += 20
print("Choose model?")
model = str(input())
    if model in favourite_models: print("Great one!")
        rate += 10
print("choose Color?")
color = str(input())
if color in favourite_colors: print("in top charts!")
rate += 10
print("choose year?")
year = input()
try:
    x = int(x)
    # exept ValueError is e:...
    year = str(input())
except ValueError: print("smth is wrong with input :\n", ValueError)
price -= 80
print("choose engine volume?")
engine_volume = float(input())
print(engine_volume)
print("choose odometer?")
odometer = int(input())
if odometer < 1000: print("1 rate- Almost new")
elif odometer > 50000: print("2 rate -old car")
rate += 10


result = price * 10 / 100
print(result)


print(f"""Your car will be {brand} brand, {model} model,
      in {color} Color, made in {year} year,
      engine has a {engine_volume} L volume,
      with {odometer} odometer, and we will call you via this number {phone_number}""")



