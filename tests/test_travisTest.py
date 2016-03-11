"""
Example unit tests for travisTest package
"""
import unittest
import desc.travistest

class travisTestTestCase(unittest.TestCase):
    def setUp(self):
        self.message = 'Hello, world'
        
    def tearDown(self):
        pass

    def test_run(self):
        foo = desc.travistest.travisTest(self.message)
        self.assertEquals(foo.run(), self.message)

    def test_failure(self):
        self.assertRaises(TypeError, desc.travistest.travisTest)
        foo = desc.travistest.travisTest(self.message)
        self.assertRaises(RuntimeError, foo.run, True)

if __name__ == '__main__':
    unittest.main()
