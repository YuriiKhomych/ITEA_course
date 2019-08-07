#Code for receiving info from user credit card

input_credit_number = input("Type your card number: ")
input_credit_cvv = input("Type your CVV number: ")
input_credit_year = input("Type your expiration date in format mm\yy : ")

# Checking card length and exiting if False

credit_length = len(input_credit_number)

if credit_length == 16:
	credit_length = True
else:
	exit(1)

# Setting card number to int. if error will be caught set to exit

try:
	credit_int = int(input_credit_number)
except ValueError as error:
	exit(1)
else:
	print("OK")

# Checking all info

credit_length = len(input_credit_number)
cvv_length = len(input_credit_cvv)
year_length = len(input_credit_year)

if credit_length != 16 and cvv_length != 3 and year_length != 5:
	exit(1)
else:
	print("Everything fine")