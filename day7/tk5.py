import tkinter as tk
def bt_click():
    btn['text']='Clicked!!'
root=tk.Tk()
root.title('わしのまど')
root.geometry('600x400')
btn=tk.Button(root,text='こ↑こ↓',font=('Arial',50),command=bt_click)
btn.place(x=100,y=100)
root.mainloop()
