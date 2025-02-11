import requests
import colorama
from colorama import Fore, Style


def delete_webhook():
    bor_prompt = (
        f"{Fore.MAGENTA}[{Style.RESET_ALL}Bor{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL}"
    )
    print(
        bor_prompt
        + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}WebHook{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL}"
        + " ~ ",
        end="",
    )
    webhook_url = input()

    print(
        bor_prompt
        + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} # is this a scam webhook? y/n ~ ",
        end="",
    )
    confirmation = input().lower()

    if confirmation == "y":
        try:
            response = requests.delete(webhook_url)
            response.raise_for_status()
            print(
                bor_prompt
                + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ {Fore.GREEN}WebHook has been deleted!{Style.RESET_ALL}"
            )
        except requests.exceptions.RequestException as e:
            print(
                bor_prompt
                + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ Error deleting WebHook: {e}"
            )
    elif confirmation == "n":
        print(
            bor_prompt
            + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ I will not delete a NON-fraudulent webhook"
        )
    else:
        print(
            bor_prompt
            + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ Invalid input."
        )

    input(
        bor_prompt
        + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ Press Enter to return to the main menu"
    )
