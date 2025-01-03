# Hide the credit card number
credit_card_number=input("Enter credit card number : ")
credit_number='*'*(len(credit_card_number)-4)+credit_card_number[12:]
print("credit card number={}".format(credit_number))