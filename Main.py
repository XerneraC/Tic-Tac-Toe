import random

class ttt:
	def __init__(self):
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
			self.doRandomX()
			print()

			if self.whoWon() != "-":
				break

			self.printGame()
			self.doRandomO()
			print()
		if self.winner != "N":
			print("Yay! " + self.winner + " won!")
		else:
			print("It's a draw!\n\n")
		self.printGame()

test = ttt()
test.bvb()
