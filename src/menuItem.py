class MenuItem:
    id: int
    call: str

    def __init__(
        self,
        id: int,
        call: str
    ) -> None:
        self.id = id
        self.call = call

    def isSame(self, itemSelected: int) -> bool:
        return self.id == itemSelected

    def display(self) -> None:
        print(str(self.id) + ' - ' + self.call)