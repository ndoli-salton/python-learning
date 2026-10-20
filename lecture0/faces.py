def main():
    user_input = input("use hapy and sad emoticons in text i will convert them to emojis")
    print(convert(user_input))

def convert(text):
    return text.replace(":)", "\U0001F642").replace(":(", "\U0001F641")

main ()