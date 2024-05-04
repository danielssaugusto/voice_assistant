import os
import json

class SimpleDatabase:
    def __init__(self, db_file):
        self.db_file = db_file
        self.data = {}
        self.load_data()

    def load_data(self):
        if os.path.exists(self.db_file):
            with open(self.db_file, 'r') as file:
                self.data = json.load(file)

    def save_data(self):
        with open(self.db_file, 'w') as file:
            json.dump(self.data, file)

    def create_table(self, table_name):
        if table_name not in self.data:
            self.data[table_name] = {}

    def insert_record(self, table_name, record):
        if table_name in self.data:
            if table_name not in self.data:
                self.data[table_name] = []
            self.data[table_name].append(record)
            self.save_data()

    def get_records(self, table_name):
        if table_name in self.data:
            return self.data[table_name]
        return []

# Exemplo de uso:
db = SimpleDatabase("my_database.json")

# Criando uma tabela chamada "users"
db.create_table("users")

# Inserindo um registro na tabela "users"
user1 = {"id": 1, "name": "John Doe", "age": 30}
db.insert_record("users", user1)

# Obtendo registros da tabela "users"
users = db.get_records("users")
print(users)
