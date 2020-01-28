import tkinter as tk
import tkinter.ttk as ttk
from tkinter import font
import random
#pip install pillow
from PIL import Image, ImageTk
import threading
import time


class TitleScene(object):
    def __init__(self, root, on_cleanup):
        self.root = root
        self.on_cleanup = on_cleanup
        self.label1 = None
        self.button1 = None
        self.button2 = None
        self.button3 = None
        self.button4 = None


    def setup(self):
        self.root.geometry("750x750")
        self.root.title("タイトル")
        self.root.configure(background="#000000")

        self.label1 = tk.Label(self.root, text="間違い探しゲーム", font=("",46), height=5, bg="black", fg="red")
        self.label1.pack(fill="x")

        self.button1 = tk.Button(self.root, text="Stage1", font=("",36), width=50, bg="red", command=self.cleanup)
        self.button1.pack()

        self.button2 = tk.Button(self.root, text="Stage2", font=("",36), width=50, bg="red", command=self.cleanup)
        self.button2.pack()

        self.button3 = tk.Button(self.root, text="Stage3", font=("",36), width=50, bg="red", command=self.cleanup)
        self.button3.pack()

        self.button4 = tk.Button(self.root, text="Stage4", font=("",36), width=50, bg="red", command=self.cleanup)
        self.button4.pack()

    def cleanup(self):
        self.button4.destroy()
        self.button3.destroy()
        self.button2.destroy()
        self.button1.destroy()
        self.label1.destroy()
        self.on_cleanup()

class MainStage(object):
    def __init__(self, root):
        self.root = root

    def setup(self):
        self.root.geometry('1250x1000')
        self.root.title("メインステージ")
        self.root.configure(background="#000000")

        #文字色、背景色、サイズ、フォントを指定。
        font1 = font.Font(family='Helvetica', size=40)
        label1 = tk.Label(self.root, text="画像探しゲーム！", font=font1,bg="yellow",fg="red")
        label1.pack(side="top")

        #座標入力
        font2 = font.Font(family='Helvetica', size=18)
        label2 = tk.Label(self.root, text="並んでいる画像の中に一つだけ大きな画像と同じ画像が紛れ込んでいるので", font=font2,bg="yellow",fg="red")
        label2.place(x=400, y=700)

        font3 = font.Font(family='Helvetica', size=18)
        label3 = tk.Label(self.root, text="その画像と同じ位置関係にあるボタンをクリックしてください！", font=font2,bg="yellow",fg="red")
        label3.place(x=400, y=730)

        # 画像を表示するためのキャンバスの作成（ピンクで表示）
        canvas = tk.Canvas(root, bg = "pink", width=400, height=360)
        canvas.create_polygon(250, 90, 250, 200, 150, 200,fill="green")
        canvas.place(x=100, y=100) # 左上の座標を指定
            
        # 画像を表示するためのキャンバスの作成（ピンクで表示）
        canvas = tk.Canvas(bg = "pink", width=100, height=100)
        canvas.create_oval(10, 10, 90, 90,fill="red")
        canvas.place(x=580, y=200) # 左上の座標を指定
        
        # 画像を表示するためのキャンバスの作成（ピンクで表示）
        canvas = tk.Canvas(bg = "pink", width=100, height=100)
        canvas.create_rectangle(10, 10, 90, 90,fill="green")
        canvas.place(x=730, y=200) # 左上の座標を指定
        
        # 画像を表示するためのキャンバスの作成（ピンクで表示）
        canvas = tk.Canvas(bg = "pink", width=100, height=100)
        canvas.create_oval(10, 10, 90, 90,fill="blue")
        canvas.place(x=880, y=200) # 左上の座標を指定

        # 画像を表示するためのキャンバスの作成（ピンクで表示）
        canvas = tk.Canvas(bg = "pink", width=100, height=100)
        canvas.create_rectangle(10, 10, 90, 90,fill="green")
        canvas.place(x=580, y=350) # 左上の座標を指定
        
        # 画像を表示するためのキャンバスの作成（ピンクで表示）
        canvas = tk.Canvas(bg = "pink", width=100, height=100)
        canvas.create_rectangle(10, 10, 90, 90,fill="yellow")
        canvas.place(x=730, y=350) # 左上の座標を指定
        
        # 画像を表示するためのキャンバスの作成（ピンクで表示）
        canvas = tk.Canvas(bg = "pink", width=100, height=100)
        canvas.create_polygon(80, 10, 80, 90, 10, 90,fill="red")
        canvas.place(x=880, y=350) # 左上の座標を指定

        # 画像を表示するためのキャンバスの作成（ピンクで表示）
        canvas = tk.Canvas(bg = "pink", width=100, height=100)
        canvas.create_polygon(80, 10, 80, 90, 10, 90,fill="purple")
        canvas.place(x=580, y=500) # 左上の座標を指定

        # 画像を表示するためのキャンバスの作成（ピンクで表示）
        canvas = tk.Canvas(bg = "pink", width=100, height=100)
        canvas.create_polygon(80, 10, 80, 90, 10, 90,fill="blue")
        canvas.place(x=730, y=500) # 左上の座標を指定
        
        # 画像を表示するためのキャンバスの作成（ピンクで表示）
        canvas = tk.Canvas(bg = "pink", width=100, height=100)
        canvas.create_rectangle(10, 10, 90, 90,fill="green")
        canvas.place(x=880, y=500) # 左上の座標を指定

        # 画像を表示するためのキャンバスの作成（ピンクで表示）
        canvas = tk.Canvas(bg = "pink", width=100, height=100)
        canvas.create_rectangle(10, 10, 90, 90,fill="green")
        canvas.place(x=1020, y=200) # 左上の座標を指定

        # 画像を表示するためのキャンバスの作成（ピンクで表示）
        canvas = tk.Canvas(bg = "pink", width=100, height=100)
        canvas.create_polygon(80, 10, 80, 90, 10, 90,fill="green")
        canvas.place(x=1020, y=350) # 左上の座標を指定

        # 画像を表示するためのキャンバスの作成（ピンクで表示）
        canvas = tk.Canvas(bg = "pink", width=100, height=100)
        canvas.create_rectangle(10, 10, 90, 90,fill="green")
        canvas.place(x=1020, y=500) # 左上の座標を指定

        def btn_click1():
            print("不正解！！")
            

        def btn_click2():
            print("不正解！！")
            

        def btn_click3():
            print("不正解！！")
      

        def btn_click4():
            print("不正解！！")
       

        def btn_click5():
            print("不正解！！")
            

        def btn_click6():
            print("不正解！！")
        

        def btn_click7():
            print("不正解！！")
        

        def btn_click8():
            print("正解！！")
        

        def btn_click9():
            print("不正解！！")
            

        def btn_click10():
            print("不正解！！")
            

        def btn_click11():
            print("不正解！！")

        
        def btn_click12():
            print("不正解！！")


        # ボタン
        btn = tk.Button(self.root, text='1', command=btn_click1,height=5,width=10)
        btn.place(x=10, y=500)
        btn = tk.Button(self.root, text='2', command=btn_click2,height=5,width=10)
        btn.place(x=100, y=500)
        btn = tk.Button(self.root, text='3', command=btn_click3,height=5,width=10)
        btn.place(x=190, y=500)
        btn = tk.Button(self.root, text='4', command=btn_click3,height=5,width=10)
        btn.place(x=280, y=500)
        btn = tk.Button(self.root, text='5', command=btn_click4,height=5,width=10)
        btn.place(x=10, y=600)
        btn = tk.Button(self.root, text='6', command=btn_click5,height=5,width=10)
        btn.place(x=100, y=600)
        btn = tk.Button(self.root, text='7', command=btn_click6,height=5,width=10)
        btn.place(x=190, y=600)
        btn = tk.Button(self.root, text='10', command=btn_click6,height=5,width=10)
        btn.place(x=100, y=700)
        btn = tk.Button(self.root, text='9', command=btn_click7,height=5,width=10)
        btn.place(x=10, y=700)
        btn = tk.Button(self.root, text='8', command=btn_click8,height=5,width=10)
        btn.place(x=280, y=600)
        btn = tk.Button(self.root, text='11', command=btn_click9,height=5,width=10)
        btn.place(x=190, y=700)
        btn = tk.Button(self.root, text='12', command=btn_click9,height=5,width=10)
        btn.place(x=280, y=700)

root = tk.Tk()

mainstage = MainStage(root)

title = TitleScene(root, mainstage.setup)
title.setup()

root.mainloop()


