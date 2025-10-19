from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


def midPoint(X1, Y1, X2, Y2):
    points = []
    dx = abs(X2 - X1)
    dy = abs(Y2 - Y1)
    x, y = X1, Y1
    sx = 1 if X2 > X1 else -1
    sy = 1 if Y2 > Y1 else -1
    d = 2 * dy - dx if dx >= dy else 2 * dx - dy  #both sign handle korsi

    if dx >= dy:
        while x != X2:
            points.append((x, y))
            print(x, ",i am from first loop", y)
            x += sx
            if d < 0:
                d += 2 * dy
            else:
                d += 2 * (dy - dx)
                y += sy
    else:
        while y != Y2:
            points.append((x, y))
            y += sy
            if d < 0:
                d += 2 * dx
            else:
                d += 2 * (dx - dy)
                x += sx
                print(x, ",i am from second loop", y)
    points.append((X2, Y2))
    print(points)
    return points


def draw_line(x1, y1, x2, y2):
    points = midPoint(x1, y1, x2, y2)
    glBegin(GL_POINTS)
    for (x, y) in points:
        glVertex2f(x, y)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 0.0)
    glPointSize(3.0)

    
    A_x, A_y = 100, 100
    B_x, B_y = 200, 150
    C_x, C_y = 200, 250
    D_x, D_y = 100, 200

  
    E_x, E_y = 150, 150
    F_x, F_y = 250, 200
    G_x, G_y = 250, 300
    H_x, H_y = 150, 250

   
    draw_line(A_x, A_y, B_x, B_y)
    draw_line(B_x, B_y, C_x, C_y)
    draw_line(C_x, C_y, D_x, D_y)
    draw_line(D_x, D_y, A_x, A_y)

    
    draw_line(E_x, E_y, F_x, F_y)
    draw_line(F_x, F_y, G_x, G_y)
    draw_line(G_x, G_y, H_x, H_y)
    draw_line(H_x, H_y, E_x, E_y)

   
    draw_line(A_x, A_y, E_x, E_y)
    draw_line(B_x, B_y, F_x, F_y)
    draw_line(C_x, C_y, G_x, G_y)
    draw_line(D_x, D_y, H_x, H_y)

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
    glutCreateWindow(b"Midpoint Line Drawing - Hollow Cube")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glClearColor(0.0, 0.0, 0.0, 1.0)


def main():
    init_glut_window()
    glutMainLoop()


if __name__ == "__main__":
    main()
