import os
import asyncio
import discord
import json
from pystyle import Colorate, Colors
import subprocess

def load_config():
    with open('./config/config.json', 'r') as file:
        config = json.load(file)
    return config

config = load_config()
theme = config['theme']

def read_tokens(file_path):
    with open(file_path, 'r') as file:
        tokens = [line.strip() for line in file.readlines()]
    return tokens

class MyClient(discord.Client):
    def __init__(self, token, user_id, message, repeat_count, *args, **kwargs):
        intents = discord.Intents.default()
        intents.members = True
        super().__init__(intents=intents, *args, **kwargs)
        self.token = token
        self.user_id = user_id
        self.message = message
        self.repeat_count = repeat_count

    async def on_ready(self):
        print(Colorate.Horizontal(getattr(Colors, theme), f'Connecté en tant que {self.user} (ID: {self.user.id})'))
        print('------')
        user = await self.fetch_user(self.user_id)
        try:
            for _ in range(self.repeat_count):
                await user.send(self.message)
                await asyncio.sleep(1)
            print(Colorate.Horizontal(getattr(Colors, theme), f'Messages envoyés avec succès à {user.name}#{user.discriminator}'))
        except discord.HTTPException as e:
            print(Colorate.Horizontal(Colors.red_to_yellow, f'Échec de l\'envoi des messages à {user.name}#{user.discriminator} : {e}'))
        finally:
            await self.close()  

async def start_bot(token, user_id, message, repeat_count):
    client = MyClient(token, user_id, message, repeat_count)
    await client.start(token)

def print_colored_message():
    message = """
██████╗ ███╗   ███╗    ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
██╔══██╗████╗ ████║    ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
██║  ██║██╔████╔██║    ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
██║  ██║██║╚██╔╝██║    ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
██████╔╝██║ ╚═╝ ██║    ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
╚═════╝ ╚═╝     ╚═╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝.                                                                                                                                                                                                                                
        """
    for line in message.splitlines():
        print(Colorate.Horizontal(getattr(Colors, theme), line))

async def main():
    print_colored_message()
    
    tokens = read_tokens('./tokens-bot.txt')  

    user_id = int(input(Colorate.Horizontal(getattr(Colors, theme), "Entrez l'ID de la personne à qui envoyer le message : ")))
    message = input(Colorate.Horizontal(getattr(Colors, theme), "Entrez le message à envoyer : "))
    repeat_count = int(input(Colorate.Horizontal(getattr(Colors, theme), "Entrez le nombre de fois à envoyer le message : ")))

    tasks = [start_bot(token, user_id, message, repeat_count) for token in tokens]
    await asyncio.gather(*tasks)

    input(Colorate.Horizontal(getattr(Colors, theme), "Appuyez sur Entrée pour revenir au menu : "))
    subprocess.run(["python", "./main.py"]) 
    
if __name__ == "__main__":
    asyncio.run(main())
