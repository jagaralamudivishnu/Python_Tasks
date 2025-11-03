#-----------Strings---------------

#you are given a string sentence.print the characters at even indices.
#example: sentence = "python is amazing"
#output: "pto saaig"

sentence = "python is amazing"
print("char at even indices of sentence is: ")
print(f" {sentence[::2]} ")

#You are given a string s. Replace all spaces in the string with underscores(_)
#and print the modified string.
#example: s = "python is fun and powerful"
#output: "python_is_fun_and_powerful"

s = "python is fun and powerful"
modified_s = s.replace(' ','_')
print(f" modified string after replacing spaces with underscores is: {modified_s}")

#you are given a string s. Check if the string contains only digits.

s = "12345"
print(f" does string s: {s} contains only digits? {s.isdigit()}")
 
#you are given a string s. Print the string in reverse order.

s = "Python is amazing"
print(f"reverse of the string s: {s} is {s[-1: :-1]}")

#you are given a string s. Capitalize the first letter of each word in the string
#and print the modified string.

s = "Python programming is fun"
#output: "python Programming is fun"
modified_s = upper_s = s
print(f" modified string after Capitalizing first letter of each word in string s: {modified_s.title()} ")

