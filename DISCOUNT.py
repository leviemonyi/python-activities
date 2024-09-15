#Assign a discount of 5%
def calculate_discount(amount):
    # Check if the amount exceeds Ksh. 1000
    if amount > 1000:
        discount = amount * 0.05  # 5% discount
        final_amount = amount - discount
        return final_amount, discount
    else:
        # No discount if amount is 1000 or less
        return amount, 0

# Prompt user to enter the amount of purchase
amount = float(input("Enter the amount of purchase (in Ksh): "))

final_amount, discount = calculate_discount(amount)

if discount > 0:
    print(f"Discount applied: Ksh. {discount:.2f}")
else:
    print("No discount applied.")

print(f"Final amount to be paid: Ksh. {final_amount:.2f}")
