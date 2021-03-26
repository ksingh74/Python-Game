from board import main_board
from mandalorin import hero,boss

mag_listy=[]
mag_listx=[]

class obstacles:
	def __init__(self,xpos,ypos):
		self._xpos=xpos
		self._ypos=ypos
		
	def show_obs(self):
		print("error:polymorphism error in obstacles class")

class firebeam_hor(obstacles):
	def show_obs(self):	
		main_board.board[self._xpos][self._ypos]='_'	
		main_board.board[self._xpos][self._ypos+1]='_'	
		main_board.board[self._xpos][self._ypos+2]='_'	
		main_board.board[self._xpos][self._ypos+3]='_'	
		main_board.board[self._xpos][self._ypos+4]='_'	
		main_board.board[self._xpos][self._ypos+5]='_'	

	@staticmethod	
	def remove_beam(x,y):
		for i in range(6):
			if main_board.board[x][y+i]=='_':
				main_board.board[x][y+i]=' '	

class firebeam_ver(obstacles):
	def show_obs(self):	
		main_board.board[self._xpos][self._ypos]='|'	
		main_board.board[self._xpos+1][self._ypos]='|'	
		main_board.board[self._xpos+2][self._ypos]='|'	
		main_board.board[self._xpos+3][self._ypos]='|'	
		main_board.board[self._xpos+4][self._ypos]='|'	

	@staticmethod	
	def remove_beam(x,y):
		for i in range(5):
			if main_board.board[x+i][y]=='|':
				main_board.board[x+i][y]=' '
			if main_board.board[x-i][y]=='|':	
				main_board.board[x-i][y]=' '
		

class firebeam_slant(obstacles):
	def show_obs(self):	
		main_board.board[self._xpos][self._ypos]='/'	
		main_board.board[self._xpos-1][self._ypos+1]='/'	
		main_board.board[self._xpos-2][self._ypos+2]='/'	
		main_board.board[self._xpos-3][self._ypos+3]='/'	
		main_board.board[self._xpos-4][self._ypos+4]='/'	

	@staticmethod	
	def remove_beam(x,y):
		for i in range(5):
			if main_board.board[x-i][y+i]=='/':
				main_board.board[x-i][y+i]=' '
			if main_board.board[x+i][y-i]=='/':	
				main_board.board[x+i][y-i]=' '
		
class coins(obstacles):
	def show_obs(self,type,size):
		if type==1:
			for i in range(size):
				main_board.board[self._xpos][self._ypos+i]='$'	
		elif type==2:
			for i in range(size):
				main_board.board[self._xpos+i][self._ypos]='$'				

class boost(obstacles):
	def show_obs(self):
		main_board.board[self._xpos][self._ypos]='B'	
		main_board.board[self._xpos][self._ypos+1]='B'	
		main_board.board[self._xpos-1][self._ypos]='B'	
		main_board.board[self._xpos-1][self._ypos+1]='B'	

class bullet:

	bulletx=[]
	bullety=[]
	fl=[]

	def __init__(self,xpos,ypos):
		self._xpos=xpos
		self._ypos=ypos
		self.bulletx.append(self._xpos)
		self.bullety.append(self._ypos)
		self.fl.append(0)

	def hide_obs(self):	
		for i in range(len(self.bullety)):
			main_board.board[self.bulletx[i]][self.bullety[i]]=' '	

	def move_bullets(self,cnt):
		# flag=0
		for i in range(len(self.bullety)):
			flag=0
			if self.fl[i]==0:
				if hero.return_boost==0:
					self.bullety[i]+=3
				else:
					self.bullety[i]+=4
				xp=boss.xpos	
				yp=boss.ypos	
				for j in range(0,4):
					for k in range(-5,1):
						if self.bulletx[i]==xp+j and self.bullety[i]==yp+k:
							flag=1	

			if flag==1:
				boss.dec_life()		
				self.fl[i]=1		
				
		for i in range(len(self.bullety)):
			if self.bullety[i]>cnt+100:
				self.fl[i]=1

	def show_obs(self):	
		for i in range(len(self.bullety)):
			if self.fl[i]==0:
				if main_board.board[self.bulletx[i]][self.bullety[i]]!='$' and main_board.board[self.bulletx[i]][self.bullety[i]]!='B':				
					main_board.board[self.bulletx[i]][self.bullety[i]]='>'	

	def check_bullet_collision(self):
		flag=0
		for i in range(len(self.bullety)):
			if self.fl[i]==0:
				if main_board.board[self.bulletx[i]][self.bullety[i]]=='_':
					firebeam_hor.remove_beam(self.bulletx[i],self.bullety[i])
					self.fl[i]=1
				elif main_board.board[self.bulletx[i]][self.bullety[i]+1]=='_':
					firebeam_hor.remove_beam(self.bulletx[i],self.bullety[i]+1)
					self.fl[i]=1
				elif main_board.board[self.bulletx[i]][self.bullety[i]+2]=='_':
					firebeam_hor.remove_beam(self.bulletx[i],self.bullety[i]+2)
					self.fl[i]=1
				elif main_board.board[self.bulletx[i]][self.bullety[i]]=='|':
					firebeam_ver.remove_beam(self.bulletx[i],self.bullety[i])
					self.fl[i]=1
				elif main_board.board[self.bulletx[i]][self.bullety[i]+1]=='|':
					firebeam_ver.remove_beam(self.bulletx[i],self.bullety[i]+1)
					self.fl[i]=1
				elif main_board.board[self.bulletx[i]][self.bullety[i]+2]=='|':
					firebeam_ver.remove_beam(self.bulletx[i],self.bullety[i]+2)	
					self.fl[i]=1
				elif main_board.board[self.bulletx[i]][self.bullety[i]]=='/':
					firebeam_slant.remove_beam(self.bulletx[i],self.bullety[i])		
					self.fl[i]=1
				elif main_board.board[self.bulletx[i]][self.bullety[i]+1]=='/':
					firebeam_slant.remove_beam(self.bulletx[i],self.bullety[i]+1)		
					self.fl[i]=1
				elif main_board.board[self.bulletx[i]][self.bullety[i]+2]=='/':
					firebeam_slant.remove_beam(self.bulletx[i],self.bullety[i]+2)					
					self.fl[i]=1
				# else:
					# flag=0
					# y1=self.bullety[i]		
					# y2=self.bullety[i]+1		
					# y3=self.bullety[i]+2	
					# for k in range(0,3):
					# 	for j in range(-2,1):
					# 		xp=boss.xpos+k
					# 		yp=boss.ypos+j
					# 		if xp==self.bulletx[i] and (yp==y1 or yp==y2 or yp==y3):
					# 			flag=1

					# if flag==1:
					# 	boss.dec_life()		
					# 	self.fl[i]

				# 	xp=boss.xpos	
				# 	yp=boss.ypos	
				# 	for j in range(0,4):
				# 		for k in range(-3,1):
				# 			if main_board.board[xp+j][yp+k]=='>':
				# 				flag=1	

				# if flag==1:
				# 	boss.dec_life()				
	# def hide_obs(self):	
	# 	main_board.board[self._xpos][self._ypos]=' '	

class boss_bullet:
	bulletx=[]
	bullety=[]
	fl=[]

	def __init__(self,xpos,ypos):
		self._xpos=xpos
		self._ypos=ypos
		self.bulletx.append(self._xpos)
		self.bullety.append(self._ypos)
		self.fl.append(0)	

	def hide_obs(self):	
		for i in range(len(self.bullety)):
			main_board.board[self.bulletx[i]][self.bullety[i]]=' '		

	def move_boss_bullets(self,cnt):
		# flag=0
		for i in range(len(self.bullety)):
			flag=0
			if self.fl[i]==0:
				self.bullety[i]-=3
				xp=hero.xpos
				yp=hero.ypos	
				for j in range(0,3):
					for k in range(-2,1):
						if self.bulletx[i]==xp+j and self.bullety[i]==yp+k:
							flag=1	

			if flag==1:
				hero._din__life-=1		
				self.fl[i]=1		
				
		for i in range(len(self.bullety)):
			if self.bullety[i]<boss.ypos-100:
				self.fl[i]=1		

	def show_obs(self):	
		for i in range(len(self.bullety)):
			if self.fl[i]==0:				
				if main_board.board[self.bulletx[i]][self.bullety[i]]!='$' and main_board.board[self.bulletx[i]][self.bullety[i]]!='B':				
					main_board.board[self.bulletx[i]][self.bullety[i]]='<'				

class Magnet(obstacles):
	global mag_listy
	global mag_listx
	
	def __init__(self,xpos,ypos):
		self._xpos=xpos
		self._ypos=ypos
		mag_listy.append(ypos)
		mag_listx.append(xpos)


	def show_obs(self):	
		main_board.board[self._xpos][self._ypos]='%'	
		main_board.board[self._xpos][self._ypos-1]='%'	
		main_board.board[self._xpos][self._ypos-2]='%'	
		main_board.board[self._xpos+1][self._ypos]='%'	
		main_board.board[self._xpos+1][self._ypos-1]='M'	
		main_board.board[self._xpos+1][self._ypos-2]='%'	
		main_board.board[self._xpos+2][self._ypos]='%'	
		main_board.board[self._xpos+2][self._ypos-1]='%'	
		main_board.board[self._xpos+2][self._ypos-2]='%'	
