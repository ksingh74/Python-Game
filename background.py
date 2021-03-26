import time
import random
import os
from colorama import init,Fore,Style
from board import main_board
from mandalorin import hero,boss,print_last_lose
from play import *
from objects import *

flag=0

def show_obstacles(type):
	rx=random.randint(8,30)
	ry=random.randint(20,1850)
	if type==1:
		obs=firebeam_hor(rx,ry)
	elif type==2:
		obs=firebeam_ver(rx,ry)
	elif type==3:
		obs=firebeam_slant(rx,ry)

	obs.show_obs()

def show_magnet():
	rx=random.randint(6,33)
	ry=random.randint(10,1850)
	mgn=Magnet(rx,ry)

	mgn.show_obs()

def show_coins(type,size):
	rx=random.randint(6,33)
	ry=random.randint(10,1850)
	coin=coins(rx,ry)

	coin.show_obs(type,size)

def show_boosters():
	rx=random.randint(10,30)
	ry=random.randint(30,1850)
	booster=boost(rx,ry)

	booster.show_obs()

def show_last_screen():
	main_board.finalboard()

def print_board():
	os.system('clear')
	i=40
	j=100
	cnt=0
	rep=0
	rep_time=0
	var=0
	prevboost=time.time()
	boostruntime=0
	initial_game_time=time.time()
	# enableshieldtime=-65
	prev_time=time.time()
	global flag
	while True:
		if(time.time()-prev_time>0.1):
			prev_time=time.time()
			print("\033[0;0H")
			hero.hide_din(var)
			initial_time=time.time()
			movehero(cnt)	
			# final_time=time.time()
			# while(time.time()-initial_time<0.1):
			# 	pass
			# if final_time-initial_time<0.06:
			# 	time.sleep(0.06-(final_time-initial_time))
			hero.show_score(cnt)
			hero.show_life(cnt)
			for k in range(len(mag_listy)):
				if hero.ypos>mag_listy[k]-20 and hero.ypos<mag_listy[k] and ((hero.xpos<mag_listx[k]+20 and hero.xpos>mag_listx[k]) or (hero.xpos>mag_listx[k]-20 and hero.xpos<mag_listx[k])):
					hero.magnet_effect_fwd(cnt)
				if hero.ypos>mag_listy[k] and hero.ypos<mag_listy[k]+20 and ((hero.xpos<mag_listx[k]+20 and hero.xpos>mag_listx[k]) or (hero.xpos>mag_listx[k]-20 and hero.xpos<mag_listx[k])):
					hero.magnet_effect_bwd(cnt)	
			# for k in range(len(mag_listx)):		
			# 	if hero.xpos>mag_listx[k] and hero.xpos<mag_listx[k]+20:
			# 		hero.magnet_effect_up(cnt)	
			# 	if hero.xpos<mag_listx[k] and hero.xpos>mag_listx[k]-20:
			# 		hero.magnet_effect_down(cnt)			

			for k in range(len(mag_listy)):
				curx=mag_listx[k]
				cury=mag_listy[k]
				for i in range(curx,curx+3):
					for j in range(cury-2,cury+1):
						main_board.board[i][j]='%'
				main_board.board[curx+1][cury-1]='M'		


			if flag==1:
				boss.hide_boss()
				boss.move_boss()
			if flag==0 or flag==1:
				boss.show_boss(cnt)
				flag=1

			# time_elapsed=time.time()-initial_game_time	
			# main_board.board[0][cnt+26]="Time remaining:"
			# main_board.board[0][cnt+27]=str(400-time_elapsed)
			
			if hero.ypos<cnt+4:
				hero.ypos=cnt+4
				
			hero.display_din(cnt)


			# hero.coin_collision()
			for i in range(0,40):
				for j in range(cnt,100+cnt):
					# if hero.ypos<=cnt+3:
					# 	hero.hide_din()
					# 	hero.ypos=cnt+3
					# 	hero.display_din()
					if main_board.board[i][j]=='$':
						print(Fore.YELLOW+Style.BRIGHT+main_board.board[i][j], end='')
					elif i>=hero.xpos and i<hero.xpos+3 and j<=hero.ypos and j>hero.ypos-3:
						if hero.return_shield==1:	
							print(Fore.GREEN+Style.BRIGHT+main_board.board[i][j], end='')
						elif hero.return_boost==1:	
							print(Fore.BLUE+Style.BRIGHT+main_board.board[i][j], end='')	
						else:
							print(Fore.WHITE+Style.BRIGHT+main_board.board[i][j], end='')
					elif i>=boss.xpos and i<boss.xpos+4 and j<=boss.ypos and j>boss.ypos-4:	
						print(Fore.CYAN+Style.BRIGHT+main_board.board[i][j], end='')			
					elif main_board.board[i][j]=='/' or main_board.board[i][j]=='_' or main_board.board[i][j]=='|':	
						print(Fore.RED+Style.BRIGHT+main_board.board[i][j], end='')
					elif main_board.board[i][j]=='B':	
						print(Fore.BLUE+Style.BRIGHT+main_board.board[i][j], end='')
					elif main_board.board[i][j]=='%' or main_board.board[i][j]=='M':	
						print(Fore.CYAN+Style.BRIGHT+main_board.board[i][j], end='')	
					elif i==0 and j==cnt+21:	
						if hero.return_shield==1:
							print(Fore.GREEN+Style.BRIGHT+main_board.board[i][j], end='')	
						else:	
							print(Fore.RED+Style.BRIGHT+main_board.board[i][j], end='')
					elif i==0 and j==cnt+24:	
						if hero.return_boost==1:
							print(Fore.BLUE+Style.BRIGHT+main_board.board[i][j], end='')	
						else:	
							print(Fore.RED+Style.BRIGHT+main_board.board[i][j], end='')	
					elif i==1 or i==2 or i==38 or i==39:				
							print(Fore.MAGENTA+Style.BRIGHT+main_board.board[i][j], end='')	
					elif main_board.board[i][j]=='<':		
							print(Fore.RED+Style.BRIGHT+main_board.board[i][j], end='')	
					elif main_board.board[i][j]=='>':		
							print(Fore.GREEN+Style.BRIGHT+main_board.board[i][j], end='')			
					else:	
						print(Fore.WHITE+Style.BRIGHT+main_board.board[i][j], end='')
				print()	
			# time.sleep(0.00005)

			time_elapsed=time.time()-initial_game_time
			if 400-time_elapsed<0:
				os.system('clear')
				print_last_lose()
				quit()	
			print("Time remaining:",end='')
			print(400-time_elapsed)

			if hero.return_boost==1:
				cnt+=2
				boostruntime+=time.time()-prevboost
				prevboost=time.time()
				if boostruntime>=10:
					hero.disable_boost()
					boostruntime=0
					# continue
			else:
				prevboost=time.time()	

			if hero.return_shield==0:
				x=time.time()	

			var=hero.return_shield		

			if hero.return_shield==1:
				y=time.time()
				rep_time+=y-x;
				x=y;	
				if rep_time>10:
					hero.disable_shield()
					rep_time=0

			if cnt<1890:		
				cnt+=1		

# hero.move_up()
# hero.move_up()
# print(hero.xpos,end=' ')
# print(hero.ypos)
for i in range(15):
	show_obstacles(1)
for i in range(15):
	show_obstacles(2)
for i in range(15):
	show_obstacles(3)		

for i in range(30):
	show_coins(1,4)
for i in range(30):
	show_coins(1,5)

for i in range(8):
	show_coins(2,4)
for i in range(8):
	show_coins(2,5)	

for i in range(16):
	show_boosters()	

for i in range(10):
	show_magnet()

print_board()		