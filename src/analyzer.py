import logging
import math
import os

os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | [%(levelname)-7s] | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("logs/file_txt.log", encoding="utf-8"),
    ],
)


class TriangleAnalyzer:
    def __init__(self, eps: float = 1e-9) -> None:
        self.eps = eps

    def analyze(self, side1, side2, side3):
        if not (side1 > 0 and side2 > 0 and side3 > 0):
            logging.error("Длины должны быть больше 0")
            return "Ошибка: длины должны быть больше 0", [[-1, -1], [-1, -1], [-1, -1]]

        if (side1 + self.eps >= side2 + side3 or
                side2 + self.eps >= side1 + side3 or
                side3 + self.eps >= side2 + side1):
            logging.info("Не треугольник")
            return "Не треугольник", [[-1, -1], [-1, -1], [-1, -1]]

        if side1 == side2 == side3:
            triangle_type = "Треугольник равносторонний"
        elif side1 == side2 or side2 == side3 or side1 == side3:
            triangle_type = "Треугольник равнобедренный"
        else:
            triangle_type = "Треугольник разносторонний"

        x3 = (side2 ** 2 + side3 ** 2 - side1 ** 2) / (2 * side3)
        y3 = math.sqrt(max(side2 ** 2 - x3 ** 2, 0.0))
        x3 = round(x3, 10)
        y3 = round(y3, 10)
        coordinates = [[0, 0], [side3, 0], [x3, y3]]

        logging.info(f"{triangle_type}, координаты: {coordinates}")
        return triangle_type, coordinates