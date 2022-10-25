import pygame as pg
import sys

def main():
    """ゲームの本体関数"""
    pg.display.set_caption("逃げろ！こうかとん") #タイトル
    scrn_sfc = pg.display.set_mode((1600, 900)) #ウィンドウ

    # 背景
    bg_sfc = pg.image.load("fig/pg_bg.jpg") #Surface
    bg_rct = bg_sfc.get_rect() #Rect
    
    # クロック
    clock = pg.time.Clock()
    
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct) # 貼り付け
        pg.display.update()
        
        for event in pg.event.get():
            if event.type == pg.QUIT: # pg.QUIT = バツボタン
                return  #メイン関数から出る
        
        clock.tick(1000) # = 2500秒間
    
    
if __name__ == "__main__":
    pg.init() #初期化
    main() #ゲームの本体
    pg.quit() #初期化の解除
    sys.exit()