import unittest
import logging

logger = logging.getLogger("test")
logging.basicConfig(format="%(asctime)s-%(msg)s", level=logging.DEBUG)


class TestBasicSetup(unittest.TestCase):

    def test_first_ever_test(self):
        self.assertEqual("Foo", "Foo")

    def test_word_in_list_of_words(self):
        self.assertIn("Jaydeep",["Vishal", "Jaydeep", "Shreeja"])

    def test_if_input_is_of_particular_class(self):
        self.assertIsInstance("jaydeep", str)

    def test_assert_logs(self):
        with self.assertLogs("test", level="INFO") as lm:
            logger.info("THIS IS AN INFO MESSAGE")
            print(lm.records)
            self.assertEqual(lm.records[0].getMessage(),"THIS IS AN INFO MESSAGE")

if __name__ == "__main__":
    unittest.main()
