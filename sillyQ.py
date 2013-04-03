import AIClass
import copy
import random

class sampleAI(AIClass.AI):
	prevBoard = ""
	def makeMove(self, board):
		winPositions = self.findWinSpots(board,'computer')
		riskPositions = self.findWinSpots(board,'player')
		for position in winPositions:
			if position [1] < 5:
				if board[position[0]][position[1]+1] == '_':
					if position [1] < 4:
						if board[position[0]][position[1]+2] != '_':
							winPositions.remove(position)
		for pos in riskPositions:
			if pos [1] < 5:
				if board[pos[0]][pos[1]+1] == '_':
					if pos [1] < 4:
						if board[pos[0]][pos[1]+2] != '_':
							riskPositions.remove(pos)
		if(self.prevBoard == ""):
			self.dropMarker(board,random.randint(0,6))
		else:
			lastMove = self.findLastMove(board)
			if(lastMove == 0 or lastMove == -1):
				self.dropMarker(board, 0)
			elif winPositions == [] and riskPositions == []:
				self.dropMarker(board, random.randint(0,6))
			elif winPositions != []:
				self.dropMarker(board, winPositions[0][0])
			else:
				self.dropMarker(board, riskPosition[0][0])
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
	def findWinSpots(self,board,player):
		checkResult = None
		riskSpots = []
		for column in range (6):
			for row in range(5):
				if board[column][row] == '_':
					checkResult = self.triSpots(board,player,'up',column,row)
					if checkResult != None:
						riskSpots.append(checkResult)
					checkResult = self.triSpots(board,player,'upRight',column,row)
					if checkResult != None:
						riskSpots.append(checkResult)
					checkResult = self.triSpots(board,player,'right',column,row)
					if checkResult != None:
						riskSpots.append(checkResult)
					checkResult = self.triSpots(board,player,'downRight',column,row)
					if checkResult != None:
						riskSpots.append(checkResult)
					checkResult = self.triSpots(board,player,'down',column,row)
					if checkResult != None:
						riskSpots.append(checkResult)
					checkResult = self.triSpots(board,player,'downLeft',column,row)
					if checkResult != None:
						riskSpots.append(checkResult)
					checkResult = self.triSpots(board,player,'left',column,row)
					if checkResult != None:
						riskSpots.append(checkResult)
					checkResult = self.triSpots(board,player,'upLeft',column,row)
					if checkResult != None:
						riskSpots.append(checkResult)
		return riskSpots	
	
	def triSpots(self,board,target,direction,x,y):
		xMod = 0
		yMod = 0
		distance = 1
		checked = False
		riskFound = False
		risk = None
		if target == 'player':
			piece = 'o'
		elif target == 'computer':
			piece = 'x'
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
			if y+(yMod*distance) < 0:
				checked = True
			if x+(xMod*distance) < 0:
				checked = True
			if x+(xMod*distance) > 6:
				checked = True
			if y+(yMod*distance) > 5:
				checked = True
			elif board[x+(xMod*distance)][y+(yMod*distance)] != piece:
				checked = True
			elif board[x+(xMod*distance)][y+(yMod*distance)] == piece:
				distance+=1
				if distance == 3:
					riskFound = True
					checked = True
		return (x,y)					