from assistant import voice, speech_recognition
from reminder import test_connection, add_reminder, delete_reminder, read_reminders, edit_reminder

def adicionar_lembrete():
    """Função para adicionar um novo lembrete."""
    title = input("Título do lembrete: ")
    description = input("Descrição: ")
    add_reminder(title, description)
    voice("Seu lembrete foi adicionado ao banco de dados!")

def ler_lembretes():
    """Função para ler todos os lembretes."""
    read_reminders()

def editar_lembrete():
    """Função para editar um lembrete existente."""
    voice("Qual lembrete você quer editar?")
    edit_reminder()  # Chamando a função edit_reminder sem ID, já que a lógica foi alterada

def excluir_lembrete():
    """Função para excluir um lembrete existente."""
    voice("Qual lembrete você deseja excluir?")
    delete_reminder()  # Chamando a função delete_reminder sem ID, já que a lógica foi alterada

def main(message):
    """Função principal que interpreta a mensagem do usuário e aciona as funções apropriadas."""
    if "lembrete" in message:
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
                voice("Desculpe, não entendi sua solicitação.")

if __name__ == "__main__":
    user = input("You: ")
    main(user)
