import os
from board import main_board
import time
from colorama import Fore,Style
# from background import cnt

accl=0
cntglobal=0
dragoncnt=0

def print_last_lose():
	for i in range(0,40):
		for j in range(800,990):
			main_board.board[i][j]=' '

	with open("ascii_texts/gameover.txt") as myfile:
		lines = myfile.readlines()
		for i in range(15,15+len(lines)):
		    for j in range(900,900+len(lines[i-15])):
		        if lines[i-15][j-900] == '\t' or lines[i-15][j-900]=='\n':
		            main_board.board[i][j]=' '
		        else :
		            main_board.board[i][j]=lines[i-15][j-900]		
	
	print("\033[0;0H")

	for i in range(0,40):
		for j in range(840,990):
			print(Fore.RED+Style.BRIGHT+main_board.board[i][j],end='')
		print()   

def print_last_win():
	for i in range(0,40):
		for j in range(800,990):
			main_board.board[i][j]=' '

	with open("ascii_texts/winner.txt") as myfile:
		lines = myfile.readlines()
		for i in range(15,15+len(lines)):
		    for j in range(880,880+len(lines[i-15])):
		        if lines[i-15][j-880] == '\t' or lines[i-15][j-880]=='\n':
		            main_board.board[i][j]=' '
		        else :
		            main_board.board[i][j]=lines[i-15][j-880]		
	
	print("\033[0;0H")

	for i in range(0,40):
		for j in range(840,990):
			print(Fore.GREEN+Style.BRIGHT+main_board.board[i][j],end='')
		print()   		

class Person:
	def __init__(self,xpos,ypos):
		self._xpos=xpos
		self._ypos=ypos
	# @xpos.setter
	# def xpos(self,x):
	# 	self._xpos=x

	# @ypos.setter
	# def ypos(self,y):
	# 	self._ypos=y					

class din(Person):

	global userflag
	def __init__(self):
		super().__init__(35,20)
		self.__score=0
		self.__life=4
		self.__boost=0
		self.__shield=0
		self.__userdragon=0

	def display_din(self,cnt):

		global dragoncnt
		x=self.__life
		flag=0
		dragonflag=0
		flagbooster=0
		if hero.userdragon==0:
			for i in range(0,3):
				for j in range(-2,1):
					if main_board.board[self._xpos+i][self._ypos+j]=='$':
						self.__score+=1
					if main_board.board[self._xpos+i][self._ypos+j]=='_' or main_board.board[self._xpos+i][self._ypos+j]=='|' or main_board.board[self._xpos+i][self._ypos+j]=='/':
						flag=1
						self._xpos=35	
					if main_board.board[self._xpos+i][self._ypos+j]=='B':
						flagbooster=1
		else:
			if dragoncnt%4==0:
				with open("ascii_texts/1.txt") as myfile:
						lines = myfile.readlines()
						for i in range(len(lines)):
							for j in range(len(lines[i])):
								if main_board.board[self._xpos+i][self._ypos+j]=='$':
									self.__score+=1
								if main_board.board[self._xpos+i][self._ypos+j]=='_' or main_board.board[self._xpos+i][self._ypos+j]=='|' or main_board.board[self._xpos+i][self._ypos+j]=='/':
									dragonflag=1
									self._xpos=30	
								if main_board.board[self._xpos+i][self._ypos+j]=='B':
									flagbooster=1
			elif dragoncnt%4==1:
				with open("ascii_texts/2.txt") as myfile:
						lines = myfile.readlines()
						for i in range(len(lines)):
							for j in range(len(lines[i])):
								if main_board.board[self._xpos+i][self._ypos+j]=='$':
									self.__score+=1
								if main_board.board[self._xpos+i][self._ypos+j]=='_' or main_board.board[self._xpos+i][self._ypos+j]=='|' or main_board.board[self._xpos+i][self._ypos+j]=='/':
									dragonflag=1
									self._xpos=30	
								if main_board.board[self._xpos+i][self._ypos+j]=='B':
									flagbooster=1
			elif dragoncnt%4==2:
				with open("ascii_texts/3.txt") as myfile:
						lines = myfile.readlines()
						for i in range(len(lines)):
							for j in range(len(lines[i])):
								if main_board.board[self._xpos+i][self._ypos+j]=='$':
									self.__score+=1
								if main_board.board[self._xpos+i][self._ypos+j]=='_' or main_board.board[self._xpos+i][self._ypos+j]=='|' or main_board.board[self._xpos+i][self._ypos+j]=='/':
									dragonflag=1
									self._xpos=30	
								if main_board.board[self._xpos+i][self._ypos+j]=='B':
									flagbooster=1
			elif dragoncnt%4==3:
				with open("ascii_texts/2.txt") as myfile:
						lines = myfile.readlines()
						for i in range(len(lines)):
							for j in range(len(lines[i])):
								if main_board.board[self._xpos+i][self._ypos+j]=='$':
									self.__score+=1
								if main_board.board[self._xpos+i][self._ypos+j]=='_' or main_board.board[self._xpos+i][self._ypos+j]=='|' or main_board.board[self._xpos+i][self._ypos+j]=='/' or main_board.board[self._xpos+i][self._ypos+j]=='<':
									dragonflag=1
									self._xpos=30	
								if main_board.board[self._xpos+i][self._ypos+j]=='B':
									flagbooster=1																		
							

		if flag==1:
			if self.return_shield==0:
				self.__life-=1	
			# else:
			# 	self.disable_shield()			
		
		if dragonflag==1:
			hero.userdragon=0		

		if flagbooster==1 and hero.userdragon==0:
			self.enable_boost()

		# if x-self.__life==1:
		# 	self.__life+=1

		if self.__life==-1:
			os.system('clear')
			print_last_lose()
			quit()			
		# if x-self.__life==1:
			# print("yoyo",end='')
			# time.sleep(0.5)	
		# if self.return_shield==1:		
		# 	for j in range(3):
		# 		main_board.board[self._xpos-1][self._ypos-j]='-'
		# 	for j in range(3):	
		# 		main_board.board[self._xpos+j][self._ypos+1]='|'
		# 	for j in range(3):	
		# 		main_board.board[self._xpos+j][self._ypos-3]='|'	

		for j in range(cnt+17,cnt+21):
			main_board.board[0][j]=' '

		if self.return_shield==1:
			main_board.board[0][cnt+21]="Shield Activated!"
		else: 	
			main_board.board[0][cnt+21]="Shield Deactivated!"

		main_board.board[0][cnt+22]=' '	
		main_board.board[0][cnt+23]=' '	
		main_board.board[0][cnt+25]=' '	

		if self.return_boost==1:
			main_board.board[0][cnt+24]="Boost Activated!"
		else:		
			main_board.board[0][cnt+24]="Boost Deactivated!"

		

		for j in range(cnt+28,cnt+98):
			main_board.board[0][j]=' '

		if self.__userdragon==0:
			main_board.board[self._xpos][self._ypos]='o'
			main_board.board[self._xpos][self._ypos-1]=' '
			main_board.board[self._xpos][self._ypos-2]='o'
			main_board.board[self._xpos+1][self._ypos]=' '
			main_board.board[self._xpos+1][self._ypos-1]='|'
			main_board.board[self._xpos+1][self._ypos-2]=' '
			main_board.board[self._xpos+2][self._ypos]='\\'
			main_board.board[self._xpos+2][self._ypos-1]=' '
			main_board.board[self._xpos+2][self._ypos-2]='/'
		else:
			dragoncnt+=1
			if dragoncnt%4==0:
				with open("ascii_texts/1.txt") as myfile:
					lines = myfile.readlines()
					for i in range(len(lines)):
						for j in range(len(lines[i])):
							main_board.board[hero.xpos+i][hero.ypos+j]=' '

					for i in range(len(lines)):
						for j in range(len(lines[i])):
							if lines[i][j] == '\t' or lines[i][j]=='\n':
								main_board.board[hero.xpos+i][hero.ypos+j]=' '
							else:
								main_board.board[hero.xpos+i][hero.ypos+j]=lines[i][j]			
			elif dragoncnt%4==1:
				with open("ascii_texts/2.txt") as myfile:
					lines = myfile.readlines()
					for i in range(len(lines)):
						for j in range(len(lines[i])):
							main_board.board[hero.xpos+i][hero.ypos+j]=' '

					for i in range(len(lines)):
						for j in range(len(lines[i])):
							if lines[i][j] == '\t' or lines[i][j]=='\n':
								main_board.board[hero.xpos+i][hero.ypos+j]=' '
							else:
								main_board.board[hero.xpos+i][hero.ypos+j]=lines[i][j]	
			elif dragoncnt%4==2:
				with open("ascii_texts/3.txt") as myfile:
					lines = myfile.readlines()
					for i in range(len(lines)):
						for j in range(len(lines[i])):
							main_board.board[hero.xpos+i][hero.ypos+j]=' '

					for i in range(len(lines)):
						for j in range(len(lines[i])):
							if lines[i][j] == '\t' or lines[i][j]=='\n':
								main_board.board[hero.xpos+i][hero.ypos+j]=' '
							else:
								main_board.board[hero.xpos+i][hero.ypos+j]=lines[i][j]															
			elif dragoncnt%4==3:
				with open("ascii_texts/2.txt") as myfile:
					lines = myfile.readlines()
					for i in range(len(lines)):
						for j in range(len(lines[i])):
							main_board.board[hero.xpos+i][hero.ypos+j]=' '

					for i in range(len(lines)):
						for j in range(len(lines[i])):
							if lines[i][j] == '\t' or lines[i][j]=='\n':
								main_board.board[hero.xpos+i][hero.ypos+j]=' '
							else:
								main_board.board[hero.xpos+i][hero.ypos+j]=lines[i][j]								
	
	def move_fwd(self,cnt):
		if self._ypos<cnt+97:
			# for j in range(3):
			# 	if main_board.board[self._xpos+j][self._ypos]=='$':
			# 		self.__score+=1
			if self.return_boost==0:
				self._ypos+=3	
			else: 
				self._ypos+=5	

	def move_up(self,cnt):
		global accl
		if self._xpos>5:
			# for j in range(3):
			# 	if main_board.board[self._xpos-1][self._ypos-j+1]=='$':
			# 		self.__score+=1
			if self.return_boost==0:
				self._xpos-=1
				if cnt<1850:
					self._ypos+=1
			else:
				self._xpos-=2	
				if cnt<1850:
					self._ypos+=1	
			accl=0

	def move_bwd(self):
		if self._ypos>5:
			self._ypos-=3

	def move_down(self):
		global accl
		if self._xpos<=34:
			# for j in range(3):
			# 	if main_board.board[self._xpos+3][self._ypos-j]=='$':
			# 		self.__score+=1
			if cntglobal%2==0:
				accl+=1
			prev=self._xpos	
			self._xpos+=int((accl*accl)/4)
			self._ypos+=1
			if self.__userdragon==0:
				if self._xpos>35:
					self._xpos=35
			else:		
				if self._xpos>30:
					self._xpos=30

			flagbooster=0		
			flagobs=0
			for i in range(prev,self._xpos+1):
				for j in range(self._ypos-2,self._ypos+1):
					if main_board.board[i][j]=='$':
						main_board.board[i][j]=' '
						self.__score+=1	
					if main_board.board[i][j]=='B':
						flagbooster=1
					if main_board.board[i][j]=='_' and main_board.board[i][j]=='/' and d.board[i][j]=='|':
						flagobs=1	
						self._xpos=35	

			if flagbooster==1 and hero.userdragon==0:
				self.enable_boost()		

			if flagobs==1:
				if self.return_shield==0:
					self.__life-=1			

	def enable_boost(self):
		self.__boost=1	

	def disable_boost(self):
		self.__boost=0		

	@property	
	def return_boost(self):
		return self.__boost	

	def enable_shield(self):
		self.__shield=1	

	def disable_shield(self):
		self.__shield=0		

	@property	
	def return_shield(self):
		return self.__shield	

	@property	
	def xpos(self):
		return self._xpos		

	@property	
	def ypos(self):
		return self._ypos	

	@xpos.setter
	def xpos(self,x):
		self._xpos=x

	@ypos.setter
	def ypos(self,y):
		self._ypos=y	

	@property
	def userdragon(self):
		return self.__userdragon

	@userdragon.setter
	def userdragon(self,x):
		self.__userdragon=x
					

	def hide_din(self,var):	
		if self.__userdragon==0:		
			main_board.board[self._xpos][self._ypos]=' '
			main_board.board[self._xpos][self._ypos-1]=' '
			main_board.board[self._xpos][self._ypos-2]=' '
			main_board.board[self._xpos+1][self._ypos]=' '
			main_board.board[self._xpos+1][self._ypos-1]=' '
			main_board.board[self._xpos+1][self._ypos-2]=' '
			main_board.board[self._xpos+2][self._ypos]=' '
			main_board.board[self._xpos+2][self._ypos-1]=' '
			main_board.board[self._xpos+2][self._ypos-2]=' '
		else:	
			global dragoncnt
			if dragoncnt%4==0:
				with open("ascii_texts/1.txt") as myfile:
					lines = myfile.readlines()
					for i in range(len(lines)):
						for j in range(len(lines[i])):
							main_board.board[hero.xpos+i][hero.ypos+j]=' '
			elif dragoncnt%4==1:
				with open("ascii_texts/2.txt") as myfile:
					lines = myfile.readlines()
					for i in range(len(lines)):
						for j in range(len(lines[i])):
							main_board.board[hero.xpos+i][hero.ypos+j]=' '
			elif dragoncnt%4==2:
				with open("ascii_texts/3.txt") as myfile:
					lines = myfile.readlines()
					for i in range(len(lines)):
						for j in range(len(lines[i])):
							main_board.board[hero.xpos+i][hero.ypos+j]=' '
			elif dragoncnt%4==3:
				with open("ascii_texts/2.txt") as myfile:
					lines = myfile.readlines()
					for i in range(len(lines)):
						for j in range(len(lines[i])):
							main_board.board[hero.xpos+i][hero.ypos+j]=' '												

		# if var==1:
		# 	for j in range(3):
		# 			main_board.board[self._xpos-1][self._ypos-j]=' '
		# 	for j in range(3):	
		# 		main_board.board[self._xpos+j][self._ypos+1]=' '
		# 	for j in range(3):	
		# 		main_board.board[self._xpos+j][self._ypos-3]=' '

	def move_with_board(self):
		self._ypos+=3;	

	def show_score(self,cnt):
		main_board.board[0][cnt]='S'	
		main_board.board[0][cnt+1]='c'	
		main_board.board[0][cnt+2]='o'	
		main_board.board[0][cnt+3]='r'	
		main_board.board[0][cnt+4]='e'	
		main_board.board[0][cnt+5]=':'
		# c=str(self.score)
		# l=len(c)
		main_board.board[0][cnt+6]=str(self.__score)
		main_board.board[0][cnt+7]=' '
		main_board.board[0][cnt+8]=' '

	def show_life(self,cnt):
		main_board.board[0][cnt+9]=' '	
		main_board.board[0][cnt+10]=' '	
		main_board.board[0][cnt+11]='L'	
		main_board.board[0][cnt+12]='i'	
		main_board.board[0][cnt+13]='f'	
		main_board.board[0][cnt+14]='e'		
		main_board.board[0][cnt+15]=':'		
		main_board.board[0][cnt+16]=str(self.__life)

	def magnet_effect_bwd(self,cnt):
		if self._ypos>cnt+4:
			self._ypos-=1	

	def magnet_effect_fwd(self,cnt):
		if self._ypos<cnt+95:
			self._ypos+=2	

	def magnet_effect_up(self,cnt):
		if self._ypos>5:
			self._xpos-=1

	def magnet_effect_down(self,cnt):
		if self._ypos<=34:
			self._xpos+=1	

	# def show_dragon(self,cnt):		

	# 	with open("ascii_texts/1.txt") as myfile:
	# 		lines = myfile.readlines()
	# 		for i in range(len(lines)):
	# 			for j in range(len(lines[i])):
	# 				main_board.board[hero.xpos+i][hero.ypos+j]=' '

	# 		for i in range(len(lines)):
	# 		    for j in range(len(lines[i])):
	# 		        if lines[i][j] == '\t' or lines[i][j]=='\n':
	# 		            main_board.board[hero.xpos+i][hero.ypos+j]=' '
	# 		        else :
	# 		            main_board.board[hero.xpos+i][hero.ypos+j]=lines[i][j]		
		
		# print("\033[0;0H")

		# for i in range(len(lines)):
		# 	for j in range(len(lines[i])):
		# 		print(main_board.board[hero.xpos+i][hero.ypos+j],end='')
		# 	print()   							
	  	

hero=din()	

class Bosss(Person):
	def __init__(self):
		# self._x=xpo
		# self._y=ypo
		super().__init__(30,1980)
		self.__life=30

	def show_boss(self,cnt):
		# print(self.y)
		# print(self.x)
		main_board.board[self._xpos][self._ypos]=' '
		main_board.board[self._xpos][self._ypos-1]='\\'
		main_board.board[self._xpos][self._ypos-2]='/'
		main_board.board[self._xpos][self._ypos-3]='_'
		main_board.board[self._xpos+1][self._ypos]=' '
		main_board.board[self._xpos+1][self._ypos-1]='|'
		main_board.board[self._xpos+1][self._ypos-2]=' '
		main_board.board[self._xpos+1][self._ypos-3]='_'
		main_board.board[self._xpos+2][self._ypos]=' '
		main_board.board[self._xpos+2][self._ypos-1]='/'
		main_board.board[self._xpos+2][self._ypos-2]='\\'
		main_board.board[self._xpos+2][self._ypos-3]=' '
		main_board.board[self._xpos+3][self._ypos]=' '
		main_board.board[self._xpos+3][self._ypos-1]='|'
		main_board.board[self._xpos+3][self._ypos-2]='|'
		main_board.board[self._xpos+3][self._ypos-3]=' '

		main_board.board[0][cnt+26]="Boss_Lives_Remaining:"
		main_board.board[0][cnt+27]=str(self.__life)

	def hide_boss(self):			
		main_board.board[self._xpos][self._ypos]=' '
		main_board.board[self._xpos][self._ypos-1]=' '
		main_board.board[self._xpos][self._ypos-2]=' '
		main_board.board[self._xpos][self._ypos-3]=' '
		main_board.board[self._xpos+1][self._ypos]=' '
		main_board.board[self._xpos+1][self._ypos-1]=' '
		main_board.board[self._xpos+1][self._ypos-2]=' '
		main_board.board[self._xpos+1][self._ypos-3]=' '
		main_board.board[self._xpos+2][self._ypos]=' '
		main_board.board[self._xpos+2][self._ypos-1]=' '
		main_board.board[self._xpos+2][self._ypos-2]=' '
		main_board.board[self._xpos+2][self._ypos-3]=' '
		main_board.board[self._xpos+3][self._ypos]=' '
		main_board.board[self._xpos+3][self._ypos-1]=' '
		main_board.board[self._xpos+3][self._ypos-2]=' '
		main_board.board[self._xpos+3][self._ypos-3]=' '

	def move_boss(self):
		xp=hero.xpos		
		self._xpos=xp-1
		# print(self.x)

	@property	
	def xpos(self):
		return self._xpos

	@property	
	def ypos(self):
		return self._ypos

	# def return_ypos(self):
	# 	return self.y		

	def dec_life(self):
		self.__life-=1	
		if self.__life==-1:
			os.system('clear')
			print_last_win()
			quit()
	
boss=Bosss()

