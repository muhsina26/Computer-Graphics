from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

def display():
    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT)

    # Set line color and width
    glColor3f(0.0, 1.0, 0.0)   # green
    glLineWidth(3.0)

    # Draw triangle with lines
    glBegin(GL_LINES)

    # Base
    glVertex2f(200, 100)
    glVertex2f(600, 100)

    # Left side
    glVertex2f(200, 100)
    glVertex2f(400, 400)

    # Right side
    glVertex2f(600, 100)
    glVertex2f(400, 400)

    glEnd()

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
    glutCreateWindow(b"Task 2: Multiple Lines - Lab 1")

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glClearColor(0.0, 0.0, 0.0, 1.0)  # black background

def main():
    init_glut_window()
    glutMainLoop()

if __name__ == "__main__":
    main()
