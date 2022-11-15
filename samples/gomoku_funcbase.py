import tkinter as tk
from tkinter import messagebox


#定数
CANVAS_SIZE = 400

NUM_LINE = 10

BOARD_COLOR = 'burlywood3' # 盤面の背景色
PLAYER1_COLOR = 'black' # Player1の石の色
PLAYER2_COLOR = 'white' # Player2の石の色

PLAYER1 = 1
PLAYER2 = 2

def create_canvas(app):
    '''ウィジェットを作成・配置する'''
    # キャンバスの作成
    canvas = tk.Canvas(
        app,
        width=CANVAS_SIZE,
        height=CANVAS_SIZE,
        highlightthickness=0
    )
    
    canvas.pack(padx=10, pady=10)
    bg_image = tk.PhotoImage(file='woodgrain.png')
    canvas.create_image(
            CANVAS_SIZE / 2,       # 画像表示位置(Canvasの中心)
            CANVAS_SIZE / 2,                   
            image=bg_image  # 表示画像データ
            )
    return canvas


def create_board(canvas):
    '''ゲームの初期化を行う'''
    board = [[None] * (NUM_LINE) for i in range(NUM_LINE)]
    interval = CANVAS_SIZE // (NUM_LINE + 1)
    offset_x = interval
    offset_y = interval
    # 縦線を描画
    for x in range(NUM_LINE):
        xs = x * interval + offset_x
        ys = offset_y
        xe = xs
        ye = (NUM_LINE - 1) * interval + offset_y
        canvas.create_line(
            xs, ys,
            xe, ye,
        )

    # 横線を描画
    for y in range(NUM_LINE):
        xs = offset_x
        ys = y * interval + offset_y
        xe = (NUM_LINE - 1) * interval + offset_x
        ye = ys
        canvas.create_line(
            xs, ys,
            xe, ye,
        ) 
    return board, offset_x, offset_y, interval       

            
def draw_disk(x, y, color):
    global canvas, interval, offset_x, offset_y
    '''円を描画する'''
    center_x = x * interval + offset_x
    center_y = y * interval + offset_y
    xs = center_x - (interval * 0.8) // 2
    ys = center_y - (interval * 0.8) // 2
    xe = center_x + (interval * 0.8) // 2
    ye = center_y + (interval * 0.8) // 2

    tag_name = 'disk_' + str(x) + '_' + str(y)
    canvas.create_oval(
        xs, ys,
        xe, ye,
        fill=color,
    )

    return tag_name

    
def intersection(offset_x, offset_y, interval, x, y):
    '''キャンバス上の座標を交点の位置に変換'''
    ix = (x - offset_x + interval // 2) // interval
    iy = (y - offset_y + interval // 2) // interval

    return ix, iy

    
def click(event):
    '''盤面がクリックされた時の処理'''
    global color
    x, y = intersection(offset_x, offset_y, interval, event.x, event.y)

    if x < 0 or x >= NUM_LINE or y < 0 or y >= NUM_LINE:
        return

    if not board[y][x]:
        place(x, y, color[player])


def place(x, y):
    '''石を置く'''
    global color
    draw_disk(x, y, color)
    board[y][x] = color

    if count(x, y, color) >= 5:
        show_result()
        return
    if player == PLAYER2:
        player = PLAYER1
    else:
        player = PLAYER2


def count(board, x, y, color):
    '''並び数をチェック'''
    count_dir = [
        (1, 0), # 右
        (1, 1), # 右下
        (0, 1), # 上
        (-1, 1), # 左下
    ]
    max = 0 #最大値
    for i, j in count_dir:
        count_num = 1
        for s in range(1, NUM_LINE):            
            xi = x + i * s
            yj = y + j * s

            if xi < 0 or xi >= NUM_LINE or yj < 0 or yj >= NUM_LINE:
                break

            if board[yj][xi] != color:
                break

            count_num += 1

        for s in range(-1, -(NUM_LINE), -1):
            xi = x + i * s
            yj = y + j * s

            if xi < 0 or xi >= NUM_LINE or yj < 0 or yj >= NUM_LINE:
                break

            if board[yj][xi] != color:
                break

            count_num += 1

        if max < count_num:
            max = count_num
    return max
    

def show_result(self):
        '''ゲーム終了時の結果を表示する'''
        winner = self.player
        if winner == PLAYER1:
            messagebox.showinfo('結果', 'プレイヤー1の勝ちです!!!')
        else:
            messagebox.showinfo('結果', 'プレイヤー2の勝ちです!!!')


def timer(canvas):
    global tmr,score
    if tmr == 0:                #timerが０になったら
        messagebox.showinfo("終了", "おわりです") #メッセージを表示
        tmr = 100                 #timerを100にして
    tmr -= 1                   #timerを減らす
    lbltimer["text"]= "timer: "+str(tmr/10)     #timerを表示
    if tmr < 30 :                               #3秒きったら
        lbltimer["foreground"]="#ff0000"        #文字の色を赤にする
    else:
        lbltimer["foreground"]="#000000"        #文字の色を黒にする
    
    canvas.after(100, timer)                         #0.1秒ごとにtimer処理を実行する


if __name__ == "__main__":
    app = tk.Tk()
    app.title('五目並べ')
    player = PLAYER1
    board = None
    color = {
        PLAYER1 : PLAYER1_COLOR,
        PLAYER2 : PLAYER2_COLOR
    }
    
    nextDisk = None
    canvas = create_canvas(app)
    board, offset_x, offset_y, interval = create_board(canvas)
    canvas.bind('<ButtonPress>', click)
    # timer(canvas)
    
    app.mainloop()    