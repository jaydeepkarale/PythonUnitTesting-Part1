import unittest


class Product:

    def __init__(self,):
        self.product_dict = {}

    def add_product(self, name, price, stock_quantity):
        self.product_dict[name] = {"price": price, "qty": stock_quantity}
        return {name: self.product_dict[name]}

    def search_product_by_name(self, name):
        return {name: self.product_dict[name]}

    def delete_product(self, name):
        del self.product_dict[name]


class Order:
    def __init__(self):
        self.order_dict = {}

    def create_order(self, name, quantity):
        self.order_dict[name] = quantity

    def update_order(self, name, quantity):
        self.order_dict[name] = quantity


class TestProduct(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("Inside setupclass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("inside teardown class")

    def setUp(self):
        print("Inside setup method")
        self.product = Product()

    def tearDown(self):
        print("Inside tear down method")

    def test_add_product_returns_dictionary(self):
        product = Product()
        data = product.add_product("Iphone13", 999, 100)
        self.assertIsInstance(data, dict)

    def test_add_product_returns_name_of_product(self):
        product = Product()
        data = product.add_product("LGMonitor", 1000, 10)
        self.assertIn("LGMonitor", data.keys())

    def test_add_product_returns_price_of_product(self):
        data = self.product.add_product("GalaxyS22", 800, 100)
        self.assertEqual(800, list(data.values())[0]["price"])

    def test_search_product_by_name(self):
        # ARRANGE
        self.product.add_product("GalaxyS22", 800, 100)
        # ACT
        data = self.product.search_product_by_name("GalaxyS22")
        # ASSERT
        self.assertIn("GalaxyS22", data)









if __name__ == "__main__":
    unittest.main()

