/****************************************************************************
** Meta object code from reading C++ file 'widget.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.9.1)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../Monika/Qt Desktop Application/Monika/widget.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'widget.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.9.1. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_Widget_t {
    QByteArrayData data[15];
    char stringdata0[264];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_Widget_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_Widget_t qt_meta_stringdata_Widget = {
    {
QT_MOC_LITERAL(0, 0, 6), // "Widget"
QT_MOC_LITERAL(1, 7, 15), // "runPythonScript"
QT_MOC_LITERAL(2, 23, 0), // ""
QT_MOC_LITERAL(3, 24, 17), // "closeAllProcesses"
QT_MOC_LITERAL(4, 42, 15), // "loopingFunction"
QT_MOC_LITERAL(5, 58, 10), // "fileExists"
QT_MOC_LITERAL(6, 69, 29), // "on_deleteNotification_clicked"
QT_MOC_LITERAL(7, 99, 25), // "updateNotificationDisplay"
QT_MOC_LITERAL(8, 125, 15), // "addNotification"
QT_MOC_LITERAL(9, 141, 14), // "qtTextModifier"
QT_MOC_LITERAL(10, 156, 26), // "on_availableStatus_toggled"
QT_MOC_LITERAL(11, 183, 7), // "checked"
QT_MOC_LITERAL(12, 191, 21), // "on_busyStatus_toggled"
QT_MOC_LITERAL(13, 213, 25), // "on_sleepingStatus_toggled"
QT_MOC_LITERAL(14, 239, 24) // "on_nappingStatus_toggled"

    },
    "Widget\0runPythonScript\0\0closeAllProcesses\0"
    "loopingFunction\0fileExists\0"
    "on_deleteNotification_clicked\0"
    "updateNotificationDisplay\0addNotification\0"
    "qtTextModifier\0on_availableStatus_toggled\0"
    "checked\0on_busyStatus_toggled\0"
    "on_sleepingStatus_toggled\0"
    "on_nappingStatus_toggled"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_Widget[] = {

 // content:
       7,       // revision
       0,       // classname
       0,    0, // classinfo
      12,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    2,   74,    2, 0x08 /* Private */,
       3,    0,   79,    2, 0x08 /* Private */,
       4,    0,   80,    2, 0x08 /* Private */,
       5,    1,   81,    2, 0x08 /* Private */,
       6,    0,   84,    2, 0x08 /* Private */,
       7,    0,   85,    2, 0x08 /* Private */,
       8,    3,   86,    2, 0x08 /* Private */,
       9,    4,   93,    2, 0x08 /* Private */,
      10,    1,  102,    2, 0x08 /* Private */,
      12,    1,  105,    2, 0x08 /* Private */,
      13,    1,  108,    2, 0x08 /* Private */,
      14,    1,  111,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, QMetaType::QString, QMetaType::QString,    2,    2,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Bool, QMetaType::QString,    2,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, QMetaType::Int, QMetaType::QString, QMetaType::QString,    2,    2,    2,
    QMetaType::Void, QMetaType::QString, QMetaType::QString, QMetaType::QString, QMetaType::QString,    2,    2,    2,    2,
    QMetaType::Void, QMetaType::Bool,   11,
    QMetaType::Void, QMetaType::Bool,   11,
    QMetaType::Void, QMetaType::Bool,   11,
    QMetaType::Void, QMetaType::Bool,   11,

       0        // eod
};

void Widget::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Widget *_t = static_cast<Widget *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->runPythonScript((*reinterpret_cast< QString(*)>(_a[1])),(*reinterpret_cast< QString(*)>(_a[2]))); break;
        case 1: _t->closeAllProcesses(); break;
        case 2: _t->loopingFunction(); break;
        case 3: { bool _r = _t->fileExists((*reinterpret_cast< QString(*)>(_a[1])));
            if (_a[0]) *reinterpret_cast< bool*>(_a[0]) = std::move(_r); }  break;
        case 4: _t->on_deleteNotification_clicked(); break;
        case 5: _t->updateNotificationDisplay(); break;
        case 6: _t->addNotification((*reinterpret_cast< int(*)>(_a[1])),(*reinterpret_cast< QString(*)>(_a[2])),(*reinterpret_cast< QString(*)>(_a[3]))); break;
        case 7: _t->qtTextModifier((*reinterpret_cast< QString(*)>(_a[1])),(*reinterpret_cast< QString(*)>(_a[2])),(*reinterpret_cast< QString(*)>(_a[3])),(*reinterpret_cast< QString(*)>(_a[4]))); break;
        case 8: _t->on_availableStatus_toggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 9: _t->on_busyStatus_toggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 10: _t->on_sleepingStatus_toggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 11: _t->on_nappingStatus_toggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObject Widget::staticMetaObject = {
    { &QWidget::staticMetaObject, qt_meta_stringdata_Widget.data,
      qt_meta_data_Widget,  qt_static_metacall, nullptr, nullptr}
};


const QMetaObject *Widget::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *Widget::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_Widget.stringdata0))
        return static_cast<void*>(const_cast< Widget*>(this));
    return QWidget::qt_metacast(_clname);
}

int Widget::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 12)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 12;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 12)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 12;
    }
    return _id;
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
