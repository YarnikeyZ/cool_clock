##Requirments: Python3, Figlet
from time import sleep, strftime, localtime;
from subprocess import getoutput as gout
from random import randint as rd

clear = gout('clear')

def color(text, t_color, b_color):
    return f'\033[38;5;{t_color}m\033[48;5;{b_color}m{text}\033[0;0m'

def big(text):
    return f'{gout(f"figlet {text}")[1:]}\n'

def get_time(str_time):
    return strftime(str_time, localtime())

try:
    type_of = input('Type of clock (w/r/wtf/c/p):').lower()
    rainbow = [196, 208, 226, 82, 39, 21, 93, 196, 208]
    types_times = ['%H', '%M', '%S', '%d', '%m', '%a', '%b', '%Y']
    while True:
        times = []
        for tim in types_times:
            times.append(get_time(tim))
        if type_of == 'white' or type_of == 'w':
            print(clear,
            big(f'[ {times[5]} . {times[6]} ]'),
            big(f'[ {times[3]} . {times[4]} . {times[7]} ]'),
            big(f'{times[0]} : {times[1]} : {times[2]}'))
            sleep(1)
        elif type_of == 'rainbow' or type_of == 'r':
            for rainbow_num in range(0, 7):
                print(clear,
                color(big(f'[ {times[5]} . {times[6]} ]'), rainbow[rainbow_num+2], 0),
                color(big(f'[ {times[3]} . {times[4]} . {times[7]} ]'), rainbow[rainbow_num+1], 0),
                color(big(f'{times[0]} : {times[1]} : {times[2]}'), rainbow[rainbow_num+0], 0))
                sleep(0.1)
        elif type_of == 'wtf':
            WTF = rd(0,7)
            print(clear,
            color(big(f'[ {times[5]} . {times[6]} ]'), 0, rainbow[WTF]),
            color(big(f'[ {times[3]} . {times[4]} . {times[7]} ]'), 0, rainbow[WTF]),
            color(big(f'{times[0]} : {times[1]} : {times[2]}'), 0, rainbow[WTF]))
            sleep(0.2)
        elif type_of == 'compact' or type_of == 'c':
            print(f"""{clear}\n\n\n\n\n
                  Time: {times[0]}:{times[1]}:{times[2]}
                  Date: {times[3]}.{times[4]}.{times[7]}
                  Uptime: {gout('uptime').replace(' days,', 'd')[12:][:-42]}\n\n\n\n\n""")
            sleep(1)
        elif type_of == 'progress' or type_of == 'p':
            print(f"""{clear}\n\n\n\n\n\n\n\n\n
[Hour] [{times[0]}] [{color(''.ljust(int(times[0]), '#'), 9, 0)}{color(''.ljust(24-int(times[0]), '-'), 52, 0)}]
[Min ] [{times[1]}] [{color(''.ljust(int(times[1]), '#'), 154, 0)}{color(''.ljust(60-int(times[1]), '-'), 100, 0)}]
[Sec ] [{times[2]}] [{color(''.ljust(int(times[2]), '#'), 10, 0)}{color(''.ljust(60-int(times[2]), '-'), 34, 0)}]""")
            sleep(1)
        else:
            exit()
except KeyboardInterrupt:
        print(clear)
        exit()
