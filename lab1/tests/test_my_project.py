import unittest
from main import TriangleAnalyzer


class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.tr = TriangleAnalyzer()
        self.tr_strict = TriangleAnalyzer(eps=0)

    def tearDown(self):
        del self.tr
        del self.tr_strict

    # ---------- Корректные треугольники ----------

    def test_equilateral(self):
        """Равносторонний треугольник: все стороны равны."""
        result, coords = self.tr.analyze(3, 3, 3)
        self.assertEqual(result, "Треугольник равносторонний")
        self.assertEqual(len(coords), 3)

    def test_isosceles(self):
        """Равнобедренный треугольник: две стороны равны."""
        result, coords = self.tr.analyze(5, 5, 6)
        self.assertEqual(result, "Треугольник равнобедренный")
        self.assertEqual(len(coords), 3)

    def test_scalene(self):
        """Разносторонний треугольник: все стороны разные."""
        result, coords = self.tr.analyze(3, 4, 5)
        self.assertEqual(result, "Треугольник разносторонний")
        self.assertEqual(len(coords), 3)

    def test_right_triangle(self):
        """Прямоугольный треугольник 3-4-5: проверка координат."""
        result, coords = self.tr.analyze(3, 4, 5)
        # Первая вершина всегда (0, 0), вторая (side3, 0) = (5, 0)
        self.assertEqual(coords[0], [0, 0])
        self.assertEqual(coords[1], [5, 0])
        # Третья вершина: x = (side2^2 + side3^2 - side1^2) / (2*side3)
        # x = (16 + 25 - 9) / 10 = 3.2, y = sqrt(16 - 10.24) = sqrt(5.76) = 2.4
        self.assertAlmostEqual(coords[2][0], 3.2, places=9)
        self.assertAlmostEqual(coords[2][1], 2.4, places=9)

    # ---------- Ошибки: отрицательные и нулевые стороны ----------

    def test_negative_side(self):
        """Отрицательная длина стороны — ошибка."""
        result, coords = self.tr.analyze(-1, 2, 2)
        self.assertEqual(result, "Ошибка: длины должны быть больше 0")
        self.assertEqual(coords, [[-1, -1], [-1, -1], [-1, -1]])

    def test_zero_side(self):
        """Нулевая длина стороны — ошибка."""
        result, coords = self.tr.analyze(0, 2, 2)
        self.assertEqual(result, "Ошибка: длины должны быть больше 0")
        self.assertEqual(coords, [[-1, -1], [-1, -1], [-1, -1]])

    # ---------- Ошибки: неравенство треугольника ----------

    def test_not_triangle_sum_equal(self):
        """Сумма двух сторон равна третьей — не треугольник."""
        result, coords = self.tr_strict.analyze(1, 2, 3)
        self.assertEqual(result, "Не треугольник")
        self.assertEqual(coords, [[-1, -1], [-1, -1], [-1, -1]])

    def test_not_triangle_sum_less(self):
        """Сумма двух сторон меньше третьей — не треугольник."""
        result, coords = self.tr.analyze(1, 2, 10)
        self.assertEqual(result, "Не треугольник")
        self.assertEqual(coords, [[-1, -1], [-1, -1], [-1, -1]])

    def test_almost_triangle_with_eps(self):
        """Почти треугольник: 1, 2, 3 + eps — при eps=1e-9 считается не треугольником."""
        result, coords = self.tr.analyze(1, 2, 3 + 1e-10)
        self.assertEqual(result, "Не треугольник")

    # ---------- Граничные случаи ----------

    def test_very_small_sides(self):
        """Очень маленькие стороны — равносторонний треугольник."""
        result, coords = self.tr.analyze(1e-6, 1e-6, 1e-6)
        self.assertEqual(result, "Треугольник равносторонний")
        self.assertEqual(len(coords), 3)

    def test_large_sides(self):
        """Большие стороны — разносторонний треугольник."""
        result, coords = self.tr.analyze(1e6, 1.1e6, 1.2e6)
        self.assertEqual(result, "Треугольник разносторонний")
        self.assertEqual(len(coords), 3)


if __name__ == "__main__":
    unittest.main()