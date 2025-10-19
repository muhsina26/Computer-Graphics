from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


def get_zone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) > abs(dy):
        if dx >= 0 and dy >= 0:
            return 0
        elif dx < 0 and dy >= 0:
            return 3
        elif dx < 0 and dy < 0:
            return 4
        else:
            return 7
    else:
        if dx >= 0 and dy >= 0:
            return 1
        elif dx < 0 and dy >= 0:
            return 2
        elif dx < 0 and dy < 0:
            return 5
        else:
            return 6

def convert_to_zone0(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return y, -x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return -y, x
    elif zone == 7:
        return x, -y

def convert_from_zone0(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return -y, x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return y, -x
    elif zone == 7:
        return x, -y

def midPoint(X1, Y1, X2, Y2):
    points = []
    zone = get_zone(X1, Y1, X2, Y2)

    
    x1_zone0, y1_zone0 = convert_to_zone0(X1, Y1, zone)
    x2_zone0, y2_zone0 = convert_to_zone0(X2, Y2, zone)


    if x1_zone0 > x2_zone0:
        x1_zone0, x2_zone0 = x2_zone0, x1_zone0
        y1_zone0, y2_zone0 = y2_zone0, y1_zone0

    dx = x2_zone0 - x1_zone0
    dy = y2_zone0 - y1_zone0

    d = 2 * dy - dx
    dE = 2 * dy
    dNE = 2 * (dy - dx)

    x = x1_zone0
    y = y1_zone0

    while x <= x2_zone0:
        orig_x, orig_y = convert_from_zone0(x, y, zone)
        points.append((orig_x, orig_y))

        if d > 0:
            y += 1
            d += dNE
        else:
            d += dE
        x += 1

    return points

def draw_line(x1, y1, x2, y2):
    pts = midPoint(int(x1), int(y1), int(x2), int(y2))
    glBegin(GL_POINTS)
    for (px, py) in pts:
        glVertex2f(px, py)
    glEnd()


# ---- DISPLAY ----
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 0.0)
    glPointSize(3.0)

   
    A_x, A_y = 100, 100
    B_x, B_y = 220, 100
    C_x, C_y = 220, 180
    D_x, D_y = 100, 180

    
    H_x, H_y = 220, 100   
    E_x, E_y = 260, 120   
    F_x, F_y = 260, 200   
    G_x, G_y = 220, 180   

    R1_x, R1_y = 100, 180
    R2_x, R2_y = 160, 230
    R3_x, R3_y = 260, 200

  
    draw_line(A_x, A_y, B_x, B_y)
    draw_line(B_x, B_y, C_x, C_y)
    draw_line(C_x, C_y, D_x, D_y)
    draw_line(D_x, D_y, A_x, A_y)

    draw_line(H_x, H_y, E_x, E_y)
    draw_line(E_x, E_y, F_x, F_y)
    draw_line(F_x, F_y, G_x, G_y)
    draw_line(G_x, G_y, H_x, H_y)

 
    draw_line(R1_x, R1_y, R2_x, R2_y)
    draw_line(R2_x, R2_y, R3_x, R3_y)
    draw_line(R3_x, R3_y, C_x, C_y)
    draw_line(R2_x, R2_y, F_x, F_y)


    door_left_x, door_left_y = 135, 100
    door_right_x, door_right_y = 165, 100
    door_top_left_x, door_top_left_y = 135, 140
    door_top_right_x, door_top_right_y = 165, 140

    draw_line(door_left_x, door_left_y, door_right_x, door_right_y)
    draw_line(door_left_x, door_left_y, door_top_left_x, door_top_left_y)
    draw_line(door_right_x, door_right_y, door_top_right_x, door_top_right_y)
    draw_line(door_top_left_x, door_top_left_y, door_top_right_x, door_top_right_y)

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
    glutCreateWindow(b"Midpoint Line Drawing - House (raw coords)")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glClearColor(0.0, 0.0, 0.0, 1.0)

def main():
    init_glut_window()
    glutMainLoop()

if __name__ == "__main__":
    main()
