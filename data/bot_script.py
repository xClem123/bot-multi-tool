import discord
import os
import subprocess
from discord.ext import commands
from pystyle import Colorate, Colors
import json

def clear_screen():
    if os.name == 'posix':  
        _ = os.system('clear')
    elif os.name == 'nt':  
        _ = os.system('cls')

def load_config():
    with open('./config/config.json', 'r') as file:
        return json.load(file)

config = load_config()
theme = config.get('theme', 'green_to_cyan')

intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

async def create_channels(guild, channel_count, name, message, num_messages):
    for _ in range(channel_count):
        try:
            new_channel = await guild.create_text_channel(name)
            for _ in range(1):
                print(Colorate.Horizontal(getattr(Colors, theme), f'Salon créé: {new_channel.name}'))
            for _ in range(num_messages):
                await new_channel.send(message)
                for _ in range(1):
                    print(Colorate.Horizontal(getattr(Colors, theme), f'Message envoyé dans {new_channel.name}: {message}'))
        except Exception as e:
            print(Colorate.Horizontal(Colors.red_to_yellow, f'Erreur en créant le salon {name} ou en envoyant le message: {e}'))

@bot.event
async def on_ready():
    print(Colorate.Horizontal(getattr(Colors, theme), f'Bot is ready. Logged in as {bot.user}'))

    guild = bot.guilds[0]  
    print(Colorate.Horizontal(getattr(Colors, theme), f'Connected to guild: {guild.name} (id: {guild.id})'))

    channel_count = int(input(Colorate.Horizontal(getattr(Colors, theme), "Combien de salons voulez-vous créer? ")))
    name = input(Colorate.Horizontal(getattr(Colors, theme), "Nom du salon: "))
    message = input(Colorate.Horizontal(getattr(Colors, theme), "Message à envoyer dans ce salon: "))
    num_messages = int(input(Colorate.Horizontal(getattr(Colors, theme), "Combien de messages voulez-vous envoyer dans chaque salon? ")))

    for channel in guild.channels:
        try:
            await channel.delete()
            print(Colorate.Horizontal(getattr(Colors, theme), f'Salon supprimé: {channel.name}'))
        except Exception as e:
            print(Colorate.Horizontal(Colors.red_to_yellow, f'Erreur en supprimant le salon {channel.name}: {e}'))

    await create_channels(guild, channel_count, name, message, num_messages)

    await bot.close()
    input(Colorate.Horizontal(getattr(Colors, theme), "Appuyez sur Entrée pour revenir au menu : "))
    subprocess.run(["python", "./main.py"])
    clear_screen()

if __name__ == "__main__":
    clear_screen()
    ascii_art = """
██████╗  █████╗ ██╗██████╗     ██████╗  ██████╗ ████████╗
██╔══██╗██╔══██╗██║██╔══██╗    ██╔══██╗██╔═══██╗╚══██╔══╝
██████╔╝███████║██║██║  ██║    ██████╔╝██║   ██║   ██║   
██╔══██╗██╔══██║██║██║  ██║    ██╔══██╗██║   ██║   ██║   
██║  ██║██║  ██║██║██████╔╝    ██████╔╝╚██████╔╝   ██║   
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═════╝     ╚═════╝  ╚═════╝    ╚═╝   
                                                                        
    """
    print(Colorate.Horizontal(getattr(Colors, theme), ascii_art))
    token = input(Colorate.Horizontal(getattr(Colors, theme), "Entrez le token du bot: "))
    print(Colorate.Horizontal(getattr(Colors, theme), ascii_art))
    bot.run(token)
    print(Colorate.Horizontal(getattr(Colors, theme), "Tout est fini sans erreur."))
