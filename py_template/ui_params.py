# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_paramszYQvZo.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_params_form(object):
    def setupUi(self, params_form):
        if not params_form.objectName():
            params_form.setObjectName(u"params_form")
        params_form.resize(250, 265)
        params_form.setMinimumSize(QSize(250, 250))
        params_form.setMaximumSize(QSize(250, 265))
        self.bt_params_confirm = QPushButton(params_form)
        self.bt_params_confirm.setObjectName(u"bt_params_confirm")
        self.bt_params_confirm.setGeometry(QRect(85, 225, 75, 24))
        self.widget = QWidget(params_form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 13, 217, 204))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.cb_label = QCheckBox(self.widget)
        self.cb_label.setObjectName(u"cb_label")

        self.verticalLayout.addWidget(self.cb_label)

        self.cb_utf8 = QCheckBox(self.widget)
        self.cb_utf8.setObjectName(u"cb_utf8")

        self.verticalLayout.addWidget(self.cb_utf8)

        self.cb_multi_label = QCheckBox(self.widget)
        self.cb_multi_label.setObjectName(u"cb_multi_label")

        self.verticalLayout.addWidget(self.cb_multi_label)

        self.cb_binar = QCheckBox(self.widget)
        self.cb_binar.setObjectName(u"cb_binar")

        self.verticalLayout.addWidget(self.cb_binar)

        self.cb_strip_var = QCheckBox(self.widget)
        self.cb_strip_var.setObjectName(u"cb_strip_var")

        self.verticalLayout.addWidget(self.cb_strip_var)

        self.cb_base_with_label = QCheckBox(self.widget)
        self.cb_base_with_label.setObjectName(u"cb_base_with_label")

        self.verticalLayout.addWidget(self.cb_base_with_label)

        self.cb_time_in_page = QCheckBox(self.widget)
        self.cb_time_in_page.setObjectName(u"cb_time_in_page")

        self.verticalLayout.addWidget(self.cb_time_in_page)

        self.cb_create_client_bases = QCheckBox(self.widget)
        self.cb_create_client_bases.setObjectName(u"cb_create_client_bases")

        self.verticalLayout.addWidget(self.cb_create_client_bases)


        self.retranslateUi(params_form)

        QMetaObject.connectSlotsByName(params_form)
    # setupUi

    def retranslateUi(self, params_form):
        params_form.setWindowTitle(QCoreApplication.translate("params_form", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.bt_params_confirm.setText(QCoreApplication.translate("params_form", u"OK", None))
        self.cb_label.setText(QCoreApplication.translate("params_form", u"\u041b\u0435\u0439\u0431\u043b\u044b \u043f\u043e \u0432\u0441\u0435\u0439 \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0435", None))
        self.cb_utf8.setText(QCoreApplication.translate("params_form", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u0432 \u043a\u043e\u0434\u0438\u0440\u043e\u0432\u043a\u0435 UTF-8", None))
        self.cb_multi_label.setText(QCoreApplication.translate("params_form", u"\u041c\u043d\u043e\u0436\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0435 \u043b\u0435\u0439\u0431\u043b\u044b CheckBox", None))
        self.cb_binar.setText(QCoreApplication.translate("params_form", u"CheckBox \u0432 \u0431\u0438\u043d\u0430\u0440\u043d\u043e\u043c \u0432\u0438\u0434\u0435", None))
        self.cb_strip_var.setText(QCoreApplication.translate("params_form", u"\u041e\u0431\u0440\u0435\u0437\u0430\u0442\u044c var lab(256) \u0438 val lab(120)", None))
        self.cb_base_with_label.setText(QCoreApplication.translate("params_form", u"\u0411\u0430\u0437\u0430 \u0441 \u043b\u0435\u0439\u0431\u043b\u0430\u043c\u0438 \u0432 Excel", None))
        self.cb_time_in_page.setText(QCoreApplication.translate("params_form", u"\u0412\u0440\u0435\u043c\u044f \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430\u0445", None))
        self.cb_create_client_bases.setText(QCoreApplication.translate("params_form", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043a\u043b\u0438\u0435\u043d\u0442\u0441\u043a\u0438\u0445 \u0431\u0430\u0437 \u0432 Excel", None))
    # retranslateUi

