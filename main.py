import logging
import sys

# Шаблон строки лога (аналог template в Serilog)
# Содержит: время, уровень (до 7 символов для выравнивания), имя логгера и сообщение
log_format = "%(asctime)s | [%(levelname)-7s] | %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"

# Базовая настройка корневого логгера
logging.basicConfig(
    level=logging.DEBUG, # Минимальный уровень логирования (аналог MinimumLevel.Debug)
    format=log_format,
    datefmt=date_format,
    handlers=[
        logging.StreamHandler(sys.stdout),          # Настройка логирования в консоль
        logging.FileHandler("logs/file_txt.log", encoding="utf-8") # Настройка логирования в файл
    ]
)

logging.info("Логгер успешно сконфигурирован")
logging.info("Приложение запущено")

side1 = float(input('Введите длину первой стороны '))
side2 = float(input('Введите длину второй стороны '))
side3 = float(input('Введите длину третьей стороны '))

if side1 > 0 and side2 > 0 and side3 > 0:
    if side1 > side2 + side3 and side2 > side1 + side3 and side3 > side2 + side1:
        logging.info("Сумма двух сторон должна быть больше третьей")
    else:
        if side1 == side2 or side2 == side3 or side1 == side3:
            if side1 == side2 and side1 == side3:
                logging.info("Треугольник равносторонний")
            else:
                logging.info("Треугольник равнобедренный")
        logging.info("Треугольник разносторонний")
else:
    logging.info("Длины должны быть больше 0")