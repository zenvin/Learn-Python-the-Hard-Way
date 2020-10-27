types_of_people = 10 # sets the varible of types of people.
x = f"There are {types_of_people} types of people." # sets x to equal this line.

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}." # another way to add variables

print(x)
print(y) # printing varibles

print(f"I said: {x}")
print(f"I also said {y}") # print varibles with a varible

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}" # not sure why the bracket is empty. for insert?

print(joke_evaluation.format(hilarious)) 

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
