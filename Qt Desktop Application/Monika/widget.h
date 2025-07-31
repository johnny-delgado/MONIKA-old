#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>

namespace Ui {
class Widget;
}

class Widget : public QWidget
{
    Q_OBJECT

public:
    explicit Widget(QWidget *parent = 0);
    ~Widget();

private slots:
    void runPythonScript(QString, QString);

    void closeAllProcesses();

    void loopingFunction();

    bool fileExists(QString);

    void on_deleteNotification_clicked();
    void updateNotificationDisplay();
    void addNotification(int, QString, QString);

    void qtTextModifier(QString, QString, QString, QString);

    void on_availableStatus_toggled(bool checked);
    void on_busyStatus_toggled(bool checked);
    void on_sleepingStatus_toggled(bool checked);
    void on_nappingStatus_toggled(bool checked);

private:
    Ui::Widget *ui;
};

#endif // WIDGET_H
