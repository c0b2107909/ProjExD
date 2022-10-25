import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ！こうかとん") #タイトル
    scrn_sfc = pg.display.set_mode((1600, 900)) #ウィンドウ

    # 背景
    bg_sfc = pg.image.load("fig/pg_bg.png") #Surface
    bg_rct = bg_sfc.get_rect() #Rect
    bg_rct.center = 0, 0
    scrn_sfc.blit(bg_sfc, bg_rct) # 貼り付け
    
    pg.display.update()
    clock = pg.time.Clock()
    clock.tick(0.2) #fps 0.2 = 5秒間
    
    
if __name__ == "__main__":
    pg.init() #初期化
    main() #ゲームの本体
    pg.quit() #初期化の解除
    sys.exit()