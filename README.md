# sample
import tkinter as tk
import tkinter.ttk as ttk
root=tk.Tk()
root.geometry("550x450")
root.title("あ")
root.configure(background="#000000")
label1 = tk.Label(root,text="あ",font=("",46),height=5,bg="black",fg="red")
label1.pack(fill="x")
#ステージボタンの設定
button1 = tk.Button(root,text="Stage1",font=("",36),width=50,bg="red")
button1.pack()
button1 = tk.Button(root,text="Stage2",font=("",36),width=50,bg="red")
button1.pack()
root.mainroop()
