from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

def get_chatbot():
    bot = ChatBot(
        "TerminalBot",
        read_only=False,
        logic_adapters=["chatterbot.logic.BestMatch"]
    )

    conversation = [
        "Good morning!",
        "How are you"
        "I am doing very well, thank you for asking.",
        "You're welcome.",
        "Do you like hats?",
        "Yes, I like hats. Do you like hats?"
    ]

    trainer = ListTrainer(bot)
    trainer.train(conversation)
    return bot
