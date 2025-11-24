from django.core.management.base import BaseCommand
from chatbot_app.chatbot_engine import get_chatbot

class Command(BaseCommand):
    help = "Start terminal chat with ChatterBot"

    def handle(self, *args, **options):
        bot = get_chatbot()
        self.stdout.write(self.style.SUCCESS("ChatBot is ready!"))
        self.stdout.write("Type 'quit' or 'exit' to stop.\n")
        while True:
            try:
                user_input = input("user: ").strip()
                if user_input.lower() in ["quit", "exit"]:
                    self.stdout.write("bot: Goodbye!")
                    break
                bot_response = bot.get_response(user_input)
                self.stdout.write(f"bot: {bot_response}")
            except (KeyboardInterrupt, EOFError):
                self.stdout.write("\nbot: Goodbye!")
                break
