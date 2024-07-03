import speech_recognition as sr
import pyttsx3

class VoiceAssistant:
    @classmethod
    def listeningAssistant(cls):
        """
        English:
        Initiates voice assistant listening to capture and recognize user's voice command.

        Uses the speech_recognition library to capture audio from the microphone,
        adjust voice recognition for ambient noise, and attempt speech recognition
        using the Sphinx recognizer.

        Returns the recognized message as a string.

        Português:
        Inicia a escuta do assistente de voz para capturar e reconhecer o comando de voz do usuário.

        Utiliza a biblioteca speech_recognition para capturar áudio do microfone,
        ajustar o reconhecimento de voz para o ruído ambiente e tentar reconhecer
        o discurso usando o reconhecedor Sphinx.

        Retorna a mensagem reconhecida como uma string.
        """
        recognizer = sr.Recognizer()
        cls.voiceAssistant('Hey there! How can I help you today?')

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
                    cls.voiceAssistant("Sorry, I didn't catch that.")
                    return ''
                except sr.RequestError as e:
                    cls.voiceAssistant(f'Oops, error retrieving results: {e}')
                    return ''

    @staticmethod                
    def voiceAssistant(message, velocidade=150, volume=1.0):
        """
        English:
        Generates the spoken response of the voice assistant.

        Uses the pyttsx3 library to initialize a text-to-speech engine,
        set speech speed and volume, and pronounce the provided message.

        Português:
        Gera a resposta falada do assistente de voz.

        Utiliza a biblioteca pyttsx3 para inicializar um mecanismo de síntese de voz,
        definir a velocidade e o volume da voz, e pronunciar a mensagem passada como argumento.
        """
        engine = pyttsx3.init()
        engine.setProperty('rate', velocidade)
        engine.setProperty('volume', volume)

        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)

        engine.say(message)
        print(f'Assistant: {message}')
        engine.runAndWait()

    def user():
        """
        English:
        Prompts the user for text input and returns the typed text converted to lowercase.

        Português:
        Solicita uma entrada de texto ao usuário e retorna o texto digitado convertido para minúsculas.
        """
        typeUser = input(f'You: ')
        return typeUser.lower()

def task():
    while True:
        assistant = VoiceAssistant()
        assistant.voiceAssistant('What do you want me to remember? or type "exit"')
        userInput = assistant.user()

        if userInput == 'exit':
            assistant.voiceAssistant('Okay, exiting now...')
            break

        assistant.voiceAssistant('Task added! Do you want to continue?')
        userInput = assistant.user()
        if userInput != 'yes':
            assistant.voiceAssistant('Noted!')
            break
            
def main(message):
    if 'add' in message and 'task' in message:
        task()

if __name__ == '__main__':
    while True:
        assistant = VoiceAssistant()
        assistant.listeningAssistant()
