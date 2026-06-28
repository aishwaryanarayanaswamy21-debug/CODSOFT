from datetime import datetime

print("Type 'bye' to exit.\n")

while True:
    user = input("You : ").lower()

    if user in ["hi", "hello", "hey"]:
        print("Bot : Hello! How can I help you?")

    elif "name" in user:
        print("Bot : My name is CodSoft Chatbot.")

    elif "how are you" in user:
        print("Bot : I am fine. Thanks for asking!,How about you???")

    elif "time" in user:
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot : Current time is", current_time)

    elif "date" in user:
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Bot : Today's date is", current_date)

    elif "python" in user:
        print("Bot : Python is a popular programming language used in AI and Machine Learning.")

    elif "ai" in user:
        print("Bot : Artificial Intelligence enables machines to mimic human intelligence.")
    
    elif "your role" in user:
        print("ChatBot : I am here to assist you and guide you over the things you askk..!")

    elif user in ["bye", "exit", "quit"]:
        print("Bot : Goodbye! Have a great day.")
        break

    else:
        print("Bot : Sorry, I didn't understand that.")