import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""
    
    
def main_proc():
    global mx, my
    if key == "Up":
        my -= 1
    elif key == "Down":
        my += 1    
    elif key == "Right":
        mx += 1
    elif key == "Left":
        mx -= 1
    if maze_lst[my][mx] == 0: #床の処理
        canv.coords("tori", cx * mx + 50, cy * my + 50)
        
    elif maze_lst[my][mx] == 1: #壁の処理
        if key == "Up":
            my += 1
        elif key == "Down":
            my -= 1    
        elif key == "Right":
            mx -= 1
        elif key == "Left":
            mx += 1
        
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()
    key = "" #現在押されているキーを表す
    
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    

    
    maze_lst = mm.make_maze(15, 9)
    mm.show_maze(canvas=canv, maze_lst=maze_lst)
    
    tori = tk.PhotoImage(file="./fig/2.png")
    mx, my = 1, 1
    cx, cy = 100 * mx, 100 * my
    canv.create_image(cx, cy, image=tori, tag="tori")
    
    main_proc()
    print(maze_lst)
    root.mainloop()
    
    