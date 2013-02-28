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

ai = silly.sampleAI("bill","x")
b = [["_","_","_","_","_","_"],["_","_","_","_","_","_"],["_","_","_","_","_","_"],["_","_","_","_","_","_"],["_","_","_","_","_","_",],["_","_","_","_","_","_"],["_","_","_","_","_","_"]]
print "Play Connect 4"

won = False
ai.printBoard(b)
while not won:
	print "Player, Please make a move"
	valid = False
	while not valid:
		tempInputt = raw_input()
		try:
			inputt = int(tempInputt)
			if (inputt <= 6):
				valid = True
			elif (inputt > 6):
				print "That column is not in the board, please enter a number between 0 and 6."
		except:
			print "Invalid input, please enter a number between 0 and 6."
		else:
			if len(tempInputt) != 1:
				print "please enter only 1 digit."
	dropMarker(b, inputt)
	ai.printBoard(b)
	print "Computer, Make a move"
	ai.makeMove(b)
	ai.printBoard(b)