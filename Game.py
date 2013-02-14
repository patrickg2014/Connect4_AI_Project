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

while(True):
	print "Player, Please make a move"
	inputt = int(raw_input())
	dropMarker(b, inputt)
	ai.printBoard(b)
	print "Computer, Make a move"
	ai.makeMove(b)
	ai.printBoard(b)