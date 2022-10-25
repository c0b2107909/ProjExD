import pygame as pg
import sys
from random import randint

def main():
    """ゲームの本体関数"""
    pg.display.set_caption("逃げろ！こうかとん") #タイトル
    scrn_sfc = pg.display.set_mode((1600, 900)) #ウィンドウ
    scrn_rct = scrn_sfc.get_rect()

    # 背景
    bg_sfc = pg.image.load("fig/pg_bg.jpg") #Surface
    bg_rct = bg_sfc.get_rect() #Rect
    
    # こうかとん
    tori_sfc = pg.image.load("fig/6.png") #Surface
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect() #Rect
    tori_rct.center = 900, 400
    
    # 爆弾
    bomb_sfc = pg.Surface((20, 20))
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc,(255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = randint(0, scrn_rct.width)
    bomb_rct.centery = randint(0, scrn_rct.height)
    
    vx, vy = 1, 1
    
    
    # クロック
    clock = pg.time.Clock()
    
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct) # 貼り付け

        for event in pg.event.get():
            if event.type == pg.QUIT: # pg.QUIT = バツボタン
                return  #メイン関数から出る
        
        # こうかとん移動キー受付
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
        
        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct)
        
        pg.display.update()
        clock.tick(1000) # = 2500秒間
    
    
if __name__ == "__main__":
    pg.init() #初期化
    main() #ゲームの本体
    pg.quit() #初期化の解除
    sys.exit()