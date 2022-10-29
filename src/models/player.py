from stats import Stats

class Player:
    def __init__(self, fname, lname, pos, stats):
        self._fname = fname
        self._lname = lname
        self._pos = pos
        self._stats = []

    @property
    def fname(self):
        return self._fname
    
    @property
    def lname(self):
        return self._lname

    @property
    def stats(self):
        return self._stats

    @property
    def stats(self):
        return self._stats

    @fname.setter
    def fname(self, name):
        self._fname = name

    @lname.setter
    def lname(self, name):
        self._lname = name

    @stats.setter
    def stats(self, key, val):
        stats = []
        self._stats = None