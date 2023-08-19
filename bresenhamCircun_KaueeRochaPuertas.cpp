
#include<windows.h>
#include <GL/glut.h>
#include <stdlib.h>
#include <cmath>
// function bresen
void bresenhamCircun(float raio, float xc, float yc);
void myDisplay();
void recalculate(int w, int h);

void myDisplay() {

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glColor3f(0, 0, 1);

    glMatrixMode(GL_MODELVIEW);

    glLoadIdentity();

    bresenhamCircun(50.0f, 200.0f, 200.0f);

    glutSwapBuffers();
}

void bresenhamCircun(float raio, float xc, float yc) {
    glBegin(GL_POINTS);
    glColor3f(0.0f, 1.0f, 0.0f);

    int x = 0;
    int y = round(raio);
    int d = 3 - 2 * round(raio);

    while (x <= y){
        glVertex2f(xc + x, yc + y);

        glVertex2f(xc + y, yc + x);
        glVertex2f(xc - x, yc + y);
        glVertex2f(xc - y, yc + x);
        glVertex2f(xc + x, yc - y);
        glVertex2f(xc + y, yc - x);
        glVertex2f(xc - x, yc - y);
        glVertex2f(xc - y, yc - x);

        x++;

        if (d < 0){
            d += 4 * x + 6;
        }
        else{
            d += 4 * (x - y) + 10;
            y--;
        }
    }
    glEnd();
}

void recalculate(int w, int h) {

    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0.0, w, 0.0, h);
}


int main(int argc, char** argv)
{
    glutInit(&argc, argv);

    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH);

    glutInitWindowSize(500,500);

    glutCreateWindow("Bresenham para Circurferência");

    glutDisplayFunc(myDisplay);
    
    glutReshapeFunc(recalculate);

    glutMainLoop();

    return 0;
}
