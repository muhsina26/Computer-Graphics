from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.8, 1.0)   # cyan blue
    glLineWidth(3.0)

    # Rectangle coordinates
    x1, y1 = 200, 150  # bottom-left
    x2, y2 = 600, 400  # top-right

    # Draw rectangle using 4 corners
    glBegin(GL_LINE_LOOP)
    glVertex2f(x1, y1)   # bottom-left
    glVertex2f(x2, y1)   # bottom-right
    glVertex2f(x2, y2)   # top-right
    glVertex2f(x1, y2)   # top-left
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
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(200, 100)
    glutCreateWindow(b"Rectangle using Lines - Lab 1")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glClearColor(0.0, 0.0, 0.0, 1.0)

def main():
    init_glut_window()
    glutMainLoop()

if __name__ == "__main__":
    main()
