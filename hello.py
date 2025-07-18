# #Ask user their name
# #Remove whitespace from str and Capitalized
# name = input("what is your name? ").strip().title()
#
# #split user's name into firstname and last name
# first, last =name.split(" ")
# #say hello to the user
# print(f"hello, {first}" )



def main():
    hello()
    name = input("Whats your name? ")
    hello(name)

def hello(to="world"):
    print("Hello!", to)



main()


