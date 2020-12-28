import requests

class KabuPlusClient:

    def __init__ (self, username, password):
        self.username = username
        self.password = password

    def get(self, url):
        res = requests.get(url, auth = (self.username, self.password))
        res.encoding = res.apparent_encoding
        return res.text
