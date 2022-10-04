from ast import operator
import tkinter as tk
import tkinter.messagebox as tkm

def btn_click(event):
    btn = event.widget
    num = btn["text"]
    if btn["text"] in operators and entry.get()[-1] in operators:
        pass
    else:  
        entry.insert(tk.END, num)
    #tkm.showinfo(txt, f"[{txt}]ボタンが押されました")
    
# def ac_click(event):
#     entry.delete(0, tk.END)
    
def delete_click(event):
    str = entry.get()[:-1]
    entry.delete(0, tk.END)
    entry.insert(tk.END, str)
    
    
def enter_bg(event):
    event.widget['bg'] = '#b0c4de'
    
def leave_bg(event):
    event.widget['bg'] = "SystemButtonFace"
     
def equal_click(event):
    try:
        calc = entry.get()
        calc = calc.replace("×", "*")
        calc = calc.replace("÷", "/")
        result = eval(calc)
    except ZeroDivisionError as e:
        result = e
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)
    

root = tk.Tk()
root.title("電卓")
root.geometry("410x590")

#------テキスト入力欄------

entry = tk.Entry(width = 14, justify="right", font = ("Times New Roman", 40))
entry.grid(row=0 ,column=0, columnspan=4)

#------その他ボタン------
# btns = ["%", "CE", "C", "1/x", "x^2", "√x"]
# r, c = 1, 0 # r : 行を表す変数/c : 列を表す変数
# for i, num in enumerate(btns, 1):
#     btn = tk.Button(root, text=f"{num}", font=("", 30), width=4, height=2)
#     btn.bind("<1>", btn_click)
#     btn.bind("<Enter>", enter_bg)
#     btn.bind("<Leave>", leave_bg)
#     btn.grid(row=r, column=c)
#     c += 1
#     if i % 3 == 0:
#         r += 1
#         c = 0    

#------数字ボタン------
numbers = [i for i in range(9, -1, -1)] # 数字のリスト
r, c = 1, 2 # r : 行を表す変数/c : 列を表す変数
for i, num in enumerate(numbers, 1):
    btn = tk.Button(root, text=f"{num}", font=("", 30), width=4, height=2)
    btn.bind("<1>", btn_click)
    btn.bind("<Enter>", enter_bg)
    btn.bind("<Leave>", leave_bg)
    btn.grid(row=r, column=c)
    c -= 1
    if i % 3 == 0:
        r += 1
        c = 2
        if i == 9:
            c = 1

#-----ACボタン-------
# ac_btn = tk.Button(root, text=f"AC", font=("", 30), width=4, height=2)
# ac_btn.bind("<1>", ac_click)
# ac_btn.bind("<Enter>", enter_bg)
# ac_btn.bind("<Leave>", leave_bg)
# ac_btn.grid(row=2, column=3)

#-----演算子ボタン

operators = ["÷", "×", "-", "+"] #演算子のリスト
for i, op in enumerate(operators, 1):
    btn = tk.Button(root, text=f"{op}", font=("", 30), width=4, height=2)
    btn.bind("<1>", btn_click)
    btn.bind("<Enter>", enter_bg)
    btn.bind("<Leave>", leave_bg)
    btn.grid(row=i, column=3)
    
#------デリートボタン----
delete_btn = tk.Button(root, text=f"del", font=("", 30), width=4, height=2)
delete_btn.bind("<1>", delete_click)
delete_btn.bind("<Enter>", enter_bg)
delete_btn.bind("<Leave>", leave_bg)
delete_btn.grid(row=r, column=c)

#----イコールボタン
equal_btn = tk.Button(root, text=f"=", font=("", 30), width=4, height=2)
equal_btn.bind("<1>", equal_click)
equal_btn.bind("<Enter>", enter_bg)
equal_btn.bind("<Leave>", leave_bg)
equal_btn.grid(row=r, column=c + 2)



root.mainloop()


