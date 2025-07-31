/********************************************************************************
** Form generated from reading UI file 'chatbottester.ui'
**
** Created by: Qt User Interface Compiler version 5.9.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_CHATBOTTESTER_H
#define UI_CHATBOTTESTER_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QTextBrowser>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_ChatBotTester
{
public:
    QVBoxLayout *verticalLayout;
    QTextBrowser *textBrowser;
    QLineEdit *lineEdit;

    void setupUi(QWidget *ChatBotTester)
    {
        if (ChatBotTester->objectName().isEmpty())
            ChatBotTester->setObjectName(QStringLiteral("ChatBotTester"));
        ChatBotTester->resize(400, 300);
        ChatBotTester->setStyleSheet(QStringLiteral("background-color: rgb(255, 255, 255);"));
        verticalLayout = new QVBoxLayout(ChatBotTester);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        textBrowser = new QTextBrowser(ChatBotTester);
        textBrowser->setObjectName(QStringLiteral("textBrowser"));

        verticalLayout->addWidget(textBrowser);

        lineEdit = new QLineEdit(ChatBotTester);
        lineEdit->setObjectName(QStringLiteral("lineEdit"));

        verticalLayout->addWidget(lineEdit);


        retranslateUi(ChatBotTester);

        QMetaObject::connectSlotsByName(ChatBotTester);
    } // setupUi

    void retranslateUi(QWidget *ChatBotTester)
    {
        ChatBotTester->setWindowTitle(QApplication::translate("ChatBotTester", "Form", Q_NULLPTR));
        lineEdit->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class ChatBotTester: public Ui_ChatBotTester {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_CHATBOTTESTER_H
