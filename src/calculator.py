from .menuItem import MenuItem

class Calculator:
    x: float
    y: float

    def call(self, menuItem: MenuItem) -> None:
        try:
            call = menuItem.call.lower()
            method = getattr(self, call)
            method()
        except AttributeError as e:
            raise AttributeError(e.args[0]) 
        except SystemExit as e:
            raise SystemExit(e.args[0]) 
        except:
            raise NotImplementedError('not exist function') 
        
    def giveMeUnit(self) -> None:
        self.x = float(input("Enter the firt unit: "))
        self.y = float(input("Enter the second unit: "))

    def addition(self) -> None:
        self.giveMeUnit()
        result = self.x + self.y
        print('The sum of two unit is: ' + str(result))

    def substraction(self) -> None:
        self.giveMeUnit()
        result = self.x - self.y
        print('The substraction of two unit is: ' + str(result))

    def multiplication(self) -> None:
        self.giveMeUnit()
        result = self.x * self.y
        print('The multiplication of two unit is: ' + str(result))

    def division(self) -> None:
        self.giveMeUnit()
        if 0 == self.y:
            raise AttributeError('0 is not a good value, sorry')
        result = self.x / self.y
        print('The division of two unit is: ' + str(result))

    def ragequit(self) -> None:
        raise SystemExit('Thx for try ma calculator') 