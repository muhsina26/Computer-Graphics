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
    glColor3f(1.0, 1.0, 0.0)   # yellow star
    glLineWidth(2.0)

    # Draw a star using multiple lines
    glBegin(GL_LINES)

    # 5-point star coordinates
    glVertex2f(400, 500)   # top point
    glVertex2f(300, 300)

    glVertex2f(300, 300)
    glVertex2f(500, 420)

    glVertex2f(500, 420)
    glVertex2f(250, 420)

    glVertex2f(250, 420)
    glVertex2f(450, 300)

    glVertex2f(450, 300)
    glVertex2f(400, 500)

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
