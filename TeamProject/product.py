class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def __str__(self) -> str:
        return (f"Product [ "
                f"{self.__name} — €{self.__price:.2f} "
                )