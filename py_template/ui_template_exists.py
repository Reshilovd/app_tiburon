# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'template_existsUofJpP.ui'
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

class Ui_template_exists_form(object):
    def setupUi(self, template_exists_form):
        if not template_exists_form.objectName():
            template_exists_form.setObjectName(u"template_exists_form")
        template_exists_form.resize(285, 125)
        template_exists_form.setMinimumSize(QSize(285, 125))
        template_exists_form.setMaximumSize(QSize(285, 125))
        self.lb_template_exists = QLabel(template_exists_form)
        self.lb_template_exists.setObjectName(u"lb_template_exists")
        self.lb_template_exists.setGeometry(QRect(0, 10, 281, 61))
        self.bt_repeat_template = QPushButton(template_exists_form)
        self.bt_repeat_template.setObjectName(u"bt_repeat_template")
        self.bt_repeat_template.setGeometry(QRect(100, 80, 75, 24))

        self.retranslateUi(template_exists_form)

        QMetaObject.connectSlotsByName(template_exists_form)
    # setupUi

    def retranslateUi(self, template_exists_form):
        template_exists_form.setWindowTitle(QCoreApplication.translate("template_exists_form", u"\u0418\u043d\u0444\u043e", None))
        self.lb_template_exists.setText(QCoreApplication.translate("template_exists_form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">\u0428\u0430\u0431\u043b\u043e\u043d \u0443\u0436\u0435 \u043b\u0435\u0436\u0438\u0442 \u0432 \u043f\u0430\u043f\u043a\u0435!<br/>\u0415\u0441\u043b\u0438 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u043f\u0435\u0440\u0435\u0432\u044b\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0443\u0434\u0430\u043b\u0438\u0442\u0435 \u0435\u0433\u043e <br/>\u0438\u0437 \u043f\u0430\u043f\u043a\u0438 \u0438 \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 </span><span style=\" font-size:10pt; font-weight:700;\">\u0412\u044b\u0433\u0440\u0443\u0437\u0438\u0442\u044c</span></p></body></html>", None))
        self.bt_repeat_template.setText(QCoreApplication.translate("template_exists_form", u"\u0412\u044b\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
    # retranslateUi

