# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'permission_error_formkhqDhj.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_permission_error_form(object):
    def setupUi(self, permission_error_form):
        if not permission_error_form.objectName():
            permission_error_form.setObjectName(u"permission_error_form")
        permission_error_form.resize(240, 125)
        self.bt_repeat_template = QPushButton(permission_error_form)
        self.bt_repeat_template.setObjectName(u"bt_repeat_template")
        self.bt_repeat_template.setGeometry(QRect(90, 80, 75, 24))
        self.lb_permission_error = QLabel(permission_error_form)
        self.lb_permission_error.setObjectName(u"lb_permission_error")
        self.lb_permission_error.setGeometry(QRect(10, 10, 221, 61))

        self.retranslateUi(permission_error_form)

        QMetaObject.connectSlotsByName(permission_error_form)
    # setupUi

    def retranslateUi(self, permission_error_form):
        permission_error_form.setWindowTitle(QCoreApplication.translate("permission_error_form", u"\u041e\u0448\u0438\u0431\u043a\u0430", None))
        self.bt_repeat_template.setText(QCoreApplication.translate("permission_error_form", u"\u041f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u044c", None))
        self.lb_permission_error.setText(QCoreApplication.translate("permission_error_form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:700;\">\u041e\u0448\u0438\u0431\u043a\u0430 \u0434\u043e\u0441\u0442\u0443\u043f\u0430 </span><span style=\" font-size:10pt;\">\u043a \u0444\u0430\u0439\u043b\u0443!</span><span style=\" font-size:10pt;\"><br/>\u0417\u0430\u043a\u0440\u043e\u0439\u0442\u0435 \u0448\u0430\u0431\u043b\u043e\u043d \u0438 \u043d\u0430\u0436\u043c\u0438\u0442\u0435<br/>\u043a\u043d\u043e\u043f\u043a\u0443 </span><span style=\" font-size:10pt; font-weight:700;\">\u041f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u044c</span></p></body></html>", None))
    # retranslateUi

