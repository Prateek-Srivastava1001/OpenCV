#include <bits/stdc++.h>
#include <GL/glut.h>
#include <stdio.h>
#include <math.h>
#include <cmath>
#include <time.h>
#include <stdlib.h>
#include <windows.h>



#define maxWD 640
#define maxHT 480






int vertice1[3][1] = {{100}, {90}, {1}};
int vertice2[3][1] = {{200}, {90}, {1}};
int vertice3[3][1] = {{200}, {150}, {1}};
int vertice4[3][1] = {{100}, {150}, {1}};


void myInit(void)
{
    glClearColor(1.0, 1.0, 1.0, 0.0);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0.0, maxWD, 0.0, maxHT);
    glClear(GL_COLOR_BUFFER_BIT);
    glFlush();
}

void drawPoint()
{

    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(0.0,0.0,1.0);

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);

    glBegin(GL_POLYGON);
        glVertex2i(vertice1[0][0],vertice1[1][0]);
        glVertex2i(vertice2[0][0],vertice2[1][0]);
        glVertex2i(vertice3[0][0],vertice3[1][0]);
        glVertex2i(vertice4[0][0],vertice4[1][0]);
    glEnd();

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);

    glFlush();

}


void rotateRectangle (void) {
    drawPoint();
    Sleep(1000);
    double rotMat[3][3] = {{0.866, -0.5, 0}, {0.5, 0.866, 0}, {0, 0, 1}};



    // vertex 1
    int res[3][1];


    res[0][0] = vertice1[0][0];
    res[1][0] = vertice1[1][0];
    res[2][0] = vertice1[2][0];
    vertice1[0][0] = rotMat[0][0]*res[0][0]+rotMat[0][1]*res[1][0]+rotMat[0][2]*res[2][0];
    vertice1[1][0] = rotMat[1][0]*res[0][0]+rotMat[1][1]*res[1][0]+rotMat[1][2]*res[2][0];
    vertice1[2][0] = rotMat[2][0]*res[0][0]+rotMat[2][1]*res[1][0]+rotMat[2][2]*res[2][0];



    // vertex 2

    res[0][0] = vertice2[0][0];
    res[1][0] = vertice2[1][0];
    res[2][0] = vertice2[2][0];
    vertice2[0][0] = rotMat[0][0]*res[0][0]+rotMat[0][1]*res[1][0]+rotMat[0][2]*res[2][0];
    vertice2[1][0] = rotMat[1][0]*res[0][0]+rotMat[1][1]*res[1][0]+rotMat[1][2]*res[2][0];
    vertice2[2][0] = rotMat[2][0]*res[0][0]+rotMat[2][1]*res[1][0]+rotMat[2][2]*res[2][0];


    // vertex 3

    res[0][0] = vertice3[0][0];
    res[1][0] = vertice3[1][0];
    res[2][0] = vertice3[2][0];
    vertice3[0][0] = rotMat[0][0]*res[0][0]+rotMat[0][1]*res[1][0]+rotMat[0][2]*res[2][0];
    vertice3[1][0] = rotMat[1][0]*res[0][0]+rotMat[1][1]*res[1][0]+rotMat[1][2]*res[2][0];
    vertice3[2][0] = rotMat[2][0]*res[0][0]+rotMat[2][1]*res[1][0]+rotMat[2][2]*res[2][0];


    // vertex 4

    res[0][0] = vertice4[0][0];
    res[1][0] = vertice4[1][0];
    res[2][0] = vertice4[2][0];
    vertice4[0][0] = rotMat[0][0]*res[0][0]+rotMat[0][1]*res[1][0]+rotMat[0][2]*res[2][0];
    vertice4[1][0] = rotMat[1][0]*res[0][0]+rotMat[1][1]*res[1][0]+rotMat[1][2]*res[2][0];
    vertice4[2][0] = rotMat[2][0]*res[0][0]+rotMat[2][1]*res[1][0]+rotMat[2][2]*res[2][0];

    drawPoint();


}



int main(int argc, char** argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(maxWD, maxHT);
    glutInitWindowPosition(100, 150);
    glutCreateWindow("Rotation");
    glutDisplayFunc(rotateRectangle);
    myInit();
    glutMainLoop();

    return 0;
}
