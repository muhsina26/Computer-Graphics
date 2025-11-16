from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

def midPointCircle(xc,yc,r):
    points=[]

    x=0
    y=r
    d=1-r

    while x<=y:

        points.extend([
            (xc+x,yc+y),
            (xc-x,yc+y),
            (xc-x,yc-y),
            (xc+x,yc-y),

            (xc+y,yc+x),
            (xc-y,yc+x),
            (xc+y,yc-x),
            (xc-y,yc-x)
        ])
        if d<0:
            d+=2*x+3
        else:
            d+=2*(x-y)+5
            y-=1
        x+=1
    return points





def draw_circle(xc,yc,r):
    points=midPointCircle(xc,yc,r)
    glBegin(GL_POINTS)
    for  (x,y) in points:
        glVertex2f(x,y)
    glEnd() 



def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 0.0)  
    glPointSize(2.5)
    draw_circle(300, 300, 100)

   
    

    glutSwapBuffers()


# ---- RESHAPE FUNCTION ----
def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


# ---- GLUT WINDOW INITIALIZATION ----
def init_glut_window():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(200, 100)
    glutCreateWindow(b"Midpoint Circle Algorithm - Single Circle")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glClearColor(0.0, 0.0, 0.0, 1.0)


# ---- MAIN FUNCTION ----
def main():
    init_glut_window()
    glutMainLoop()


if __name__ == "__main__":
    main()
