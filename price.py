def discount(price,discount):
    if discount >= 100:
        price_width_discount = price
        print("OBMAN")
    else:
        price_width_discount = price - price * discount / 100
        print(price_width_discount)

discount(100,101)
discount(100,12)
