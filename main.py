from assistant import voice, speech_recognition, functions
from reminder import test_connection, add_reminder, delete_reminder, read_reminders, edit_reminder
import sys

def adicionar_lembrete():
    print("\n----- Adicionar Lembrete -----")
    title = input("Título do lembrete: ")
    description = input("Descrição: ")
    add_reminder(title, description)
    voice("Claro! Vou lembrar disso para você! Pode deixar!\n")

def ler_lembretes():
    print("\n----- Sua lista de lembretes -----")
    read_reminders()

def editar_lembrete():
    print("\n----- Menu de edição -----")
    voice("Ah, entendi! Qual tarefa você quer mudar agora?")
    edit_reminder()

def excluir_lembrete():
    print("\n----- Excluir lembrete -----")
    voice("Qual lembrete você quer que eu esqueça?")
    delete_reminder()

def display_functions(func_dict):
    voice("Então, aqui estão as funções que você pode usar!")
    for category, functions in func_dict.items():
        print(f"\n{category}:")
        for function in functions:
            print(f" - {function}")

def main(message):
    if "lembrete" in message:
        print("\n***** Testando Conexão *****")
        db_connection = test_connection()
        if db_connection:
            actions = {
                "adicionar lembrete": adicionar_lembrete,
                "ler lembretes": ler_lembretes,
                "editar lembrete": editar_lembrete,
                "excluir lembrete": excluir_lembrete
            }

            for action in actions:
                if action in message:
                    actions[action]()
                    break
            else:
                voice("Desculpe, mas não consegui pegar o que você disse.")

    elif "ajuda" in message:
        result = functions()
        display_functions(result)
    
    elif any(phrase in message for phrase in ["sair", "tchau", "adeus"]):
        voice("Até mais!")
        sys.exit()
        

if __name__ == "__main__":
    voice("Olá, como posso ajudar?")
    while True:
        user = speech_recognition()
        if user:
            main(user)
