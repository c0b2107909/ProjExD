import pygame as pg
import sys

def main():
    """ゲームの本体関数"""
    pg.display.set_caption("逃げろ！こうかとん") #タイトル
    scrn_sfc = pg.display.set_mode((1600, 900)) #ウィンドウ

    # 背景
    bg_sfc = pg.image.load("fig/pg_bg.jpg") #Surface
    bg_rct = bg_sfc.get_rect() #Rect
    
    # こうかとん
    tori_sfc = pg.image.load("fig/6.png") #Surface
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect() #Rect
    tori_rct.center = 900, 400
    
    # クロック
    clock = pg.time.Clock()
    
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct) # 貼り付け

        for event in pg.event.get():
            if event.type == pg.QUIT: # pg.QUIT = バツボタン
                return  #メイン関数から出る
        
        key_stats = pg.key.get_pressed()
        if key_stats[pg.K_UP]:
            tori_rct.centery -= 1
        if key_stats[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_stats[pg.K_RIGHT]:
            tori_rct.centerx += 1
        if key_stats[pg.K_LEFT]:
            tori_rct.centerx -= 1
            
            
        scrn_sfc.blit(tori_sfc, tori_rct) # 貼り付け
        
        pg.display.update()
        clock.tick(1000) # = 2500秒間
    
    
if __name__ == "__main__":
    pg.init() #初期化
    main() #ゲームの本体
    pg.quit() #初期化の解除
    sys.exit()