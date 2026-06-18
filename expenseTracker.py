# Initialize a running total for expenses
total = 0.0

# Continuous loop to prompt user for expenses
while True:
    try:
        expense = input("Enter the expense:")
        # Graceful exit when user inputs sentinel commands
        if expense.lower() in ("quit", "stop", "exit"):
            break
        else:
            # Convert expense to integer and add to total
            total+=int(expense)
    # Catches non-numeric inputs and prints an error message
    except ValueError:
        print("Invalid data.")
        continue

# Display the final formatted total currency amount
print(f"Final total: ${total:.2f}")