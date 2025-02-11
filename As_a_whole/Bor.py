#This is not a broken source code with a recommendation from AI.
import colorama
from colorama import Fore, Back, Style
import time
import os
import requests
import json
from datetime import datetime

colorama.init(autoreset=True)

def colorama_purple(text):
    """Applies a simple purple color using colorama."""
    return Fore.MAGENTA + text + Style.RESET_ALL

def print_centered(text, color_func=lambda x: x):  # Default is no color function
    """Prints text centered in the terminal."""
    terminal_width = os.get_terminal_size().columns
    padding = (terminal_width - len(text)) // 2
    print(" " * padding + color_func(text))

def print_banner():
    """Prints the banner in colorama purple."""
    banner = """
  ____             
 |  _ \            
 | |_) | ___  _  
 |  _ < / _ \| '|
 | |_) | (_) | |   
 |____/ \___/|_| 
    """
    print_centered(banner, color_func=colorama_purple)  # Use colorama_purple

def print_menu():
    """Prints the main menu with left-aligned options."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console

    # Banner
    print_banner()
    print()

    print(f"{Fore.MAGENTA}[01]{Style.RESET_ALL} Spam WebHook")  # Left-aligned
    print(f"{Fore.MAGENTA}[02]{Style.RESET_ALL} Delete WebHook")  # Left-aligned
    print(f"{Fore.MAGENTA}[03]{Style.RESET_ALL} Rename WebHook")  # Left-aligned
    print()

    # [Purple Bor White Purple]
    bor_prompt = f"{Fore.MAGENTA}[{Style.RESET_ALL}Bor{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL}"
    command_prompt = f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}command{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL}"
    print(bor_prompt + command_prompt + " ~ ", end="")

def spam_webhook(webhook_name=""): #Added webhook name parameter
    """Spams a specified webhook with a message."""

    bor_prompt = f"{Fore.MAGENTA}[{Style.RESET_ALL}Bor{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL}"
    print(bor_prompt + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}WebHook{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL}" + " ~ ", end="")
    webhook_url = input()

    print(bor_prompt + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}message{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL}"+ " ~ ", end="")
    message = input()

    print(bor_prompt + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}quantity{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL}"+ " ~ ", end="")

    try:
        quantity = int(input())
    except ValueError:
        print(bor_prompt + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ Invalid quantity. Returning to main menu.")
        input("Press Enter to return to the main menu")
        return

    success_count = 0
    webhook_preview = webhook_url[:87] + "..." #Create webhook preview
    for i in range(quantity):
        now = datetime.now().strftime("%H:%M:%S")  # Get current time
        send_prompt = f"{Fore.MAGENTA}[{Style.RESET_ALL}Bor{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}send{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}{now}{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ {Fore.GREEN}Successfully{Style.RESET_ALL} send to {webhook_preview}"
        print(send_prompt) # Print send prompt
        try:
            data = {"content": message}
            if webhook_name:
                data["username"] = webhook_name #added username
            response = requests.post(webhook_url, json=data)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            success_count += 1
        except requests.exceptions.RequestException as e:
            print(bor_prompt + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ Error sending message: {e}")

        time.sleep(0.5)  # 2 messages per second

    success_rate = (success_count / quantity) * 100 if quantity > 0 else 0
    if success_rate == 100:
        print(bor_prompt + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ {Fore.GREEN}Successfully 100%{Style.RESET_ALL}")
    elif success_rate == 0:
        print(bor_prompt + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ Not successful - 0%")
    else:
        print(bor_prompt + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ {Fore.GREEN}Successfully {success_rate:.0f}%{Style.RESET_ALL}")
    input(bor_prompt + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ Press Enter to return to the main menu")


def delete_webhook():
    """Deletes a specified webhook after confirmation."""
    bor_prompt = f"{Fore.MAGENTA}[{Style.RESET_ALL}Bor{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL}"
    print(bor_prompt + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}WebHook{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL}" + " ~ ", end="")
    webhook_url = input()

    print(bor_prompt + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} # is this a scam webhook? y/n ~ ", end="")
    confirmation = input().lower()

    if confirmation == "y":
        try:
            response = requests.delete(webhook_url)
            response.raise_for_status()  # Raise HTTPError for bad responses
            print(bor_prompt + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ {Fore.GREEN}WebHook has been deleted!{Style.RESET_ALL}")
        except requests.exceptions.RequestException as e:
            print(bor_prompt + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ Error deleting WebHook: {e}")
    elif confirmation == "n":
        print(bor_prompt + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ I will not delete a NON-fraudulent webhook")
    else:
        print(bor_prompt + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ Invalid input.")

    input(bor_prompt + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ Press Enter to return to the main menu")

def rename_webhook():
    """Renames a specified webhook."""
    bor_prompt = f"{Fore.MAGENTA}[{Style.RESET_ALL}Bor{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL}"
    print(bor_prompt + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}WebHook{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL}" + " ~ ", end="")
    webhook_url = input()

    print(bor_prompt + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}Rename{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL}" + " ~ ", end="")
    new_name = input()

    try:
        data = {"name": new_name} # Corrected the data field
        response = requests.patch(webhook_url, json=data) # Using PATCH request to modify the webhook
        response.raise_for_status()

        try:
            webhook_info = requests.get(webhook_url).json()
            print(bor_prompt + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ WebHook name has been changed to: {Fore.GREEN}{webhook_info['name']}{Style.RESET_ALL}")
        except:
            print(bor_prompt + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ {Fore.GREEN}WebHook name has been changed!{Style.RESET_ALL}")
    except requests.exceptions.RequestException as e:
        print(bor_prompt + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ Error renaming WebHook: {e}")

    input(bor_prompt + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ Press Enter to return to the main menu")

    return new_name

def main():
    """Main function to run the menu."""
    while True:
        print_menu()
        choice = input()

        bor_prompt = f"{Fore.MAGENTA}[{Style.RESET_ALL}Bor{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL}"

        if choice == "1":
            spam_webhook()
        elif choice == "2":
            delete_webhook()
        elif choice == "3":
            webhook_name = rename_webhook()
        else:
            print(bor_prompt + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ Invalid choice.")
            input(bor_prompt + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ Press Enter to return to the main menu")


if __name__ == "__main__":
    main()
