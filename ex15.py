from sys import argv #this line imports the argument

script, filename = argv #not sure what script here does (script is just the name of the py file. ). filename var is being set to argv

txt = open(filename) #makes a file object of filename.

print(f"Here's your file {filename}:") # straight forward print with variable
print(txt.read()) #read function is used to read the open file, what if we didn't set open file to txt?

print("Type that filename again:")
file_again = input ("> ") #input to get the filename from the user, alternate to agrument.

txt_again = open(file_again) #similar to line 5 but with the user input

print(txt_again.read()) #similar to line  8

txt.close()
txt_again.close()
