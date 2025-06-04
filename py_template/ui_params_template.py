# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_params_templateqnhiHe.ui'
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

class Ui_params_template_form(object):
    def setupUi(self, params_template_form):
        if not params_template_form.objectName():
            params_template_form.setObjectName(u"params_template_form")
        params_template_form.resize(250, 300)
        params_template_form.setMinimumSize(QSize(250, 235))
        params_template_form.setMaximumSize(QSize(250, 300))
        self.bt_template_params_confirm = QPushButton(params_template_form)
        self.bt_template_params_confirm.setObjectName(u"bt_template_params_confirm")
        self.bt_template_params_confirm.setGeometry(QRect(90, 260, 75, 24))
        self.lb_template_name = QLabel(params_template_form)
        self.lb_template_name.setObjectName(u"lb_template_name")
        self.lb_template_name.setGeometry(QRect(10, 10, 171, 16))
        self.le_template_name = QLineEdit(params_template_form)
        self.le_template_name.setObjectName(u"le_template_name")
        self.le_template_name.setGeometry(QRect(10, 30, 231, 31))
        self.le_template_macro_name = QLineEdit(params_template_form)
        self.le_template_macro_name.setObjectName(u"le_template_macro_name")
        self.le_template_macro_name.setGeometry(QRect(10, 90, 231, 31))
        self.lb_template_macro_name = QLabel(params_template_form)
        self.lb_template_macro_name.setObjectName(u"lb_template_macro_name")
        self.lb_template_macro_name.setGeometry(QRect(10, 70, 191, 16))
        self.lb_template_sheet_name = QLabel(params_template_form)
        self.lb_template_sheet_name.setObjectName(u"lb_template_sheet_name")
        self.lb_template_sheet_name.setGeometry(QRect(10, 130, 191, 16))
        self.le_template_sheet_name = QLineEdit(params_template_form)
        self.le_template_sheet_name.setObjectName(u"le_template_sheet_name")
        self.le_template_sheet_name.setGeometry(QRect(10, 150, 231, 31))
        self.lb_opens_syntax_name = QLabel(params_template_form)
        self.lb_opens_syntax_name.setObjectName(u"lb_opens_syntax_name")
        self.lb_opens_syntax_name.setGeometry(QRect(10, 190, 211, 16))
        self.le_opens_syntax_name = QLineEdit(params_template_form)
        self.le_opens_syntax_name.setObjectName(u"le_opens_syntax_name")
        self.le_opens_syntax_name.setGeometry(QRect(10, 210, 231, 31))

        self.retranslateUi(params_template_form)

        QMetaObject.connectSlotsByName(params_template_form)
    # setupUi

    def retranslateUi(self, params_template_form):
        params_template_form.setWindowTitle(QCoreApplication.translate("params_template_form", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0448\u0430\u0431\u043b\u043e\u043d\u0430", None))
        self.bt_template_params_confirm.setText(QCoreApplication.translate("params_template_form", u"OK", None))
        self.lb_template_name.setText(QCoreApplication.translate("params_template_form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0443\u0441\u0442\u043e\u0433\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u0430:", None))
        self.le_template_macro_name.setText("")
        self.lb_template_macro_name.setText(QCoreApplication.translate("params_template_form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043c\u0430\u043a\u0440\u043e\u0441\u0430 \u0434\u043b\u044f \u0432\u044b\u0433\u0440\u0443\u0437\u043a\u0438:", None))
        self.lb_template_sheet_name.setText(QCoreApplication.translate("params_template_form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0432\u043a\u043b\u0430\u0434\u043a\u0438 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438:", None))
        self.le_template_sheet_name.setText("")
        self.lb_opens_syntax_name.setText(QCoreApplication.translate("params_template_form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0438\u043d\u0442\u0430\u043a\u0441\u0438\u0441\u0430 \u0434\u043b\u044f \u043e\u0442\u043a\u0440\u044b\u0442\u044b\u0445:", None))
        self.le_opens_syntax_name.setText("")
    # retranslateUi

