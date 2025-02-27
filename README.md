# Assistente Virtual de Lembretes

## Descrição do Projeto

Este projeto consiste em um assistente virtual que interage com o usuário por meio de comandos de voz e texto, sendo capaz de gerenciar lembretes. O assistente permite ao usuário adicionar, ler, editar e excluir lembretes utilizando comandos de voz ou texto. O sistema armazena esses lembretes em um banco de dados MongoDB, garantindo a persistência das informações.

### Tecnologias Utilizadas:
- **Python**: Linguagem principal do projeto.
- **MongoDB**: Banco de dados NoSQL para armazenamento dos lembretes.
- **SpeechRecognition**: Biblioteca para reconhecimento de fala do usuário.
- **pyttsx3**: Biblioteca para síntese de fala (text-to-speech).
- **dotenv**: Biblioteca para carregar variáveis de ambiente, como credenciais do banco de dados.

### Funcionalidades

1. **Adicionar Lembrete**: O usuário pode adicionar um novo lembrete com título e descrição, que será armazenado no banco de dados.
2. **Ler Lembretes**: O usuário pode visualizar todos os lembretes armazenados.
3. **Editar Lembrete**: O usuário pode modificar o título, a descrição ou o status de conclusão de um lembrete existente.
4. **Excluir Lembrete**: O usuário pode excluir um ou todos os lembretes armazenados.

### Funcionamento

O assistente oferece a opção de comunicação via **texto ou voz**. Quando o assistente é iniciado, ele pergunta ao usuário o que ele deseja fazer, respondendo com base em comandos como "adicionar lembrete", "ler lembretes", "editar lembrete" e "excluir lembrete". A resposta pode ser dada por comandos de voz ou digitada diretamente no terminal.

O sistema utiliza um banco de dados **MongoDB** para armazenar os lembretes. Para garantir que o usuário tenha a melhor experiência possível, o assistente responde com áudio de feedback em cada ação executada.

## Estrutura do Código

### Arquivos e Funções

#### **main.py**:
Este arquivo contém a lógica principal de interação com o usuário. Ele monitora os comandos de voz e texto, chama as funções apropriadas e executa as ações correspondentes.

##### Funções principais:
- **adicionar_lembrete()**: Adiciona um novo lembrete ao banco de dados.
- **ler_lembretes()**: Lê todos os lembretes armazenados no banco de dados.
- **editar_lembrete()**: Edita um lembrete existente com base na escolha do usuário.
- **excluir_lembrete()**: Exclui um lembrete selecionado ou todos os lembretes.
- **display_functions()**: Exibe as funções disponíveis para o usuário.
- **main()**: Função principal que processa a entrada do usuário (voz ou texto).

#### **voice.py**:
Contém as funções relacionadas à interação de voz com o usuário.
- **voice()**: Responde ao usuário com a fala, utilizando a biblioteca **pyttsx3**.
- **speech_recognition()**: Captura e converte o áudio do usuário em texto, utilizando a biblioteca **SpeechRecognition**.

#### **db.py**:
Contém as funções para interação com o banco de dados MongoDB. Ele utiliza a biblioteca **pymongo** para realizar operações CRUD (Criar, Ler, Atualizar, Excluir) nos lembretes.

##### Funções principais:
- **db_connection()**: Realiza a conexão com o MongoDB.
- **test_connection()**: Testa a conexão com o banco de dados.
- **add_reminder()**: Adiciona um novo lembrete ao banco de dados.
- **read_reminders()**: Lê todos os lembretes armazenados.
- **edit_reminder()**: Edita um lembrete existente.
- **delete_reminder()**: Exclui um lembrete selecionado ou todos os lembretes.

### Estrutura do Banco de Dados

A estrutura do banco de dados MongoDB contém uma coleção de documentos, onde cada documento representa um lembrete.

Exemplo de documento de lembrete:
```json
{
    "_id": ObjectId("605c72ef15320732bc3b2874"),
    "title": "Comprar leite",
    "description": "Lembrete para comprar leite no mercado",
    "data_criacao": ISODate("2025-02-25T12:00:00Z"),
    "completed": false
}
```

### Como Rodar o Projeto
Pré-requisitos

    Python 3.x
    MongoDB instalado e rodando localmente ou remotamente
    Instalação das dependências do projeto:

    pip install -r requirements.txt

### Passos para Executar

Certifique-se de que o MongoDB está em execução.
Crie um arquivo .env na raiz do projeto com as credenciais de conexão com o MongoDB.
Execute o script principal:

```script
python main.py
```
