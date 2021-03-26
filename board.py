#from coloroma import init
import os
import time

class Board:
	def __init__(self):
		self.board=[[] for i in range(0,40)]
		for i in range(0,40):
			for j in range(0,2000):
				self.board[i].append(' ')

		for i in range(1,3):
			for j in range(0,2000):
				self.board[i][j]='-'

		for i in range(38,40):
			for j in range(0,2000):
				self.board[i][j]='-'

		for i in range(1,3):
			for j in range(1850,1000):
				self.board[i][j]='*'

		for i in range(38,40):
			for j in range(1850,1000):
				self.board[i][j]='*'		

		self.__dragon=[]		

	def finalboard(self):
		for i in range(1,3):
			for j in range(0,1000):
				self.board[i][j]='*'

		for i in range(38,40):
			for j in range(0,1000):
				self.board[i][j]='*'		

	# def create_dragon(self,x,y):
	# 	with open("./scenes/boss.txt") as obj:
	# 		for line in obj:
	# 			strings=line.split()
	# 			self.__dragon.append(strings)		
	# 	f=y	
	# 	print(len(self.__dragon))
	# 	for i in range(len(self.__dragon)):
	# 		for j in range(len(self.__dragon[i])):
	# 			# try:
	# 			self.board[x][y] = self.__dragon[i][j]
	# 			# except:
	# 			# 	pass
	# 			y+=1
	# 		y=f	
	# 		x+=1


	# def print_board(self):
	# 	i=40;
	# 	j=100;
	# 	cnt=0;
	# 	while True:
	# 		print("\033[0;0H")	
	# 		hero.display_din()
	# 		for i in range(0,40):
	# 			for j in range(cnt,100+cnt):
	# 				print(self.board[i][j], end='')
	# 			print()	
	# 		time.sleep(0.2)	 	
	# 		cnt+=1		


main_board=Board()								
			
#os.system('clear')
# main_board.print_board()

