# Ask user for their name
name = input(" What's your name?").strip().title()

#SPlit user's name into first name and last name
first, last = name.split(" ")

# Say hello to user
print(f"hello, {first}") 