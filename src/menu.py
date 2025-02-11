import os
import colorama
from colorama import Fore, Style


def colorama_purple(text):
    return Fore.MAGENTA + text + Style.RESET_ALL


def print_centered(text, color_func=lambda x: x):
    terminal_width = os.get_terminal_size().columns
    padding = (terminal_width - len(text)) // 2
    print(" " * padding + color_func(text))


def print_banner():
    banner = '''
  ____             
 |  _ \            
 | |_) | ___  _  
 |  _ < / _ \| '|
 | |_) | (_) | |   
 |____/ \___/|_| 
    '''
    print_centered(banner, color_func=colorama_purple)


def print_menu():
    os.system("cls" if os.name == "nt" else "clear")

    print_banner()
    print()

    print(f"{Fore.MAGENTA}[01]{Style.RESET_ALL} Spam WebHook")
    print(f"{Fore.MAGENTA}[02]{Style.RESET_ALL} Delete WebHook")
    print(f"{Fore.MAGENTA}[03]{Style.RESET_ALL} Rename WebHook")
    print()

    bor_prompt = (
        f"{Fore.MAGENTA}[{Style.RESET_ALL}Bor{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL}"
    )
    command_prompt = (
        f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}command{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL}"
    )
    print(bor_prompt + command_prompt + " ~ ", end="")
