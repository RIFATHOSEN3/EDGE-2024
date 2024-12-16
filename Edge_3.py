import random
# Generate a list L of 50 random numbers between 1 and 100
L = [random.randint(1, 100)
     for _ in range(50)]
# Replace each element in the list with its square
L = [x**2 for x in L]
print("List of squares:", L)