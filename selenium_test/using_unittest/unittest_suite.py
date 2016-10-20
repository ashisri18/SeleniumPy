from selenium_test.using_unittest.scripts.sign_in_out import *
from selenium_test.using_unittest.scripts.buy_product import *


class Suite(unittest.TestCase):

    def test_main(self):
        logging.info('Inside test suite')
        self.suite = unittest.TestSuite([unittest.defaultTestLoader.loadTestsFromTestCase(SignInOut),
                                         unittest.defaultTestLoader.loadTestsFromTestCase(BuyProduct),])

        runner = unittest.TextTestRunner()
        runner.run(self.suite)