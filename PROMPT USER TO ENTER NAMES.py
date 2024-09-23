def process_names():
    # Prompt the user to enter names
    user_input = input("Enter a list of names, separated by commas: ")

    # Split the input into individual names, strip extra spaces, and store them in a list
    names = [name.strip() for name in user_input.split(",")]

    # Remove duplicates by converting the list to a set, then sort the names alphabetically
    unique_names = sorted(set(names))

    # Display the sorted list of unique names
    print("\nSorted list of unique names:")
    for name in unique_names:
        print(name)

    # Display the total number of names entered
    print(f"\nTotal number of names entered (including duplicates): {len(names)}")

# Call the function to run the program
process_names()
