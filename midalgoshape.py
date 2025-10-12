from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Midpoint line algorithm
def midpoint_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    x, y = x1, y1

    # Handle slope < 1 and slope > 1 separately
    if abs(dx) > abs(dy):  # slope < 1
        p = 2 * abs(dy) - abs(dx)
        x_inc = 1 if dx > 0 else -1
        y_inc = 1 if dy > 0 else -1
        glBegin(GL_POINTS)
        for _ in range(abs(dx) + 1):
            glVertex2f(x, y)
            x += x_inc
            if p < 0:
                p += 2 * abs(dy)
            else:
                y += y_inc
                p += 2 * abs(dy) - 2 * abs(dx)
        glEnd()
    else:  # slope >= 1
        p = 2 * abs(dx) - abs(dy)
        x_inc = 1 if dx > 0 else -1
        y_inc = 1 if dy > 0 else -1
        glBegin(GL_POINTS)
        for _ in range(abs(dy) + 1):
            glVertex2f(x, y)
            y += y_inc
            if p < 0:
                p += 2 * abs(dx)
            else:
                x += x_inc
                p += 2 * abs(dx) - 2 * abs(dy)
        glEnd()


# Draw basic shapes
def draw_shapes():
    # Triangle (roof of house)
    midpoint_line(300, 400, 400, 500)
    midpoint_line(400, 500, 500, 400)
    midpoint_line(500, 400, 300, 400)

    # House rectangle
    midpoint_line(320, 200, 320, 400)
    midpoint_line(480, 200, 480, 400)
    midpoint_line(320, 200, 480, 200)

    # Tree trunk
    midpoint_line(600, 200, 600, 350)
    midpoint_line(620, 200, 620, 350)
    midpoint_line(600, 200, 620, 200)

    # Tree branches (triangle)
    midpoint_line(580, 350, 610, 450)
    midpoint_line(610, 450, 640, 350)
    midpoint_line(580, 350, 640, 350)


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 0.0)  # Yellow
    glPointSize(3.0)

    draw_shapes()

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
    glutCreateWindow(b"Midpoint Algorithm Shapes - OpenGL")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glClearColor(0.0, 0.0, 0.0, 1.0)


def main():
    init_glut_window()
    glutMainLoop()


if __name__ == "__main__":
    main()
