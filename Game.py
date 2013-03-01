import AIClass
import silly

def dropMarker(board, x):
		temp = highestY(board,x)
		board[x][temp] = "o"
		return temp
def highestY(board, x):
	i = 5
	while(board[x][i] != "_" and i >= 0):
		i -= 1
	return i
def checkWin(board):
	checkResult = None
	for column in range (6):
		for row in range(5):
			if board[column][row] != '_':
				checkResult = pieceCheck(board,board[column][row], 'up',column,row)
				if checkResult != None:
					return checkResult
				checkResult = pieceCheck(board,board[column][row],'upRight',column,row)
				if checkResult != None:
					return checkResult
				checkResult = pieceCheck(board,board[column][row],'right',column,row)
				if checkResult != None:
					return checkResult
				checkResult = pieceCheck(board,board[column][row],'downRight',column,row)
				if checkResult != None:
					return checkResult
				checkResult = pieceCheck(board,board[column][row],'down',column,row)
				if checkResult != None:
					return checkResult
				checkResult = pieceCheck(board,board[column][row],'downLeft',column,row)
				if checkResult != None:
					return checkResult
				checkResult = pieceCheck(board,board[column][row],'left',column,row)
				if checkResult != None:
					return checkResult
				checkResult = pieceCheck(board,board[column][row],'upLeft',column,row)
				if checkResult != None:
					return checkResult
	return checkResult
				
def pieceCheck(board, piece, direction,x,y):
	xMod = 0
	yMod = 0
	distance = 1
	checked = False
	winnerFound = False
	winner = None
	if piece == 'x':
		candidate = ai.AIname
	elif piece == 'o':
		candidate = "You"
	if direction == 'up':
		yMod = -1
	elif direction == 'upRight':
		yMod = -1
		xMod = 1
	elif direction == 'right':
		xMod = 1
	elif direction == 'downRight':
		yMod = 1
		xMod = 1
	elif direction == 'down':
		yMod = 1
	elif direction == 'downLeft':
		yMod = 1
		xMod = -1
	elif direction == 'left':
		xMod = -1
	elif direction == 'upLeft':
		yMod = -1
		xMod = -1
	while not checked:
		if direction == 'up':
			if x+(xMod*distance) < 0:
				checked = True
		elif direction == 'upLeft':
			if x+(xMod*distance) < 0:
				checked = True
			if y+(yMod*distance) < 0:
				checked = True
		elif direction == 'upRight':
			if x+(xMod*distance) < 0:
				checked = True
			if y+(yMod*distance) > 5:
				checked = True
		elif direction == 'right':
			if x+(xMod*distance) > 6:
				checked = True		
		elif direction == 'downRight':
			if x+(xMod*distance) > 6:
				checked = True
			if y+(yMod*distance) > 5:
				checked = True
		elif direction == 'left':
			if x+(xMod*distance) < 0:
				checked = True
		elif direction == 'downLeft':
			if y+(yMod*distance) > 5:
				checked = True
			if x+(xMod*distance) < 0:
				checked = True
		elif direction == 'down':
			if y+(yMod*distance) > 5:
				checked = True
		if board[y+(yMod*distance)][x+(xMod*distance)] != piece:
			checked = True
		elif board[y+(yMod*distance)][x+(xMod*distance)] == piece:
			distance+=1
			if distance == 4:
				winnerFound = True
				checked = True
	if winnerFound == True:
		if piece == 'x':
			winner = 'computer'
		elif piece == 'o':
			winner = 'player'
	return winner
		
ai = silly.sampleAI("Bill","x")
b = [["_","_","_","_","_","_"],["_","_","_","_","_","_"],["_","_","_","_","_","_"],["_","_","_","_","_","_"],["_","_","_","_","_","_",],["_","_","_","_","_","_"],["_","_","_","_","_","_"]]
print "Play Connect 4"

won = False
ai.printBoard(b)
while not won:
	print "Player, Please make a move"
	validInput = False
	while not validInput:
		tempInputt = raw_input()
		try:
			inputt = int(tempInputt)
			if (inputt <= 6):
				validInput = True
			elif (inputt > 6):
				print "That column is not in the board, please enter a number between 0 and 6."
		except:
			print "Invalid input, please enter a number between 0 and 6."
		else:
			if len(tempInputt) != 1:
				print "please enter only 1 digit."
	dropMarker(b, inputt)
	ai.printBoard(b)
	candidate = checkWin(b)
	if candidate != None:
		won = True
		if candidate == 'computer':
			print ai.AIname + " has won! Better luck next time."
		elif candidate == 'player':
			print "Congratulations! you have beaten " + ai.AIname + " in Connect 4."
	print "Computer, Make a move"
	ai.makeMove(b)
	ai.printBoard(b)
	candidate = checkWin(b)
	if candidate != None:
		won = True
		if candidate == 'computer':
			print ai.AIname + " has won! Better luck next time."
		elif candidate == 'player':
			print "Congratulations! you have beaten " + ai.AIname + " in Connect 4."