# scene_lines.py
# Simple scene using only lines: house with triangular roof + tree with branches
# Requires: PyOpenGL, PyOpenGL_accelerate, and GLUT (from FreeGLUT)
# Run: python scene_lines.py

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Window size constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# -------------------------
# Drawing helper functions
# -------------------------

def draw_house():
    """
    Draw a house composed of:
    - rectangular base (GL_LINE_LOOP)
    - triangular roof (GL_LINE_LOOP)
    - door (GL_LINE_LOOP)
    - window (crossed lines inside a square)
    All shapes are drawn using only line primitives.
    """
    # House base (rectangle)
    glColor3f(0.9, 0.6, 0.2)   # brown-ish outline for the house base
    glLineWidth(3.0)
    glBegin(GL_LINE_LOOP)
    # bottom-left, bottom-right, top-right, top-left
    glVertex2f(200, 150)   # (x1, y1)
    glVertex2f(500, 150)   # (x2, y1)
    glVertex2f(500, 350)   # (x2, y2)
    glVertex2f(200, 350)   # (x1, y2)
    glEnd()

    # Roof (triangle sitting on top of the rectangle)
    glColor3f(0.7, 0.1, 0.1)  # dark red outline for roof
    glLineWidth(3.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(180, 350)  # left overhang
    glVertex2f(350, 470)  # apex (peak) of roof
    glVertex2f(520, 350)  # right overhang
    glEnd()

    # # Door (smaller rectangle centered on base)
    # glColor3f(0.3, 0.2, 0.1)  # darker for door
    # glLineWidth(2.5)
    # glBegin(GL_LINE_LOOP)
    # glVertex2f(320, 150)  # door bottom-left
    # glVertex2f(380, 150)  # door bottom-right
    # glVertex2f(380, 260)  # door top-right
    # glVertex2f(320, 260)  # door top-left
    # glEnd()

    # # Window (square with cross inside)
    # glColor3f(0.2, 0.6, 0.9)  # blue-ish for window outline
    # glLineWidth(2.0)
    # # window outer square
    # wx1, wy1 = 230, 230
    # wx2, wy2 = 280, 280
    # glBegin(GL_LINE_LOOP)
    # glVertex2f(wx1, wy1)
    # glVertex2f(wx2, wy1)
    # glVertex2f(wx2, wy2)
    # glVertex2f(wx1, wy2)
    # glEnd()
    # # window cross (two lines)
    # glBegin(GL_LINES)
    # glVertex2f(wx1, (wy1 + wy2) / 2)  # mid-left
    # glVertex2f(wx2, (wy1 + wy2) / 2)  # mid-right
    # glVertex2f((wx1 + wx2) / 2, wy1)  # bottom-mid
    # glVertex2f((wx1 + wx2) / 2, wy2)  # top-mid
  


def draw_tree():
    """
    Draw a simple stylized tree using lines:
    - trunk as two parallel lines (to look thicker)
    - branches as multiple lines radiating from trunk
    - triangular outlines for foliage (only line outlines)
    Uses only GL_LINES and GL_LINE_LOOP primitives.
    """
    # Trunk (two close vertical lines to simulate thickness)
    glColor3f(0.45, 0.25, 0.07)  # brown trunk color
    glLineWidth(6.0)
    glBegin(GL_LINES)
    # left edge of trunk
    glVertex2f(620, 150)
    glVertex2f(620, 260)
    # right edge of trunk
    glVertex2f(640, 150)
    glVertex2f(640, 260)
    glEnd()

    # Branches (emanating lines)
    glColor3f(0.45, 0.25, 0.07)
    glLineWidth(3.0)
    glBegin(GL_LINES)
    # lower branches
    glVertex2f(620, 240); glVertex2f(560, 300)
    glVertex2f(640, 240); glVertex2f(700, 300)
    # middle branches
    glVertex2f(620, 280); glVertex2f(560, 360)
    glVertex2f(640, 280); glVertex2f(700, 360)
    # upper branches
    glVertex2f(620, 320); glVertex2f(580, 420)
    glVertex2f(640, 320); glVertex2f(680, 430)
    glEnd()

    # Foliage outlines (three overlapping triangular line-loops)
    glColor3f(0.1, 0.6, 0.1)  # green foliage outline
    glLineWidth(2.5)
    # bottom foliage triangle
    glBegin(GL_LINE_LOOP)
    glVertex2f(560, 340)
    glVertex2f(700, 340)
    glVertex2f(630, 420)
    glEnd()

    # middle foliage triangle (slightly smaller & higher)
    glBegin(GL_LINE_LOOP)
    glVertex2f(570, 380)
    glVertex2f(690, 380)
    glVertex2f(630, 460)
    glEnd()

    # top foliage triangle (smallest)
    glBegin(GL_LINE_LOOP)
    glVertex2f(585, 420)
    glVertex2f(675, 420)
    glVertex2f(630, 500)
    glEnd()


# -------------------------
# GLUT callbacks
# -------------------------
def display():
    """
    Main display callback: clears screen and draws the scene (house + tree).
    """
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw ground guideline (optional) using a thin line
    glColor3f(0.3, 0.7, 0.3)  # faint green line as ground
    glLineWidth(1.5)
    glBegin(GL_LINES)
    glVertex2f(0, 140)
    glVertex2f(WINDOW_WIDTH, 140)
    glEnd()

    # Draw the objects
    draw_house()   # draw house on left
    draw_tree()    # draw tree on right

    glutSwapBuffers()


def reshape(width, height):
    """
    Reshape callback: keep viewport and orthographic projection matched
    to window pixel coordinates so coordinates in code match actual pixels.
    """
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Set origin at bottom-left and top to window height (pixel coords)
    gluOrtho2D(0, width, 0, height)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def init_glut_window():
    """
    Initialize GLUT window and callbacks.
    """
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(200, 100)
    glutCreateWindow(b"Line-only Scene: House + Tree (Lab)")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glClearColor(0.9, 0.95, 1.0, 1.0)  # light sky-blue background


def main():
    init_glut_window()
    glutMainLoop()


if __name__ == "__main__":
    main()
