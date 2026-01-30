print(dir("x"))
print(help("x".capitalize)) # if you type . after "", pycharm gives you the strings
s = "bob ATE piZZA"
print(s.capitalize()) # Bob ate pizza

print(s.count("A")) # 2 capital A in string
s = "banana and another ana + ana again" # 3 ana
print(s.count("ana"))

# find finds the position of the first occurrence
s = "banana"
print(s.find("ana"))
print(s.find("ana", 2))

# replace, replace string inside string
print(s.replace("ana", "BOB"))
s = "I, like: to go out!"
print(s.split(" "))

# remove punctuation from a sentence and extract words
punct = ",.!:"
for c in punct:
    s = s.replace(c, "")
print(s.split())