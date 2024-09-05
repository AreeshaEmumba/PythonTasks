# Read the input
n = int(input())  # Number of words
word_count = {}  # Dictionary to store the word counts
order = []  # List to maintain the order of appearance of distinct words

# Process each word
for _ in range(n):
    word = input().strip()  # Read the word and remove trailing newlines
    if word in word_count:
        word_count[word] += 1  # Increment count if word already seen
    else:
        word_count[word] = 1  # Initialize count if word is new
        order.append(word)  # Add word to order list

# Output number of distinct words
print(len(order))

# Output the counts of the distinct words in the order they first appeared
print(' '.join(str(word_count[word]) for word in order))