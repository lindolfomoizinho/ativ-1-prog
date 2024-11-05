def calculate_discount(price, discount_percentage):
    discount = price * (discount_percentage / 100)
    final_price = price - discount
    return final_price


price = float(input("Enter the original price of the product: "))
discount_percentage = float(input("Enter the discount percentage: "))

price_with_discount = calculate_discount(price, discount_percentage)

print(f"The price after a discount of {discount_percentage}% is: R${price_with_discount:.2f}")