from abc import ABC, abstractmethod


class UserInterface(ABC):
    """Абстрактный интерфейс взаимодействия с пользователем."""

    @abstractmethod
    def get_input(self) -> tuple:
        """Запросить у пользователя три стороны треугольника."""
        ...


class ConsoleUserInterface(UserInterface):
    """Реализация через консольный ввод."""

    def get_input(self) -> tuple:
        side1 = float(input("Введите длину первой стороны: "))
        side2 = float(input("Введите длину второй стороны: "))
        side3 = float(input("Введите длину третьей стороны: "))
        return side1, side2, side3