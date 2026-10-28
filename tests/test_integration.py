import unittest
from unittest.mock import MagicMock

from src.analyzer import TriangleAnalyzer
from src.database import TriangleDatabase
from src.user_interface import UserInterface
from src.external_service import ExternalService
from src.controller import Controller


def make_controller(stub_input, mock_external=None, db=None):
    """Фабрика контроллера с заглушками."""
    ui_stub = MagicMock(spec=UserInterface)
    ui_stub.get_input.return_value = stub_input

    if mock_external is None:
        mock_external = MagicMock(spec=ExternalService)
        mock_external.send_data.return_value = True

    return Controller(
        analyzer=TriangleAnalyzer(),
        database=db or TriangleDatabase(),
        user_interface=ui_stub,
        external_service=mock_external,
    )


class TestIntegration(unittest.TestCase):

    def test_full_scenario_new_data(self):
        """Сценарий: данные не в БД -> вычисление -> сохранение -> отправка."""
        db = TriangleDatabase()
        external = MagicMock(spec=ExternalService)
        external.send_data.return_value = True

        controller = make_controller((3.0, 4.0, 5.0), external, db)
        result = controller.run()

        self.assertEqual(result, "Треугольник разносторонний")
        self.assertIsNotNone(db.get_record(3.0, 4.0, 5.0))
        external.send_data.assert_called_once_with("Треугольник разносторонний")
        db.close()

    def test_scenario_from_cache(self):
        """Сценарий: данные есть в БД -> берём из БД, анализатор не вызывается."""
        db = TriangleDatabase()
        db.add_record(3.0, 4.0, 5.0, "Треугольник разносторонний", None)

        analyzer_mock = MagicMock(spec=TriangleAnalyzer)
        external = MagicMock(spec=ExternalService)
        external.send_data.return_value = True

        ui_stub = MagicMock(spec=UserInterface)
        ui_stub.get_input.return_value = (3.0, 4.0, 5.0)

        controller = Controller(analyzer_mock, db, ui_stub, external)
        result = controller.run()

        self.assertEqual(result, "Треугольник разносторонний")
        analyzer_mock.analyze.assert_not_called()
        external.send_data.assert_called_once()
        db.close()

    def test_scenario_invalid_triangle(self):
        """Сценарий: не треугольник -> ошибка сохраняется в БД и отправляется."""
        db = TriangleDatabase()
        external = MagicMock(spec=ExternalService)
        external.send_data.return_value = True

        controller = make_controller((1.0, 2.0, 10.0), external, db)
        result = controller.run()

        self.assertEqual(result, "Не треугольник")
        record = db.get_record(1.0, 2.0, 10.0)
        self.assertIsNotNone(record)
        self.assertEqual(record[0], "Не треугольник")
        external.send_data.assert_called_once_with("Не треугольник")
        db.close()

    def test_scenario_input_error(self):
        """Сценарий: некорректный ввод от пользователя (заглушка кидает ValueError)."""
        ui_stub = MagicMock(spec=UserInterface)
        ui_stub.get_input.side_effect = ValueError("bad input")
        external = MagicMock(spec=ExternalService)

        controller = Controller(
            TriangleAnalyzer(), TriangleDatabase(), ui_stub, external
        )
        result = controller.run()

        self.assertEqual(result, "Ошибка ввода")
        external.send_data.assert_not_called()

    def test_scenario_equal_sides(self):
        """Сценарий: равносторонний треугольник через полный цикл."""
        db = TriangleDatabase()
        external = MagicMock(spec=ExternalService)
        external.send_data.return_value = True

        controller = make_controller((5.0, 5.0, 5.0), external, db)
        result = controller.run()

        self.assertEqual(result, "Треугольник равносторонний")
        self.assertIsNotNone(db.get_record(5.0, 5.0, 5.0))
        external.send_data.assert_called_once_with("Треугольник равносторонний")
        db.close()


if __name__ == "__main__":
    unittest.main()