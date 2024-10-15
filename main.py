import speech_recognition as sr
import pyttsx3


# Fala
def voice(message, rate=150, volume=1.0, voice_id=1):
    engine = pyttsx3.init()

    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)

    voices = engine.getProperty('voices')
    if voice_id < len(voices):
        engine.setProperty('voice', voices[voice_id].id)
    else:
        engine.setProperty('voice', voices[0].id)

    engine.say(message)
    print(f'Assistant: {message}')
    engine.runAndWait()


# Escuta
def speech_recognition():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        voice('Estou ouvindo, você precisa de algo?')
        audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)

    try:
        message = recognizer.recognize_sphinx(audio)
        print(f'Você disse: {message}')
    except sr.UnknownValueError:
        voice('Desculpe, não consegui entender o que você disse, pode tentar de novo?')  
    except sr.RequestError as e:
        voice(f'Parece que houve um problema com o serviço. Tente novamente mais tarde. {e}')

speech_recognition()