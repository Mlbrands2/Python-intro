#!/usr/bin/python3
def calculate_discount(price, discount_percent):
  if discount_percent >= 20:
    discount = price * discount_percent / 100
    final_price = price - discount
  else:
    final_price = price
  return final_price
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage (0-100): "))
l
final_price = calculate_discount(original_price, discount_percentage)

if discount_percentage >= 20:
  print(f"Final price after applying {discount_percentage}% discount: ${final_price:.2f}")
else:
  print(f"No discount applied. Price remains: ${original_price:.2f}")
