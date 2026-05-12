
"""
Q. write a program which contains different functions, the 1st
function converts list which was given by the user into a matrix format of 3*3,
2nd function will convert the same list into a tuple and find the
mean, median and the mode and the 3rd function will iterate over this
two functions and find the gaps fill with null values respectively and gives a
dictionary format mapped with first to the second function. 
"""


# Function 1: Convert list into 3x3 matrix
def list_to_matrix(lst):
    matrix = []
    for i in range(0, 9, 3):
        row = lst[i:i+3]
        # Fill missing values with None
        while len(row) < 3:
            row.append(None)
        matrix.append(row)
    return matrix

# Function 2: Convert list into tuple and calculate statistics
def tuple_statistics(lst):
    return {
        "tuple": tuple(lst),
        "mean": mean(lst),
        "median": median(lst),
        "mode": mode(lst)
    }

# Function 3: Combine both functions into a dictionary
def process_data(lst):
    return {
        "matrix_function": list_to_matrix(lst),
        "statistics_function": tuple_statistics(lst)
    }

# User Input
user_list = list(map(int, input("Enter elements: ").split()))

# Output
result = process_data(user_list)

print("\nFinal Dictionary Output:")
print(result)