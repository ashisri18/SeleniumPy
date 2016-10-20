from selenium_test.using_pytest.pytest_scripts.scripts import *


class Suite(unittest.TestCase):

    def suite(self):
        logging.info('Inside test suite')
        self.suite = unittest.TestSuite([unittest.defaultTestLoader.loadTestsFromTestCase(TestSignInOut),
                                         unittest.defaultTestLoader.loadTestsFromTestCase(TestBuyProduct)])

        runner = unittest.TextTestRunner()
        runner.run(self.suite)