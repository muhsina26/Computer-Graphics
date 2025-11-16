def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.9, 0.4, 0.9)
    glPointSize(2.0)

    xc, yc = 100, 100
    r = 30
    spacing = int(r * 1.8)

    for i in range(10):
        draw_circle(xc + i * spacing, yc + i * spacing, r)

    glutSwapBuffers()