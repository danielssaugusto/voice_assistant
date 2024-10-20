import os
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv

# Carregar as cariáveis do arquivo .env
load_dotenv()

# Conectar ao MongoDB
mongo_host = os.getenv("DB_HOST")
client = MongoClient(mongo_host)

# Obter o nome do banco de dados e da coleção do .env
db_name = os.getenv(    "DB_CLIENT") # Nome do banco de dados
collection_name = os.getenv("DB_COLLECTION") # Nome da coleção (tabela)

# Conectar ao banco de dados e à coleção
db = client[db_name]
tasks_collection = db[collection_name]  

# Função: Adicionar nova tarefa
def add_document(data):
    try:
        # Inserir o documento na coleção
        result = tasks_collection.insert_one(data)
        print(f"Documento adicionado com o ID: {result.inserted_id}")
    except Exception as e:
        print(f"Erro ao adicionar documento: {e}")

# Exemplo de dados para inserir
new_task = {
    "title": "Comprar leite",
    "completed": False
}
add_document(new_task)



# Função: Listar todas as tarefas

# Função: Editar tarefa existente

# Função: Excluir uma tarefa

# Função para testar a conexão
def test_connection():
    try:
        # Listar todas as coleções no banco de dados
        print("Coleções disponíveis:", db.list_collection_names())

        # Tenta acessar uma coleção e contar os documentos
        count = tasks_collection.count_documents({})
        print(f"Conexão bem-sucedida! Número de documentos na coleção: {count}")
    except Exception as e:
        print(f"Erro ao conectar ao MongoDB: {e}")


test_connection()
