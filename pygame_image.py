import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img_rev = pg.transform.flip(bg_img, True, False)
    koukaton_img = pg.image.load("ex01/fig/3.png")
    angle = 0
    koukaton_1 = pg.transform.flip(koukaton_img, True, False)
    tmr = 0
    bg_x = 0
    plus_angle = 0.1
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        screen.blit(bg_img, [-bg_x, 0])
        screen.blit(bg_img_rev, [1600 - bg_x, 0])
        screen.blit(bg_img, [3200 - bg_x, 0])

        koukaton_2 = pg.transform.rotozoom(koukaton_1, angle, 1.0)
        screen.blit(koukaton_2, [300, 200])
        pg.display.update()
        tmr += 1
        angle += plus_angle
        if angle > 10 or angle <= 0:
            plus_angle *= -1
        bg_x += 1
        if bg_x >= 3200:
            bg_x = 0
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()