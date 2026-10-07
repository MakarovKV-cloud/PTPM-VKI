import logging
import sys
import math
import os

log_format = "%(asctime)s | [%(levelname)-7s] | %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG,
    format=log_format,
    datefmt=date_format,
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("logs/file_txt.log", encoding="utf-8"),
    ],
)

logging.info("Логгер успешно сконфигурирован")
logging.info("Приложение запущено")


class TriangleAnalyzer:
    def __init__(self, eps=1e-9):
        self.eps = eps

    def analyze(self, side1, side2, side3):

        # Проверка на положительность
        if not (side1 > 0 and side2 > 0 and side3 > 0):
            logging.error("Длины должны быть больше 0")
            return "Ошибка: длины должны быть больше 0", [[-1, -1], [-1, -1], [-1, -1]]

        # Проверка неравенства треугольника
        if (side1 + self.eps >= side2 + side3 or
            side2 + self.eps >= side1 + side3 or
            side3 + self.eps >= side2 + side1):
            logging.info("Сумма двух сторон должна быть больше третьей. Не треугольник")
            return "Не треугольник", [[-1, -1], [-1, -1], [-1, -1]]

        # Определение типа треугольника
        if side1 == side2 == side3:
            triangle_type = "Треугольник равносторонний"
            logging.info(triangle_type)
        elif side1 == side2 or side2 == side3 or side1 == side3:
            triangle_type = "Треугольник равнобедренный"
            logging.info(triangle_type)
        else:
            triangle_type = "Треугольник разносторонний"
            logging.info(triangle_type)

        # Вычисление координат третьей вершины
        x3 = (side2 ** 2 + side3 ** 2 - side1 ** 2) / (2 * side3)
        y3 = math.sqrt(max(side2 ** 2 - x3 ** 2, 0.0))
        x3 = round(x3, 10)
        y3 = round(y3, 10)

        coordinates = [[0, 0], [side3, 0], [x3, y3]]
        logging.info(f"Координаты вершин: {coordinates}")

        return triangle_type, coordinates

    def run_interactive(self):
        try:
            side1 = float(input("Введите длину первой стороны "))
            side2 = float(input("Введите длину второй стороны "))
            side3 = float(input("Введите длину третьей стороны "))

            self.analyze(side1, side2, side3)

        except ValueError:
            logging.warning("Нечисловые данные")
            logging.info("[[-2, -2], [-2, -2], [-2, -2]]")


if __name__ == "__main__":
    analyzer = TriangleAnalyzer()
    analyzer.run_interactive()