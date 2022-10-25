import pygame as pg
import sys
from random import randint, uniform

def check_bound(obj_rct, scrn_rct):
    """
    obj_rct = こうかとん・爆弾rct
    scrn_rct = スクリーンrct
    領域内：-1・領域内：1
    """
    yoko, tate = 1, 1
    if obj_rct.left < scrn_rct.left or scrn_rct.right < obj_rct.right: # x軸の判定
        yoko = -1
    if obj_rct.top < scrn_rct.top or scrn_rct.bottom < obj_rct.bottom: # y軸の判定
        tate = -1
    return yoko, tate

def main():
    """ゲームの本体関数"""
    pg.display.set_caption("逃げろ！こうかとん") #タイトル
    scrn_sfc = pg.display.set_mode((1600, 900)) #ウィンドウ
    scrn_rct = scrn_sfc.get_rect()
    time = pg.time.get_ticks()

    # 背景
    bg_sfc = pg.image.load("fig/pg_bg.jpg") #Surface
    bg_rct = bg_sfc.get_rect() #Rect
    
    # こうかとん
    tori_size = 2.0
    tori_sfc = pg.image.load("fig/6.png") #Surface
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, tori_size)
    tori_rct = tori_sfc.get_rect() #Rect
    tori_rct.center = 900, 400
    kx, ky = 2, 2 #こうかとん速度
    
    # 爆弾（赤）
    bomb_red_sfc = pg.Surface((20, 20))
    bomb_red_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_red_sfc,(255, 0, 0), (10, 10), 10)
    bomb_red_rct = bomb_red_sfc.get_rect()
    bomb_red_rct.centerx = randint(0, scrn_rct.width)
    bomb_red_rct.centery = randint(0, scrn_rct.height)
    vx_r, vy_r = 1, 1 # 爆弾移動速度
    
    # 爆弾（緑）
    bomb_green_sfc = pg.Surface((40, 40))
    bomb_green_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_green_sfc,(0, 255, 0), (20, 20), 20)
    bomb_green_rct = bomb_green_sfc.get_rect()
    bomb_green_rct.centerx = randint(0, scrn_rct.width)
    bomb_green_rct.centery = randint(0, scrn_rct.height)
    vx_g, vy_g = 1, 1 
    
    # クロック
    clock = pg.time.Clock()
    
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct) # 貼り付け

        for event in pg.event.get():
            if event.type == pg.QUIT: # pg.QUIT = バツボタン
                return  #メイン関数から出る
        
        # こうかとん移動
        key_stats = pg.key.get_pressed()
        if key_stats[pg.K_UP]: tori_rct.centery -= ky
        if key_stats[pg.K_DOWN]: tori_rct.centery += ky
        if key_stats[pg.K_RIGHT]: tori_rct.centerx += kx
        if key_stats[pg.K_LEFT]: tori_rct.centerx -= kx
        # 画面外判定        
        yoko, tate = check_bound(tori_rct, scrn_rct)
        if yoko == -1:
            if key_stats[pg.K_LEFT]:
                tori_rct.centerx += kx
            if key_stats[pg.K_RIGHT]:
                tori_rct.centerx -= kx       
        if tate == -1:
            if key_stats[pg.K_UP]:
                tori_rct.centery += ky
            if key_stats[pg.K_DOWN]:
                tori_rct.centery -= ky  
        # こうかとん加速
        if key_stats[pg.K_k]:
            ky += 0.1
            kx += 0.1
        scrn_sfc.blit(tori_sfc, tori_rct) # 貼り付け
        
        #爆弾（赤）移動
        yoko, tate = check_bound(bomb_red_rct, scrn_rct)
        vx_r *= yoko
        vy_r *= tate
        if time % 3000:
            vx_r += uniform(-0.5, 0.5)
            vy_r += uniform(-0.5, 0.5)
        bomb_red_rct.move_ip(vx_r, vy_r)
        scrn_sfc.blit(bomb_red_sfc, bomb_red_rct)
        
        #爆弾（緑）移動
        yoko, tate = check_bound(bomb_green_rct, scrn_rct)
        vx_g *= yoko
        vy_g *= tate
        bomb_green_rct.move_ip(vx_g, vy_g)
        scrn_sfc.blit(bomb_green_sfc, bomb_green_rct)
        
        
        #あたり判定 爆弾（赤）
        if tori_rct.colliderect(bomb_red_rct):
            fonto = pg.font.Font(None, 100)
            txt = fonto.render("GAMEOVER", True, "RED")        
            scrn_sfc.blit(txt, (800, 450))
            pg.display.update()
            pg.time.wait(1000)
            return
        
        #あたり判定 爆弾（緑）
        if tori_rct.colliderect(bomb_green_rct):
            idx = randint(0, 9)
            tori_sfc = pg.image.load(f"fig/{idx}.png") #Surface
            tori_sfc = pg.transform.rotozoom(tori_sfc, 0, tori_size)
        
        pg.display.update()
        clock.tick(1000) # = 2500秒間
    
    
if __name__ == "__main__":
    pg.init() #初期化
    main() #ゲームの本体
    pg.quit() #初期化の解除
    sys.exit()