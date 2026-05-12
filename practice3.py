"""
write a program to print the multiple of 5 in three differnt ways in python.
"""

# Method 1: Using for loop

print("Method 1:")
for i in range(1, 11):
    print(i * 5)
    
    
# Method 2: Using while loop

print("Method 2:")
num = 5

while num <= 50:
    print(num)
    num += 5
    

# Method 3: Using list comprehension

print("Method 3:")
multiples = [5 * i for i in range(1, 11)]
print(multiples)


