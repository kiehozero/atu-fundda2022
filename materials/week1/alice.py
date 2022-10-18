# this library handles requests for resources from the internet
import urllib.request
import random

# the actual location of this file we wish to use, in this
# case the Gutenberg Project's copy of Alice in Wonderland
book_url = "https://www.gutenberg.org/files/11/11-0.txt"

# stores the file as a list after opening the file with a library function, with each line being a list item
book = list(urllib.request.urlopen(book_url))

# Decode the lines and strip line endings (carriage returns or the backslash-n character)
# this is also the alternative format of writing a for loop, called a list comprehension
book = [line.decode('utf-8-sig').strip() for line in book]

# Returns a paragraph defined by the row numbers given
paragraph = ' '.join(book[417:436])

# print(paragraph)

# Let's lower-case it.
alice = paragraph.lower()

# print(alice)

# All letters and a space.
chars = 'abcdefghijklmnopqrstuvwxyz '

# And strip anything that is not a letter or space.
alice = ''.join([c for c in alice if c in chars])

# Get the length of alice.
N = len(alice)

# Generate N random characters from chars.
gener = random.choices(chars, k=N)

# Join them together in a string.
gener = ''.join(gener)

# print(gener)

# Get the whole book in one big string, the 26 just starts the string after all of the intro pages and publishing notes
sbook = ''.join(book[26:]).lower()

# Create the weights - count the occurences of each character in the whole book.
weights = [sbook.count(c) for c in chars]

# print(weights)

# Generate a string using those weights (first 'weights' is the parameter name, second is the variable created above)
wgenr = random.choices(chars, weights=weights, k=N)

# Join them together in a string.
wgenr = ''.join(wgenr)

# print(wgenr)