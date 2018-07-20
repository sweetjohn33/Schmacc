class Effect:

    # This class holds the effects of all the creatures, buildings, and spells

    def __init__(self, function, target=[], mandatory=False, aftereffect=None, trigger=[], conditions=None):
        """

        :param target:
        :param function:
        :param aftereffect:
        :param trigger:
        :param conditions:
        """

        self._Target = target
        self._Function = function
        self._Aftereffect = aftereffect
        self._Trigger = trigger
        self._Conditions = conditions
        self._Mandatory = mandatory


class Target:

    # This class holds the criteria for the targeting of an effect, with the purpose of returning all the viable
    # targets in the game for a given effect

    def __init__(self, type_object="all", place="all", what_players="all", number_of="all"):
        """

        :param type_object:
        :param place:
        :param what_players:
        :param number_of:
        """

        self._Type_object = type_object
        self._Place = place
        self._What_players = what_players
        self._Number_of = number_of
        