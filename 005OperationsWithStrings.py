# Concatenation of strings
greetings = "Hello"
first_name = "Jack"
last_name = 'White'
exclamation_sign = "!"
space = " "
sentence = greetings + space + first_name + " " + last_name + exclamation_sign
print(sentence)

# Use "\" if code string is too long
sentence = greetings + space + first_name + " " \
    + last_name + exclamation_sign
print(sentence)

# Escaping <'>, <"> and <\> with strings
string_1 = "I'm a programmer"
print(string_1)
string_2 = 'I want to learn "Python"'
print(string_2)
string_3 = 'I\'m a programmer'
print(string_3)
string_4 = "I want to learn \"Python\""
print(string_4)

# \-KEYS
#   <\n> make a new line
string_10 = "<\\n> key\nmove cursor to the next line"
print(string_10)
#   <\r> move cursor to start of the line
#       "Hello! " will be rewrite by " World is wonderful!" in example
string_11 = "<\\r> key \r move cursor to start of the line. So '<\\r> key ' will be rewrite by ' move cursor<...>' in example"
print(string_11)
string_12 = "Next line will start at 1st position. \n      \rNo matter how much space is after previous string and before <\\n> command"
print(string_12)
#   <\t> make tabulation
string_13 = 'Numbers without tabulation by \\t: 12345'
string_14 = 'Numbers with tabulation by \\t: 1\t2\t3\t4\t5'
print(string_13)
print(string_14)

#   <\\> allow write <\> symbol
string_15 = "Double <\\\\> is being use to write <\\> symbol"
print(string_15)

#   <"""> allow to write any number of <'> and <"> symbols between triple <""">
string_16 = """"Triple quotes allow to write any number of <'> and <"> symbols between triple quotes."""
print(string_16)
#   <'''> allow to write any number of <'> and <"> symbols between triple <'''>
string_17 = '''Triple apostrophe allow to write any number of <'> and <"> symbols between triple apostrophe.'''
print(string_17)
#       Also allow to save formatting avoid <\n>, <\r> and <\t> keys
string_18 = '''Also allow to save formatting avoid keys:
    <\\n>, 
    <\\r>,
    <\\t>.'''
print(string_18)
