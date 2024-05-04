class Assistant:
    def __init__(self):
        self.library = {
            'Hello': "Hi there! I'm your friendly assistant. How can I help you today?",
            'Functions': "I'm here to lend a hand whenever you need me.",
        }
        self.database = {}

    def greet(self):
        return self.library['Hello']

    def listen(self):
        return input('You: ').strip().lower()

    def Assistant(self, message):
        print("Assistant:", message)

    def add_info(self):
        self.Assistant("Let's add some info. Type 'stop' when you're done.")
        while True:
            question = input('What do you want to save?: ').strip()
            if question == 'stop':
                break
            elif question in self.database:
                self.Assistant("Oh, that's already in my memory bank.")
            else:
                answer = input('What should I remember?: ').strip()
                self.database[question] = answer
                self.Assistant("Got it. I'll remember that.")

    def help(self):
        return self.library['Functions']

    def handle_input(self, message):
        if message == 'help':
            self.Assistant(self.help())
        elif message == 'add info':
            self.add_info()
        elif any(keyword in message for keyword in self.database):
            for keyword, response in self.database.items():
                if keyword in message:
                    self.Assistant(response)
                    break
            else:
                self.Assistant("Hmm, I don't have an answer for that.")
        else:
            self.Assistant("I'm not sure how to respond to that.")

    def run(self):
        self.Assistant(self.greet())
        while True:
            user_input = self.listen()
            self.handle_input(user_input)


if __name__ == "__main__":
    assistant = Assistant()
    assistant.run()
