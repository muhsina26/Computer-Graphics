from OpenGL.GL import *             # Core OpenGL functions (glBegin, glVertex, glClear, etc.)
from OpenGL.GLU import *            # Utility library (gluOrtho2D)
from OpenGL.GLUT import *           # GLUT functions (window creation, main loop)

# Window size constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Simple line coordinates
X0, Y0 = 100, 80
X1, Y1 = 600, 400

def display():
    # Clear screen
    glClear(GL_COLOR_BUFFER_BIT)

    # Set line color (r,g,b)
    glColor3f(0.0, 1.0, 0.0)   # green

    # Set line width
    glLineWidth(3.0)

    # Draw a single line
    glBegin(GL_LINES)
    glVertex2f(X0, Y0)
    glVertex2f(X1, Y1)
    glEnd()

    glutSwapBuffers()   # swap front & back buffers

def reshape(width, height):
    # Set viewport
    glViewport(0, 0, width, height)

    # Switch to projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Orthographic projection (2D pixel coordinates)
    gluOrtho2D(0, width, 0, height)

    # Back to modelview
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def init_glut_window():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)   # double buffering + RGBA
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(200, 100)
    glutCreateWindow(b"Basic OpenGL Window - Lab 1")

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    # Background color (black)
    glClearColor(0.0, 0.0, 0.0, 1.0)

def main():
    init_glut_window()
    glutMainLoop()

if __name__ == "__main__":
    main()
