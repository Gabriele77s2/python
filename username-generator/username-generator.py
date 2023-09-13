import random

# Lists of random words and numbers
words = ["apple", "banana", "cherry", "dog", "elephant", "flower", "grape", "happy", "igloo", "jungle"]
numbers = [str(i) for i in range(10)]

def generate_username():
    # Choose random words and numbers
    word = random.choice(words)
    number1 = random.choice(numbers)
    number2 = random.choice(numbers)
    
    # Combine them to form a username
    username = f"{word}{number1}{number2}"
    
    return username

# Generate and print a username
username = generate_username()
print("Generated Username:", username)

# We have a list of random words and a list of numbers.
# The generate_username function chooses a random word and two random numbers.
# It then combines them to create a username (e.g., "apple42").
# Finally, it returns the generated username
