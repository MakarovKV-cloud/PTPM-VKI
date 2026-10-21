import unittest


from src.analyzer import TriangleAnalyzer
from src.database import TriangleDatabase


class TestUnit(unittest.TestCase):
    """Юнит-тесты"""

    def test_database_add_and_get(self):
        """Тест добавления и получения записи из БД."""
        db = TriangleDatabase()
        db.add_record(3.0, 4.0, 5.0, "Треугольник разносторонний", None)
        result = db.get_record(3.0, 4.0, 5.0)
        self.assertEqual(result[0], "Треугольник разносторонний")
        db.close()

    def test_database_delete(self):
        """Тест удаления записи из БД."""
        db = TriangleDatabase()
        db.add_record(6.0, 8.0, 10.0, "Треугольник разносторонний", None)
        self.assertTrue(db.delete_record(6.0, 8.0, 10.0))
        self.assertIsNone(db.get_record(6.0, 8.0, 10.0))
        db.close()


if __name__ == "__main__":
    unittest.main()