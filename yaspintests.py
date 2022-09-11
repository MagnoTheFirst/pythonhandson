from yaspin import yaspin

output = "This is your name {}"
test = input("Enter your name")

print(output.format(test))
# Function decorator:
@yaspin(text="enter your name")
def some_operations():
    output = input("Enter Your Name!")
    print(output)


some_operations()