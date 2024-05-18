import random

# Ouvir
def listening():
    input_user = input("You: ")
    return input_user

# Pensar
def thinking():
    library = {}
    with open("knowledge.txt", "r", encoding="UTF-8") as archive:
        for x in archive:
            question, *answers = x.strip().split(",")
            library[question] = answers
    return library

# Falar
def speak(message):
    print(f"Assistant: {message}")

# Responder
def respond(question, library):
    if question in library:
        answers = library[question]
        return random.choice(answers)
    else:
        return "Not found."

def main():
    speak("Hello! How can I assist you today?")
    library = thinking()  # Chamar a função para obter o dicionário de conhecimento
    while True:
        message = listening()
        if "hello" in message:
            speak("Hello! How can I assist you today?")
        elif any(word in message for word in library):  # Verificar se alguma palavra da mensagem está no dicionário
            response = respond(message, library)
            speak(response)
        elif "goodbye" in message:
            speak("Goodbye!")
            break
        elif "how are you" in message:
            speak("I'm doing great! Thank you for asking.")
        else:
            speak("Sorry, I'm not sure how to help with that.")

if __name__ == "__main__":
    main()
