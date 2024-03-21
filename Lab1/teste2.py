import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def wc_to_ndc(x, y, x_min, x_max, y_min, y_max):
    ndc_x = (x - x_min) / (x_max - x_min)
    ndc_y = (y - y_min) / (y_max - y_min)
    return ndc_x, ndc_y

def ndc_to_wc(ndc_x, ndc_y, x_min, x_max, y_min, y_max):
    wc_x = ndc_x * (x_max - x_min) - x_min
    wc_y = ndc_y * (y_max - y_min) - y_min
    return wc_x, wc_y

def ndc_to_dc(ndc_x, ndc_y, ndh, ndv):  
    dc_x = round(ndc_x * (ndh - 1))
    dc_y = round(ndc_y * (ndv - 1))
    return dc_x, dc_y

def draw_pixel(dc_x, dc_y):
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(dc_x, dc_y)
    glEnd()

pg.init()
info = pg.display.Info()
height = info.current_h - 100
width = info.current_w - 100
display = (width, height)
screen = pg.display.set_mode(display)
text_font = pg.font.SysFont("Arial", 30)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def main():
    while True:
        screen.fill((0,0,0))
        draw_text("Hello world", text_font, (255,255,255), 220, 150)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        pg.display.flip()

if __name__ == "__main__":
    main()
