from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700

def midPointCircle(xc, yc, r):
    points = []
    x, y = 0, r
    d = 1 - r
    while x <= y:
        points.extend([
            (xc+x, yc+y), (xc-x, yc+y),
            (xc+x, yc-y), (xc-x, yc-y),
            (xc+y, yc+x), (xc-y, yc+x),
            (xc+y, yc-x), (xc-y, yc-x)
        ])
        if d < 0:
            d += 2*x + 3
        else:
            d += 2*(x-y) + 5
            y -= 1
        x += 1
    return points

def draw_circle(xc, yc, r):
    glBegin(GL_POINTS)
    for x, y in midPointCircle(xc, yc, r):
        glVertex2f(x, y)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1, 0)
    glPointSize(2)

    xc, yc = 300, 400
    r = 70

    draw_circle(xc - 100, yc, r)
    draw_circle(xc, yc, r)
    draw_circle(xc + 100, yc, r)

    draw_circle(xc - 50, yc - 80, r)
    draw_circle(xc + 50, yc - 80, r)

    glutSwapBuffers()

def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0,w,0,h)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def init():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutCreateWindow(b"Olympic Rings")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glClearColor(0,0,0,1)

def main():
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()
