# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_auth_formfcnfyp.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
                               QSizePolicy, QWidget)


class Ui_auth_form(object):
    def setupUi(self, auth_form):
        if not auth_form.objectName():
            auth_form.setObjectName(u"auth_form")
        auth_form.resize(200, 235)
        auth_form.setMinimumSize(QSize(200, 235))
        auth_form.setMaximumSize(QSize(200, 235))
        self.lb_data_in_tib = QLabel(auth_form)
        self.lb_data_in_tib.setObjectName(u"lb_data_in_tib")
        self.lb_data_in_tib.setGeometry(QRect(30, 10, 171, 21))
        self.bt_auth_confirm = QPushButton(auth_form)
        self.bt_auth_confirm.setObjectName(u"bt_auth_confirm")
        self.bt_auth_confirm.setGeometry(QRect(60, 200, 75, 24))
        self.le_login_tib = QLineEdit(auth_form)
        self.le_login_tib.setObjectName(u"le_login_tib")
        self.le_login_tib.setGeometry(QRect(10, 60, 181, 21))
        self.le_login_tib.setMinimumSize(QSize(0, 0))
        self.le_password_tib = QLineEdit(auth_form)
        self.le_password_tib.setObjectName(u"le_password_tib")
        self.le_password_tib.setGeometry(QRect(10, 110, 181, 21))
        self.le_password_tib.setEchoMode(QLineEdit.Password)
        self.lb_password_tib = QLabel(auth_form)
        self.lb_password_tib.setObjectName(u"lb_password_tib")
        self.lb_password_tib.setGeometry(QRect(10, 90, 132, 16))
        self.lb_login_tib = QLabel(auth_form)
        self.lb_login_tib.setObjectName(u"lb_login_tib")
        self.lb_login_tib.setGeometry(QRect(10, 40, 132, 16))
        self.lb_mail = QLabel(auth_form)
        self.lb_mail.setObjectName(u"lb_mail")
        self.lb_mail.setGeometry(QRect(10, 140, 121, 16))
        self.le_mail = QLineEdit(auth_form)
        self.le_mail.setObjectName(u"le_mail")
        self.le_mail.setGeometry(QRect(10, 160, 181, 21))
        self.le_mail.setMinimumSize(QSize(0, 0))

        self.retranslateUi(auth_form)

        QMetaObject.connectSlotsByName(auth_form)

    # setupUi

    def retranslateUi(self, auth_form):
        auth_form.setWindowTitle(QCoreApplication.translate("auth_form",
                                                            u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f",
                                                            None))
        self.lb_data_in_tib.setText(QCoreApplication.translate("auth_form",
                                                               u"<html><head/><body><p><span style=\" font-size:11pt;\">\u0414\u0430\u043d\u043d\u044b\u0435 \u043e\u0442 \u0442\u0438\u0431\u0443\u0440\u043e\u043d\u0430:</span></p></body></html>",
                                                               None))
        self.bt_auth_confirm.setText(QCoreApplication.translate("auth_form", u"OK", None))
        self.lb_password_tib.setText(
            QCoreApplication.translate("auth_form", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.lb_login_tib.setText(QCoreApplication.translate("auth_form", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.lb_mail.setText(QCoreApplication.translate("auth_form", u"\u041f\u043e\u0447\u0442\u0430:", None))
    # retranslateUi
