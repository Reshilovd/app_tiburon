# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'outputSDepcI.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QTextBrowser, QWidget)


class Ui_output(object):
    def setupUi(self, output):
        if not output.objectName():
            output.setObjectName(u"output")
        output.resize(600, 200)
        output.setMinimumSize(QSize(600, 200))
        output.setMaximumSize(QSize(1000, 200))
        self.tb_output = QTextBrowser(output)
        self.tb_output.setObjectName(u"tb_output")
        self.tb_output.setGeometry(QRect(0, 0, 1000, 200))

        self.retranslateUi(output)

        QMetaObject.connectSlotsByName(output)

    # setupUi

    def retranslateUi(self, output):
        output.setWindowTitle(QCoreApplication.translate("output", u"\u0412\u044b\u0432\u043e\u0434", None))
        self.tb_output.setHtml(QCoreApplication.translate("output",
                                                          u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                          "p, li { white-space: pre-wrap; }\n"
                                                          "hr { height: 1px; border-width: 0; }\n"
                                                          "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                          "li.checked::marker { content: \"\\2612\"; }\n"
                                                          "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                          "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                                                          None))
    # retranslateUi
