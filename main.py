# -*- coding: utf-8 -*-

from wox import Wox
import pyperclip


class Exchange(Wox):

    def query(self, query):
        results = []
        results.append({
            "Title": "转换为大写",
            "SubTitle": query.upper(),
            "IcoPath": "./Images/up.png",
            "JsonRPCAction": {
                "method": "copyToClipBoard",
                "parameters": [query.upper()],
                "dontHideAfterAction": False
            }
        })
        results.append({
            "Title": "转换为小写",
            "SubTitle": query.lower(),
            "IcoPath": "./Images/down.png",
            "JsonRPCAction": {
                "method": "copyToClipBoard",
                "parameters": [query.lower()],
                "dontHideAfterAction": False
            }
        })
        return results

    def copyToClipBoard(self, str):
        pyperclip.copy(str)


if __name__ == "__main__":
    Exchange()
