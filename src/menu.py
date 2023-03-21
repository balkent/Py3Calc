from .menuItem import MenuItem
from var_dump import var_dump

class Menu:
    itemMenus: list
    itemSelected: str
    itemMenusConf = {
        1: 'Addition',
        2: 'Substraction',
        3: 'Multiplication',
        4: 'Division',
        99: 'RageQuit',
    }

    def __init__(self):
        self.itemMenus = []
        self.init()

    def init(self) -> None:
        for id, call in self.itemMenusConf.items():
            self.itemMenus.append(MenuItem(id, call))

    def displayItem(self) -> None:
        for itemMenu in self.itemMenus:
            itemMenu.display()

    def inputKey(self) -> None:
        self.itemSelected = int(input("Enter id of menu: "))

    def findItem(self) -> MenuItem|None:
        for itemMenu in self.itemMenus:
            if itemMenu.isSame(self.itemSelected):
                return itemMenu
        raise NotImplementedError('not exist function') 