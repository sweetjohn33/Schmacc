# A module to hold the Land class


class Land:

    # Here are our plots of land. They have a name and a list of lists, of which the first list contains their monsters
    # and the second list contains their buildings. A land should only be able to have at the most
    # one monster and two buildings at a time

    def __init__(self, name, owner=""):
        """

        :param name: The name of the class
        """
        self._contents = [[], []]
        self._name = name
        self._empty = False
        self._owner = owner

    def __repr__(self):
        return self._name

    def name(self):
        return self._name

    def owner(self):
        return self._owner

    def set_owner(self, player):
        self._owner = player.name()

    def add_monster(self, monster):
        self._contents[0].append(monster)
        monster.check_land_compatibility(self)

    def delete_monster(self):
        del self._contents[0][0]

    def add_building(self, building):
        self._contents[1].append(building)

    def delete_building(self, index):
        del self._contents[1][index]

    def contents(self):
        return self._contents

    def print_contents_neatly(self):
        monsters = []
        for monster in self._contents[0]:
            monsters.append(monster.name())
        buildings = []
        for building in self._contents[1]:
            buildings.append(building.name())
        print(self._name + ": Monsters: " + ', '.join(monsters) +
              "  |||  Buildings: " + ', '.join(buildings))

    def print_monsters_in_depth(self):
        print(self._name + ": " + self._contents[0][0].name() + "\nHealth: " +
              str(self._contents[0][0].current_health())+ "/" +
              str(self._contents[0][0].original_health()) + "\nDefense: " +
              str(self._contents[0][0].current_defense()) + "/" +
              str(self._contents[0][0].original_defense()) +
              "\nAttack: " + str(self._contents[0][0].current_attack()) + "/" +
              str(self._contents[0][0].original_attack()))

    def monster_slot(self):
        return self._contents[0][0]

        # Returns whatever monster is on that land
    def length_monster_list(self):
        return len(self.contents()[0])

        # Useful in determining whether or not there is a monster on the land

    def building_slots(self):
        return self._contents[1]

        # Returns the list of buildings on that land

    def check_if_empty(self):
        if len(self._contents[1]) == 0 and self.length_monster_list() == 0:
            return True



