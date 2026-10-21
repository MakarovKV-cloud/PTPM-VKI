import logging


class Controller:
    """Контроллер бизнес-логики."""

    def __init__(self, analyzer, database, user_interface, external_service):
        self.analyzer = analyzer
        self.database = database
        self.ui = user_interface
        self.external = external_service

    def run(self) -> str:
        """Сквозной сценарий."""
        try:
            side1, side2, side3 = self.ui.get_input()
        except (ValueError, TypeError) as e:
            logging.error(f"Некорректный ввод: {e}")
            return "Ошибка ввода"

        # Проверка наличия в БД
        record = self.database.get_record(side1, side2, side3)
        if record is not None:
            triangle_type, error_message = record
            logging.info("Результат взят из БД")
            result = triangle_type
        else:
            result, _coords = self.analyzer.analyze(side1, side2, side3)
            error_message = result if "Ошибка" in result or "Не треугольник" in result else None
            self.database.add_record(side1, side2, side3, result, error_message)
            logging.info("Результат вычислен и добавлен в БД")

        # Отправка во внешнюю зависимость
        self.external.send_data(result)
        return result