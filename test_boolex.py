from boolexer import boolex    # The code to test
import unittest   # The test framework

class Test_Testboolex(unittest.TestCase):
    def test_boolex(self):
        self.assertListEqual(list(boolex("x3")),[('literal','x3')])
        self.assertListEqual(list(boolex("x3+x1")),[('literal', 'x3'), ('dnf', '+'), ('literal', 'x1')])
        
if __name__ == '__main__':
    print("test")
    unittest.main()