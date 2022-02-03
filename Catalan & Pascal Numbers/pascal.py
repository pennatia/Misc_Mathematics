# Define the Function
def pascal(n):
    if n == 0:                                                  # Define the two base cases
        return []
    elif n == 1:
        return [[1]]
    else:
        new_row = [1]                                           # Define calculation for all other cases
        result = pascal(n-1)                                    # Call the function recursively
        last_row = result[-1]
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])         # Perform the Row Operation
        new_row += [1]
        result.append(new_row)                                  # Append to the initial Result
    return result


# Initialize Parameters, Call the Function and Print formatted results
N = 10
output = pascal(N)

for row in output:
    print(*row, sep=' ')
