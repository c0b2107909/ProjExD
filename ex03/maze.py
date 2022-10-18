import tkinter as tk

def key_down(event):
    global key
    key = event.keysym

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()
    key = ""
    
    root.bind("<KeyRelease>", key_down)
    
    tori = tk.PhotoImage(file="./fig/2.png")
    cx, cy = 300, 400
    canv.create_image(cx, cy, image=tori, tag="tori")
    
    root.mainloop()
    
    