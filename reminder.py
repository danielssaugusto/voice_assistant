from pymongo import MongoClient
from bson.objectid import ObjectId

# Conectar ao MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["#"] # Nome do banco de dados
tasks_collection = db["#"] # Nome da coleção (tabela)

# Função: Adicionar nova tarefa

# Função: Listar todas as tarefas

# Função: Editar tarefa existente

# Função: Excluir uma tarefa