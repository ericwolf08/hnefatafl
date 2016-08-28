© by Eric Wolf, Sebastian Hamann

Installation of the Module.
	make sure the folder /level/ is in the same path like the module or you won't be able to play any game
	you can create your own games look at the bottom.

on Windows:
	make sure you have the module on a hard drive
	and python installed

Start the Game.
	start main.py in IDLE (or cmd on winows)
	start main.py with double-klick

How to use the program.
	at any given time, the game will most likely tell you what you can do and what is allowed
	you have to confirm all your actions with enter
	you can exit the program everytime with [quit]
	first you have to choose the game you want to play, see list above input
	if you choose to play a game you will be asked for each player if he's a human oder computer player
	in case of computerenemies, the names are set in config
	if you enter your name, there has to be at least 1 letter
	name "quit" is not possible. check above
	coordinates must be of the format e.g. "A3 B3"
		first the old position with the column than the row
		than the new position with the row than the column
	player1 is always the attacker 
	player2 is always the defender (with the king)
	if its the turn of the computerplayer you have to confirm his turn with [ENTER]
	you can see his move before confirm him
	while ingame you can always go back to choosing the level with the command [break]
	if you choose to give up, you can do so by typing [continue]
		in this case you will get asked again what level do you want to play, however, the player names and points will get saved
	after the game is finished you can restart it, with typing [restart]
		just like when choosing [continue] player names and points are saved so you can easily restart a match

Rules.
	the attacker begins the game
	you must move in every turn
	you can move horizontal or vertical unlimited
	you can't jump over other pawns
	you can't move diagonal
	your move can only land on a free field
	entering a field with value (x) is only allowed for the king
	other pawns have to move over it

Optional Rules.
	Rules can easily be changed by going to the options menu and pressing the number of the rule you want to change

	Rule 1: King has to get to the corners/edge (corners is automatically activated)
		If the King gets to the edge/corners the game ends
		If he moves between to enemy pawns and Rule 2 is set to 2 pawns however, the king will get captured

	Rule 2: King gets caught by 2/4 pawns (2 is automatically activated)
		Game ends if king gets caught
		2: King gets caught horinzontal or vertical
		4: King gets caught only if he is surrounded vertical AND horizontal

	Rule 3: Pawns get removed/blocked (removed is automatically activated)
		blocked: pawns get blocked if they are surrounded vertical OR horizontal
		blocked: blocked pawns can block other pawns/king
		for more details about block/kill, check below

	Rule 4: Changes the search method of KI into depth/bredth
	
Pawn gets killed/blocked.
	if you stand between to pawns of the enemy
	kills are only horizontal or vertical possible, they get automatically removed or if chosen blocked
	king gets killed/blocked like every other pawn
	the throne and the corners count as players from the defender
	you dont have to kick on every opportunity
	you can move through two enemies with no impact
	the last moved pawn kills first
	throne and corners are signed with [x]

forward/backward n.
	the backward feature is available after your first turn
	if you type "backward n" the game will take you back exactly n turns into the "past",
	you can go back till the beginning of the game
	if you are in the "past" you can type "forward n" to get back n turns into the "future"
	if you are in the past and make a valid move, you can't go back into the "future", 
	because you created a new one (look up time travel paradox)


Have fun.
Sebastian & Eric


Create your own game.
	File has to have the following syntax:
	boardsize over 26 is not recommended

	# size of the board 	 <int>
	SIZE := 7
	# value for empty field 	 <char>
	EMPTY := "-"

	# writes the X-fields to the mid and the corners
	# <char>@[(<int>,<int>),(<int>,<int>),...,(<int>,<int>)]
	DECORATE := "X"@[(3,3),(0,0),(0,6),(6,0),(6,6)]

	# the attacker without king
	PLAYER_0 := "O"@[(3,0),(3,1),(3,5),(3,6),(0,3),(1,3),(5,3),(6,3)]

	# the defender with king
	PLAYER_1 := "#"@[(2,3),(3,2),(4,3),(3,4)]
	# king 	 <char>@(<int>,<int>)
	KING := "+"@(3,3)

	put the file in the foler /level/
	if file has the wrong syntax, game will give you an error message