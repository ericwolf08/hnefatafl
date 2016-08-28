class Frame():
    """class for Frame in top half of the screen"""
    
    def __init__(self):
        "initialize an object with attributs of this class"
        self._top = ""
        self._mid_top = ""
        self._mid = ""
        self._mid_bot = ""
        self._bot = ""
        self.main()
        
    def __str__(self):
        "prints the out the frame"
        return "\n #####################PLEASE*SELECT###################### \
            \n ##                                                    ## \
            \n ## "+self._top.center(50)+" ## \
            \n ## "+self._mid_top.center(50)+" ## \
            \n ## "+self._mid.center(50)+" ## \
            \n ## "+self._mid_bot.center(50)+" ## \
            \n ## "+self._bot.center(50)+" ## \
            \n ##                                                    ## \
            \n ######################################################## \
            \n__________________________________________________________"
    
    def main(self):
        "sets attributes for the main menu"
        self._top = "Welcome to Hnefatafl & Co"
        self._mid_top = "Choose one of the levels below."
        self._mid = "Confirm with Enter"
        self._mid_bot = ""
        self._bot = "[QUIT]"
        self._gameover = False
        
    def menu(self):
        "sets attributes for the standard menu"
        self._top = "[P]LAY A GAME"
        self._mid_top = ""
        self._mid = "[O]ptions"
        self._mid_bot = ""
        self._bot = "[QUIT]"
        
    def options(self, rule1, rule2, rule3, rule4):
        "sets attributes for the options menu"
        self._top = "You can change the following:"        
        if rule1: # text in frame changes with values
            self._mid_top = " [1] King has to get to the corners."
        else:
            self._mid_top = " [1] King has to get to the edge."
        
        if rule2:
            self._mid = "[2] King gets caught by 2 pawns."
        else:
            self._mid = "[2] King gets caught by 4 pawns."
        
        if rule3:
            self._mid_bot = "[3] Pawns get removed."
        else:
            self._mid_bot = "[3] Pawns get blocked only."
            
        if rule4:
            self._bot = "[4] Breadth-first"
        else:
            self._bot = "[4] Depth-first"
            
    def ingame(self):
        "sets attributes for the ingame menu"
        self._top = "First type the column than the row"
        self._mid_top = "Example:  \"d1 c1\""
        self._mid = "Type \"backward n\" to go back n turns"
        self._mid_bot = "Type \"forward n\" to go forth n turns"
        self._bot = "[BREAK][QUIT][CONTINUE]"
        
    def gameover(self, winner, name0, name1, pp0, pp1):
        "sets attributes for the gameover menu"
        self._top = "Congratulations, " + winner + " you won!"
        self._mid_top = name0 + ":" + str(pp0)
        self._mid = name1 + ":" + str(pp1)
        self._mid_bot = "[RESTART]"
        self._bot = "[QUIT]"
        self._gameover = True

    def isgameover(self):
        return self._gameover
