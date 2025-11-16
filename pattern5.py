from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

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
    for x, y in midPointCircle(int(round(xc)), int(round(yc)), int(round(r))):
        glVertex2f(x, y)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.7, 0.0)
    glPointSize(2.0)

    xc, yc = 350, 350
    bigR = 140
    petalR = 70

    # central big circle
    draw_circle(xc, yc, bigR)

    # petals at 60-degree steps
    for deg in range(0, 360, 60):
        rad = math.radians(deg)
        # petal center sits at distance = bigR - (petalR/2) for overlap look
        dist = bigR - (petalR // 2)
        px = xc + math.cos(rad) * dist
        py = yc + math.sin(rad) * dist
        draw_circle(px, py, petalR)

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
    glutCreateWindow(b"Hex Flower")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glClearColor(0, 0, 0, 1)

def main():
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()
