from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700


def midPointCircle(xc, yc, r):
    points = []
    x = 0
    y = r
    d = 1 - r

    while x <= y:
        points.extend([
            (xc + x, yc + y),
            (xc - x, yc + y),
            (xc + x, yc - y),
            (xc - x, yc - y),
            (xc + y, yc + x),
            (xc - y, yc + x),
            (xc + y, yc - x),
            (xc - y, yc - x)
        ])
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1
    return points


def draw_circle(xc, yc, r):
    points = midPointCircle(xc, yc, r)
    glBegin(GL_POINTS)
    for (x, y) in points:
        glVertex2f(x, y)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 0.0)
    glPointSize(2.0)

#boro circle
    xc, yc = 250, 250
    R = 150

    draw_circle(xc, yc, R)

   
    r = R // 2  
    

    value = int(r * 87 / 100)  


 
    draw_circle(xc, yc + r, r)
    draw_circle(xc, yc - r, r)
    draw_circle(xc + r, yc, r)
    draw_circle(xc - r, yc, r)
   
    draw_circle(xc + 53.5, yc + 53.55, r)
    draw_circle(xc - 53.5, yc + 53.55, r)
    draw_circle(xc + 53.5, yc - 53.55, r)
    draw_circle(xc - 53.5, yc - 53.55, r)

  
    glutSwapBuffers()


def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def init_glut_window():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(200, 100)
    glutCreateWindow(b"Flower of Circles - Midpoint Circle Algorithm")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glClearColor(0.0, 0.0, 0.0, 1.0)


def main():
    init_glut_window()
    glutMainLoop()


if __name__ == "__main__":
    main()
