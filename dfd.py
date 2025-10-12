from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Line endpoints (you can change these)
x1, y1 = 100, 100
x2, y2 = 700, 400

def dda_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    # Determine number of steps
    steps = int(max(abs(dx), abs(dy)))

    # Handle case where both points are same
    if steps == 0:
        glBegin(GL_POINTS)
        glVertex2f(x1, y1)
        glEnd()
        return

    # Calculate increments
    x_inc = dx / steps
    y_inc = dy / steps

    # Start point
    x, y = x1, y1

    # Draw points
    glBegin(GL_POINTS)
    for i in range(steps + 1):
        glVertex2f(round(x), round(y))
        x += x_inc
        y += y_inc
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)  # red
    glPointSize(3.0)

    dda_line(x1, y1, x2, y2)

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
    glutCreateWindow(b"DDA Line Drawing Algorithm - OpenGL")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glClearColor(0.0, 0.0, 0.0, 1.0)


def main():
    init_glut_window()
    glutMainLoop()


if __name__ == "__main__":
    main()
