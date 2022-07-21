from stats import Stats

class Player():
    def __init__(self, fname, lname, pos):
        self._fname = fname
        self._lname = lname
        self._pos = pos
        self._stats = []

    @stats.setter
    def stats(self, key, val):
        stats = []
        self._stats = None