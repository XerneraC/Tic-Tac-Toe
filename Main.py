import random
import numpy

class ttt:
	def __init__(self, botXDiff = 0.0, botODiff = 0.0):
		self.board = [
			["-", "-", "-"],
			["-", "-", "-"],
			["-", "-", "-"]
		]
		self.winner = "-"
		self.botXDiff = botXDiff
		self.botODiff = botODiff

	def reset(self):
		self.board = [
			["-", "-", "-"],
			["-", "-", "-"],
			["-", "-", "-"]
		]
		self.winner = "-"

	def xMove(self, x, y):
		if self.board[x - 1][y - 1] == "-":
			self.board[x - 1][y - 1] = "X"
			self.winner = self.whoWon()
		else:
			print("You can't overwrite your oponents move! Try again!\n")
			nx = int(input("The Row: "))
			ny = int(input("The Collum: "))
			print()

			nx = nx if (nx < 4) else 3
			nx = nx if (nx > 0) else 1

			ny = ny if (ny < 4) else 3
			ny = ny if (ny > 0) else 1

			self.xMove(nx, ny)

	def oMove(self, x, y):
		if self.board[x - 1][y - 1] == "-":
			self.board[x - 1][y - 1] = "O"
			self.winner = self.whoWon()
		else:
			print("You can't overwrite your oponents move! Try again!\n")
			nx = int(input("The Row: "))
			ny = int(input("The Collum: "))
			print()

			nx = nx if (nx < 4) else 3
			nx = nx if (nx > 0) else 1

			ny = ny if (ny < 4) else 3
			ny = ny if (ny > 0) else 1

			self.oMove(nx, ny)


	def printGame(self):
		string = str(self.board).replace("], [", "\n ")
		string = " " + string
		string = string.replace("[", "").replace("]", "").replace("'", "").replace(",", "")
		string = string.replace("X", "\033[35mX\033[0m")
		string = string.replace("O", "\033[94mO\033[0m")
		print(string)

	def whoWon(self):
		winner = "-"

		noEmpties = 0
		for row in self.board:
			noEmpties += row.count("-")

		if noEmpties == 0:
			winner = "N"

		if (self.board[0][0] == self.board[1][1] == self.board[2][2]) & (self.board[0][0] != "-"): winner = self.board[0][0]
		if (self.board[0][2] == self.board[1][1] == self.board[2][0]) & (self.board[0][2] != "-"): winner = self.board[0][2]

		if (self.board[0][0] == self.board[0][1] == self.board[0][2]) & (self.board[0][0] != "-"): winner = self.board[0][0]
		if (self.board[1][0] == self.board[1][1] == self.board[1][2]) & (self.board[1][0] != "-"): winner = self.board[1][0]
		if (self.board[2][0] == self.board[2][1] == self.board[2][2]) & (self.board[2][0] != "-"): winner = self.board[2][0]

		if (self.board[0][0] == self.board[1][0] == self.board[2][0]) & (self.board[0][0] != "-"): winner = self.board[0][0]
		if (self.board[0][1] == self.board[1][1] == self.board[2][1]) & (self.board[0][1] != "-"): winner = self.board[0][1]
		if (self.board[0][2] == self.board[1][2] == self.board[2][2]) & (self.board[0][2] != "-"): winner = self.board[0][2]

		return winner

	def check2InARow(self):
		possibleCoordinates = []

		if (self.board[0][0] == self.board[1][1] != self.board[2][2]) & (self.board[0][0] != "-") & (self.board[2][2] == "-"): possibleCoordinates.append([2, 2, self.board[0][0]])
		if (self.board[0][2] == self.board[1][1] != self.board[2][0]) & (self.board[0][2] != "-") & (self.board[2][0] == "-"): possibleCoordinates.append([2, 0, self.board[0][2]])

		if (self.board[0][0] == self.board[0][1] != self.board[0][2]) & (self.board[0][0] != "-") & (self.board[0][2] == "-"): possibleCoordinates.append([0, 2, self.board[0][0]])
		if (self.board[1][0] == self.board[1][1] != self.board[1][2]) & (self.board[1][0] != "-") & (self.board[1][2] == "-"): possibleCoordinates.append([1, 2, self.board[1][0]])
		if (self.board[2][0] == self.board[2][1] != self.board[2][2]) & (self.board[2][0] != "-") & (self.board[2][2] == "-"): possibleCoordinates.append([2, 2, self.board[2][0]])

		if (self.board[0][0] == self.board[1][0] != self.board[2][0]) & (self.board[0][0] != "-") & (self.board[2][0] == "-"): possibleCoordinates.append([2, 0, self.board[0][0]])
		if (self.board[0][1] == self.board[1][1] != self.board[2][1]) & (self.board[0][1] != "-") & (self.board[2][1] == "-"): possibleCoordinates.append([2, 1, self.board[0][1]])
		if (self.board[0][2] == self.board[1][2] != self.board[2][2]) & (self.board[0][2] != "-") & (self.board[2][2] == "-"): possibleCoordinates.append([2, 2, self.board[0][2]])


		if (self.board[0][0] != self.board[1][1] == self.board[2][2]) & (self.board[2][2] != "-") & (self.board[0][0] == "-"): possibleCoordinates.append([0, 0, self.board[2][2]])
		if (self.board[0][2] != self.board[1][1] == self.board[2][0]) & (self.board[2][0] != "-") & (self.board[0][2] == "-"): possibleCoordinates.append([0, 2, self.board[2][0]])

		if (self.board[0][0] != self.board[0][1] == self.board[0][2]) & (self.board[0][2] != "-") & (self.board[0][0] == "-"): possibleCoordinates.append([0, 0, self.board[0][2]])
		if (self.board[1][0] != self.board[1][1] == self.board[1][2]) & (self.board[1][2] != "-") & (self.board[1][0] == "-"): possibleCoordinates.append([1, 0, self.board[1][2]])
		if (self.board[2][0] != self.board[2][1] == self.board[2][2]) & (self.board[2][2] != "-") & (self.board[2][0] == "-"): possibleCoordinates.append([2, 0, self.board[2][2]])

		if (self.board[0][0] != self.board[1][0] == self.board[2][0]) & (self.board[2][0] != "-") & (self.board[0][0] == "-"): possibleCoordinates.append([0, 0, self.board[2][0]])
		if (self.board[0][1] != self.board[1][1] == self.board[2][1]) & (self.board[2][1] != "-") & (self.board[0][1] == "-"): possibleCoordinates.append([0, 1, self.board[2][1]])
		if (self.board[0][2] != self.board[1][2] == self.board[2][2]) & (self.board[2][2] != "-") & (self.board[0][2] == "-"): possibleCoordinates.append([0, 2, self.board[2][2]])


		if (self.board[1][1] != self.board[0][0] == self.board[2][2]) & (self.board[2][2] != "-") & (self.board[1][1] == "-"): possibleCoordinates.append([1, 1, self.board[2][2]])
		if (self.board[1][1] != self.board[0][2] == self.board[2][0]) & (self.board[2][0] != "-") & (self.board[1][1] == "-"): possibleCoordinates.append([1, 1, self.board[2][0]])

		if (self.board[0][1] != self.board[0][0] == self.board[0][2]) & (self.board[0][2] != "-") & (self.board[0][1] == "-"): possibleCoordinates.append([0, 1, self.board[0][2]])
		if (self.board[1][1] != self.board[1][0] == self.board[1][2]) & (self.board[1][2] != "-") & (self.board[1][1] == "-"): possibleCoordinates.append([1, 1, self.board[1][2]])
		if (self.board[2][1] != self.board[2][0] == self.board[2][2]) & (self.board[2][2] != "-") & (self.board[2][1] == "-"): possibleCoordinates.append([2, 1, self.board[2][2]])

		if (self.board[1][0] != self.board[0][0] == self.board[2][0]) & (self.board[2][0] != "-") & (self.board[1][0] == "-"): possibleCoordinates.append([1, 0, self.board[2][0]])
		if (self.board[1][1] != self.board[0][1] == self.board[2][1]) & (self.board[2][1] != "-") & (self.board[1][1] == "-"): possibleCoordinates.append([1, 1, self.board[2][1]])
		if (self.board[1][2] != self.board[0][2] == self.board[2][2]) & (self.board[2][2] != "-") & (self.board[1][2] == "-"): possibleCoordinates.append([1, 2, self.board[2][2]])

		return possibleCoordinates

	def doPlayerX(self):
		self.printGame()
		print("It's X's turn")
		x = int(input("The Row: "))
		y = int(input("The Collum: "))
		print()

		x = x if (x < 4) else 3
		x = x if (x > 0) else 1

		y = y if (y < 4) else 3
		y = y if (y > 0) else 1

		self.xMove(x, y)

	def doPlayerO(self):
		self.printGame()
		print("It's O's turn")
		x = int(input("The Row: "))
		y = int(input("The Collum: "))
		print()

		x = x if (x < 4) else 3
		x = x if (x > 0) else 1

		y = y if (y < 4) else 3
		y = y if (y > 0) else 1

		self.oMove(x, y)

	def doRandomX(self):
		possibleCoordinates = []
		for i in range(len(self.board)):
			for j in range(len(self.board[i])):
				if self.board[i][j] == "-":
					possibleCoordinates.append([i, j])
		coordinate = random.choice(possibleCoordinates)
		self.xMove(coordinate[0] + 1, coordinate[1] + 1)

	def doRandomO(self):
		possibleCoordinates = []
		for i in range(len(self.board)):
			for j in range(len(self.board[i])):
				if self.board[i][j] == "-":
					possibleCoordinates.append([i, j])
		coordinate = random.choice(possibleCoordinates)
		self.oMove(coordinate[0] + 1, coordinate[1] + 1)

	def doSimpleBotX(self):
		possibleWinningMovesX = []
		possibleWinningMovesO = []
		possibleCorners = []
		possibleSides = []

		possibleWinningMoves = self.check2InARow()
		for move in possibleWinningMoves:
			if move[2] == "X":
				possibleWinningMovesX.append(move)
			if move[2] == "O":
				possibleWinningMovesO.append(move)

		for corner in [0, 0], [0, 2], [2, 2], [2, 0]:
			if self.board[corner[0]][corner[1]] == "-":
				possibleCorners.append(corner)

		for side in [0, 1], [1, 2], [2, 1], [1, 0]:
			if self.board[side[0]][side[1]] == "-":
				possibleSides.append(side)


		if len(possibleWinningMovesX) != 0:
			move = random.choice(possibleWinningMovesX)
			self.xMove(move[0] + 1, move[1] + 1)

		elif len(possibleWinningMovesO) != 0:
			move = random.choice(possibleWinningMovesO)
			self.xMove(move[0] + 1, move[1] + 1)

		elif len(possibleCorners) != 0:
			move = random.choice(possibleCorners)
			self.xMove(move[0] + 1, move[1] + 1)

		elif self.board[1][1] == "-":
			self.xMove(2, 2)

		elif len(possibleSides) != 0:
			move = random.choice(possibleSides)
			self.xMove(move[0] + 1, move[1] + 1)

	def doSimpleBotO(self):
		possibleWinningMovesX = []
		possibleWinningMovesO = []
		possibleCorners = []
		possibleSides = []

		possibleWinningMoves = self.check2InARow()
		for move in possibleWinningMoves:
			if move[2] == "X":
				possibleWinningMovesX.append(move)
			if move[2] == "O":
				possibleWinningMovesO.append(move)

		for corner in [0, 0], [0, 2], [2, 2], [2, 0]:
			if self.board[corner[0]][corner[1]] == "-":
				possibleCorners.append(corner)

		for side in [0, 1], [1, 2], [2, 1], [1, 0]:
			if self.board[side[0]][side[1]] == "-":
				possibleSides.append(side)

		if len(possibleWinningMovesO) != 0:
			move = random.choice(possibleWinningMovesO)
			self.oMove(move[0] + 1, move[1] + 1)

		elif len(possibleWinningMovesX) != 0:
			move = random.choice(possibleWinningMovesX)
			self.oMove(move[0] + 1, move[1] + 1)
		
		elif len(possibleCorners) != 0:
			move = random.choice(possibleCorners)
			self.oMove(move[0] + 1, move[1] + 1)
		
		elif self.board[1][1] == "-":
			self.oMove(2, 2)

		elif len(possibleSides) != 0:
			move = random.choice(possibleSides)
			self.oMove(move[0] + 1, move[1] + 1)

	def doDumbX(self):
		possibleWinningMovesX = []
		possibleWinningMovesO = []

		possibleWinningMoves = self.check2InARow()
		for move in possibleWinningMoves:
			if move[2] == "X":
				possibleWinningMovesX.append(move)
			if move[2] == "O":
				possibleWinningMovesO.append(move)


		if len(possibleWinningMovesX) != 0:
			move = random.choice(possibleWinningMovesX)
			self.xMove(move[0] + 1, move[1] + 1)

		elif len(possibleWinningMovesO) != 0:
			move = random.choice(possibleWinningMovesO)
			self.xMove(move[0] + 1, move[1] + 1)

		else:
			self.doRandomX()

	def doDumbO(self):
		possibleWinningMovesX = []
		possibleWinningMovesO = []

		possibleWinningMoves = self.check2InARow()
		for move in possibleWinningMoves:
			if move[2] == "X":
				possibleWinningMovesX.append(move)
			if move[2] == "O":
				possibleWinningMovesO.append(move)


		if len(possibleWinningMovesO) != 0:
			move = random.choice(possibleWinningMovesO)
			self.oMove(move[0] + 1, move[1] + 1)

		elif len(possibleWinningMovesX) != 0:
			move = random.choice(possibleWinningMovesX)
			self.oMove(move[0] + 1, move[1] + 1)

		else:
			self.doRandomO()

	def aiMoveX(self):
		difficulty = self.botXDiff
		botDiffs = []
		wheights = []
		for lvl in range(3):
			botDiffs.append(lvl)
			wheights.append(2-abs(difficulty-float(lvl)) if (2-abs(difficulty-float(lvl)) > 0.0) else 0.0)
		bot = numpy.random.choice(botDiffs, 1, wheights)
		if bot == 0: self.doRandomX()
		if bot == 1: self.doDumbX()
		if bot == 2: self.doSimpleBotX()

	def aiMoveO(self):
		difficulty = self.botODiff
		botDiffs = []
		wheights = []
		for lvl in range(3):
			botDiffs.append(lvl)
			wheights.append(2-abs(difficulty-float(lvl)) if (2-abs(difficulty-float(lvl)) > 0.0) else 0.0)
		bot = numpy.random.choice(botDiffs, 1, wheights)
		if bot == 0: self.doRandomO()
		if bot == 1: self.doDumbO()
		if bot == 2: self.doSimpleBotO()
		


	def pvp(self):
		while self.winner == "-":
			self.doPlayerX()

			if self.whoWon() != "-":
				break

			self.doPlayerO()
		if self.winner != "N":
			print("Yay! " + self.winner + " won!")
		else:
			print("It's a draw!")
		print()
		self.printGame()

	def bvb(self):
		while self.winner == "-":
			self.printGame()
			self.aiMoveX()
			print()

			if self.whoWon() != "-":
				break

			self.printGame()
			self.aiMoveO()
			print()
		if self.winner != "N":
			print("Yay! " + self.winner + " won!")
		else:
			print("It's a draw!\n\n")
		self.printGame()

game = ttt(3.0,0.0)
game.bvb()
