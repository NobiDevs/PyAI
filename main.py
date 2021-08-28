import time

print("Py: What's your name?")
name = input("You: ")
print(" ")

print("Py: Where are you from?")
place = input("You: ")
print(" ")

print("Py: What is your hobby?")
hobby = input("You: ")
print(" ")

print("Processing...")
time.sleep(5)

print("Py: " + "\nHello " + '\033[1m' + name + "\nFrom " + '\033[1m' + place + "\nThat likes " + '\033[1m' + hobby)
