import signal
import os
import time
from colorama import init, Fore

from getinput import AlarmException
from getch import _getChUnix as getChar
from mandalorin import hero,boss
from objects import bullet,boss_bullet

count=0
obj=1
bull_boss=0
enableshieldtime=-65
userdragon=0
flagdragon=0

def movehero(cnt):
	global count
	global obj
	global bull_boss
	global enableshieldtime
	global userdragon
	global flagdragon
	bull_boss+=1

	def alarmhandler(signum, frame):
		''' input method '''
		raise AlarmException

	def user_input(timeout=0.1):
		''' input method '''
		signal.signal(signal.SIGALRM, alarmhandler)
		signal.setitimer(signal.ITIMER_REAL, timeout)
		
		try:
			text = getChar()()
			signal.alarm(0)
			return text
		except AlarmException:
			pass
		signal.signal(signal.SIGALRM, signal.SIG_IGN)
		return ''

	char = user_input()

	if char=='d':
		hero.move_fwd(cnt)
		# hero.move_down()

	elif char=='a':
		hero.move_bwd()

	elif char=='w':
		hero.move_up(cnt)

	# elif char=='b':
	# 	hero.enable_boost()	

	elif char==' ':
		# enableshieldtime+=time.time()-y
		# y=time.time()
		if time.time()-enableshieldtime>60 and hero.userdragon==0:
			hero.enable_shield()
			enableshieldtime=time.time()
		# 	enableshieldtime=0	

	elif char=='b':
		count+=1
		obj=bullet(hero.xpos,hero.ypos+1)	
		# obj.hide_obs()
		# obj.move_bullets(cnt)
		# obj.check_bullet_collision()
		# obj.show_obs()			

	elif char=='q':
		quit()		

	elif char=='j':
		# hero.show_dragon(cnt)
		if flagdragon==0:
			if hero.xpos>30:
				hero.xpos=30
			hero.userdragon=1
			flagdragon=1

	else:		
		hero.move_down()	

	if hero.userdragon==1:
		count+=1	

	if hero.userdragon==1 and count%2==0:
		# count+=1
		# if count%3==0:
		obj=bullet(hero.xpos+2,hero.ypos+45)	
		obj.hide_obs()
		obj.move_bullets(cnt)
		obj.check_bullet_collision()
		obj.show_obs()	

	if count>=1 and hero.userdragon==0:
		obj.hide_obs()
		obj.move_bullets(cnt)
		obj.check_bullet_collision()
		obj.show_obs()		

	if bull_boss%5==0:	
		bull=boss_bullet(boss.xpos+2,boss.ypos-4)
		bull.hide_obs()
		bull.move_boss_bullets(cnt)
		bull.show_obs()
	

def return_user_dragon():
	return userdragon	

	# boss.hide_boss()
	# boss.move_boss()
	# boss.show_boss(cnt)		