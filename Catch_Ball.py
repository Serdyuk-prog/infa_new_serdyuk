from tkinter import *
import math
from random import randrange as rnd, choice

root = Tk()
WIGHT = 800
HIGHT = 600
colors = ['red', 'orange', 'yellow', 'green', 'blue']

class Ball():
    def __init__(self):
        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(30, 50)
        self.dx = +10
        self.dy = +10
        self.ball_id = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                                        fill=choice(colors), width=0)
    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.r >= WIGHT or self.x - self.r <= 0:
            self.dx = -self.dx
        if self.y + self.r > HIGHT or self.y - self.r <= 0:
            self.dy = -self.dy

    def show(self):
        canv.move(self.ball_id, self.dx, self.dy)

    def ball_click(self, mous_x, mous_y):
        if (math.sqrt(abs(self.x - mous_x)) ** 2 + math.sqrt(abs(self.y - mous_y)) ** 2) <= self.r:
            return TRUE
        else:
            return FALSE


def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(50, tick)


def click(event):
    x_mous, y_mous = event.x, event.y
    for ball in balls:
        if ball.ball_click(x_mous, y_mous):
            increase_score()

def increase_score():
    global score, canv, l
    score += 1
    #canv.create_text(500, 500, text="Your score:\n" + str(score),
     #             justify=CENTER, font="Verdana 14")
    l['text'] = "Your score: \n" + str(score)



def main():
    global canv, balls, score, l
    score = 0
    l = Label(bg='black', fg='white', width=20)
    l['text'] = "Your score: \n" + str(score)
    l.pack()
    root.geometry(str(WIGHT) + 'x' + str(HIGHT))
    canv = Canvas(root, bg='white')
    canv.pack(fill=BOTH, expand=1)

    canv.bind('<Button-1>', click)
    balls = [Ball() for i in range(1)]
    tick()
    mainloop()
    l.pack()


main()
