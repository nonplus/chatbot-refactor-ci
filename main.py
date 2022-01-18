def main():
    while True:
        user_input = input()
        if "What is your name?" == user_input:
            print("My name is chatbot! What's yours?")
        else:
            print("Sorry I didn't understand that.")

if __name__ == '__main__':
    main()
