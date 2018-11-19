# A module to hold the Land class


class Land:

    # Here are our plots of land. They have a name and a list of lists, of which the first list contains their monsters
    # and the second list contains their buildings. A land should only be able to have at the most
    # one monster and two buildings at a time

    def __init__(self, name):
        """

        :param name: The name of the object
        """
        self.contents = [[], []]
        self.name = name
        self.owner = None

    def __repr__(self):
        return self.name





