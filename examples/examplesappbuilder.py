from telegram.ext import ApplicationBuilder
from tokenprovider import TokenProvider


class ExamplesAppBuilder(ApplicationBuilder):
    def __init__(self, bot_name: str):
        super().__init__()
        self.bot_name = bot_name
        self.token(TokenProvider().get_token(self.bot_name))


