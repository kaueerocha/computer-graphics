#include <GL/glut.h>
#include <stdlib.h>
#include <math.h>
#include <stdio.h>
#include <vector>

void myInit(void);
void myDisplay(void);
void keyboard(unsigned char key, int x, int y);
void handle_motion(GLint x, GLint y);
void handle_mouse(GLint button, GLint action, GLint x, GLint y);
void handle_menu(GLint op);
void handle_submenuCor(GLint op);
void handle_submenuEsp(GLint op);
void create_menu();

int mouseX = 0, mouseY = 0, defaultWindowHeight = 480;
float lineWidth = 2.0; // default


using namespace std;

vector<vector<pair<int, int>>> desenhos;
int currentDrawing = 0;



int main(int argc, char** argv) {
    glutInit(&argc, argv); // Inicializa o GLUT e processa qualquer parâmetro passado pela linha de comandos. Deve ser chamada antes de qualquer outra rotina GLUT.
    glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB); // Especifica como o vídeo será utilizado, no caso será alocado um buffer e o sistema de cor será RGB.
    glutInitWindowSize (640, 480); // Especifica as dimensões da janela em pixels.
    glutInitWindowPosition (100, 100); // Especifica a coordenada superior esquerda da janela. Define a localização da janela dentro da tela
    glutCreateWindow ("Paintaum"); // Cria a janela e devolve um identificador único para a janela. Até que o comando glutMainLoop seja chamado, a janela não será mostrada.
    myInit(); // Rotina que implementa as configurações iniciais do programa.
    glutDisplayFunc(myDisplay); // Chamada para a função de desenho
        // Toda vez que o GLUT determinar que a janela tem de ser desenhada, ele chamará a função aqui determinada.
    glutKeyboardFunc(keyboard); // Determinam as funções que usaremos para ler o teclado e o mouse respectivamente.
    glutMouseFunc(handle_mouse);
    create_menu();
    glutMotionFunc(handle_motion);
    glutMainLoop( ); // É o último comando que chamamos. Ele faz com que todas as janelas criadas sejam mostradas. Uma vez que entramos neste loop, só saímos quando o programa se encerra.
    return 0;
    
}

void myInit(void) { 
    
    glClearColor(1.0,1.0,1.0,0.0);     // cor de fundo branco
    glColor3f(0.0f, 0.0f, 0.0f);          // Define cor corrente de desenho
    glPointSize(4.0);             // Define o tamanho do ponto: 4 por 4 pixels
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
                                           // janela com resolução de 640 por 480
    gluOrtho2D(0.0, 640.0, 0.0, 480.0);
}

void myDisplay(void) {

        glClear(GL_COLOR_BUFFER_BIT); // Limpa a janela
        glLineWidth(lineWidth);

        for(auto& desenho : desenhos){
            glBegin(GL_LINE_STRIP);
            for( auto& ponto : desenho){
                glVertex2i(ponto.first, defaultWindowHeight - ponto.second); // inverter Y
            }
            glEnd();
        }
        glFlush(); // Garante a execução de todas as rotinas de desenho
}


// A rotina a seguir termina o programa com a tecla Esc
void keyboard(unsigned char key, int x, int y) {
     switch (key) {
        case 27:
            exit(0);
        break;
        case 'd':
            desenhos.clear();
            myDisplay();
        break;
        // EXTRA: reset
        case 'r':
            desenhos.clear();               // limpa vetor de vetores
            glColor3f(0.0f, 0.0f, 0.0f);    // reseta cor para preto  
            lineWidth = 2.0;                // reseta espessura para default = 2.0
            myDisplay();                    // limpa tela
        break;
     }
}

// INTERACAO MOUSE

void handle_motion(GLint x, GLint y) {
    // Insere x e y do desenho atual no vetor de desenhos
    desenhos[currentDrawing].push_back({x, y});
    glutPostRedisplay();
}

void handle_mouse(GLint button, GLint action, GLint x, GLint y) {
    // Identifica a "quebra" de linha. 
    // "Aloca" novo vetor para novo desenho
    if (button == GLUT_LEFT_BUTTON && action == GLUT_DOWN) {
        desenhos.push_back(vector<pair<int, int>>());
        currentDrawing = desenhos.size() - 1;
    }
    glutPostRedisplay();
}

// MENU

void handle_menu(GLint op) { 
    switch(op) {
        case 0:
            handle_submenuCor(op);
        break;
        case 1:
            handle_submenuEsp(op);
        break;
    }
}

void handle_submenuCor(GLint op) {
    switch(op) {
        case 0:
            glColor3f(1.0f, 0.0f, 0.0f);
        break;
        case 1:
            glColor3f(0.0f, 1.0f, 0.0f);
        break;
        case 2:
            glColor3f(0.0f, 0.0f, 1.0f);
        break;
    }
    // glutPostRedisplay();
}

void handle_submenuEsp(GLint op) {
    switch(op) {
        case 0:
            lineWidth = 2.0;
        break;
        case 1:
            lineWidth = 4.0;
        break;
        case 2:
            lineWidth = 6.0;
        break;
        case 3:
            lineWidth = 10.0;
        break;
    }
    glutPostRedisplay();
}

void create_menu() {
    GLint menu, submenuCor, submenuEsp;
    submenuCor = glutCreateMenu(handle_submenuCor);
    glutAddMenuEntry("vermelho", 0);
    glutAddMenuEntry("verde", 1);
    glutAddMenuEntry("azul", 2);

    submenuEsp = glutCreateMenu(handle_submenuEsp);
    glutAddMenuEntry("2px", 0);
    glutAddMenuEntry("4px", 1);
    glutAddMenuEntry("6px", 2);
    glutAddMenuEntry("10px", 3);
    
    menu = glutCreateMenu(handle_menu);
    glutAddSubMenu("Cor", submenuCor);
    glutAddSubMenu("Espessura", submenuEsp);

    glutAttachMenu(GLUT_RIGHT_BUTTON);
} 
