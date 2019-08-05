"""

car industry

"""

#create a car?))))
class Car:

    def __init__(self, Brand, Model, Color, Year, Engine_volume, Odometr, Phone_number):

        self.Brand = Brand
        self.Model = Model
        self.Color = Color
        self.Year = Year
        self.Engine_volume = Engine_volume
        self.Odometr = Odometr
        self.Phone_number = Phone_number

        return self

car = {}
price = 0


#input for every parametr
car["Brand"] = input()
price += 10
car['Model'] = input()
price += 10
car['Color'] = input()
price += 10
car['Year'] = input()
price += 10
car['Engine volume'] = input()
price += 10
car['Odometer'] = input()
price += 10
car['Phone number'] = input()
price += 10
price /=10
car['Odometer'] = float(car['Odometer']) - 1
car['Year'] = float(car['Year']) - 1

# print the result

for key in car:

    print(f"Your car {key} is: {car[key]}",end='\t')