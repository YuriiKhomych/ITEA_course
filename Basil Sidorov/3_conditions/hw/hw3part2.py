card_number = input()
card_cvv = input()
credit_expire_date = input()

if len(card_number) == 16
    card_number = True
else
    exit(1)
try:
    ccn = int(card_number)
except ValueError as e:
    exit(1)
else:
    print("Done")

if card_number != 16 and card_cvv != 3 and credit_expire_date != 5:
    exit(1)
else
    print("Everything fine")
