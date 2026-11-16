

# promt and input the name
name = input("what is your name?")

print("0 hello", name) # print 2 arguments hello and the string name

print("1 hello," + name) # add the string 'name' to hello

print("2 hello ")
print(name)

print("3 hello ", end=" ") # overwriting the value of the default /n with " "
print(name)

print(f"4 hello {name}" ) # formation strings

name = name.strip()
print(f"5 hello , {name}")
name = name.title()        # Capitalize first letter of each word
print(f"6 hello {name}")

name2 = input("Your other name?")
name2 = name2.strip().title()  # Combine instructioms in one line
print("-----")
print(f"7 Hi there {name2}")

# compine everything in one line
name3 = input("Your friend?").strip().title()
print(f"8 Glad to meet you {name3}")

print("9 Long separator", name3, sep="        ") # Long separation between the arguments

print(f"10 Glad to meet you {name3} {name2}")

print("'11 Glad to meet you'", name3)       # how to print quotes inside quotes
print("\"11 Glad to meet you\"", name3)

Firstname, Lastname = name3.split() #split and assign 2 variable at the same time
print("hello", Firstname)
