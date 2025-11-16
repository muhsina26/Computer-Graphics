from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

def draw_polygon(xc, yc, r, sides):
    glBegin(GL_LINE_LOOP)
    for i in range(sides):
        theta = 2 * math.pi * i / sides
        x = xc + r * math.cos(theta)
        y = yc + r * math.sin(theta)
        glVertex2f(x, y)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(2)
    glColor3f(1, 0, 1)

    # Draw various polygons
    draw_polygon(200, 300, 80, 3)   # Triangle
    draw_polygon(400, 300, 80, 5)   # Pentagon
    draw_polygon(600, 300, 80, 8)   # Octagon

    glutSwapBuffers()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, w, 0, h)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutCreateWindow(b"Polygon Approximation - Circle Logic")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glClearColor(0, 0, 0, 1)
    glutMainLoop()

if __name__ == "__main__":
    main()


#venv\Scripts\activate
