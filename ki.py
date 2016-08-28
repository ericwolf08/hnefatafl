from mpawns import MPawns
from kpawns import KPawns
from queue import Queue
import random

class KI():
    """class to get the best possible move"""
    
    def __init__(self, size, p0, p1, k, d, pnumb, search, target):
        "initialize the given values and starts threads"
        self._size = size
        self._p0_coord = p0
        self._p1_coord = p1
        self._k_coord = k
        self._pnumb = pnumb
        self._decorate = d
        self._M = MPawns(size, p0, p1, k, d, pnumb)
        self._K = KPawns(size, p0, p1, k, d, pnumb)
        self._M.start()
        self._K.start()
        self._search = search # bredth/depth
        self._target = target

    def gettarget(self):
        "returns target for king"
        return self._target # True == corners
    
    def getsearch(self):
        "returns search mode"
        return self._search # True == bredth
        
    def getsize(self):
        "returns current size"
        return self._size

    def setkillable(self):
        "sets list of coordinates to kill enemies"
        self._killable = self._K.getkillable()

    def setmoveable(self):
        "sets list of moveable pawns"
        self._moveable = self._M.getmoveable()

    def getkillable(self):
        "returns list of coordinates to kill enemies"
        self._K.join()
        self.setkillable()
        return self._killable

    def getmoveable(self):
        "returns list of moveable pawns"
        self._M.join()
        self.setmoveable()        
        return self._moveable

    def getallpawns(self):
        "returns all pawns"
        lst = []
        for i in self.getpawn(0):
            lst.append(i)
        for i in self.getpawn(1):
            lst.append(i)
        lst.append(self.getpawn("k"))
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
            return self._decorate

    def move(self):
        "method to return the move the ki makes, depending on possible actions"
        _possible_move = []
        _move = []
        _prediction = []
        if len(self.getmoveable()) == 0: # KI gives up if he can't move
            return "continue"
        king = self.getpawn("k")
        if king in self.getmoveable() and ((king[0], king[1] + 1) in \
           self.getenemies(1) or (king[0], king[1] - 1) in self.getenemies(1)\
           or (king[0] + 1, king[1]) in self.getenemies(1) or \
           (king[0] - 1, king[1]) in self.getenemies(1)):
            # if king is threatened he moves away if possible
            _prediction = self.prediction()
            if _prediction != 0:
                return self.convert([_prediction[0], _prediction[1]])
        

        # first checks for horizontal/vertical moves
        for i in self.getmoveable():
            for j in self.getkillable():
                if i[0] == j[0]:
                    _possible_move.append([i, j])
                elif i[1] == j[1]:
                    _possible_move.append([i, j])

        for i in self.notpossible(_possible_move, 0):
            if i in _possible_move:
                _possible_move.remove(i)
                # removes the impossible moves

        for i in _possible_move: # garantees King kill, if possible
            if (i[1][0] + 1, i[1][1]) == self.getpawn("k") and \
                 self.getcurrplayer() == 0 and \
               (i[1][0] + 2, i[1][1]) in self.getpawn(self.getcurrplayer()):
                _move.append(i)
            elif(i[1][0] -1, i[1][1]) == self.getpawn("k") and \
                self.getcurrplayer() == 0 and \
               (i[1][0] - 2, i[1][1]) in self.getpawn(self.getcurrplayer()):
                _move.append(i)
            elif(i[1][0], i[1][1] + 1) == self.getpawn("k") and \
                self.getcurrplayer() == 0 and \
               (i[1][0], i[1][1] + 2) in self.getpawn(self.getcurrplayer()):
                _move.append(i)
            elif(i[1][0], i[1][1] - 1) == self.getpawn("k") and \
                self.getcurrplayer() == 0 and \
               (i[1][0], i[1][1] - 2) in self.getpawn(self.getcurrplayer()):
                _move.append(i) 

        if len(_move) != 0:
            return self.convert(_move[random.randint(0, len(_move) - 1)])
        # pawn that kills the king is decided randomly
        
        if len(_possible_move) != 0:
            _move = _possible_move[random.randint(0, len(_possible_move) - 1)]
            return self.convert(_move)
        # returns a random move in which a pawn gets killed

        # if no pawn can be killed, player 1 tries to move with king to target
        if self.getcurrplayer() == 1 and self.getpawn("k") in \
           self.getmoveable():
            _prediction = self.prediction()
            if _prediction != 0:
                return self.convert([_prediction[0], _prediction[1]])
            
        # if no pawns can be killed, KI moves randomly
        for i in self.getmoveable():
            k = 0
            while k != self.getsize():
                _possible_move.append([i, (i[0], k)])
                _possible_move.append([i, (k, i[1])])
                k = k + 1
     
        for i in self.notpossible(_possible_move, 0):
            if i in _possible_move:
                _possible_move.remove(i)
                # removes the impossible moves

                
        _move = _possible_move[random.randint(0, len(_possible_move) - 1)]
        # appends a random move legit move
        return self.convert(_move)

    def prediction(self):
        "returns the predicted way"
        adj = self.create_adj(self.getpawn("k"), adj = {})
        if self.getsearch(): # bredth search
            adj[self.getpawn("k")]
            _prediction = self.bredth_search(adj)
        else:
            _prediction = self.depth_search(adj)
        print(_prediction)
##                to test what way the king wants to move 
        return _prediction
                
                
    def notpossible(self, move_list, k):
        "method to check if for impossible moves"
        _not_possible = []
        _king_moves = []
        for i in move_list:
            if i[0] == i[1]:
                _not_possible.append(i)
            
            if i[0][0] == i[1][0] and (i[0][1] < i[1][1]):
                for k in range(i[0][1] + 1, i[1][1] + 1):
                    if (i[0][0], k) in self.getallpawns():
                        _not_possible.append(i)
            if i[0][0] == i[1][0] and (i[1][1] < i[0][1]):
                
                for k in range(i[1][1], i[0][1]):
                    if (i[0][0], k) in self.getallpawns():
                        _not_possible.append(i)
                            
            if i[0][1] == i[1][1] and (i[0][0] < i[1][0]):
                for k in range(i[0][0] + 1, i[1][0] + 1):
                    if (k, i[0][1]) in self.getallpawns():
                        _not_possible.append(i)
            if i[0][1] == i[1][1] and (i[1][0] < i[0][0]):
                for k in range(i[1][0], i[0][0]):
                    if (k, i[0][1]) in self.getallpawns():
                        _not_possible.append(i)
                                             
            if i[1] in self.getpawn("d") and k == 0:
                _not_possible.append(i)

            if i[1] in self.getallpawns():
                _not_possible.append(i)
        
        for i in _not_possible: # guarantees king can move on x
            if i[0] == self.getpawn("k") and i[1] in self.getpawn("d") and \
               k == 0:
                _king_moves.append(i)

        for i in _not_possible:
            if i in _king_moves:
                _not_possible.remove(i)
                
        return _not_possible

    def convert(self, move):
        "method to convert the move in output for player"
        _output = ""
        for i in move:
            _output = _output + chr(i[1] + 65) + str(i[0] + 1) + " "
        return _output                                                       
            
    def getcurrplayer(self):
        "return current player (number)"
        return self._pnumb
    
    def getenemies(self, pnumb):
        "get the enemy pawns of the current player"
        if pnumb == 0:
            _enemies = self.getpawn(1)[0:]
            _enemies.append(self.getpawn("k"))
            return _enemies
        else:
            _enemies = self.getpawn(0)
            return _enemies

    
    def create_adj(self, pawn, adj):
        "creates an  adjacency list"        
        _possible_move = []
        k = 0
        for k in range(self.getsize()):
            _possible_move.append([pawn, (pawn[0], k)])
            _possible_move.append([pawn, (k, pawn[1])])
            k = k + 1
            
        _helplist = _possible_move[:]
        _possible_move = []
        for i in _helplist:
            if i not in self.notpossible(_helplist, 1):
                _possible_move.append(i)
        # all possible moves
        
        _dangerzone = []
        _enemies = self.getenemies(1)
        for i in _possible_move:
            if (i[1][0], i[1][1] + 1) in _enemies:
                _dangerzone.append(i)
            elif (i[1][0], i[1][1] - 1) in _enemies:
                _dangerzone.append(i)
            elif (i[1][0] + 1, i[1][1]) in _enemies:
                _dangerzone.append(i)
            elif (i[1][0] - 1, i[1][1]) in _enemies:
                _dangerzone.append(i)
        # looks if pawn would get into DANGERZONE

        for j in _dangerzone:
            if (0, 0) == j[1] or (0, self.getsize() - 1) == j[1] or \
               (self.getsize() - 1, self.getsize() - 1) == j[1] or \
               (self.getsize() - 1, 0) == j[1]:
                _dangerzone.remove(j)
                
        _helplist = _possible_move[:]
        _possible_move = []
        for k in _helplist:
            if k not in _dangerzone:
                _possible_move.append(k)

        for i in _possible_move:
                if i[0] in adj:
                    adj[i[0]].add(i[1])
                else:
                    adj[i[0]] = {i[1]}
        # writes the adj.list
        
        for i in _possible_move:
            if i[1] not in adj:
                adj = self.create_adj(i[1], adj)               
        return adj    

    
    def bredth_search(self, adj):
        "looks for shortest way"
        q = Queue()
        if self.getpawn("k") not in adj:
            return 0 # no save way
        _target = self.createtarget()
        way = [self.getpawn("k")] # writes starting point to list
        q.put(way) # puts way in queue
        
        while True:
            if q.empty():
                return 0
            help_way = q.get() # always gets the whole move (til the point)
            last_array = help_way[len(help_way) - 1] # gets last element
            if last_array in _target: # break condition for reaching target
                return help_way
            if last_array in adj:
                for next_array in adj[last_array]:
                    if len(help_way) >= 10: # breaks for 10 moves
                        return 0 # takes way too long
                    if next_array not in help_way: # preventing loops
                        new_way = []
                        new_way = help_way + [next_array]
                        q.put(new_way)                 
            
    def createtarget(self):
        "creates target list depending on options edge/corners"
        if self.gettarget(): # corners
            _target = [(0, 0), (0, self.getsize() - 1), (self.getsize() - 1, 0)\
                       , (self.getsize() - 1, self.getsize() - 1)]
        else: # edges
            _target = []
            k = 0
            for k in range(11):
                _target.append((0, k))
                _target.append((k, 0))
                _target.append((10, k))
                _target.append((k, 10))
                k = k + 1
        _target = list(set(_target))
        return _target

    def depth_search(self, adj):
        "looks for depth search way"
        if self.getpawn("k") not in adj:
            return 0 # no save way
        way = [] # used as stack
        start = [self.getpawn("k")]
        way.append(start)
        _target = self.createtarget()
        while True:
            if len(way) == 0:
                return 0
            help_way = way.pop()
            last_array = help_way[len(help_way) - 1] # get last array
            if last_array in _target: # break condition for reaching target
                return help_way
            if last_array in adj:
                for next_array in adj[last_array]:
                    if len(help_way) >= 6: # jumps to next array
                        break # takes way too long
                    if next_array not in help_way: # preventing loops
                        new_way = []
                        new_way = help_way + [next_array] # appends way
                        way.append(new_way)
                    
