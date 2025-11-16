from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600



def find_zone(x1, y1, x2, y2):
    dx=x2-x1
    dy=y2-y1

    if abs(dx)>abs(dy):
        if dx>=0 and dy>=0:
            return 0
        elif dx <0 and dy >=0:
            return 3
        
        elif dx<0 and dy<0:
            return 4
        else:
            return 7

    else:
        if dx>=0 and dy>=0:
            return 1
        elif dx<0 and dy>=0:
            return 2
        elif dx<0 and dy<0:
            return 5
        else: 
           return 6
        



def convert_to_zone0(x, y, zone):
    if zone==0:
        return x,y
    elif zone==1:
        return y,x
    elif zone==2:
        return y,-x
    elif zone ==3:
        return -x,y
    elif zone==4:
        return -x,-y
    elif zone==5:
        return -y,-x
    elif zone==6:
        return -y,x
    elif zone==7:
        return x,-7
    

    


def convert_from_zone0(x, y, zone):

  if zone==0:
      return x,y
  elif zone==1:
      return y,x
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
      



def midPoint_zone0(x1, y1, x2, y2):
    points=[]
    dx=x2-x1
    dy=y2-y1

    d=2*dy-dx
    incE=2*dy
    incNE=2*(dy-dx)
    x,y=x1,y1

    while x<=x2:
        points.append((x,y))
        if(d<=0):
            d+=incE
        else:
            d+=incNE
            y+=1
        x+=1
    return points



   



def draw_line(x1, y1, x2, y2):
    zone=find_zone(x1,y1,x2,y2)

    X1,Y1=convert_to_zone0(x1,y1,zone)
    X2,Y2=convert_to_zone0(x2,y2,zone)

    points_zone0=midPoint_zone0(X1,Y1,X2,Y2)

    points_final=[convert_from_zone0(x,y,zone)for (x,y) in points_zone0]

    glBegin(GL_POINTS)
    for(x,y) in points_final:
        glVertex2f(x,y);
    glEnd()


   



def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 0.0)
    glPointSize(2.5)

    #Rombous
    # draw_line(100, 100, 200, 100)
    # draw_line(100, 100, 150, 200)
    # draw_line(200, 100, 250, 200)
    # draw_line(150, 200, 250, 200)

    #concentric square
    # draw_line(100, 100, 300, 100)
    # draw_line(100, 100, 100, 300)
    # draw_line(100, 300, 300, 300)
    # draw_line(300, 300, 300, 100)

    
    # draw_line(150, 150, 250, 150)
    # draw_line(150, 150, 150, 250)
    # draw_line(150, 250, 250, 250)
    # draw_line(250, 150, 250, 250)

    # draw_line(170, 170, 220, 170)
    # draw_line(170,220, 220, 220)
    # draw_line(170, 170, 170, 220)
    # draw_line(220, 170, 220, 220)

    #cross
    draw_line(100, 100, 350, 350)
    draw_line(350,100, 100, 350)
    # draw_line(170, 170, 170, 220)
    # draw_line(220, 170, 220, 220)


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
    glutCreateWindow(b"Midpoint Line with Zone Logic - Straight Hollow Cube")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glClearColor(0.0, 0.0, 0.0, 1.0)



def main():
    init_glut_window()
    glutMainLoop()


if __name__ == "__main__":
    main()
