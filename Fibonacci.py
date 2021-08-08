# Fibonacci Sequence!

# Importing the relevant modules
import matplotlib.pyplot as plt

# Create a function

def Fibonacci(N):
    # Starting sequence
    starting_sequence = [1, 1]

    # Our sequence will be as long as our 'N' value
    for i in range(2, N):
        # Calculating the next number in the sequence
        next_number = starting_sequence[-1] + starting_sequence[-2]
        # Append this new number to our sequence
        starting_sequence.append(next_number)

    return starting_sequence

# print(Fibonacci(100))

# Plotting fibonacci numbers on a simple graph
plt.plot(Fibonacci(10))
plt.show()
