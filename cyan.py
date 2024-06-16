import speech_recognition as sr
import pyttsx3

def listeningAssistant():
    recognizer = sr.Recognizer()
    voiceAssistant('Olá! em que posso ajudar?')

    while True:
        with sr.Microphone() as source:
            print('Diga algo...')
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            try:
                message = recognizer.recognize_sphinx(audio, language='pt-BR')
                print(f'Você disse: {message}')
                return message
            except sr.UnknownValueError:
                voiceAssistant('Não entendi o que você disse.')
                return ''
            except sr.RequestError as e:
                voiceAssistant(f'Erro ao recuperar resultados {e}')
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
        voiceAssistant('O que você quer colocar na sua agenda? (ou digite "sair")')
        userInput = user()

        if userInput == 'sair':
            voiceAssistant('Saindo...')
            break

        voiceAssistant('Tarefa adicionada!\nDeseja continuar?')
        userInput = user()
        if userInput != 'sim':
            voiceAssistant('Anotado!')
            break
            
def main(message):
    if 'adicionar' in message and 'tarefa' in message:
        task()

if __name__ == '__main__':
    while True:
        listeningAssistant()