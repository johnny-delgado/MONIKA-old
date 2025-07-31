/********************************************************************************
** Form generated from reading UI file 'widget.ui'
**
** Created by: Qt User Interface Compiler version 5.9.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_WIDGET_H
#define UI_WIDGET_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Widget
{
public:
    QLabel *dialogueBox;
    QLabel *dialogueLabel;
    QLabel *label;
    QListWidget *notificationsList;
    QPushButton *deleteNotification;
    QLabel *label_2;
    QLabel *label_3;
    QWidget *formLayoutWidget;
    QFormLayout *formLayout_2;
    QRadioButton *availableStatus;
    QLabel *availableLabel;
    QRadioButton *busyStatus;
    QRadioButton *sleepingStatus;
    QLabel *sleepingLabel;
    QRadioButton *nappingStatus;
    QLabel *nappingLabel;
    QLineEdit *busyLabel;

    void setupUi(QWidget *Widget)
    {
        if (Widget->objectName().isEmpty())
            Widget->setObjectName(QStringLiteral("Widget"));
        Widget->resize(1660, 260);
        Widget->setFocusPolicy(Qt::NoFocus);
        Widget->setStyleSheet(QStringLiteral(""));
        dialogueBox = new QLabel(Widget);
        dialogueBox->setObjectName(QStringLiteral("dialogueBox"));
        dialogueBox->setGeometry(QRect(0, 0, 16777215, 16777215));
        QSizePolicy sizePolicy(QSizePolicy::Maximum, QSizePolicy::Maximum);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(dialogueBox->sizePolicy().hasHeightForWidth());
        dialogueBox->setSizePolicy(sizePolicy);
        dialogueBox->setStyleSheet(QStringLiteral("background-color: rgb(209, 156, 255);"));
        dialogueLabel = new QLabel(Widget);
        dialogueLabel->setObjectName(QStringLiteral("dialogueLabel"));
        dialogueLabel->setGeometry(QRect(60, 40, 561, 151));
        label = new QLabel(Widget);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(1490, 180, 161, 31));
        notificationsList = new QListWidget(Widget);
        new QListWidgetItem(notificationsList);
        new QListWidgetItem(notificationsList);
        new QListWidgetItem(notificationsList);
        new QListWidgetItem(notificationsList);
        new QListWidgetItem(notificationsList);
        new QListWidgetItem(notificationsList);
        new QListWidgetItem(notificationsList);
        new QListWidgetItem(notificationsList);
        new QListWidgetItem(notificationsList);
        new QListWidgetItem(notificationsList);
        new QListWidgetItem(notificationsList);
        new QListWidgetItem(notificationsList);
        new QListWidgetItem(notificationsList);
        new QListWidgetItem(notificationsList);
        new QListWidgetItem(notificationsList);
        new QListWidgetItem(notificationsList);
        notificationsList->setObjectName(QStringLiteral("notificationsList"));
        notificationsList->setGeometry(QRect(660, 30, 501, 192));
        QFont font;
        font.setPointSize(16);
        notificationsList->setFont(font);
        notificationsList->setFocusPolicy(Qt::NoFocus);
        notificationsList->setStyleSheet(QStringLiteral(""));
        notificationsList->setSelectionMode(QAbstractItemView::SingleSelection);
        deleteNotification = new QPushButton(Widget);
        deleteNotification->setObjectName(QStringLiteral("deleteNotification"));
        deleteNotification->setGeometry(QRect(660, 220, 181, 32));
        deleteNotification->setStyleSheet(QStringLiteral("background-color: rgba(253, 149, 140, 133);"));
        label_2 = new QLabel(Widget);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(1180, 10, 221, 101));
        label_2->setWordWrap(true);
        label_3 = new QLabel(Widget);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setGeometry(QRect(1080, 160, 271, 101));
        label_3->setWordWrap(true);
        formLayoutWidget = new QWidget(Widget);
        formLayoutWidget->setObjectName(QStringLiteral("formLayoutWidget"));
        formLayoutWidget->setGeometry(QRect(1480, 30, 141, 101));
        formLayout_2 = new QFormLayout(formLayoutWidget);
        formLayout_2->setSpacing(6);
        formLayout_2->setContentsMargins(11, 11, 11, 11);
        formLayout_2->setObjectName(QStringLiteral("formLayout_2"));
        formLayout_2->setContentsMargins(0, 0, 0, 0);
        availableStatus = new QRadioButton(formLayoutWidget);
        availableStatus->setObjectName(QStringLiteral("availableStatus"));

        formLayout_2->setWidget(0, QFormLayout::LabelRole, availableStatus);

        availableLabel = new QLabel(formLayoutWidget);
        availableLabel->setObjectName(QStringLiteral("availableLabel"));

        formLayout_2->setWidget(0, QFormLayout::FieldRole, availableLabel);

        busyStatus = new QRadioButton(formLayoutWidget);
        busyStatus->setObjectName(QStringLiteral("busyStatus"));

        formLayout_2->setWidget(1, QFormLayout::LabelRole, busyStatus);

        sleepingStatus = new QRadioButton(formLayoutWidget);
        sleepingStatus->setObjectName(QStringLiteral("sleepingStatus"));

        formLayout_2->setWidget(2, QFormLayout::LabelRole, sleepingStatus);

        sleepingLabel = new QLabel(formLayoutWidget);
        sleepingLabel->setObjectName(QStringLiteral("sleepingLabel"));

        formLayout_2->setWidget(2, QFormLayout::FieldRole, sleepingLabel);

        nappingStatus = new QRadioButton(formLayoutWidget);
        nappingStatus->setObjectName(QStringLiteral("nappingStatus"));

        formLayout_2->setWidget(3, QFormLayout::LabelRole, nappingStatus);

        nappingLabel = new QLabel(formLayoutWidget);
        nappingLabel->setObjectName(QStringLiteral("nappingLabel"));

        formLayout_2->setWidget(3, QFormLayout::FieldRole, nappingLabel);

        busyLabel = new QLineEdit(formLayoutWidget);
        busyLabel->setObjectName(QStringLiteral("busyLabel"));
        QSizePolicy sizePolicy1(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(busyLabel->sizePolicy().hasHeightForWidth());
        busyLabel->setSizePolicy(sizePolicy1);
        busyLabel->setAutoFillBackground(true);
        busyLabel->setStyleSheet(QStringLiteral(""));
        busyLabel->setFrame(false);
        busyLabel->setCursorPosition(4);

        formLayout_2->setWidget(1, QFormLayout::FieldRole, busyLabel);


        retranslateUi(Widget);

        QMetaObject::connectSlotsByName(Widget);
    } // setupUi

    void retranslateUi(QWidget *Widget)
    {
        Widget->setWindowTitle(QApplication::translate("Widget", "Widget", Q_NULLPTR));
        dialogueBox->setText(QString());
        dialogueLabel->setText(QApplication::translate("Widget", "Text Here", Q_NULLPTR));
        label->setText(QApplication::translate("Widget", "You have __ unread texts.", Q_NULLPTR));

        const bool __sortingEnabled = notificationsList->isSortingEnabled();
        notificationsList->setSortingEnabled(false);
        QListWidgetItem *___qlistwidgetitem = notificationsList->item(0);
        ___qlistwidgetitem->setText(QApplication::translate("Widget", "hello", Q_NULLPTR));
        QListWidgetItem *___qlistwidgetitem1 = notificationsList->item(1);
        ___qlistwidgetitem1->setText(QApplication::translate("Widget", "ewq", Q_NULLPTR));
        QListWidgetItem *___qlistwidgetitem2 = notificationsList->item(2);
        ___qlistwidgetitem2->setText(QApplication::translate("Widget", "dd", Q_NULLPTR));
        QListWidgetItem *___qlistwidgetitem3 = notificationsList->item(3);
        ___qlistwidgetitem3->setText(QApplication::translate("Widget", "New Item", Q_NULLPTR));
        QListWidgetItem *___qlistwidgetitem4 = notificationsList->item(4);
        ___qlistwidgetitem4->setText(QApplication::translate("Widget", "dqewff", Q_NULLPTR));
        QListWidgetItem *___qlistwidgetitem5 = notificationsList->item(5);
        ___qlistwidgetitem5->setText(QApplication::translate("Widget", "awd", Q_NULLPTR));
        QListWidgetItem *___qlistwidgetitem6 = notificationsList->item(6);
        ___qlistwidgetitem6->setText(QApplication::translate("Widget", "wfefwe", Q_NULLPTR));
        QListWidgetItem *___qlistwidgetitem7 = notificationsList->item(7);
        ___qlistwidgetitem7->setText(QApplication::translate("Widget", "e", Q_NULLPTR));
        QListWidgetItem *___qlistwidgetitem8 = notificationsList->item(8);
        ___qlistwidgetitem8->setText(QApplication::translate("Widget", "fqwwfe", Q_NULLPTR));
        QListWidgetItem *___qlistwidgetitem9 = notificationsList->item(9);
        ___qlistwidgetitem9->setText(QApplication::translate("Widget", "qewq", Q_NULLPTR));
        QListWidgetItem *___qlistwidgetitem10 = notificationsList->item(10);
        ___qlistwidgetitem10->setText(QApplication::translate("Widget", "f", Q_NULLPTR));
        QListWidgetItem *___qlistwidgetitem11 = notificationsList->item(11);
        ___qlistwidgetitem11->setText(QApplication::translate("Widget", "qef", Q_NULLPTR));
        QListWidgetItem *___qlistwidgetitem12 = notificationsList->item(12);
        ___qlistwidgetitem12->setText(QApplication::translate("Widget", "asda", Q_NULLPTR));
        QListWidgetItem *___qlistwidgetitem13 = notificationsList->item(13);
        ___qlistwidgetitem13->setText(QApplication::translate("Widget", "asdasda", Q_NULLPTR));
        QListWidgetItem *___qlistwidgetitem14 = notificationsList->item(14);
        ___qlistwidgetitem14->setText(QApplication::translate("Widget", "afwasdas", Q_NULLPTR));
        QListWidgetItem *___qlistwidgetitem15 = notificationsList->item(15);
        ___qlistwidgetitem15->setText(QApplication::translate("Widget", "greergger", Q_NULLPTR));
        notificationsList->setSortingEnabled(__sortingEnabled);

        deleteNotification->setText(QApplication::translate("Widget", "delete notification", Q_NULLPTR));
        label_2->setText(QApplication::translate("Widget", "if none are clicked it will use the NN to guess but these buttons are so I can manually set it. pressing one will turn off the others and pressing one that's on will turn them all off so the system can rely on the NN", Q_NULLPTR));
        label_3->setText(QApplication::translate("Widget", "have the 'other' radiop button bring up a popup window when toggled on that allows me to set a custom state (ex. on vacation). maybe replace the napping button with the cusrtom one. also when i type my state it will change the label of the radio button", Q_NULLPTR));
        availableStatus->setText(QString());
        availableLabel->setText(QApplication::translate("Widget", "Available", Q_NULLPTR));
        busyStatus->setText(QString());
        sleepingStatus->setText(QString());
        sleepingLabel->setText(QApplication::translate("Widget", "Sleeping", Q_NULLPTR));
        nappingStatus->setText(QString());
        nappingLabel->setText(QApplication::translate("Widget", "Napping", Q_NULLPTR));
        busyLabel->setText(QApplication::translate("Widget", "Busy", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class Widget: public Ui_Widget {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_WIDGET_H
