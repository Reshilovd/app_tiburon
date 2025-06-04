# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dict_not_foundmHKCol.ui'
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


class Ui_dict_not_found_form(object):
    def setupUi(self, dict_not_found_form):
        if not dict_not_found_form.objectName():
            dict_not_found_form.setObjectName(u"dict_not_found_form")
        dict_not_found_form.resize(240, 125)
        dict_not_found_form.setMinimumSize(QSize(240, 125))
        dict_not_found_form.setMaximumSize(QSize(240, 125))
        self.lb_dict_not_found = QLabel(dict_not_found_form)
        self.lb_dict_not_found.setObjectName(u"lb_dict_not_found")
        self.lb_dict_not_found.setGeometry(QRect(10, 10, 221, 61))
        self.bt_repeat_template = QPushButton(dict_not_found_form)
        self.bt_repeat_template.setObjectName(u"bt_repeat_template")
        self.bt_repeat_template.setGeometry(QRect(80, 80, 75, 24))

        self.retranslateUi(dict_not_found_form)

        QMetaObject.connectSlotsByName(dict_not_found_form)

    # setupUi

    def retranslateUi(self, dict_not_found_form):
        dict_not_found_form.setWindowTitle(QCoreApplication.translate("dict_not_found_form", u"dict", None))
        self.lb_dict_not_found.setText(QCoreApplication.translate("dict_not_found_form",
                                                                  u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">\u041d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d\u0430 \u0432\u043a\u043b\u0430\u0434\u043a\u0430 </span><span style=\" font-size:10pt; font-weight:700;\">dict!</span><span style=\" font-size:10pt;\"><br/>\u041f\u0440\u043e\u0432\u0435\u0440\u044c\u0442\u0435 \u0447\u0442\u043e \u0448\u0430\u0431\u043b\u043e\u043d \u0432 \u043f\u0430\u043f\u043a\u0435 \u043f\u0443\u0441\u0442<br/>\u0438 \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 </span><span style=\" font-size:10pt; font-weight:700;\">\u041f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u044c</span></p></body></html>",
                                                                  None))
        self.bt_repeat_template.setText(
            QCoreApplication.translate("dict_not_found_form", u"\u041f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u044c",
                                       None))
    # retranslateUi
