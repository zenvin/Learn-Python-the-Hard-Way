people = 4
cars = 5
trucks = 4


if cars > people or cars > trucks:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("ALright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
