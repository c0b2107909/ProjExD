import tkinter as tk
import tkinter.messagebox as tkm

def count_up():
    global tmr, jid
    tmr += 1
    label["text"] = tmr
    jid = root.after(1000, count_up)
    
def key_down(event):
    global jid
    if jid != None:
        root.after_cancel(jid)
        jid = None
        return
    # key = event.keysym
    # tkm.showinfo("キー押下", f"{key}が押されました")
    jid = root.after(1000, count_up)

if __name__ == "__main__":
    root = tk.Tk()
    label = tk.Label(root, font=("", 80))
    label.pack() #ウィンドウに貼り付け
    
    tmr = 0
    jid = None
    root.after(100, count_up)
    
    root.bind("<KeyPress>", key_down)
    
    tori = tk.PhotoImage(file="./fig/5.png")
    cx, cy = 300, 400
    root.create_image(cx, cy, image=tori, tag="tori")
    
    root.mainloop()
    
    