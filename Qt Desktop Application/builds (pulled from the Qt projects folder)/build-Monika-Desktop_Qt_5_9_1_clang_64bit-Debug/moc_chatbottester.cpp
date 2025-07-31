/****************************************************************************
** Meta object code from reading C++ file 'chatbottester.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.9.1)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../Monika/Qt Desktop Application/Monika/chatbottester.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'chatbottester.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.9.1. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_ChatBotTester_t {
    QByteArrayData data[5];
    char stringdata0[66];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_ChatBotTester_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_ChatBotTester_t qt_meta_stringdata_ChatBotTester = {
    {
QT_MOC_LITERAL(0, 0, 13), // "ChatBotTester"
QT_MOC_LITERAL(1, 14, 25), // "on_lineEdit_returnPressed"
QT_MOC_LITERAL(2, 40, 0), // ""
QT_MOC_LITERAL(3, 41, 15), // "thinkOfResponse"
QT_MOC_LITERAL(4, 57, 8) // "findName"

    },
    "ChatBotTester\0on_lineEdit_returnPressed\0"
    "\0thinkOfResponse\0findName"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_ChatBotTester[] = {

 // content:
       7,       // revision
       0,       // classname
       0,    0, // classinfo
       3,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    0,   29,    2, 0x08 /* Private */,
       3,    6,   30,    2, 0x08 /* Private */,
       4,    1,   43,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void,
    QMetaType::QString, QMetaType::QString, QMetaType::QString, QMetaType::Bool, QMetaType::Bool, QMetaType::Int, QMetaType::Bool,    2,    2,    2,    2,    2,    2,
    QMetaType::QString, QMetaType::QString,    2,

       0        // eod
};

void ChatBotTester::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        ChatBotTester *_t = static_cast<ChatBotTester *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->on_lineEdit_returnPressed(); break;
        case 1: { QString _r = _t->thinkOfResponse((*reinterpret_cast< QString(*)>(_a[1])),(*reinterpret_cast< QString(*)>(_a[2])),(*reinterpret_cast< bool(*)>(_a[3])),(*reinterpret_cast< bool(*)>(_a[4])),(*reinterpret_cast< int(*)>(_a[5])),(*reinterpret_cast< bool(*)>(_a[6])));
            if (_a[0]) *reinterpret_cast< QString*>(_a[0]) = std::move(_r); }  break;
        case 2: { QString _r = _t->findName((*reinterpret_cast< QString(*)>(_a[1])));
            if (_a[0]) *reinterpret_cast< QString*>(_a[0]) = std::move(_r); }  break;
        default: ;
        }
    }
}

const QMetaObject ChatBotTester::staticMetaObject = {
    { &QWidget::staticMetaObject, qt_meta_stringdata_ChatBotTester.data,
      qt_meta_data_ChatBotTester,  qt_static_metacall, nullptr, nullptr}
};


const QMetaObject *ChatBotTester::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *ChatBotTester::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_ChatBotTester.stringdata0))
        return static_cast<void*>(const_cast< ChatBotTester*>(this));
    return QWidget::qt_metacast(_clname);
}

int ChatBotTester::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 3)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 3;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 3)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 3;
    }
    return _id;
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
