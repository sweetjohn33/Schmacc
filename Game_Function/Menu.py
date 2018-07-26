


class Menu:

    def __init__(self, list_of_options, procedures):
        """
        Through pygame and this class we will present the player with a menu. The player will click on an option of the menu which
        will carry out another function, which could also mean that another menu is created
        :param list_of_options: the list of options your menu will have to click on
        :param procedures: the list of what will happen when an option in the menu is selected
        """

        self._List_of_options = list_of_options
        self._Procedures = procedures