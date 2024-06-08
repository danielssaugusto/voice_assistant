def voiceAssistant(message):
    voice = print(f'Assistant: {message}')
    return voice

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
    voiceAssistant('Olá! em que posso ajudar?')
    while True:
        userInput = user()
        main(userInput)