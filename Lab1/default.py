import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_pixel(dc_x, dc_y):
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(dc_x, dc_y) 
    glEnd()


pg.init()
info = pg.display.Info()
height = info.current_h
width = info.current_w 
display = (width, height)
screen = pg.display.set_mode(display, DOUBLEBUF | OPENGL)

def main():

    gluOrtho2D(-width/2, width/2, -height/2, height/2)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        pg.display.flip()

if __name__ == "__main__":
    main()