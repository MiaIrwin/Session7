text = "Hello World"
print(text)
text = 'Hello World 2' # single vs double
print(text)
print(text[0]) # tells you letter in this place of the words
print(len(text)) # length of text
text = ""
print(len(text))

text = "Bob"
print(text[-1]) # starts from the end of the word

# print(text[3]) # error because the first character is in placement 0, so in Bob theres no character in placement 3
# print(text[6/3]) # error because it gives you 2.0, and you can only index with integers
print(text[6//3]) # put two forward slashes to make it an integer