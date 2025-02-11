import os
from src import menu
from src.webhook_operations import spam_webhook, delete_webhook, rename_webhook
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)


def main():
    while True:
        menu.print_menu()
        choice = input()

        bor_prompt = f"{Fore.MAGENTA}[{Style.RESET_ALL}Bor{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL}"

        if choice == "1":
            spam_webhook.spam_webhook()
        elif choice == "2":
            delete_webhook.delete_webhook()
        elif choice == "3":
            rename_webhook.rename_webhook()
        else:
            print(
                bor_prompt
                + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ Invalid choice."
            )
            input(
                bor_prompt
                + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ Press Enter to return to the main menu"
            )


if __name__ == "__main__":
    main()
