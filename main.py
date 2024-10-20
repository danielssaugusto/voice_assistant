from assistant import voice, speech_recognition
from reminder import test_connection, add_reminder, delete_reminder, read_reminders, edit_reminder

def main(message):
    # Acionando as funções da tarefa: Lembrete
    if "lembrete" in message:
        db_connection = test_connection()
        if db_connection == True:

            if "adicionar lembrete" in message:
                title = input("Título do lembrete: ")
                description = input("Descrição: ")
                add_reminder(title, description)
                voice("Seu lembrete foi adicionado ao banco de dados!")
            elif "ler lembretes" in message:
                read_reminders()
            elif "editar lembrete" in message:
                voice("Qual lembrete você quer editar?")
                id_lembrete = input("ID do lembrete: ")
                edit_reminder()
            elif "excluir lembrete" in message:
                voice("Qual lembrete você deseja excluir?")
                id_lembrete = input("ID do lembrete: ")
                delete_reminder(id_lembrete)
                voice(f"Lembrete com ID {id_lembrete} excluído!")

if __name__ == "__main__":
    user = speech_recognition()
    main(user)
