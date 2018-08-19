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


class ContinuousEffect(Effect):

    def __init__(self, function, target=[], mandatory=False, aftereffect=None, trigger=[], conditions=None):
        super().__init__(name, effect, health, defense, attack, good_terrain, bad_terrain)
        self._class = "Spell"

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
        self._Viable = []
        self._Chosen = []

    def return_possible_targets(self, activator, game):
        type_object = self._Type_object
        place = self._Place
        what_players = self._What_players
        viable = []
        if type_object == "self":
            viable.append(activator)

        viable_players = []
        viable = []
        if what_players == "all":
            for player in game.return_players().return_deck():
                viable_players.append(player)
        if what_players == "opponents":
            for player in game.return_players().return_deck():
                if player.name() != activator.owner().name():
                    viable_players.append(player)
        if what_players == "owner":
            for player in game.return_players().return_deck():
                if player.name() == activator.owner().name():
                    viable_players.append(player)
        if type_object == "creature" or type_object == "permanent":
            if place == "graveyard":
                for player in viable_players:
                    for monster in player.graveyard():
                        viable.append(monster)

            if place == "battlefield":
                for player in viable_players:
                    for land in player.lands():
                        for monster in land.monster_slot():
                            viable.append(monster)

        if type_object == "building" or type_object == "permanent":
            for player in viable_players:
                for land in player.lands():
                    for building in land.building_slots():
                        viable.append(building)
        if type_object == "player":
            for player in viable_players:
                viable.append(player)
        self._Viable = viable
        #

    def pick_targets(self):
        number_of = self._Number_of
        viable = self._Viable
        chosen = self._Chosen
        if number_of == "all":
            chosen = viable
        else:
            for i in range(number_of):
                for g in range(len(viable)):
                    print(str(g + 1) + ") " + viable[g].owner().name() + ": " + viable[g].name())
                target = input("Which would you like to target?")
                target = int(target) - 1
                chosen.append(viable[target])
                del viable[target]
        return chosen



