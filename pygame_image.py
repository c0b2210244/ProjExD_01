import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    koukaton_img = pg.image.load("ex01/fig/3.png")
    koukaton_1 = pg.transform.flip(koukaton_img, True, False)
    koukaton_2 = pg.transform.rotozoom(koukaton_1, 10, 1.0)
    koukaton_list = [koukaton_1, koukaton_2]
    tmr = 0
    bg_x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-bg_x, 0])
        if tmr % 2 == 0:
            screen.blit(koukaton_list[0], [300, 200])
        else:
            screen.blit(koukaton_list[1], [300, 200])
        pg.display.update()
        tmr += 1
        bg_x += 1
        if bg_x > 1600:
            bg_x = 0
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()