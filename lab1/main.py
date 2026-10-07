import logging
import sys
import math

log_format = "%(asctime)s | [%(levelname)-7s] | %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"

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

eps = 1e-9

try:
    side1 = float(input("Введите длину первой стороны "))
    side2 = float(input("Введите длину второй стороны "))
    side3 = float(input("Введите длину третьей стороны "))

    if side1 > 0 and side2 > 0 and side3 > 0:
        if (side1 + eps >= side2 + side3 or
            side2 + eps >= side1 + side3 or
            side3 + eps >= side2 + side1):
            logging.info("Сумма двух сторон должна быть больше третьей. Не треугольник")
            logging.info("[[-1,-1],[-1,-1],[-1,-1]]")
        else:
            if side1 == side2 == side3:
                logging.info("Треугольник равносторонний")
            elif side1 == side2 or side2 == side3 or side1 == side3:
                logging.info("Треугольник равнобедренный")
            else:
                logging.info("Треугольник разносторонний")

            x3 = (side2 ** 2 + side3 ** 2 - side1 ** 2) / (2 * side3)
            y3 = math.sqrt(max(side2 ** 2 - x3 ** 2, 0.0))
            x3 = round(x3, 10)
            y3 = round(y3, 10)
            logging.info(f"[[0,0],[{side3},0],[{x3},{y3}]]")

    else:
        logging.error("Длины должны быть больше 0")
        logging.info("[[-1, -1], [-1, -1], [-1, -1]]")


except ValueError:
    logging.warning("Нечисловые данные")
    logging.info("[[-2, -2], [-2, -2], [-2, -2]]")