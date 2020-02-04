from tkinter import *
root = Tk()

c = Canvas(root, width=200, height=200, bg='white')
c.pack()

def draw_lines():
    c.create_line(10, 10, 190, 50)

    c.create_line(100, 180, 100, 60, fill='green',
                    width=5, arrow=LAST, dash=(10,2),
                    activefill='lightgreen',
                    arrowshape="10 20 10")

def draw_rectangles():
    c.create_rectangle(10, 10, 190, 60)

    c.create_rectangle(60, 80, 140, 190, fill='yellow', outline='green',
                        width=3, activedash=(5, 4))

def draw_poligons():
    c.create_polygon(100, 10, 20, 90, 180, 90)

    c.create_polygon(40, 110, 160, 110, 190, 180, 10, 180,
                    fill='orange', outline='black')
def draw_ovals():
    c.create_oval(50, 10, 150, 110, width=2)
    c.create_oval(10, 120, 190, 190, fill='grey70', outline='white')

def draw_arcs():
    c.create_oval(10, 10, 190, 190, fill='lightgrey', outline='white')
    c.create_arc(10, 10, 190, 190, start=0, extent=45, fill='red')
    c.create_arc(10, 10, 190, 190, start=180, extent=25, fill='orange')
    c.create_arc(10, 10, 190, 190, start=240, extent=100, style=CHORD, fill='green')
    c.create_arc(10, 10, 190, 190, start=160, extent=-70, style=ARC, outline='darkblue', width=5)

def draw_texts():
    c.create_text(100, 100, text="Hello World,\nPython\nand Tk",
                  justify=CENTER, font="Verdana 14")
    c.create_text(200, 200, text="About this",
                  anchor=SE, fill="grey")

input_line = input()
if input_line  == 'lines':
    draw_lines()
if input_line  == 'rectangles':
    draw_rectangles()
if input_line  == 'poligons':
    draw_poligons()
if input_line  == 'ovals':
    draw_ovals()
if input_line == 'arcs':
    draw_arcs()
if input_line == 'texts':
    draw_texts()
root.mainloop()


