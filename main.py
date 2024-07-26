import subprocess
import time
import sys
import os
import getpass
import json
from pystyle import Colorate, Colors

def load_config():
    with open('config/config.json', 'r') as file:
        config = json.load(file)
    return config

def clear_screen():
    if os.name == 'posix':  
        _ = os.system('clear')
    elif os.name == 'nt':  
        _ = os.system('cls')

def rewrite_animation(theme):
    chars = "/—\\|"
    message = "Chargement en cours"
    for _ in range(3): 
        for char in chars:
            sys.stdout.write(f"\r{Colorate.Horizontal(getattr(Colors, theme), message)} {char}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r" + Colorate.Horizontal(getattr(Colors, theme), message + " ... Done!\n"))

clear_screen()

def main_menu():
    config = load_config()
    theme = config['theme']
    username = getpass.getuser()
    message = f"""
██████╗ ███████╗ █████╗ ████████╗ ██████╗██╗  ██╗      ███████╗███████╗██████╗ ██╗   ██╗██╗ ██████╗███████╗
██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝██║  ██║      ██╔════╝██╔════╝██╔══██╗██║   ██║██║██╔════╝██╔════╝
██████╔╝█████╗  ███████║   ██║   ██║     ███████║█████╗███████╗█████╗  ██████╔╝██║   ██║██║██║     █████╗  
██╔══██╗██╔══╝  ██╔══██║   ██║   ██║     ██╔══██║╚════╝╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██║██║     ██╔══╝  
██████╔╝███████╗██║  ██║   ██║   ╚██████╗██║  ██║      ███████║███████╗██║  ██║ ╚████╔╝ ██║╚██████╗███████╗
╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝      ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚═╝ ╚═════╝╚══════╝                                                                                                                                                                                                                                                                                                                    
    """
    for line in message.splitlines():
        print(Colorate.Horizontal(getattr(Colors, theme), line))

    print(Colorate.Horizontal(getattr(Colors, theme), f"Bienvenue dans le menu DM Spammer:"))
    print(Colorate.Horizontal(getattr(Colors, theme), "1. DM Spammer Bot"))
    print(Colorate.Horizontal(getattr(Colors, theme), "2. Raid bot"))
    print(Colorate.Horizontal(getattr(Colors, theme), "3. Modifier le ficher Themes"))
    print(Colorate.Horizontal(getattr(Colors, theme), "4. Afficher les credits"))
    print(Colorate.Horizontal(getattr(Colors, theme), "5. Quitter"))
    print("       ")
    choix = input(Colorate.Horizontal(getattr(Colors, theme), f"{username}@Dm-Spammer -> "))

    if choix == "1":
        print(Colorate.Horizontal(getattr(Colors, theme), "Lancement du DM Spammer Bot..."))
        clear_screen() 
        rewrite_animation(theme)
        clear_screen() 
        subprocess.run(["python", "data/bot.py"]) 
    elif choix == "2":
        print(Colorate.Horizontal(getattr(Colors, theme), "Vous avez choisi DM Spammer Account."))
        clear_screen() 
        rewrite_animation(theme)
        clear_screen() 
        subprocess.run(["python", "data/bot_script.py"]) 
    elif choix == "3":
        try:
            subprocess.run(["xdg-open", "config/config.json"])  
        except Exception:
            try:
                subprocess.run(["open", "config/config.json"])  
            except Exception:
                try:
                    subprocess.run(["start", "config/config.json"], shell=True)  
                except Exception as e:
                    print(f"Impossible d'ouvrir le fichier config.json : {e}")
        input(Colorate.Horizontal(getattr(Colors, theme), "Appuyez sur Entrée pour revenir au menu : "))
        clear_screen()
        main_menu()
    elif choix == "5":
        print(Colorate.Horizontal(getattr(Colors, theme), "Au revoir !"))
    elif choix == "4":
        print(Colorate.Horizontal(getattr(Colors, theme), "Devolepeur: clemontop"))
        print(Colorate.Horizontal(getattr(Colors, theme), "Discord server: https://discord.gg/server-boost"))
        print(Colorate.Horizontal(getattr(Colors, theme), "github: https://github.com/beatch-service"))
        input(Colorate.Horizontal(getattr(Colors, theme), "Appuyez sur Entrée pour revenir au menu : "))
        clear_screen() 
        main_menu()
    else:
        print(Colorate.Horizontal(getattr(Colors, theme), "Option invalide. Veuillez choisir parmi les options disponibles."))
        input(Colorate.Horizontal(getattr(Colors, theme), "Appuyez sur Entrée pour revenir au menu : "))
        clear_screen()
        main_menu()

if __name__ == "__main__":
    main_menu()