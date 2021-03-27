
#from pycell.peekablestream import PeekableStream
from peekablestream import PeekableStream
from boolexer import boolex

if __name__ == '__main__':
    import doctest
    doctest.testmod()

class BooParser:
    def __init__(self, tokens, stop_at):
        self.tokens = tokens
        self.stop_at = stop_at

    def next_expression(self, prev):
        self.fail_if_at_end(";")
        typ, value = self.tokens.next
        if typ in self.stop_at:
            return prev
        self.tokens.move_next()
        if typ in ("literal") and prev is None:
            return self.next_expression((typ, value))
        elif typ == "cnf":
            nxt = self.next_expression(None)
            return self.next_expression(("cnf", prev, nxt))
        elif typ == "dnf":
            nxt = self.next_expression(None)
            return self.next_expression(("dnf", prev, nxt))
        elif typ == "!":
            nxt = self.next_expression(None)
            return  self.next_expression(("!", nxt))
        elif typ == "(":
            args = self.term(")")
            return self.next_expression(("term", args))
        else:
            raise Exception("Unexpected token: " + str((typ, value)))

    def term(self, end):
        ret = []
        self.fail_if_at_end(end)
        typ = self.tokens.next[0]
        if typ == end:
            self.tokens.move_next()
        else:
            arg_parser = BooParser(self.tokens, (end))
            while typ != end:
                p = arg_parser.next_expression(None)
                if p is not None:
                    ret.append(p)
                typ = self.tokens.next[0]
                self.tokens.move_next()
                self.fail_if_at_end(end)
        return ret

    def fail_if_at_end(self, expected):
        if self.tokens.next is None:
            raise Exception("Hit end of file - expected '%s'." % expected)


def booparse(tokens_iterator):
    '''
    >>> s = "(x1+x2);"
    >>>> bp = booparse(boolex(s))
    [('term', [('dnf', ('literal', 'x1'), ('literal', 'x2'))])]
    '''
    parser = BooParser(PeekableStream(tokens_iterator), ";")
    while parser.tokens.next is not None:
        p = parser.next_expression(None)
        if p is not None:
            yield p
        parser.tokens.move_next()




