from .menu import Menu
from .calculator import Calculator

class App:
    def display(self):
        print("-----------------")
        print("Py3Calc")
        print("-----------------")

    def run(self) -> None:
        self.display()
        
        while True:
            try:
                menu = Menu()
                menu.displayItem()
                menu.inputKey()
                menuItem = menu.findItem()
                print("-----------------")
                calculator = Calculator()
                calculator.call(menuItem)
                print("-----------------")
            except AttributeError as e:
                print("-----------------")
                print(e.args[0])
                print("-----------------")
            except NotImplementedError as e:
                print("-----------------")
                print(e.args[0])
                print("-----------------")
            except SystemExit as e:
                print(e.args[0])
                print("-----------------")
                break