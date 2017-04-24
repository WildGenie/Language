# -*- coding: utf-8 -*-
"""
Website directory guess.

Hikai.
"""
import requests


class Search():
    """Search class."""

    def __init__(self, url):
        """Initialize method."""
        self.url = url
        self.run(self.url)

    def check_status_code(self, status_code):
        """Method check http status code."""
        num_front = int(status_code / 100)
        if num_front == 2:
            return True
        else:
            return False

    def run(self, url):
        """Method substantive running."""
        req = requests.get(self.url)
        if not self.check_status_code(req.status_code):
            print("Error. Exception 2xx.")

            return

        while True:
            i = 32
            url = self.url

            for num in range(0, 10):
                if i >= 127:
                    break

                url += chr(i)
                req = requests.get(url)
                if self.check_status_code(req.status_code):
                    print(chr(i))

                i += 1


if __name__ == "__main__":
    Search("http://www.naver.com")