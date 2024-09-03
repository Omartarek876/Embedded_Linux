# Open the file "file.txt" in read mode ("r")
file = open("file.txt", "r")

# Read all the lines in the file and store them in the list `data`
data = file.readlines()

# Initialize an empty list to hold all the words in the file
words = []

# Iterate over each line in the `data` list
for line in data:
    # Split the line into words and add them to the `words` list
    words.extend(line.split())

# Print the final list of words
print(words)
