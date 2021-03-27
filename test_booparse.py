import unittest   # The test framework
from booparser import booparse    # The code to test
from boolexer import boolex

class Test_Testboolex(unittest.TestCase):
    def test_booparse(self):
        s = "(x1+x2);"
        bp = booparse(boolex(s))
        self.assertListEqual(list(bp), [('term', [('dnf', ('literal', 'x1'), ('literal', 'x2'))])])
        s = "(x1+!x2);"
        bp = booparse(boolex(s))
        self.assertListEqual(list(bp), [('term', [('dnf', ('literal', 'x1'), ('!', ('literal', 'x2')))])])

    