#include "widget.h"
#include <QApplication>
#include <QDesktopWidget>
#include <QProcess>
#include <QDebug>


int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Widget w;

    //make window transparent
    w.setStyleSheet("background:transparent;");
    w.setAttribute(Qt::WA_TranslucentBackground);
    w.setWindowFlags(Qt::FramelessWindowHint);


    QRect rec = QApplication::desktop()->screenGeometry();
    //QApplication::QDesktopWidget;
    float screenHeight = rec.height();
    float screenWidth = rec.width();
    float windowHeight = screenHeight/4; //the height of the dialogue window
    float buffer = 10;
    w.setGeometry(0+buffer,screenHeight-windowHeight-buffer,screenWidth-2*buffer,windowHeight); //x,y,width,height


    QObject::connect(&a, SIGNAL(aboutToQuit()), &w, SLOT(closeAllProcesses()));


    w.show();

    return a.exec();
}

void Widget::closeAllProcesses(){

    QString textResponderLocation = "/Users/Johnny/Monika/Qt Desktop Application/Monika/textResponseSystem/";
    QString pythonLocation = "/Library/Frameworks/Python.framework/Versions/2.7/bin/python"; //the location of the version of python I should use (find it by typing `which python` in terminal)

    qDebug() << "closing all processes";
    QProcess *process = new QProcess();

    QStringList arguments {textResponderLocation + "SendQuitSignal.py"};

    process->start(pythonLocation, arguments);
    process->waitForFinished(-1);

    process->close();
}
