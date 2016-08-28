"""Date : 20.12.2011 
 Module can start differents boards inc. rules
 Programmer: Sebastian Hamann Mn.: 4549389 
             Eric Wolf Mn.: 4554086 
 Group: SHL 
        Tutor:  Pavel Safre 
"""

import os, sys
from frame import Frame
from ki import KI

class Game():
    """class for the whole game"""
    _DESC_OPTIONS = "To Change a value, just type the number and press enter.\
               \nType \"done\" when you are finished.\n"
    _INVALID_FILE = "\nFile does not exist or has wrong syntax."
    _INVALID_NAME = "\nNames have at least 1 letter.\n"
    _INVALID_INPUT = "Please check your input.\nEnter a valid value."
    _INVALID_TURN = "\nYou made a mistake.\
                \n 1. check if there was a pawn in the way\
                \n 2. check if the field was taken\
                \n 3. check if your pawn is allowed to move that way\
                \nFor detailed rules check the readme.txt"
    
    def __init__(self):
        "initialize an object with attributs of this class"
        self._rule_king_corners = True # sets the standard rules
        self._rule_king_catch = True
        self._rule_pawn_remove = True
        self._rule_search = True
        self._listpast = []
        self._listfuture = []
        self._pp0 = 0 # playerpoints for winning a game
        self._pp1 = 0
        self._player0 = ""
        self._player1 = ""
        self._p0_race = ""
        self._p1_race = ""
        self.frame = Frame()
        print(self.frame)
        self.chooselevel()

    def clearscreen(self):
        "method to clean the screen;\
        Source: http://tinyurl.com/cj2q6k date: 14.11.11"
        if os.name == "posix": # Unix/Linux/MacOS/BSD/etc
            os.system('clear')
        elif os.name in ("nt", "dos", "ce"): # DOS/Windows
            os.system('CLS')
        else: # Fallback for other operating systems.
            print ('\n' * 1337)
            
    def getpp(self, playernumber):
        "gets the current player points"
        if playernumber == 0:
            return self._pp0
        else:
            return self._pp1

    def incpp(self, playernumber):
        "increases the current player points by 1"
        if playernumber == 0:
            self._pp0 = self._pp0 + 1
        else:
            self._pp1 = self._pp1 + 1
    
    def exi(self):
        "method to exit the program"
        self.clearscreen()
        sys.exit("You killed the game")
        
    def createboard(self):
        "creats the empty board"
        _lst = []
        for y in range(1, self.getsize() + 1):
            _board_row = []
            for x in range(1, self.getsize() + 1):
                _board_row.append(self.getvalue("e"))
            _lst.append(_board_row)
        self._board = _lst

    def getboard(self):
        "returns the board"
        return self._board
    
    def getsize(self):
        "returns the size of the board"
        return self._size
    
    def printboard(self):
        "prints the board with column names and row names"
        _n = 1
        _z = 65 # "A" in ASCII code
        _string = ""
        for i in self.getboard():
            _string = _string + (" ".join(i) + "  " + str(_n)) + "\n"
            _n = _n + 1
        _board_column = ""
        for i in range(0, self.getsize()):
            _board_column = _board_column + chr(_z) + " "  
            _z = _z + 1
        print(_string + _board_column)
    
    def setnames(self):
        "sets the names of the player"
        while True:
            if self.getrace(0) == "C" or self.getrace(0) == "H":
                break
            self._p0_race = input("Is Player 1 a [H]uman or [C]omputer? ")            
            if self._p0_race.upper() == "C":
                self._p0_race = "C"
                self._player0 = "Cortana"
                break
            elif self._p0_race.upper() == "H":
                self._p0_race = "H"
                self._player0 = input("Please insert name for Player 1: ")
                if self._player0.upper() == "QUIT":
                    self.exi()
                elif self._player0.isnumeric():
                    self._p0_race = ""
                    print(self._INVALID_NAME)
                    continue
                else:
                    break
            else:
                continue                
        while True:
            if self.getrace(1) == "C" or self.getrace(1) == "H":
                break
            self._p1_race = input("Is Player 2 a [H]uman or [C]omputer? ")            
            if self._p1_race.upper() == "C":
                self._p1_race = "C"
                self._player1 = "Shodan"
                break
            elif self._p1_race.upper() == "H":
                self._p1_race = "H"
                self._player1 = input("Please insert name for Player 2: ")
                if self._player1.upper() == "QUIT":
                    self.exi()
                elif self._player1.isnumeric():
                    self._p1_race = ""
                    print(self._INVALID_NAME)
                    continue
                else:
                    break
            else:
                continue
        
    def getnames(self, player):
        "gets the player names"
        if player == 0:
            return self._player0
        else:
            return self._player1
        
    def getrules(self, number):
        "gets the current rules"
        if number == 1:
            return self._rule_king_corners
        elif number == 2:
            return self._rule_king_catch 
        elif number == 3:
            return self._rule_pawn_remove
        elif number == 4:
            return self._rule_search
        
    def changerules(self):
        "method to change the rules"
        self.frame.options(self.getrules(1), self.getrules(2),\
                           self.getrules(3), self.getrules(4))
        self.clearscreen()
        print(self.frame)
        while True:
            print(self._DESC_OPTIONS)
            number = input("Select: ")
            try:
                if int(number) == 1: # sets the boolvalues of the rules
                    if self.getrules(1):
                        self._rule_king_corners = False
                    else:
                        self._rule_king_corners = True
                    self.frame.options(self.getrules(1), self.getrules(2), \
                                  self.getrules(3), self.getrules(4))
                    # changes the self.frame
                    self.clearscreen()
                    print(self.frame)
                elif int(number) == 2:
                    if self.getrules(2):
                        self._rule_king_catch = False
                    else:
                        self._rule_king_catch = True
                    self.frame.options(self.getrules(1), self.getrules(2), \
                                  self.getrules(3), self.getrules(4))
                    self.clearscreen()
                    print(self.frame)
                elif int(number) == 3:
                    if self.getrules(3):
                        self._rule_pawn_remove = False
                    else:
                        self._rule_pawn_remove = True
                    self.frame.options(self.getrules(1), self.getrules(2), \
                                  self.getrules(3), self.getrules(4))
                    self.clearscreen()
                    print(self.frame)
                elif int(number) == 4:
                    if self.getrules(4):
                        self._rule_search = False
                    else:
                        self._rule_search = True
                    self.frame.options(self.getrules(1), self.getrules(2), \
                                  self.getrules(3), self.getrules(4))
                    self.clearscreen()
                    print(self.frame)
                else:
                    ERROR
            except:
                if number.upper() == "DONE":
                    break
                elif number.upper() == "QUIT":
                    self.exi()
                else:
                    self.clearscreen()
                    self.frame.options(self.getrules(1), self.getrules(2), \
                                  self.getrules(3), self.getrules(4))
                    self.clearscreen()
                    print(self.frame)
                    print(self._INVALID_INPUT + "\n")

    def setcurrplayer(self):
        "switches the current player"
        if self.getcurrplayer() == 1:
            self._player = self._player - 1
        else:
            self._player = self._player + 1

    def getcurrplayer(self):
        "gets the current player"
        return self._player
    
    def getenemy(self):
        "gets the current enemy player"
        if self.getcurrplayer() == 1:
            return 0
        else:
            return 1
    
    def menu(self):
        "user chooses game mode or options"
        self.clearscreen()
        self.frame.menu()
        print(self.frame)
        while True:
            choose = input("\nSelect: ")        
            if choose.upper() == "O": # opens optionsmenu
                self.changerules()
                self.clearscreen()
                self.frame.menu()
                print(self.frame)
                continue
            elif choose.upper() == "QUIT": # exits game
                self.exi()
            elif choose.upper() == "P": # starts multiplayer game
                if len(self.getnames(0)) == 0: # checks for existing names
                    self.setnames()
                self.multigame()
                break
            else:
                self.clearscreen()
                print(self.frame)
                print(self._INVALID_INPUT)
            
    def read_data(self, file):
        "method to read files and set values\coordinates"
        self._path = "level/" # sub folder level
        filedir = os.path.join(self._path, file) # full path of file
        data = open(filedir, "r")
        for line in data: # evaluates the file
            if "SIZE" in line:
                self._size = int(line.split(":=")[1])
            elif "EMPTY" in line:
                self._empty = eval(line.split(":=")[1])
            elif "DECORATE" in line:
                self._decorate_value = eval(line.split(":=")[1][0:4])
                self._decorate_coordinates = eval(line.split("@")[1])
            elif "PLAYER_0" in line:
                self._player0_value = eval(line.split(":=")[1][0:4])
                self._player0_coordinates = eval(line.split("@")[1])
            elif "PLAYER_1" in line:
                self._player1_value = eval(line.split(":=")[1][0:4])
                self._player1_coordinates = eval(line.split("@")[1])
            elif "KING" in line:
                self._king_value = eval(line.split(":=")[1][0:4])
                self._king_coordinates = eval(line.split("@")[1])    
        self.setboardvalues()
        data.close()

    def chooselevel(self):
        "user chooses the level"
        self._player = 0 # sets the current player
        self._path = "level/" # path to folder "level"
        print("\n" + str(os.listdir(self._path))) # prints content of \\level
        while True:
            try: # prevents errors
                file = input("\n" + "Choose your file: ")         
                self.read_data(file)
            except:
                if file.upper() == "QUIT": # program quits for "quit"
                    self.exi()
                self.clearscreen()
                self.frame.main()
                print(self.frame)
                print(self._INVALID_FILE) 
                self.chooselevel() 
            break
        self.menu()
        
    def setvalues(self, value, coordinates):
        "sets the values on the board"
        for i in coordinates:
            if type(coordinates) == list  and  self.getboard()[i[0]][i[1]] \
               == self.getvalue("e"):
                self.getboard()[i[0]][i[1]] = value
            elif type(coordinates) == tuple  and  \
                 self.getboard()[coordinates[0]][coordinates[1]] == self.getvalue("e"):
                self.getboard()[coordinates[0]][coordinates[1]] = value
            else:
                pass
            
    def multigame(self):
        "for beginning a multigame"
        self.frame.ingame()
        self.screenrefresh()
        self.turn()
        
    def getcoordinates(self, value):
        "returns the coordinates depending on the value"
        if value == 0:
            return self._player0_coordinates
        elif value == 1:
            return self._player1_coordinates
        elif value == "k":
            return self._king_coordinates
        elif value == "d":
            return self._decorate_coordinates

    def getvalue(self, value):
        "returns the values"
        if value == 0:
            return self._player0_value
        elif value == 1:
            return self._player1_value
        elif value == "k":
            return self._king_value
        elif value == "d":
            return self._decorate_value
        elif value == "e":
            return self._empty

    def move(self, pos, pos_new):
        "method to move the pawns"
        self.validmove(pos, pos_new)
        self.jumpcheck(pos, pos_new)
        if self.getrules(3) == False: # checks the rule setup of blocked
            self.blocked(pos)
        if pos in self.getcoordinates(self.getcurrplayer()): # moves pawns
            self.getcoordinates(self.getcurrplayer()).remove(pos)
            self.getcoordinates(self.getcurrplayer()).append(pos_new)
        elif pos == self.getcoordinates("k") and self.getcurrplayer() == 1:
            self._king_coordinates = pos_new
        else:
            ERROR # triggers an error in turn if pawn doesn't belong to you
            
    def blocked(self, pos):
        "checks if a pawn is blocked"
        if (pos[0], pos[1] - 1) in self.getenemies() and (pos[0], \
            pos[1] + 1) in self.getenemies() or ((pos[0] - 1, pos[1])\
            in self.getenemies() and (pos[0] + 1, pos[1]) \
            in self.getenemies()):
            ERROR # triggers an error in turn if pawn is blocked
            
    def getenemies(self):
        "get the enemy pawns of the current player"
        if self.getcurrplayer() == 0:
            enemies = self.getcoordinates(self.getenemy())[0:]
            enemies.append(self.getcoordinates("k"))
            for i in self.getcoordinates("d"):
                enemies.append(i)
            return enemies
        else:
            enemies = self.getcoordinates(self.getenemy())
            return enemies

    def getfriends(self):
        "get the pawns of the current player"
        if self.getcurrplayer() == 0:
            friends = self.getcoordinates(self.getcurrplayer())
            return friends
        else:
            friends = self.getcoordinates(self.getcurrplayer())[0:]
            friends.append(self.getcoordinates("k"))
            for i in self.getcoordinates("d"):
                friends.append(i)
            return friends
        
    def setboardvalues(self):
        "resets the board with current values"
        self.createboard()
        self.setvalues(self.getvalue(0), self.getcoordinates(0)) 
        self.setvalues(self.getvalue(1), self.getcoordinates(1))
        self.setvalues(self.getvalue("k"), self.getcoordinates("k"))
        self.setvalues(self.getvalue("d"), self.getcoordinates("d"))        

    def killpawn(self, pos_new):
        "checks if a pawn kills or get killed"             
        if (pos_new[0], pos_new[1] + 2) in self.getfriends() and \
           (pos_new[0], pos_new[1] + 1) in self.getenemies():
            self.remove((pos_new[0], pos_new[1] + 1)) 
        if (pos_new[0], pos_new[1] - 2) in self.getfriends() and \
           (pos_new[0], pos_new[1] - 1) in self.getenemies():
            self.remove((pos_new[0], pos_new[1] - 1))            
        if (pos_new[0] + 2, pos_new[1]) in self.getfriends() and \
           (pos_new[0] + 1, pos_new[1]) in self.getenemies():
            self.remove((pos_new[0] + 1, pos_new[1]))
        if (pos_new[0] - 2, pos_new[1]) in self.getfriends() and \
           (pos_new[0] - 1, pos_new[1]) in self.getenemies():
            self.remove((pos_new[0] - 1, pos_new[1]))            
        if (pos_new[0], pos_new[1] - 1) in self.getenemies() and \
            (pos_new[0], pos_new[1] + 1) in self.getenemies() or \
            ((pos_new[0] - 1, pos_new[1]) in self.getenemies() and \
            (pos_new[0] + 1, pos_new[1]) in self.getenemies()):
            self.remove(pos_new)
        if len(self.getcoordinates(0)) == 0:
               self.gameover(1)

    def remove(self, pos):
        "method to check if pawn gets removed"
        if pos in self.getcoordinates(0) and self.getrules(3):
            self.getcoordinates(0).remove(pos)
            self.gettimeline()[-1].append((0, pos[0], pos[1]))            
        elif pos in self.getcoordinates(1) and self.getrules(3):
            self.getcoordinates(1).remove(pos)
            self.gettimeline()[-1].append((1, pos[0], pos[1]))   
        elif pos == self.getcoordinates("k") and self.getrules(2):
            self.gameover(0) # if king gets killed by 2, game is over       

    def validmove(self, pos, pos_new):
        "checks if the move is correct"
        if pos[0] == pos_new[0] or pos[1] == pos_new[1]:
            pass # checks if move is horizontal or vertical and valid
        else:
            ERROR            
        if pos_new in self.getcoordinates(0) or pos_new in \
           self.getcoordinates(1) or pos_new == self.getcoordinates("k"):
            ERROR #  checks if field is empty
        if pos_new in self.getcoordinates("d") \
           and pos != self.getcoordinates("k"): # only king can move on throne
            ERROR  

    def jumpcheck(self, pos, pos_new):
        "checks if a pawn is in the way"
        if pos[0] == pos_new[0]: # checks for horizontal move
            for i in range (pos[1] + 1, pos_new[1]):
                if pos[1] < pos_new[1] and \
                   ((pos[0], i) in self.getallpawns()):
                    ERROR
            for i in range (pos_new[1] + 1, pos[1]):
                if pos_new[1] < pos[1] and \
                   ((pos[0], i) in self.getallpawns()):
                    ERROR
        else: # checks for vertical move
            for i in range (pos[0] + 1, pos_new[0]):
                if pos[0] < pos_new[0] and \
                   ((i, pos[1]) in self.getallpawns()):
                    ERROR
            for i in range (pos_new[0] + 1, pos[0]):
                if pos_new[0] < pos[0] and \
                   ((i, pos[1]) in self.getallpawns()):
                    ERROR

    def getallpawns(self):
        "returns all pawns"
        lst = []
        for i in self.getcoordinates(0):
            lst.append(i)
        for i in self.getcoordinates(1):
            lst.append(i)
        lst.append(self.getcoordinates("k"))
        return lst
    
    def column_check(self, column):
        "checks input(column) for correct variable"
        column = column.upper()
        if (ord(column) - 65) < self._size:
            return (ord(column) - 65)
        else:
            ERROR

    def str2int(self, string):
        "slices out the number in the coordinate"
        string = string[1:]
        if (1 <= int(string) <= self._size):
            return (int(string) - 1)
        else:
            ERROR

    def winningcondition(self):
        "checks for winning conditions after moving"
        _corners = [(0,0),(0,(self._size - 1)),((self._size - 1),0),\
                    ((self._size - 1),(self._size - 1))]
        _edge = []
        for i in range(0, self._size): # gives edge all coordinates
            _edge.append((i, 0)) # coordinates are in a tuple
            _edge.append((0, i))
            _edge.append((i, self._size - 1))
            _edge.append((self._size - 1, i))
        if self.getrules(1) and self.getcoordinates("k") in _corners:
            self.gameover(1) # winning condition for corners
        if self.getcoordinates("k") in _edge and not self.getrules(1):
            self.gameover(1) # winning condition for edge                
        if not self.getrules(2):
            self.kingsurrounded() # checks if king is surrounded

    def kingsurrounded(self):
        "checks if the king is surrounded"
        king = self.getcoordinates("k")
        enemies = self.getcoordinates(0)
        if (king[0], king[1] - 1) in enemies and (king[0], \
            king[1] + 1) in enemies and (king[0] - 1,king[1])\
            in enemies and (king[0] + 1, king[1]) in enemies:
            self.gameover(0)
            
    def turn(self):
        "method to ask for coordinates and other possible inputs"
        while True:
            if self.frame.isgameover() == True:
                self.exi()
            try:
                if self.getrace(self.getcurrplayer()) == "C":
                    ki = KI(self.getsize(), self.getcoordinates(0),\
                            self.getcoordinates(1), \
                            self.getcoordinates("k"), self.getcoordinates("d"),\
                            self.getcurrplayer(), self.getrules(4),\
                            self.getrules(1))
                    coordinates = "ERROR"
                    splitpos = ""
                    coordinates = ki.move()
                    signal = input("\n" + self.getnames(self.getcurrplayer()) + " wants to" + \
                              " move: " + coordinates + "\nConfirm with [ENTER]: ")
                    splitpos = signal.split(" ")[0]
                    if splitpos.upper() == "QUIT":
                        coordinates = signal
                        ERROR # triggers error for except
                    elif coordinates.upper() == "CONTINUE":
                        splitpos = "CONTINUE"
                        ERROR # KI can give up
                    elif splitpos.upper() == "BREAK":
                        coordinates = signal
                        ERROR # triggers error for except
                    elif splitpos.upper() == "BACKWARD":
                        coordinates = signal
                        ERROR
                    elif splitpos.upper() == "FORWARD":
                        coordinates = signal
                        ERROR
                    else:
                        self.movecheck(coordinates)
                else: #if race is human
                    coordinates = input("\nPlease insert coordinates: ")
                    splitpos = coordinates.split(" ")[0]
                    self.movecheck(coordinates)   
            except:
                if splitpos.upper() == "QUIT":
                    self.exi()
                elif splitpos.upper() == "CONTINUE":
                    self.gameover(self.getenemy())
                elif splitpos.upper() == "BREAK":
                    self.clearscreen()
                    self = Game()
                elif splitpos.upper() == "BACKWARD" and \
                    len(coordinates.split(" ")) != 1 and \
                    coordinates.split(" ")[1].isdigit() and \
                    int(coordinates.split(" ")[1]) <= len(self.gettimeline()):                    
                    self.timemachine(0, int(coordinates.split(" ")[1]))
                    self.screenrefresh()
                    continue
                elif splitpos.upper() == "FORWARD" and \
                    len(coordinates.split(" ")) != 1 and \
                    coordinates.split(" ")[1].isdigit() and \
                    int(coordinates.split(" ")[1]) <= len(self.getfuture()):
                    self.timemachine(1, int(coordinates.split(" ")[1]))
                    self.screenrefresh()
                    continue
                elif coordinates == "ERROR":
                    continue
                else:
                    self.screenrefresh()
                    print(self._INVALID_TURN)
                    continue
            self.winningcondition()
            self.setcurrplayer()
            self.resetfuture()
            self.screenrefresh()
            
    def movecheck(self, coordinates):
        splitpos = coordinates.split(" ")[0] # splits for old position
        column = self.column_check(splitpos[0])
        row = self.str2int(splitpos)
        pos = (row, column)
        splitpos2 = coordinates.split(" ")[1] # splits for new position
        row_new = self.str2int(splitpos2)
        column_new = self.column_check(splitpos2[0])
        pos_new = (row_new, column_new)
        self.move(pos, pos_new)
        self.timerecord(pos, pos_new)
        self.killpawn(pos_new)
        self.setboardvalues()

    def screenrefresh(self):
        "refreshes the screen"
        self.clearscreen()
        print(self.frame)
        print("\n" + self.getnames(self.getcurrplayer()) + "'s turn!\n")
        self.printboard()

    def resetfuture(self):
        "resets the future list after every successful turn"
        self._listfuture = []
        
    def getfuture(self):
        "returns the future-list"
        return self._listfuture

    def timemachine(self, indicator, steps):
        "the time machine travels through time and space, use with care!!!"
        if indicator == 0: # backward
            for j in range(0, steps):
                _past = self.gettimeline().pop() # gets last move
                self.getfuture().append(_past) # past is the new future
                self.setcurrplayer()
                for i in _past[2:]: # resurrects the "dead pawns"
                    self.getcoordinates(i[0]).append((i[1], i[2]))
                self.move(_past[1], _past[0])
                self.setboardvalues()
        else:
            for j in range(0, steps):
                _future = self.getfuture().pop() # gets last move
                self.gettimeline().append(_future)
                self.move(_future[0], _future[1])
                for i in _future[2:]: # kills the "dead pawns"
                    self.getcoordinates(i[0]).remove((i[1], i[2]))
                self.setboardvalues()
                self.setcurrplayer()
                       
    def gettimeline(self):
        "returns the list to travel in past"
        return self._listpast

    def timerecord(self, pos, pos_new):
        "set every succesfull turn into list_past"
        self.gettimeline().append([pos, pos_new])

    def gameover(self, player):
        "ends the game and increases the playerpoints of the winner"
        self.clearscreen()
        self.incpp(player) # increases pp
        self.frame.gameover(self.getnames(player), self.getnames(0),\
        self.getnames(1), self.getpp(0), self.getpp(1)) # gives values to self.frame
        print(self.frame)
        while True:
            x = input("\nChoose if you want to play a new game: ")
            if x.upper() == "RESTART":
                self.clearscreen()
                self.frame.main()
                print(self.frame)
                self.chooselevel()
                break
            elif x.upper() == "QUIT":
                break
            else:
                self.clearscreen()
                print(self.frame)
                print(self._INVALID_INPUT)

    def getrace(self, player):
        if player == 0:
            return self._p0_race
        else:
            return self._p1_race

