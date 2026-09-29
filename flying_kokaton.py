import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png") #こうかとん画像surfaceの作成
    kk_img = pg.transform.flip(kk_img, True, False) # 練習3こうかとん左右反転, True Trueだったら左右＋上下反転
    bg_img2 = pg.transform.flip(bg_img, True, False) # 練習8、2枚目の背景画像を反転
    kk_rct = kk_img.get_rect() # 練習10 こうかトンRectの取得
    kk_rct.center = (300, 200)
    screen.blit(kk_img, kk_rct) # 練習10：こうかとんの初期座標を設定
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed() # 練習10-3：キーの押下状態取得
        if key_lst[pg.K_UP]:
            kk_rct.move_ip((0, -1))
        if key_lst[pg.K_DOWN]:
            kk_rct.move_ip((0, +1))
    
        x = tmr % 3200 # 練習9：背景をループさせる
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [-x + 1600, 0]) # 練習7　2枚目の背景画像もう一回blit
        screen.blit(bg_img, [-x + 3200, 0])
        screen.blit(kk_img, kk_rct) # 練習4 こうかトン画像を表示（移動しないとき）
        
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()