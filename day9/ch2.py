import tkinter as tk

root=tk.Tk()
root.title("画像描画")
canvas=tk.Canvas(width=480,height=300)
canvas.pack()
img_bg=tk.PhotoImage(file="park.png")
canvas.create_image(240,150,image=img_bg)
root.mainloop()
