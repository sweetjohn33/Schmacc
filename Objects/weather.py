

class Weather:

    def __init__(self, name, other_thing):
        self._other_thing = other_thing
        self._name = name

    def other_thing(self):
        return self._other_thing

    def __str__(self):
        return self._name



