# Q4 Write a program that calculates the discount on a product based on the following criteria:
# If the price is greater than $1000, a discount of 10% is applied.
# If the price is between $500 and $1000, a discount of 5% is applied.
# If the price is below $500, no discount is applied.

price = int(input("Enter the price: "))

if price > 1000:
    discount = 0.10*price
    total_price = price-discount
    print("Total Price after discount of 10%: ",total_price)

elif price >= 500 and price <= 1000:
    discount = 0.05*price
    total_price = price-discount
    print("Total Price after discount 5%: ",total_price)
else:
    print("Total Price: ",price)