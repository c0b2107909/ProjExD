import tkinter as tk
import tkinter.messagebox as tkm

def btn_click(event):
    btn = event.widget
    num = btn["text"]
    entry.insert(tk.END, num)
    #tkm.showinfo(txt, f"[{txt}]ボタンが押されました")

root = tk.Tk()
root.title("電卓")
root.geometry("300x500")

#------テキスト入力欄------

entry = tk.Entry(width = 10, justify="right", font = ("Times New Roman", 40))
entry.grid(row=0 ,column=0, columnspan=3)

#------数字・演算子のボタン------
r, c = 1, 0 # r : 行を表す変数/c : 列を表す変数
numbers = [i for i in range(9, -1, -1)] # 数字のリスト
operators = ["+"] #演算子のリスト
for i, num in enumerate(numbers + operators, 1):
    btn = tk.Button(root, text=f"{num}", font=("", 30), width=4, height=2)
    btn.bind("<1>", btn_click)
    btn.grid(row=r, column=c)
    c += 1
    if i%3 == 0:
        r += 1
        c = 0
        
root.mainloop()
