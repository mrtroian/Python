import sys
import json

class Game():
	EMPTY = '_'
	X_S = 'X'
	O_S = 'O'
	DRAW_W = "It's a draw!"
	NOT_OVER = 'Game not over'

	def __init__(self):
		self.grid = self.init_grid()
		self.turn = 1
		self.last = str()
		self.WINNER = self.last + ' won!'
		self.players = dict()
		self.fn = str()

	def init_grid(self):
		return [[self.EMPTY for m in range(3)] for n in range(3)]

	def resume(self, data_id):
		try:
			with open(data_id, 'r') as fd:
				data = json.load(fd)
			self.players = data['players']
			self.grid = data['grid']
			self.last = data['last']
		except:
			pass

	def save(self, data_id):
		data = {'players': self.players, 'grid': self.grid, 'last': self.last}
		with open(data_id, 'w+') as fd:
			json.dump(data, fd)

	def init_file(self, player):
		self.fn = player
		open(player, 'w+')
		return

	def str_grid(self):
		s1 = list()
		for n in self.grid:
			for m in n:
				s1.append(m)
			s1.append('\n')
		return ''.join(s1)


	def print_grid(self):
		for n in self.grid:
			for m in n:
				print(m, end = '')
			print()

	def parse_grid(self):
		grid = list()
		with open(self.fn, 'r') as fd:
			grid = list(fd.read())
		i = 0
		for n in self.grid:
			for m in n:
				m = grid[i]
				i += 1

	def write_grid(self):
		with open(self.fn, 'w') as fd:
			fd.write(self.grid)

	def get_grid(self):
		str = list()
		for n in self.grid:
			for m in n:
				str.append(m)
			str.append('\n')
		return str

	def is_valid(self, x, y):
		return True if self.grid[x][y] is self.EMPTY else False

	def is_full(self):
		for m in self.grid:
			if self.EMPTY in set(m):
				return False
		return True

	def check_end(self, data):
		if len(data) is 1:
			if self.X_S in data or self.O_S in data:
				# self.over = True		
				# print('called check_end')
				# print(self.over)
				return True
		return False

	def check_winner(self, data):
		if len(data) is 1:
			if self.X_S or self.O_S in data:
				# self.over = True
				return self.WINNER
			# if self.O_S in data:
				# self.over = True
				# return self.WINNER
			return self.DRAW_W
		return 

	def eval(self, ai = False):
		grid = self.grid
		for m in grid:
			data = set(m)
			if self.check_end(data):
				return self.check_winner(data)
		for i in range(3):
			data = set(grid[k][i] for k in range(3))
			if self.check_end(data):
				return self.check_winner(data)
		data = set(grid[i][i] for i in range(3))
		if self.check_end(data):
			return self.check_winner(data)
		data = set(grid[i][2 - i] for i in range(3))
		if self.check_end(data):
			return self.check_winner(data)
		if self.is_full():
			return self.DRAW_W
		return self.NOT_OVER

	def undeclare(self, cell):
		x = cell // 3
		y = cell % 3
		grid[x][y] = self.EMPTY


	def declare(self, cell, player):
		x = cell // 3
		y = cell % 3
		if self.eval() is not self.NOT_OVER:
			return 'Game over'
		if not player in self.players.keys():
			if not 'X' in self.players.values():
				self.players[player] = 'X'
			elif not 'O' in self.players.values():
				self.players[player] = 'O'
			else:
				return 'This game is for two players only\nSorry'
		if cell < 0:
			return
		if self.last is self.players[player]:
			return 'Sorry, not your turn'
		if self.is_valid(x, y):
			self.grid[x][y] = self.players[player]
			self.last = player
			self.turn += 1
			return True
		return 'Sorry, it is a filled space'
