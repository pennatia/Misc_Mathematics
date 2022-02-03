# Define the Function
def catalan(n):
    if n <= 1:                                          # Define Base Case
        return 1
    result = 0                                          # Initialize Result Variable
    for i in range(n):                                  # Perform Calculation Loop
        result += catalan(i) * catalan(n - i - 1)

    return result


# Run the Function and Print Formatted Results
for n in range(2, 16):
    tip = catalan(n)
    print(f'Order {n} Catalan Number = {tip}')

