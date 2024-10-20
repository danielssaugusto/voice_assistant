from assistant import voice, speech_recognition
from reminder import add_reminder, delete_reminder

def main(message):

    if "adicionar lembrete" in message:
        title = input("Titulo do lembrete: ")
        description = input("Descrição: ")
        add_reminder(title, description)
        voice("Seu lembrete foi adicionado ao banco de dados!")
    elif "excluir lembrete" in message:
        voice("Qual lembrete você deseja excluir?")
        id_lembrete = input("ID do lembrete: ")
        delete_reminder(id_lembrete)

if __name__ == "__main__":
    speech_recognition()
    user = input("You: ")
    if user in main:
        main()