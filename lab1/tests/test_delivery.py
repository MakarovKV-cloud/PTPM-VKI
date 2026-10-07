import unittest
from Delivery import Delivery


class TestCalcDel(unittest.TestCase):
    def setUp(self):
        self.delivery = Delivery()


    def tearDown(self):
        del self.delivery

    def test_below_weight(self):
        self.assertEqual((Delivery.calculate_delivery_cost(-1,5, "обычный", False)),(-1,"0000-00-00"))

    def test_exceed_weight(self):
        self.assertEqual((Delivery.calculate_delivery_cost(100,5, "обычный", False)),(-1,"0000-00-00"))

    def test_below_dist(self):
        self.assertEqual((Delivery.calculate_delivery_cost(1, -1000,"обычный", False )), (-1,"0000-00-00"))

    def test_exceed_dist(self):
        self.assertEqual((Delivery.calculate_delivery_cost(1, -1000,"обычный", False )), (-1,"0000-00-00"))

    def test_another_package_type(self):
        self.assertEqual((Delivery.calculate_delivery_cost(1, 1,"маленький", False)), (-1,"0000-00-00"))

    def test_is_express(self):
        self.assertEqual((Delivery.calculate_delivery_cost(1,1, "обычный", True)), (307.5, "2026-09-03"))#ошибка логики

    def test_del_date_without_exp(self):
        self.assertEqual((Delivery.calculate_delivery_cost(1,1, "обычный", False)), (205 ,"2026-09-04"))

    def test_del_date_with_exp(self):
        self.assertEqual((Delivery.calculate_delivery_cost(1,1, "обычный", True)), (307.5, "2026-09-04"))#ошибка логики

    def test_weight_between_5_20(self):
        self.assertEqual((Delivery.calculate_delivery_cost(10, 10, "хрупкий", False)), (600, "2026-09-04"))

    def test_weight_between_20_50(self):
        self.assertEqual((Delivery.calculate_delivery_cost(30, 10, "хрупкий", False)), (675, "2026-09-04"))
