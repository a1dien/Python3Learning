greeting = "Hello"
first_name = "Jack"
last_name = 'White'
exclamation_mark = '!'
white_space = ' '
whole_sentence = greeting + white_space + first_name + white_space + last_name + \
                 exclamation_mark

print (greeting + white_space + first_name + white_space + last_name + exclamation_mark)
print (whole_sentence)

long_string = 'This is the long strong'
print (long_string)

#Escaping
some_string = "I'm a programmer"
print(some_string)
another_string = 'I want to learn "Python"'
print(another_string)
next_string = 'I\'m a programmer'
print(next_string)

string_with_new_line = "Hello \n My Name"
print(string_with_new_line)
string_with_new_line_trim = "Hello \n \rMy Name"
print(string_with_new_line_trim)
numbers = '1\t234\t5678'
print (numbers)

some_text = '\tHello! \n\tI\'m very glad to see you!'
print(some_text)

#Triple quote
string_with_triple_quotes = """This' ' is text with with "triple quotes" """
print (string_with_triple_quotes)
string_with_triple_quotes_return = """This' ' 
is text
 with with "triple quotes" """
print(string_with_triple_quotes_return)


first_name="John"
last_name = "Lee"
age = 10
white_space = ' '
print ("Hi! My name is " + first_name + white_space + last_name + ", I'm " + str(age) + " years old.")

text_song1 = """\t\tBaa, baa, black sheep,
\t\tHave you any wool?
\t\tYes sir, yes sir,
\t\tThree bags full"""

text_song2 = '\t\tOne for the master,\n\t\tOne for the dame,\n\t\tAnd one for the little boy\n\t\tWho lives down the lane'

text_song3 = """\t\tBaa, baa, black sheep,
\t\tHave you any wool?
\t\tYes sir, yes sir,
\t\tThree bags full
"""
new_line = '\n\n'
print (text_song1 + new_line + text_song2 + new_line + text_song3)