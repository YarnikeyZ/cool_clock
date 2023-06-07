from time import sleep, strftime, localtime;
from subprocess import getoutput
from random import randint
from os import get_terminal_size as gts
from sys import argv
from math import cos, pi, sin

from pypixpile.pixpile import *
from seg10py.seg10py import dnum, dseg

RAINBOW = [196, 208, 226, 82, 39, 21, 93, 196, 208]
TIMETYPES = ['%H', '%M', '%S', '%d', '%m', '%a', '%b', '%Y']

def bigIt(text):
    return f'{getoutput(f"figlet {text}")[1:]}\n'

def getTime(str_time):
    return strftime(str_time, localtime())

def clockBigWhite(strTimes):
    print(CLR,
        bigIt(f'[ {strTimes[5]} . {strTimes[6]} ]'),
        bigIt(f'[ {strTimes[3]} . {strTimes[4]} . {strTimes[7]} ]'),
        bigIt(f'{strTimes[0]} : {strTimes[1]} : {strTimes[2]}')
    )
    sleep(1)

def clockBigRainbow(strTimes):
    for rainbow_num in range(7):
        print(CLR,
            colorIt(bigIt(f'[ {strTimes[5]} . {strTimes[6]} ]'), RAINBOW[rainbow_num+2], 0),
            colorIt(bigIt(f'[ {strTimes[3]} . {strTimes[4]} . {strTimes[7]} ]'), RAINBOW[rainbow_num+1], 0),
            colorIt(bigIt(f'{strTimes[0]} : {strTimes[1]} : {strTimes[2]}'), RAINBOW[rainbow_num+0], 0)
        )
        sleep(0.1)

def clockBigWtf(strTimes):
    wtf = randint(0,7)
    print(CLR,
        colorIt(bigIt(f'[ {strTimes[5]} . {strTimes[6]} ]'), 0, RAINBOW[wtf]),
        colorIt(bigIt(f'[ {strTimes[3]} . {strTimes[4]} . {strTimes[7]} ]'), 0, RAINBOW[wtf]),
        colorIt(bigIt(f'{strTimes[0]} : {strTimes[1]} : {strTimes[2]}'), 0, RAINBOW[wtf])
    )
    sleep(0.2)

def clockSmall(strTimes):
    print(f"""{CLR}\n\n\n\n\n
        Time: {strTimes[0]}:{strTimes[1]}:{strTimes[2]}
        Date: {strTimes[3]}.{strTimes[4]}.{strTimes[7]}
        Uptime: {getoutput('uptime').replace(' days,', 'd')[12:][:-42]}\n\n\n\n\n"""
    )
    sleep(1)

def clockProgressBar(strTimes, intTimes):
    print(f"""{CLR}\n\n\n\n\n\n\n\n\n
        [Hour] [{strTimes[0]}] [{colorIt(''.ljust(intTimes[0], '#'), 9, 0)}{colorIt(''.ljust(24-intTimes[0], '-'), 52, 0)}]
        [Min ] [{strTimes[1]}] [{colorIt(''.ljust(intTimes[1], '#'), 154, 0)}{colorIt(''.ljust(60-intTimes[1], '-'), 100, 0)}]
        [Sec ] [{strTimes[2]}] [{colorIt(''.ljust(intTimes[2], '#'), 10, 0)}{colorIt(''.ljust(60-intTimes[2], '-'), 34, 0)}]"""
    )
    sleep(1)

def clockSegmented(intTimes):
    print(CLR, end="")
    x, y = 16, 5
    hdiv, hmod, mdiv, mmod = 0, 0, 0, 0

    if intTimes[0] > 0:
        hdiv = intTimes[0] // 10
        hmod = intTimes[0] %  10
    if intTimes[1] > 0:
        mdiv = intTimes[1] // 10
        mmod = intTimes[1] %  10
    
    print(dnum(hdiv, ".", x+1, y-1))
    print(dnum(hdiv, ".", x+2, y-2))
    print(dnum(hdiv, "3", x, y))
    x += 28
    print(dnum(hmod, ".", x+1, y-1))
    print(dnum(hmod, ".", x+2, y-2))
    print(dnum(hmod, "3", x, y))
    print(dseg(9,    "*", x, y))
    x += 28
    print(dnum(mdiv, ".", x+1, y-1))
    print(dnum(mdiv, ".", x+2, y-2))
    print(dnum(mdiv, "3", x, y))
    x += 28
    print(dnum(mmod, ".", x+1, y-1))
    print(dnum(mmod, ".", x+2, y-2))
    print(dnum(mmod, "3", x, y))
    sleep(1)

def clockDial(intTimes):
    print(CLR, end="")
    canvas = list(gts())
    canvas[1] -= 5
    center = [canvas[0]//2, canvas[1]//2]
    rady = center[1]
    drawEllipse("#", 15, 0, center[0], center[1], rady*2, rady)
    n=270
    drawLine("h", 10, 0, center[0], center[1], round(center[0]+(rady*2)*cos((n+30*intTimes[0] + 0.5*intTimes[1])*pi/180)), round(center[1]+rady*sin((n+30*intTimes[0] + 0.5*intTimes[1])*pi/180)))
    drawLine("m", 11, 0, center[0], center[1], round(center[0]+(rady*2)*cos((n+6 *intTimes[1] + 0.1*intTimes[2])*pi/180)), round(center[1]+rady*sin((n+6 *intTimes[1] + 0.1*intTimes[2])*pi/180)))
    drawLine("s", 9 , 0, center[0], center[1], round(center[0]+(rady*2)*cos((n+6 *intTimes[2]                  )*pi/180)), round(center[1]+rady*sin((n+6 *intTimes[2]                  )*pi/180)))
    sleep(1)

def main():
    try:
        try:
            clockType = argv[1]
        except IndexError:
            clockType = input('Type of clock (w/r/wtf/c/p/s/d):').lower()
        
        while True:
            strTimes = []
            intTimes = []
            for time in TIMETYPES:
                time = getTime(time)
                strTimes.append(time)
                try:
                    intTimes.append(int(time))
                except ValueError:
                    pass
            match clockType:
                case 'w'|'white':
                    clockBigWhite(strTimes)
                case 'r'|'rainbow':
                    clockBigRainbow(strTimes)
                case 'wtf':
                    clockBigWtf(strTimes)
                case 'c'|'compact':
                    clockSmall(strTimes)
                case 'p'|'progress':
                    clockProgressBar(strTimes, intTimes)
                case 's'|'segmented':
                    clockSegmented(intTimes)
                case 'd'|'dial':
                    clockDial(intTimes)
                case _:
                    exit()
    except KeyboardInterrupt:
        print(CLR, end="")
        exit()

if __name__ == '__main__':
    main()
