import RPi.GPIO as gpio
import time
import curses

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
screen.nodelay(True)

gpio.setmode(gpio.BOARD)
gpio.setup(7, gpio.OUT) #IN4 green wire
gpio.setup(11, gpio.OUT) #IN3 blue wire
gpio.setup(13, gpio.OUT) #IN2 purple wire
gpio.setup(15, gpio.OUT) #IN1 yellow wire
#gpio.setup(16, gpio.OUT) #servo

gpio.output(7, 0)
gpio.output(11, 0)
gpio.output(13, 0)
gpio.output(15, 0)

def forward():
    gpio.output(7, 0)
    gpio.output(13, 0)
    gpio.output(11, 1)
    gpio.output(15, 1)

def backwards():
    gpio.output(11, 0)
    gpio.output(15, 0)
    gpio.output(7, 1)
    gpio.output(13, 1)

def left():
    gpio.output(11, 1)
    gpio.output(13, 1)
    gpio.output(7, 0)
    gpio.output(15, 0)

def right():
    gpio.output(15, 1)
    gpio.output(7, 1)
    gpio.output(13, 0)
    gpio.output(11, 0)

def for_left():
    gpio.output(7, 0)
    gpio.output(11, 1)
    gpio.output(13, 0)
    gpio.output(15, 0)

def for_right():
    gpio.output(7, 0)
    gpio.output(13, 0)
    gpio.output(15, 1)
    gpio.output(11, 0)

def back_left():
    gpio.output(7, 1)
    gpio.output(11, 0)
    gpio.output(15, 0)
    gpio.output(13, 0)

def back_right():
    gpio.output(11, 0)
    gpio.output(13, 1)
    gpio.output(15, 0)
    gpio.output(7, 0)

def clean_pins():
    gpio.output(7, 0)
    gpio.output(11, 0)
    gpio.output(13, 0)
    gpio.output(15, 0)

def terminate():
    curses.nocbreak()
    screen.keypad(False)
    curses.echo()
    curses.endwin()
    gpio.cleanup()

try:
    while True:
        char = screen.getch()
        time.sleep(0.08)
        if(char != -1):
            if(char == ord('w')):
                forward()
            elif(char == ord('a')):
                left()
            elif(char == ord('s')):
                backwards()
            elif(char == ord('d')):
                right()
            elif(char == ord('q')):
                for_left()
            elif(char == ord('e')):
                for_right()
            elif(char == ord('z')):
                back_left()
            elif(char == ord('x')):
                back_right()
            else:
                clean_pins()
        else:
            clean_pins()

except KeyboardInterrupt:
    terminate()

finally:
    terminate()
