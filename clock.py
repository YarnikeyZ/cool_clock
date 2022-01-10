##Requirments: Python3, Figlet
from time import sleep, strftime, localtime;
from subprocess import check_output
from random import randint as rd

clear = check_output('clear').decode('UTF-8')

def check_none(varz):
	for var in range(0, 3):
		if varz[var] == None:
			varz[var] = 0
	return varz

def clock(ptime, style, t_color, b_color):
	look = check_none([style, t_color, b_color])
	look = f'\033[{look[0]};0;0m\033[38;5;{look[1]}m\033[48;5;{look[2]}m\n'
	print(look, check_output(['figlet', strftime(ptime, localtime())]).decode('UTF-8')[1:][:-2], '\033[0;0m', end='')

try:
	output = input('Type of color:').lower()
	rainbow = [196, 208, 226, 82, 39, 21, 93, 196, 208]
	green = [2, 22, 28, 34, 40, 46, 40, 34, 28, 22, 2, 22, 28]
	while True:
		if output == 'white' or output == 'w':
				print(clear)
				clock('[ %a . %b ] ', 1, 15, 0)
				clock('[ %d . %m . %Y ] ', 1, 15, 0)
				clock('%H : %M : %S     ', 1, 15, 0)
				sleep(1)
		elif output == 'rainbow' or output == 'r':
			for rainbow_num in range(0, 7):
				print(clear)
				clock('[ %a . %b ] ', 1, rainbow[rainbow_num+2], 0)
				clock('[ %d . %m . %Y ] ', 1, rainbow[rainbow_num+1], 0)
				clock('%H : %M : %S     ', 1, rainbow[rainbow_num+0], 0)
				sleep(0.1)
		elif output == 'wtf':
			print(clear)
			WTF = rd(0,7)
			clock('[ %a . %b ]  ', 1, 0, rainbow[WTF])
			clock('[ %d . %m . %Y ]  ', 1, 0, rainbow[WTF])
			clock('%H : %M : %S' , 1, 0, rainbow[WTF])
			sleep(0.2)
		else:
			output = 'white'
except KeyboardInterrupt:
	print(clear)
	exit()
