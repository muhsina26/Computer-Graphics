from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Line endpoints (you can change these)
x1, y1 = 100, 100
x2, y2 = 700, 400

def midpoint_line(x1, y1, x2, y2):
    # Calculate dx and dy
    dx = x2 - x1
    dy = y2 - y1

    # Initialize starting point
    x = x1
    y = y1

    # Decision parameter
    p = 2 * dy - dx

    # Start drawing pixels
    glBegin(GL_POINTS)
    glVertex2f(x, y)

    for k in range(dx):
        if p < 0:
            # Next pixel is (x+1, y)
            x = x + 1
            p = p + 2 * dy
        else:
            # Next pixel is (x+1, y+1)
            x = x + 1
            y = y + 1
            p = p + 2 * dy - 2 * dx

        # Plot next pixel
        glVertex2f(x, y)

    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 0.0)  # Yellow
    glPointSize(3.0)

    midpoint_line(x1, y1, x2, y2)

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
    glutCreateWindow(b"Midpoint Line Drawing Algorithm - OpenGL")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glClearColor(0.0, 0.0, 0.0, 1.0)


def main():
    init_glut_window()
    glutMainLoop()


if __name__ == "__main__":
    main()
