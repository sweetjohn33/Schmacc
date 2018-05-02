class Land:

    # Here are our plots of land. They have a name and a list of lists, of which the first list contains their monsters
    # and the second list contains their buildings. A land should only be able to have at the most
    # one monster and two buildings at a time

    def __init__(self, name):
        """

        :param name: The name of the class
        """
        self._contents = [[], []]
        self._name = name

    def __repr__(self):
        return self._name

    def return_name(self):
        return self._name

    def add_monster(self, monster):
        self._contents[0].append(monster)

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
        print(self._name + " : Monsters: " + ', '.join(monsters) +
              "  |||  Buildings: " + ', '.join(buildings))

    def monster_slot(self):
        return self._contents[0]

        # Returns whatever monster is on that land

    def building_slots(self):
        return self._contents[1]

        # Returns the list of buildings on that land



