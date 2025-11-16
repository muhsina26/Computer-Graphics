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
            (xc + x, yc + y), (xc - x, yc + y),
            (xc + x, yc - y), (xc - x, yc - y),
            (xc + y, yc + x), (xc - y, yc + x),
            (xc + y, yc - x), (xc - y, yc - x)
        ])
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1
    return points

def draw_circle(xc, yc, r):
    glBegin(GL_POINTS)
    for x, y in midPointCircle(int(xc), int(yc), int(r)):
        glVertex2f(x, y)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.6, 0.9, 0.2)
    glPointSize(2.0)

    xc = 350
    yc = 600
    R = 90

    # draw stacked circles, shrinking as we go down
    for i in range(7):
        draw_circle(xc, yc, R)
        yc -= int(R * 0.95)  # move down by nearly the diameter
        R = max(8, R - 10)   # shrink radius, but not below 8

    glutSwapBuffers()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, w, 0, h)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def init():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutCreateWindow(b"Vertical Stack")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glClearColor(0, 0, 0, 1)

def main():
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()
