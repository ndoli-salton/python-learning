answer = input("What ia the Answer to the grea question of life, the universe and everything? ")

if answer == "42" or answer.lower().strip() == "forty-two" or answer.lower().strip() == "forty two":
    print("Yes")
else:
    print("No")