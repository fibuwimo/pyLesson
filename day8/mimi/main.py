import tkinter as tk
key=''

def key_down(e):
    global key
    key=e.keysym

def key_up(e):
    global key
    key=''

cx=400
cy=300

def main_proc():
    global cx,cy
    if key=='Up':
        cy=cy-4
    if key=='Down':
        cy=cy+4
    if key=='Left':
        cx=cx-4
    if key=='Right':
        cx=cx+4

    canvas.coords('MYCHR',cx,cy)
    root.after(20,main_proc)

root=tk.Tk()
root.bind('<KeyPress>',key_down)
root.bind('<KeyRelease>',key_up)
canvas=tk.Canvas(width=800,height=600,bg='lightgreen')
canvas.pack()
img=tk.PhotoImage(file='mimi.png')
canvas.create_image(cx,cy,image=img,tag='MYCHR')
main_proc()
root.mainloop()
