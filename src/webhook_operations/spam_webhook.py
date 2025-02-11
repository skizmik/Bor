import requests
import time
from datetime import datetime
import colorama
from colorama import Fore, Style


def spam_webhook(webhook_name=""):
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
        + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}message{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL}"
        + " ~ ",
        end="",
    )
    message = input()

    print(
        bor_prompt
        + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}quantity{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL}"
        + " ~ ",
        end="",
    )

    try:
        quantity = int(input())
    except ValueError:
        print(
            bor_prompt
            + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ Invalid quantity. Returning to main menu."
        )
        input("Press Enter to return to the main menu")
        return

    success_count = 0
    webhook_preview = webhook_url[:60] + "..."
    for i in range(quantity):
        now = datetime.now().strftime("%H:%M:%S")
        send_prompt = (
            f"{Fore.MAGENTA}[{Style.RESET_ALL}Bor{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}send{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}{now}{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ {Fore.GREEN}Successfully{Style.RESET_ALL} send to {webhook_preview}"
        )
        print(send_prompt)
        try:
            data = {"content": message}
            if webhook_name:
                data["username"] = webhook_name
            response = requests.post(webhook_url, json=data)
            response.raise_for_status()
            success_count += 1
        except requests.exceptions.RequestException as e:
            print(
                bor_prompt
                + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ {Fore.RED}There is no webhook!"
            )

        time.sleep(0.5)

    success_rate = (success_count / quantity) * 100 if quantity > 0 else 0
    if success_rate == 100:
        print(
            bor_prompt
            + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ {Fore.GREEN}Successfully 100%{Style.RESET_ALL}"
        )
    elif success_rate == 0:
        print(
            bor_prompt
            + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ {Fore.RED}Not successful - 0%"
        )
    else:
        print(
            bor_prompt
            + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ {Fore.GREEN}Successfully {success_rate:.0f}%{Style.RESET_ALL}"
        )
    input(
        bor_prompt
        + f" {Fore.WHITE}|{Style.RESET_ALL} {Fore.MAGENTA}[{Style.RESET_ALL}main{Style.RESET_ALL}{Fore.MAGENTA}]{Style.RESET_ALL} ~ Press Enter to return to the main menu"
    )
