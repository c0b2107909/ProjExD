import tkinter as tk
import tkinter.messagebox as tkm

#print("hello")

root = tk.Tk() #Tk class のインスタンスを生成
root.title("title")
root.geometry("500x200")

label = tk.Label(root,
                 text = "ラベルを書いてみた件", 
                 font = ("Ricty Diminished", 20),
                 )
label.pack() #ウィンドウへの貼付け

def button_click(event):
    btn = event.widget # どのボタンが押されたか 引数を辞書で取得
    txt = btn["text"] # btn辞書の"text"
    tkm.showwarning("txt", f"[{txt}]ボタンが押されました")

button = tk.Button(root, text="押すな", font=("", 30), bg="yellow", fg="red", )
button.bind("<1>", button_click) # <1> = 左クリック
button.pack() #貼付け

entry = tk.Entry(root, width=30, font=("", 20))
entry.insert(tk.END, "fugapiyo")
entry.pack() #貼り付け

root.mainloop()

