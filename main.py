import discord

from discord.ext import commands
from src.read_json import read_json

class main():
    def __init__(self):
        self.token = read_json("secret/secret.json")["token"]

        @bot.event
        async def on_ready():
            print(f'{bot.user} is watching for porn ')

    def load_cogs(self):
        bot.load_extension("src.watcher")

    def run(self):
        self.load_cogs()
        bot.run(self.token)

if __name__ == "__main__":
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix='!', intents=intents)

    main = main()
    main.run()

