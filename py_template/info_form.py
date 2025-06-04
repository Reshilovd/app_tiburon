# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info_formCTLLkN.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_info_form(object):
    def setupUi(self, info_form):
        if not info_form.objectName():
            info_form.setObjectName(u"info_form")
        info_form.resize(240, 80)
        info_form.setMaximumSize(QSize(240, 80))
        self.label = QLabel(info_form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(14, 20, 211, 41))

        self.retranslateUi(info_form)

        QMetaObject.connectSlotsByName(info_form)
    # setupUi

    def retranslateUi(self, info_form):
        info_form.setWindowTitle(QCoreApplication.translate("info_form", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("info_form", u"<html><head/><body><p><br/></p></body></html>", None))
    # retranslateUi

