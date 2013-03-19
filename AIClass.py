class AI:
	def __init__(self, name, mark):
		self.AIname = name
		self.mark = mark
	def printBoard(self, board):
		i = 0
		while(i<6):
			temp = ""
			j = 0
			while(j<7):
				temp += board[j][i] + " "
				j += 1	
			print(temp)
			i += 1
		print ("0 1 2 3 4 5 6")
	def makeMove(self, board):
		result = self.dropMarker(board,0)
		return result
	def dropMarker(self, board, x):
		temp = self.highestY(board,x)
		board[x][temp] = self.mark
		return temp
	def highestY(self, board, x):
		i = 5
		while(board[x][i] != "_" and i >= 0):
			i -= 1
		return i
