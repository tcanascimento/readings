import os
from .connect_api import ConnectApi


class Agenda(object):
    def __init__(self, cache_directory):
        self.numbers = {}
        self.filename = os.path.join(cache_directory.strpath, "agenda.txt")
        self.cache = open(self.filename, "w")

    def add(self, name, number):
        self.numbers[name] = number

    def search(self, name):
        return self.numbers[name]

    def nomes(self):
        return self.numbers.keys()

    def get_user_from_api(self, user):
        connect = ConnectApi()
        return connect.get_user(user)

    def clear(self):
        self.cache.close()
        os.remove(self.filename)
