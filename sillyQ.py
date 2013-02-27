import AIClass
import copy
import random

class sampleAI(AIClass.AI):
	prevBoard = ""
	def makeMove(self, board):
		if(self.prevBoard == ""):
			self.dropMarker(board,random.randint(0,6))
		else:
			lastMove = self.findLastMove(board)
			if(lastMove == 0 or lastMove == -1):
				self.dropMarker(board, 0)
			else:
				self.dropMarker(board, random.randint(0,6))
		self.prevBoard = copy.deepcopy(board)
	def findLastMove(self, board):
		self.printBoard(board)
		self.printBoard(self.prevBoard)
		i = 0
		while(i<6):
			j = 0
			while(j<7):
				if(board[j][i] != self.prevBoard[j][i]):
					return j
				j += 1
			i += 1
		return -1
