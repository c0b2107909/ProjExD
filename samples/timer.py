import tkinter as tk
import tkinter.font as font
import tkinter.ttk as ttk

root=tk.Tk()
root.title("Timer")
text_sec=tk.StringVar()
text_sec.set("20")
my_font=font.Font(size=20)


buff_sec=tk.StringVar()
buff_sec.set("20")

text_start_stop=tk.StringVar()
text_start_stop.set("START")

progressbar=ttk.Progressbar(root,orient="horizontal",length=230,mode="determinate")
progressbar.grid(row=2,column=0,columnspan=7)

start=True
check=True
stop=False

def start():
    global start,check,text_min,text_sec,start,check,stop,value_time
    start=False
    if check==True and stop==True:
        start=True
        text_start_stop.set("STOP")
        timer()
    
    elif check==False and stop==True:
        count_sec=int(buff_sec.get())
        buff_sec.set("0")
        buff_sec.set(count_sec)
        check=True
        text_start_stop.set("START")
        
    else:
        start=True
        stop=True
        text_start_stop.set("STOP")
        buff_sec.set(int(text_sec.get()))
        maximum_time=int(buff_sec.get())
        #print(maximum_time)
        value_time=0
        progressbar.configure(maximum=maximum_time,value=value_time)
        timer()
    
        

def timer():
    global start,buff_sec,text_min,text_sec,check,value_time,div_time
    if start==True:
        if int(buff_sec.get())==0:
            pass
        else:
            check=False
            time_sec=int(buff_sec.get())
            if int(buff_sec.get())==0:
                start=False
                time_sec=0
                buff_sec.set(str(time_sec))

            
def stop():
    global start,check,stop
    start=True
    check=True
    stop=False
    time_sec=0
    buff_sec.set(str(time_sec))

entry1=tk.Entry(root,width=2,font=my_font,textvariable=text_sec)
entry1.grid(row=0,column=3)

label_sec=tk.Label(root,text=u"秒")
label_sec.grid(row=0,column=4)

button=tk.Button(root,textvariable=text_start_stop,command=start)
button.grid(row=0,column=5)

# labbel=tk.Label(root,font=my_font,textvariable=buff_min)
# labbel.grid(row=1,column=1,columnspan=1)

labbel=tk.Label(root,font=my_font,textvariable=buff_sec)
labbel.grid(row=1,column=3,columnspan=1)

labbel=tk.Label(root,text="秒")
labbel.grid(row=1,column=4,columnspan=1)

root.mainloop()