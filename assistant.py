import speech_recognition as sr
import pyttsx3

# Fala
# Velocidade original da fala: 150
def voice(message, rate=220, volume=1.0, voice_id=0):
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
        recognizer.adjust_for_ambient_noise(source)
        print("Ouvindo...")
        audio = recognizer.listen(source)

    try:
        message = recognizer.recognize_google(audio, language="pt-BR").lower()
        print(f"Você disse: {message}")
        return message
    except sr.WaitTimeoutError:
        voice("Ah, o tempo de espera acabou!")
    except sr.UnknownValueError:
        voice("Desculpe, não entendi. Pode repetir, por favor?") 
        return "" 
    except sr.RequestError as e:
        voice("Parece que estou enfrentando um probleminha agora e não consigo responder. Mas assim que der, vou voltar, tá?")
        print(f'Error!. {e}')
        return ""

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