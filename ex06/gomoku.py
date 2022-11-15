import tkinter as tk
from tkinter import messagebox

# 定数
SIZE = 700
LINE_NUM = 10 #ラインの数

PLAYER1_COLOR = 'black' # Player1の石の色
PLAYER2_COLOR = 'white' # Player2の石の色

PLAYER1 = 1
PLAYER2 = 2


class Gobang():
    def __init__(self, master):
        '''コンストラクタ'''
        self.master = master
        self.player = PLAYER1
        self.board = None
        self.color = {
            PLAYER1 : PLAYER1_COLOR,
            PLAYER2 : PLAYER2_COLOR
        }
        self.nextDisk = None

        self.create_canvas()

        # イベントの設定
        self.set_event()

        # 五目並べゲームの初期化
        self.init_gobang()
        
        # self.timer()


    def create_canvas(self):
        '''ウィジェットを作成・配置する'''
        # キャンバスの作成
        self.canvas = tk.Canvas(
            self.master,
            width=SIZE,
            height=SIZE,
            highlightthickness=0
        )
        
        self.canvas.pack(padx=10, pady=10)
        self.bg_image = tk.PhotoImage(file='woodgrain.png')
        self.canvas.create_image(
                SIZE / 2,       # 画像表示位置(Canvasの中心)
                SIZE / 2,                   
                image=self.bg_image  # 表示画像データ
                )
        
        # self.lbltimer.pack()
        # self.lbltimer.place(x=SIZE / 2, y=SIZE / 2)   

    def set_event(self):
        '''イベントを設定する'''
        self.canvas.bind('<ButtonPress>', self.click)


    def init_gobang(self):
        '''ゲームの初期化を行う'''

        self.board = [[None] * (LINE_NUM) for i in range(LINE_NUM)]

        self.interval = SIZE // (LINE_NUM + 1)

        self.offset_x = self.interval
        self.offset_y = self.interval

        # 縦線を描画
        for x in range(LINE_NUM):
            xs = x * self.interval + self.offset_x
            ys = self.offset_y
            xe = xs
            ye = (LINE_NUM - 1) * self.interval + self.offset_y

            self.canvas.create_line(
                xs, ys,
                xe, ye,
            )

        # 横線を描画
        for y in range(LINE_NUM):
            xs = self.offset_x
            ys = y * self.interval + self.offset_y
            xe = (LINE_NUM - 1) * self.interval + self.offset_x
            ye = ys
                
            self.canvas.create_line(
                xs, ys,
                xe, ye,
            )

    def draw_disk(self, x, y, color):
        '''円を描画する'''

        # 中心座標を計算
        center_x = x * self.interval + self.offset_x
        center_y = y * self.interval + self.offset_y

        # 開始座標と終了座標を計算
        xs = center_x - (self.interval * 0.8) // 2
        ys = center_y - (self.interval * 0.8) // 2
        xe = center_x + (self.interval * 0.8) // 2
        ye = center_y + (self.interval * 0.8) // 2
        
        # 円の描画
        tag = 'disk_' + str(x) + '_' + str(y)
        self.canvas.create_oval(
            xs, ys,
            xe, ye,
            fill=color,
        )

        return tag

    def intersection(self, x, y):
        '''キャンバス上の座標を交点の位置に変換'''

        ix = (x - self.offset_x + self.interval // 2) // self.interval
        iy = (y - self.offset_y + self.interval // 2) // self.interval

        return ix, iy

    def click(self, event):
        '''盤面がクリックされた時の処理'''
        x, y = self.intersection(event.x, event.y)

        if x < 0 or x >= LINE_NUM or y < 0 or y >= LINE_NUM:
            return

        if not self.board[y][x]:
            self.place(x, y, self.color[self.player])

    def place(self, x, y, color):
        '''石を置く'''
        self.draw_disk(x, y, color)
        self.board[y][x] = color

        if self.count(x, y, color) >= 5:
            self.showResult()
            return

        if self.player == PLAYER2:
            self.player = PLAYER1
        else:
            self.player = PLAYER2

    def count(self, x, y, color):
        '''石の並び数をチェック'''

        count_dir = [
            (1, 0), # 右
            (1, 1), # 右下
            (0, 1), # 上
            (-1, 1), # 左下
        ]

        max = 0 #最大値

        for i, j in count_dir:
            count_num = 1
            for s in range(1, LINE_NUM):
                
                xi = x + i * s
                yj = y + j * s

                if xi < 0 or xi >= LINE_NUM or yj < 0 or yj >= LINE_NUM:
                    break

                if self.board[yj][xi] != color:
                    break

                count_num += 1

            for s in range(-1, -(LINE_NUM), -1):
                xi = x + i * s
                yj = y + j * s

                if xi < 0 or xi >= LINE_NUM or yj < 0 or yj >= LINE_NUM:
                    break

                if self.board[yj][xi] != color:
                    break

                count_num += 1
            if max < count_num:
                max = count_num
        return max

    def show_result(self):
        '''ゲーム終了時の結果を表示する'''
        winner = self.player
        if winner == PLAYER1:
            messagebox.showinfo('結果', 'プレイヤー1の勝ち')
        else:
            messagebox.showinfo('結果', 'プレイヤー2の勝ち')
    

if __name__ == "__main__":
    app = tk.Tk()
    app.title('五目並べ')
    gobang = Gobang(app)
    app.mainloop()