#Give me the discount
def discount():
    full_price=eval(input("Enter full price of an item: "))
    discount=eval(input("discount amount of an item: "))
    return full_price-discount
dis=discount()
print("price of an item is {}".format(dis) )