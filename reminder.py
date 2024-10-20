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
    client = MongoClient(mongo_host)

    # Obter o nome do banco de dados e da coleção do .env
    db_name = os.getenv("DB_CLIENT")  # Nome do banco de dados
    collection_name = os.getenv("DB_COLLECTION")  # Nome da coleção (tabela)

    # Conectar ao banco de dados e à coleção
    db = client[db_name]
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
    reminders = task_collection.find()

    print("\nLembretes:")
    for reminder in reminders:
        print(f"ID: {reminder['_id']}, Título: {reminder['title']}, Descrição: {reminder['description']}, Criado em: {reminder['data_criacao']}, Completo: {reminder['completed']}")


# UPDATE - Editar tarefa existente
def edit_reminder(reminder_id, new_title=None, new_description=None, completed=None):
    task_collection, _ = db_connection()

    update_fields = {}
    if new_title is not None:
        update_fields["title"] = new_title
    if new_description is not None:
        update_fields["description"] = new_description
    if completed is not None:
        update_fields["completed"] = completed

    try:
        result = task_collection.update_one({"_id": ObjectId(reminder_id)}, {"$set": update_fields})
        if result.modified_count > 0:
            print(f"Lembrete com ID {reminder_id} atualizado com sucesso.")
        else:
            print(f"Nenhuma alteração feita no lembrete com ID {reminder_id}.")
    except Exception as e:
        print(f"Erro ao editar documento: {e}")


# DELETE - Excluir uma tarefa
def delete_reminder(reminder_id):
    task_collection, _ = db_connection()

    try:
        result = task_collection.delete_one({"_id": ObjectId(reminder_id)})
        if result.deleted_count > 0:
            print(f"Lembrete com ID {reminder_id} excluído com sucesso.")
        else:
            print(f"Nenhum lembrete encontrado com ID {reminder_id}.")
    except Exception as e:
        print(f"Erro ao excluir documento: {e}")
