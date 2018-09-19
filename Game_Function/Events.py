

# This file will contain the events class, which is how we will keep track of what has happened during a game.

class Event:
    def __init__(self, subject, action, directobject):
        self._event = str(subject) + " " + str(action) + " " + str(directobject)
        self._subject = subject
        self._action = action
        self._directobject = directobject

    def __repr__(self):
        return self._event

    def action(self):
        return self._action

    def subject(self):
        return self._subject

    def directobject(self):
        return self._directobject


class AttackEvent(Event):

    def __init__(self, attacker, defender):
        self._event = str(attacker) + " attacks" + str(defender)
        self._subject = attacker
        self._directobject = defender
        self._action = "attack"

class EndTurnEvent(Event):




