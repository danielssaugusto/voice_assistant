import os
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
from datetime import datetime

def db_connection():
    # Carregar as variáveis do arquivo .env
    load_dotenv()

    # Conectar ao MongoDB
    mongo_host = os.getenv("DB_HOST")
    db_name = os.getenv("DB_CLIENT")  # Obter o nome do banco de dados e da coleção do .env
    collection_name = os.getenv("DB_COLLECTION")  # Nome da coleção (tabela)

    client = MongoClient(mongo_host)
    db = client[db_name]  # Conectar ao banco de dados e à coleção
    tasks_collection = db[collection_name]

    return tasks_collection, db

# Função para testar a conexão
def test_connection():
    tasks_collection, db = db_connection()

    try:
        # Listar todas as coleções no banco de dados
        print("Coleções disponíveis:", db.list_collection_names())

        # Tenta acessar uma coleção e contar os documentos
        count = tasks_collection.count_documents({})
        print(f"Conexão bem-sucedida! Número de documentos na coleção: {count}")
        return True
    except Exception as e:
        print(f"Erro ao conectar ao MongoDB: {e}")
        return False

# CREATE - Adicionar uma nova tarefa
def add_reminder(title, description):
    task_collection, _ = db_connection()  # Corrigido para obter a coleção corretamente

    reminder = {
        "title": title,
        "description": description,
        "data_criacao": datetime.now(),
        "completed": False,
    }

    try:
        result = task_collection.insert_one(reminder)
        print(f"Lembrete adicionado com o ID: {result.inserted_id}")
    except Exception as e:
        print(f"Erro ao adicionar documento: {e}")

# READ - Listar todas as tarefas
def read_reminders():
    task_collection, _ = db_connection()
    reminders = list(task_collection.find())

    if not reminders:
        print("Nenhum lembrete encontrado.")
        return reminders

    print("\nLembretes:")
    for index, reminder in enumerate(reminders, start=1):
        print(f"""
    ID: {reminder['_id']}, 
    Número: {index} | Título: {reminder['title']} 
    Descrição: {reminder['description']} 
    Criado em: {reminder['data_criacao']} 
    Completo: {reminder['completed']}
""")

    return reminders

# UPDATE - Editar tarefa existente
def edit_reminder():
    reminders = read_reminders()

    if reminders is None or len(reminders) == 0:
        return
    
    try:
        choice = int(input("Selecione o número do lembrete que deseja editar: "))
        if 1 <= choice <= len(reminders):
            reminder_id = reminders[choice - 1]['_id']  # Pega o ID do lembrete selecionado
            new_title = input("Novo título (deixe em branco para não alterar): ")
            new_description = input("Nova descrição (deixe em branco para não alterar): ")
            completed_input = input("Marcar como completo? (s/n, deixe em branco para não alterar): ")

            completed = None
            if completed_input.lower() == 's':
                completed = True
            elif completed_input.lower() == 'n':
                completed = False

            # Atualiza o lembrete
            task_collection, _ = db_connection()
            update_fields = {}
            if new_title:
                update_fields["title"] = new_title
            if new_description:
                update_fields["description"] = new_description
            if completed is not None:
                update_fields["completed"] = completed

            result = task_collection.update_one({"_id": ObjectId(reminder_id)}, {"$set": update_fields})
            if result.modified_count > 0:
                print(f"Lembrete com ID {reminder_id} atualizado com sucesso.")
            else:
                print(f"Nenhuma alteração feita no lembrete com ID {reminder_id}.")
        else:
            print("Seleção inválida. Por favor, escolha um número válido.")
    except ValueError:
        print("Por favor, insira um número válido.")
    except Exception as e:
        print(f"Erro ao editar documento: {e}")

# DELETE - Excluir uma tarefa
def delete_reminder():
    reminders = read_reminders()

    if reminders is None or len(reminders) == 0:
        return

    try:
        choice = input("Selecione o número do lembrete que deseja excluir [pressione * para deletar todos]: ")
  
        if choice == "*":
            confirm = input("Você realmente deseja excluir todos os lembretes? (s/n): ")
            if confirm.lower() == 's':
                task_collection, _ = db_connection()
                result = task_collection.delete_many({})
                print(f"{result.deleted_count} lembretes excluídos com sucesso.")
            else:
                print("Exclusão de todos os lembretes cancelada.")

        else:
            choice = int(choice)
            if 1 <= choice <= len(reminders):
                reminder_id = reminders[choice - 1]['_i d']  # Pega o ID do lembrete selecionado
                task_collection, _ = db_connection()
                result = task_collection.delete_one({"_id": ObjectId(reminder_id)})
                if result.deleted_count > 0:
                    print(f"Lembrete com ID {reminder_id} excluído com sucesso.")
                else:
                    print(f"Nenhum lembrete encontrado com ID {reminder_id}.")
            else:
                print("Seleção inválida. Por favor, escolha um número válido.")

    except ValueError:
        print("Por favor, insira um número válido.")
    except Exception as e:
        print(f"Erro ao excluir documento: {e}")
