#include "widget.h"
#include "ui_widget.h"
#include "QDebug"
#include <QTimer>
#include <QProcess>
//#include <QDir>
//#include <QTime>
#include <QFileInfo>
#include <QFile>
//#include <QDateTime>
#include <QThread>




//QList<QString> alerts; //a list of the alerts that I can put on hold, dismiss, or interact with (respond to message)


QString pythonLocation = "/Library/Frameworks/Python.framework/Versions/2.7/bin/python"; //the location of the version of python I should use (find it by typing `which python` in terminal)
//QString monikaFolderLocation = "/Users/Johnny/Monika/Qt Desktop Application/Monika/";
QString textResponderLocation = "/Users/Johnny/Monika/Qt Desktop Application/Monika/textResponseSystem/";


Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);





    //addNotification(0, "text", "You have a new text Johnny!");
    updateNotificationDisplay();


    //clear my emails here to ignore texts I've probably already seen that I got when Monika wasn't running, then begin the text response loop
    runPythonScript(textResponderLocation, "SimpleTextResponseLoop");

    //initially setup Johnny's state to unknown: availability = -1 in JohnnyStatus.txt
    qtTextModifier("JohnnyStatus.txt", "availability", "-1", "unknown");



    QTimer *timer = new QTimer(this);
    connect(timer, SIGNAL(timeout()), this, SLOT(loopingFunction()));
    timer->start(2000);
//make this time shorter (2 seconds) if there was a text in the email but increase it if no texts were there
//this way I can get through many texts fast if I recieve about 10 at once but it won't check as
//quickly if there weren't any texts in the email address before (maybe every 20 seconds)
//do `timer->start(checkTextDelay);` and the variable checkTextDelay based on the return of pullTextFromTextFile()


}

Widget::~Widget()
{
    delete ui;
}



    /* find the relative path to a file
    //QDir dir("/home/bob");
    //s = dir.relativeFilePath("/home/mary/file.txt"); // s is "../mary/file.txt"
    QDir dir(QCoreApplication::applicationDirPath());
    QString s = dir.relativeFilePath("/Users/Johnny/Monika/Qt Desktop Application/Monika/testExample.py");
    qDebug() << s;

    //to convert this
    //QStringList arguments {  "/Users/Johnny/Monika/Qt Desktop Application/Monika/testExample.py"};
    //to this
    //QStringList arguments { QCoreApplication::applicationDirPath() + "/../../../../../Monika/Qt Desktop Application/Monika/testExample.py"};
    */



void Widget::loopingFunction(){
    qDebug() << ">";
}


//run a python script and return the output of that script
//return "" if there was no output
//scriptPathAndName is relative to the Monika folder
void Widget::runPythonScript(QString scriptPath, QString scriptName){
    QProcess *process = new QProcess();
    //QProcess *process = new QProcess(this); //not sure if it should be this

    QStringList arguments {scriptPath + scriptName + ".py"};

    process->startDetached(pythonLocation, arguments);
    //process->waitForFinished(-1);


    //QString output = process->readAllStandardOutput();


    //process->close();

    //return output;

}


void Widget::qtTextModifier(QString fileName, QString tag, QString value, QString flavorText){

    QProcess *process = new QProcess();
    QStringList arguments = {textResponderLocation + "QtTextFileModifier.py", fileName, tag, value, flavorText};

    process->startDetached(pythonLocation, arguments);
}






void Widget::on_availableStatus_toggled(bool checked)
{
    if(checked){
        qtTextModifier("JohnnyStatus.txt", "availability", "0", "available");
    }
}

void Widget::on_busyStatus_toggled(bool checked)
{
    if(checked){
        qtTextModifier("JohnnyStatus.txt", "availability", "1", ui->busyLabel->text());
    }
}

void Widget::on_sleepingStatus_toggled(bool checked)
{
    if(checked){
        qtTextModifier("JohnnyStatus.txt", "availability", "2", "sleeping");
    }
}

void Widget::on_nappingStatus_toggled(bool checked)
{
    if(checked){
        qtTextModifier("JohnnyStatus.txt", "availability", "3", "napping");
    }
}








bool Widget::fileExists(QString path) {
    QFileInfo check_file(path);
    // check if file exists and if yes: Is it really a file and no directory?
    if (check_file.exists() && check_file.isFile()) {
        return true;
    } else {
        return false;
    }
}





//add a line to the notifications text file
//importance (0 = no rush, 1 you might want to look at this, 2 yo hurry and check this)
//type: text, email, call
//alert: the message displayed
void Widget::addNotification(int importance, QString type, QString alert){
    QString textLogsPath = QCoreApplication::applicationDirPath() + "/../../../../../Monika/Qt Desktop Application/Monika/";
    QString tab = QString("\t");
    QString notification = QString::number(importance) + tab + type + tab + alert;
    notification.append("\n"); //makes a new line after adding the text
    //appendTextFile(textLogsPath, "notifications", notification);



    //revamp addNotification


    updateNotificationDisplay();
}



//sets the ui notification list according to the notifications text file
void Widget::updateNotificationDisplay(){
    qDebug() << "begin update notification display";

    QString notificationFile = QCoreApplication::applicationDirPath() + "/../../../../../Monika/Qt Desktop Application/Monika/notifications.txt";
    QFile file(notificationFile);
    file.open(QFile::ReadOnly);

    qDebug() << "1";

    ui->notificationsList->clear(); //clear the notification list

    int maxImportance = 0;
    QStringList notifications;
    while (!file.atEnd()) {
        QString line = file.readLine();

        int pos = line.lastIndexOf("\n");
        line = line.left(pos); //remove the new line from the notification string

        notifications.append(line);

        int lineImportance = line.split('\t')[0].toInt();

        if (lineImportance > maxImportance){
            maxImportance = lineImportance;
        }
    }
    file.close();


    int notificationNum = 0;
    for (int i = maxImportance; i >= 0; i--){ //go through the notifications in order of importance
        for (int l = 0; l < notifications.length(); l++){ //go through each element of notifications (there's always an extra \n at the end of the file)
            if( notifications[l].split('\t')[0].toInt() == i ){ //check if the current notification is the importance we're looking for
                ui->notificationsList->addItem(notifications[l].split('\t')[2]); //add the notification to the notificationsList in the UI

                //color code the alerts by importance (2 = red, 1 = yellow, 0 = transparent)
                if(i == 2){ //if very important
                    ui->notificationsList->item(notificationNum)->setBackgroundColor(Qt::red); //setForeground(Qt::red); //to set the text color
                }
                if(i == 1){ //if very important
                    ui->notificationsList->item(notificationNum)->setBackgroundColor(Qt::yellow); //setForeground(Qt::red); //to set the text color
                }

                notificationNum++;

            }
        }
    }
    notifications.clear();
}





//maybe make a clearAllNotifications() that just deletes the text file (a new one is automatically made when a line is added to it)



//delete the notification that is currently being focused on
void Widget::on_deleteNotification_clicked()
{
    int focusIndex = ui->notificationsList->currentIndex().row(); //the index number of the focused (last clicked on) notification
    if (focusIndex != -1){
        qDebug() << QString::number(focusIndex);
        QString text = ui->notificationsList->item(focusIndex)->text();

//search text file for the index where this notification is found

//delete that notification

    }

}






