import speech_recognition as sr
import pyttsx3


# Fala
# Velocidade original da fala: 150
def voice(message, rate=200, volume=1.0, voice_id=0):
    engine = pyttsx3.init()

    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)

    voices = engine.getProperty('voices')
    if voice_id < len(voices):
        engine.setProperty('voice', voices[voice_id].id)
    # else:
    #     engine.setProperty('voice', voices[0].id)

    engine.say(message)
    print(f'Assistant: {message}')
    engine.runAndWait()


# Escuta
def speech_recognition():
    print("Iniciando o recognizer")
    recognizer = sr.Recognizer()
    print("Recognizer funcionando")

    with sr.Microphone() as source:
        voice("Olá, como posso ajudar?")
        print("Ouvindo...")
        audio = recognizer.listen(source, timeout=5)

    try:
        message = recognizer.recognize_sphinx(audio)
        print(f'Você disse: {message}')
    except sr.WaitTimeoutError:
        voice("Tempo de espera esgotado")
    except sr.UnknownValueError:
        voice('Desculpe, não consegui entender o que você disse, pode tentar de novo?')  
    except sr.RequestError as e:
        print(f'Parece que houve um problema com o serviço. Tente novamente mais tarde. {e}')

def functions():
    funcoes = {
        "Lembretes": [
            "adicionar lembrete",
            "ler lembretes",
            "editar lembrete",
            "excluir lembrete"
        ],
    }

    return funcoes