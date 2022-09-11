#Variablen text erstellen. Der Satz hängt vom Input der Methode ab.

input = "This is a test {}"

def placeholderTest(input, value):
    return input.format(value)

print(placeholderTest(input, 1))


from urllib.request import urlopen
response = urlopen("https://python.org")
print(response.read())

from yaspin import yaspin


import time
from yaspin import yaspin

# Context manager:
with yaspin():
    time.sleep(3)  # time consuming code

# Function decorator:
@yaspin(text="enter your name")
def some_operations():
    output = input("Enter Your Name!")
    print(output)


some_operations()


import time
from random import randint
from yaspin import yaspin

with yaspin(text="Loading", color="yellow") as spinner:
    time.sleep(2)  # time consuming code

    success = randint(0, 1)
    if success:
        spinner.ok("✅ ")
    else:
        spinner.fail("💥 ")



