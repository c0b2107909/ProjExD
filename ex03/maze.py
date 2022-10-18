import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm

index = 0 #イメージのインデックス番号

def key_down(event):
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""
    
    
def main_proc():
    global mx, my, index
    if key == "Up":
        my -= 1
    elif key == "Down":
        my += 1    
    elif key == "Right":
        mx += 1
    elif key == "Left":
        mx -= 1
    elif key == "r":
        mx, my == 1, 1
        
    if maze_lst[my][mx] == 0: #床の処理
        canv.coords("tori", cx * mx + 50, cy * my + 50)   
         
    elif maze_lst[my][mx] == 1: #穴の処理
        mx, my = 1, 1
        canv.coords("tori", cx * mx + 50, cy * my + 50)  
            
    elif maze_lst[my][mx] == 2:#ゴールの処理
        index = 1
        canv.create_image(cx, cy, image=imgs_ls[index], tag="goal")
        canv.delete('tori')
        canv.coords("goal", cx * mx + 50, cy * my + 50)
        tkm.showinfo("ゴールしました", "ゴールしたので、ウィンドウを閉じます")
        root.destroy()

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
    maze_lst[7][13] = 2 #ゴールの設定
    
    mm.show_maze(canvas=canv, maze_lst=maze_lst)
    
    mx, my = 1, 1
    cx, cy = 100 * mx, 100 * my
    imgs_ls = [tk.PhotoImage(file="./fig/2.png"), tk.PhotoImage(file="./fig/6.png")] #イメージのリスト
    
    canv.create_image(cx, cy, image=imgs_ls[index], tag="tori")
    
    main_proc()

    root.mainloop()
    
    