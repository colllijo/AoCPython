import os
import re
import requests


class AoCInput:
    def __init__(self):
        self.auth_cookie = None

    def get_input(self, year: int, day: int) -> str:
        if not os.path.exists(f"input/{str(year)}/day{str(day)}.txt"):
            self.download_input(year, day)

        with open(f"input/{str(year)}/day{str(day)}.txt", 'r') as file:
            return file.read()

    def download_input(self, year: int, day: int):
        if self.auth_cookie is None:
            self.load_auth_cookie()

        url = f"https://adventofcode.com/{str(year)}/day/{str(day)}/input"
        filename = f"input/{str(year)}/day{str(day)}.txt"

        input = requests.get(url, cookies={"session": self.auth_cookie})
        open(filename, 'wb').write(input.content)

    def load_auth_cookie(self):
        cookie = os.environ.get("CAOC_AUTH_COOKIE")
        if not cookie:
            print("\033[31mNo authorisation cookie found in environment please make sure to set it \"export CAOC_AUTH_COOKIE=\"\033[0m")
            quit(1)

        if not re.match("[0-9a-f]{128}", cookie):
            print("\033[31mInvalid authorisation cookie\033[0m")
            quit(1)

        self.auth_cookie = cookie
