# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'macro_error_formPyxQwC.ui'
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

class Ui_macro_error_form(object):
    def setupUi(self, macro_error_form):
        if not macro_error_form.objectName():
            macro_error_form.setObjectName(u"macro_error_form")
        macro_error_form.resize(280, 125)
        macro_error_form.setMinimumSize(QSize(280, 125))
        macro_error_form.setMaximumSize(QSize(280, 125))
        self.lb_macro_error = QLabel(macro_error_form)
        self.lb_macro_error.setObjectName(u"lb_macro_error")
        self.lb_macro_error.setGeometry(QRect(0, 10, 281, 61))
        self.bt_repeat_template = QPushButton(macro_error_form)
        self.bt_repeat_template.setObjectName(u"bt_repeat_template")
        self.bt_repeat_template.setGeometry(QRect(110, 80, 75, 24))

        self.retranslateUi(macro_error_form)

        QMetaObject.connectSlotsByName(macro_error_form)
    # setupUi

    def retranslateUi(self, macro_error_form):
        macro_error_form.setWindowTitle(QCoreApplication.translate("macro_error_form", u"\u041e\u0448\u0438\u0431\u043a\u0430", None))
        self.lb_macro_error.setText(QCoreApplication.translate("macro_error_form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">\u041e\u0448\u0438\u0431\u043a\u0430 \u0432\u043e \u0432\u0440\u0435\u043c\u044f \u0440\u0430\u0431\u043e\u0442\u044b \u043c\u0430\u043a\u0440\u043e\u0441\u0430!<br/>\u041f\u0440\u043e\u0432\u0435\u0440\u044c\u0442\u0435 VPN \u0438 \u0442\u043e, \u0447\u0442\u043e \u043c\u0430\u043a\u0440\u043e\u0441\u044b \u0430\u043a\u0442\u0438\u0432\u043d\u044b \u0438 <br/>\u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 </span><span style=\" font-size:10pt; font-weight:700;\">\u0412\u044b\u0433\u0440\u0443\u0437\u0438\u0442\u044c</span></p></body></html>", None))
        self.bt_repeat_template.setText(QCoreApplication.translate("macro_error_form", u"\u0412\u044b\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
    # retranslateUi

