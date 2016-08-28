from threading import Thread

class MPawns(Thread):
    def __init__(self, size, p0, p1, k, d,pnumb):
        "initialize the given values"
        self._size = size
        self._p0_coord = p0
        self._p1_coord = p1
        self._k_coord = k
        self._d_coord = d
        self._pnumb = pnumb
        Thread.__init__(self)

    def getsize(self):
        "returns the size"
        return self._size

    def getcurrplayer(self):
        "returns the player number"
        return self._pnumb
    
    def getmoveable(self):
        "returns the list of unblocked pawns"
        return self._moveable
    
    def getallpawns(self):
        "returns all pawns"
        lst = []
        for i in self.getpawn(0):
            lst.append(i)
        for i in self.getpawn(1):
            lst.append(i)
        lst.append(self.getpawn("k"))
        for i in self.getpawn("d"):
            lst.append(i)
        return lst

    def getpawn(self, k):
        "returns the coordinates of the value"
        if k == 0:
            return self._p0_coord
        elif k == 1:
            return self._p1_coord
        elif k == "k":
            return self._k_coord
        elif k == "d":
            return self._d_coord
        
    def run(self):
        "checks if a pawn is able to move"
        _allpawns = []
        if self.getcurrplayer() == 0:
            for i in self.getpawn(0):   
                _allpawns.append(i)
        else:
            for i in self.getpawn(1):
                _allpawns.append(i)
            _allpawns.append(self.getpawn("k"))            
        self._moveable = []
        self._notpossible = []
        for i in _allpawns: # checks if the pawn is blocked
            if not ((i[0], i[1] - 1) in self.getallpawns() and (i[0], \
            i[1] + 1) in self.getallpawns() and (i[0] - 1, i[1])\
            in self.getallpawns() and (i[0] + 1, i[1]) in self.getallpawns()):
                self._moveable.append(i)
                
        for j in self._moveable: # checks if the pawn is on an edge (and cant walk)
            if j[0] == 0 and (j[0], j[1] - 1) in self.getallpawns() and \
               (j[0], j[1] + 1) in self.getallpawns() and (j[0] + 1, j[1])\
               in self.getallpawns():
                self._notpossible.append(j)                
            if j[1] == 0 and (j[0], j[1] + 1) in self.getallpawns() and \
               (j[0] - 1, j[1]) in self.getallpawns() and (j[0] + 1, j[1])\
               in self.getallpawns():
                self._notpossible.append(j)                    
            if j[0] == self.getsize() - 1 and (j[0], j[1] - 1) in \
               self.getallpawns() and (j[0], j[1] + 1) in self.getallpawns()\
               and (j[0] - 1, j[1]) in self.getallpawns():
                self._notpossible.append(j)                
            if j[1] == self.getsize() - 1 and (j[0], j[1] - 1) in \
               self.getallpawns() and (j[0] + 1, j[1]) in self.getallpawns()\
               and (j[0] - 1, j[1]) in self.getallpawns():
                self._notpossible.append(j)
        
        _helplist = self._moveable[:]
        # removes immobilized pawns from list of possible moves
        self._moveable = []
        if len(self._notpossible) != 0:
            for i in _helplist:
                if i not in self._notpossible:
                    self._moveable.append(i)
        else:
            self._moveable = _helplist
            
        for k in _allpawns: # checks if pawn can walk OVER X
            if (k[0], k[1] - 1) in self.getpawn("d") and (k[0], k[1] - 2) \
               not in self.getallpawns() and k[1] - 2 >= 0:
                self._moveable.append(k)
            elif (k[0], k[1] + 1) in self.getpawn("d") and (k[0], k[1] + 2)\
                 not in self.getallpawns() and k[1] + 2 < self.getsize():
                self._moveable.append(k)
            elif (k[0] + 1, k[1]) in self.getpawn("d") and (k[0] + 2, k[1])\
                 not in self.getallpawns() and k[0] + 2 < self.getsize():
                self._moveable.append(k)
            elif (k[0] - 1, k[1]) in self.getpawn("d") and (k[0] - 2, k[1])\
                 not in self.getallpawns() and k[0] - 2 >= 0:
                self._moveable.append(k)
        #remove dupiclates
        self._moveable = list(set(self._moveable))
