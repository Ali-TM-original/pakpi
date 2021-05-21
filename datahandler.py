import random


class TextDataHandler:

    @staticmethod
    def random_facts():
        with open('Data for PakPi/facts.txt', encoding="utf-8") as f:
            lines = [line.rstrip('\n') for line in f]
            f.close()

        return random.choice(lines)

    @staticmethod
    def random_roasts():
        with open('Data for PakPi/roasts.txt', encoding="utf-8") as f:
            lines = [line.rstrip('\n') for line in f]
            f.close()
        return random.choice(lines)

    @staticmethod
    def chuck():
        with open('Data for PakPi/chuck.txt', encoding="utf-8") as f:
            lines = [line.rstrip('\n') for line in f]
            f.close()
        return random.choice(lines)
