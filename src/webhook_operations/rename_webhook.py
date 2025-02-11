import requests
import colorama
from colorama import Fore, Style


def rename_webhook():
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
        + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}Rename{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL}"
        + " ~ ",
        end="",
    )
    new_name = input()

    try:
        data = {"name": new_name}
        response = requests.patch(webhook_url, json=data)
        response.raise_for_status()

        try:
            webhook_info = requests.get(webhook_url).json()
            print(
                bor_prompt
                + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ WebHook name has been changed to: {Fore.GREEN}{webhook_info['name']}{Style.RESET_ALL}"
            )
        except:
            print(
                bor_prompt
                + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ {Fore.GREEN}WebHook name has been changed!{Style.RESET_ALL}"
            )
    except requests.exceptions.RequestException as e:
        print(
            bor_prompt
            + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ Error renaming WebHook: {e}"
        )

    input(
        bor_prompt
        + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ Press Enter to return to the main menu"
    )

    return new_name
