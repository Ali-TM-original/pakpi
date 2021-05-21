import json
from random import randint


class JsonDataHandler:
    @staticmethod
    def dog_facts():
        with open("Data for PakPi/dogfacts.json") as f:
            data = json.load(f)

        return data[randint(0, int(len(data))+1)]['fact']

    @staticmethod
    def cat_facts():
        with open("Data for PakPi/catfacts.json") as f:
            data = json.load(f)

        return data[randint(0, int(len(data))+1)]

    @staticmethod
    def yomama():
        with open("Data for PakPi/jokes.json") as f:
            data = json.load(f)

        return data['data'][randint(0, int(len(data['data'])) + 1)]['description']

    @staticmethod
    def stupid():
        with open("Data for PakPi/shortjokes.json") as f:
            data = json.load(f)

        return data['data'][randint(0, int(len(data['data']) +1))]['joke']

