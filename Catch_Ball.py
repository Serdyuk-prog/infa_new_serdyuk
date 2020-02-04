from tkinter import *
import math
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')
WIGHT = 800
HIGHT = 600
canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['red','orange','yellow','green','blue']

def tick():
    global x, y, r, dx, dy
    x += dx
    y += dy
    if x + r >= WIGHT or x - r <= 0:
        dx = -dx
    if y + r > HIGHT or y - r <= 0:
        dy = -dy
    canv.move(ball_id, dx, dy)
    root.after(50, tick)


def new_ball():
    global x, y, r, ball_id, dx, dy
    canv.delete(ALL)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    dx = +10
    dy = +10
    ball_id = canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)

    #root.after(1000,new_ball)

def click(event):
    x_mous, y_mous = event.x, event.y
    if (math.sqrt(abs(x - x_mous)) ** 2  + math.sqrt(abs(y - y_mous)) ** 2) <= r:
        print('OK')

def main():
    canv.bind('<Button-1>', click)
    new_ball()
    tick()


main()

mainloop()