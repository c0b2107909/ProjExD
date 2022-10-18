import tkinter as tk
import maze_maker

def key_down(event):
    global key
    key = event.keysym
    print(key)


def key_up(event):
    global key
    key = ""
    
    
def main_proc():
    global cx, cy
    if key == "Up":
        cy -= 20
    elif key == "Down":
        cy += 20
    elif key == "Right":
        cx += 20
    elif key == "Left":
        cx -= 20
    canv.coords("tori", cx, cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()
    key = "" #現在押されているキーを表す
    
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    
    tori = tk.PhotoImage(file="./fig/2.png")
    cx, cy = 300, 400
    canv.create_image(cx, cy, image=tori, tag="tori")
    
    main_proc()
    
    root.mainloop()
    
    