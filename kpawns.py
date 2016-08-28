from threading import Thread

class KPawns(Thread):
    """Thread to look for killable pawns and returning the position to kill them"""
    
    def __init__(self, size, p0, p1, k, d, pnumb):
        "initialize the thread with all necessary attributes"
        self._size = size
        self._p0_coord = p0
        self._p1_coord = p1
        self._k_coord = k
        self._d_coord = d
        self._pnumb = pnumb
        Thread.__init__(self)
        
    def run(self):
        "checks if a pawn is killable and returns coordinates to kill it"
        _enemies = self.getenemies(self.getcurrplayer())
        _friends = self.getfriends(self.getcurrplayer())
        self._killable = []
        
        for j in _enemies:
            if (j[0], j[1] - 1) in _friends and (j[0], j[1] + 1) not in\
                self.getallpawns() and j[1] + 1 < self.getsize():
                self._killable.append((j[0], j[1] + 1))
                
            if (j[0], j[1] + 1) in _friends and (j[0], j[1] - 1) not in\
                self.getallpawns() and j[1] - 1 > 0:
                self._killable.append((j[0], j[1] - 1))
                
            if (j[0] + 1, j[1]) in _friends and (j[0] - 1, j[1]) not in\
                self.getallpawns() and j[0] - 1 >= 0:
                self._killable.append((j[0] - 1, j[1]))
                
            if (j[0] - 1, j[1]) in _friends and (j[0] + 1, j[1]) not in\
                self.getallpawns() and j[0] + 1 < self.getsize():
                self._killable.append((j[0] + 1, j[1]))
                
            #appends the coordinates to move on
            #NOT the coordinates on which the pawn stands
                
    def getkillable(self):
        "returns list with coordinates which has to be moved on to kill a pawn"
        return self._killable
               
    def getenemies(self, pnumb):
        "get the enemy pawns of the current player"
        if pnumb == 0:
            _enemies = self.getpawn(1)[0:]
            _enemies.append(self.getpawn("k"))
            return _enemies
        else:
            _enemies = self.getpawn(0)
            return _enemies

    def getfriends(self, pnumb):
        "get the pawns of the current player"
        if pnumb == 0:
            _friends = self.getpawn(0)
            return _friends
        else:
            _friends = self.getpawn(1)[0:]
            _friends.append(self.getpawn("k"))
            for i in self.getpawn("d"):
                _friends.append(i)
            return _friends

    def getpawn(self, k):
        "returns the coordinates of a specific pawn"
        if k == 0:
            return self._p0_coord
        elif k == 1:
            return self._p1_coord
        elif k == "k":
            return self._k_coord
        elif k == "d":
            return self._d_coord

    def getallpawns(self):
        "returns a list with coordinates of all pawns"
        _allpawns = []
        for i in self.getpawn(0):
            _allpawns.append(i)
        for i in self.getpawn(1):
            _allpawns.append(i)
        _allpawns.append(self.getpawn("k"))
        for i in self.getpawn("d"):
            _allpawns.append(i)
        return _allpawns
    
    def getcurrplayer(self):
        "returns current playernumber"
        return self._pnumb
    
    def getsize(self):
        "returns current size"
        return self._size
        
