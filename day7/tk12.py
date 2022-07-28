import tkinter as tk
import tkinter.messagebox as mbox

def btn_click():
    mbox.showinfo('情報','ボタンを押しました')
root=tk.Tk()
root.title('わしのまど')
root.geometry('400x200')
btn=tk.Button(text='テスト',command=btn_click)
btn.pack()
root.mainloop()
