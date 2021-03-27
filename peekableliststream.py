
class PeekableListStream:
    '''
    Differs from PeerableStream only by maintaing
    self.current and returning [None] rather than None
    '''

    def __init__(self, iterator):
        self.iterator = iter(iterator)
        self._fill()

    def _fill(self):
        try:
            self.next = next(self.iterator)
        except StopIteration:
            self.next = [None]

    def move_next(self):
        self.current = self.next
        self._fill()
        return self.current
