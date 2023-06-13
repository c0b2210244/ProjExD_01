import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    koukaton_img = pg.image.load("ex01/fig/3.png")
    koukaton_1 = pg.transform.flip(koukaton_img, True, False)
    koukaton_2 = pg.transform.rotate(koukaton_1, 10)
    koukaton_list = [koukaton_1, koukaton_2]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])
        if tmr % 2 == 0:
            screen.blit(koukaton_list[0], [300, 200])
        else:
            screen.blit(koukaton_list[1], [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()