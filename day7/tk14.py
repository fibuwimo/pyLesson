import tkinter as tk

def bt_click():
    price=int(e1.get())
    num=int(e2.get())
    n=int(price/num)
    per=int((price/num)//100*100)
    if per < n:
        per +=100

    result.delete("1.0",tk.END)
    result.insert("1.0",f'一人当たり{per}円、幹事は{price-per*(num-1)}円')


root=tk.Tk()
root.title('割り勘ちゃん')
root.resizable(False,False)
canvas = tk.Canvas(root,width=800,height=600,bg='skyblue')
canvas.pack()

t1= tk.Label(text='金額',font=('メイリオ',16),bg='skyblue')
t1.place(x=100,y=50)
e1=tk.Entry(width=20,font=('メイリオ',16))
e1.place(x=100,y=100)
t2= tk.Label(text='人数',font=('メイリオ',16),bg='skyblue')
t2.place(x=100,y=150)
e2=tk.Entry(width=20,font=('メイリオ',16))
e2.place(x=100,y=200)

btn=tk.Button(root,text="計算する",font=('メイリオ',16),command=bt_click)
btn.place(x=100,y=250)

result=tk.Text(width=30,height=5,font=('メイリオ',16),bg='skyblue')
result.place(x=100,y=300)

root.mainloop()

