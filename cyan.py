import speech_recognition as sr
import pyttsx3

def listeningAssistant():
    recognizer = sr.Recognizer()
    voiceAssistant('Hey there! How can I help you today?')

    while True:
        with sr.Microphone() as source:
            print('Listening...')
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            try:
                message = recognizer.recognize_sphinx(audio, language='en-US')
                print(f'You said: {message}')
                return message
            except sr.UnknownValueError:
                voiceAssistant("Sorry, I didn't catch that.")
                return ''
            except sr.RequestError as e:
                voiceAssistant(f'Oops, error retrieving results: {e}')
                return ''
            
def voiceAssistant(message, velocidade=150, volume=1.0):
    engine = pyttsx3.init()
    engine.setProperty('rate', velocidade)
    engine.setProperty('volume', volume)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    engine.say(message)
    print(f'Assistant: {message}')
    engine.runAndWait()

def user():
    typeUser = input(f'You: ')
    return typeUser.lower()

def task():
    while True:
        voiceAssistant('What do you want me to remember? or type "exit"')
        userInput = user()

        if userInput == 'exit':
            voiceAssistant('Okay, exiting now...')
            break

        voiceAssistant('Task added! Do you want to continue?')
        userInput = user()
        if userInput != 'yes':
            voiceAssistant('Noted!')
            break
            
def main(message):
    if 'add' in message and 'task' in message:
        task()

if __name__ == '__main__':
    while True:
        listeningAssistant()
