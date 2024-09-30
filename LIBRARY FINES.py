from datetime import datetime

# Function to calculate overdue days
def calculate_days_overdue(due_date, return_date):
    date_format = "%Y-%m-%d"
    due_date = datetime.strptime(due_date, date_format)
    return_date = datetime.strptime(return_date, date_format)
    
    # Calculate the difference in days
    days_overdue = (return_date - due_date).days
    return days_overdue if days_overdue > 0 else 0

# Function to determine fine rate based on days overdue
def calculate_fine(days_overdue):
    if days_overdue <= 7:
        fine_rate = 20
    elif 8 <= days_overdue <= 14:
        fine_rate = 50
    else:
        fine_rate = 100
    
    # Fine amount is rate multiplied by the days overdue
    fine_amount = fine_rate * days_overdue
    return fine_rate, fine_amount

# Main function to input details and calculate fine
def main():
    # Get input from the user
    book_id = input("Enter Book ID: ")
    due_date = input("Enter Due Date (YYYY-MM-DD): ")
    return_date = input("Enter Return Date (YYYY-MM-DD): ")
    
    # Calculate overdue days
    days_overdue = calculate_days_overdue(due_date, return_date)
    
    # Calculate fine rate and amount
    fine_rate, fine_amount = calculate_fine(days_overdue)
    
    # Display the results
    print("\n--- Library Fine Details ---")
    print(f"Book ID: {book_id}")
    print(f"Due Date: {due_date}")
    print(f"Return Date: {return_date}")
    print(f"Days Overdue: {days_overdue}")
    print(f"Fine Rate: Ksh {fine_rate} per day")
    print(f"Total Fine Amount: Ksh {fine_amount}")

# Run the program
if __name__ == "__main__":
    main()
