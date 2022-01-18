def respond(user_input):
    if "What is your name?" == user_input:
        print("My name is chatbot! What's yours?")
    else:
        print("Sorry I didn't understand that.")

def main():
    while True:
        user_input = input()
        respond(user_input)

if __name__ == '__main__':
    main()
