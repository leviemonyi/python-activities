from datetime import datetime

# Function to calculate the fine based on days overdue
def calculate_fine(days_overdue):
    if days_overdue <= 7:
        fine_rate = 20
    elif 8 <= days_overdue <= 14:
        fine_rate = 50
    else:
        fine_rate = 100
    return fine_rate

# Function to display the results
def display_fine(book_id, due_date, return_date, days_overdue, fine_rate, fine_amount):
    print(f"Book ID: {book_id}")
    print(f"Due Date: {due_date.strftime('%d-%m-%Y')}")
    print(f"Return Date: {return_date.strftime('%d-%m-%Y')}")
    print(f"Days Overdue: {days_overdue} days")
    print(f"Fine Rate: Ksh {fine_rate} per day")
    print(f"Fine Amount: Ksh {fine_amount}")

# Main program
def main():
    # Input from user
    book_id = input("Enter the Book ID: ")
    due_date_input = input("Enter the Due Date (dd-mm-yyyy): ")
    return_date_input = input("Enter the Return Date (dd-mm-yyyy): ")

    # Convert input dates to datetime objects
    due_date = datetime.strptime(due_date_input, '%d-%m-%Y')
    return_date = datetime.strptime(return_date_input, '%d-%m-%Y')

    # Calculate the days overdue
    days_overdue = (return_date - due_date).days

    if days_overdue > 0:
        # Calculate fine
        fine_rate = calculate_fine(days_overdue)
        fine_amount = fine_rate * days_overdue

        # Display the results
        display_fine(book_id, due_date, return_date, days_overdue, fine_rate, fine_amount)
    else:
        print("No fine. The book was returned on time or earlier.")

# Run the program
if __name__ == "__main__":
    main()
