# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainLDZBFV.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSplitter,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(520, 360)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(520, 360))
        MainWindow.setMaximumSize(QSize(520, 360))
        MainWindow.setStyleSheet(u"")
        MainWindow.setAnimated(True)
        self.actiongreg = QAction(MainWindow)
        self.actiongreg.setObjectName(u"actiongreg")
        self.auth_menu = QAction(MainWindow)
        self.auth_menu.setObjectName(u"auth_menu")
        self.params_menu = QAction(MainWindow)
        self.params_menu.setObjectName(u"params_menu")
        self.params_template = QAction(MainWindow)
        self.params_template.setObjectName(u"params_template")
        self.links_folder_path = QAction(MainWindow)
        self.links_folder_path.setObjectName(u"links_folder_path")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(20, 60, 481, 121))
        self.listWidget.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.bt_open_folder = QPushButton(self.centralwidget)
        self.bt_open_folder.setObjectName(u"bt_open_folder")
        self.bt_open_folder.setGeometry(QRect(250, 20, 101, 31))
        self.cb_my_projects = QCheckBox(self.centralwidget)
        self.cb_my_projects.setObjectName(u"cb_my_projects")
        self.cb_my_projects.setGeometry(QRect(360, 30, 151, 20))
        self.lb_list_projects = QLabel(self.centralwidget)
        self.lb_list_projects.setObjectName(u"lb_list_projects")
        self.lb_list_projects.setGeometry(QRect(20, 20, 161, 21))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lb_list_projects.setFont(font)
        self.bt_load = QPushButton(self.centralwidget)
        self.bt_load.setObjectName(u"bt_load")
        self.bt_load.setGeometry(QRect(360, 200, 101, 31))
        self.bt_load.setStyleSheet(u"")
        self.cb_show_only_ip = QCheckBox(self.centralwidget)
        self.cb_show_only_ip.setObjectName(u"cb_show_only_ip")
        self.cb_show_only_ip.setGeometry(QRect(360, 10, 151, 20))
        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(150, 190, 132, 37))
        self.splitter_2.setOrientation(Qt.Orientation.Vertical)
        self.lb_choise_panel_var = QLabel(self.splitter_2)
        self.lb_choise_panel_var.setObjectName(u"lb_choise_panel_var")
        self.splitter_2.addWidget(self.lb_choise_panel_var)
        self.le_choise_panel_var = QLineEdit(self.splitter_2)
        self.le_choise_panel_var.setObjectName(u"le_choise_panel_var")
        self.splitter_2.addWidget(self.le_choise_panel_var)
        self.lb_progress = QLabel(self.centralwidget)
        self.lb_progress.setObjectName(u"lb_progress")
        self.lb_progress.setGeometry(QRect(330, 240, 171, 21))
        self.lb_progress.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 190, 167, 100))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.cb_fin_id = QCheckBox(self.layoutWidget)
        self.cb_fin_id.setObjectName(u"cb_fin_id")

        self.verticalLayout.addWidget(self.cb_fin_id)

        self.cb_template = QCheckBox(self.layoutWidget)
        self.cb_template.setObjectName(u"cb_template")

        self.verticalLayout.addWidget(self.cb_template)

        self.cb_opens = QCheckBox(self.layoutWidget)
        self.cb_opens.setObjectName(u"cb_opens")

        self.verticalLayout.addWidget(self.cb_opens)

        self.cb_dont_load_base = QCheckBox(self.layoutWidget)
        self.cb_dont_load_base.setObjectName(u"cb_dont_load_base")

        self.verticalLayout.addWidget(self.cb_dont_load_base)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 520, 33))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.auth_menu)
        self.menuMenu.addAction(self.params_menu)
        self.menuMenu.addAction(self.params_template)
        self.menuMenu.addAction(self.links_folder_path)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0432\u044b\u0433\u0440\u0443\u0437\u043a\u0430", None))
        self.actiongreg.setText(QCoreApplication.translate("MainWindow", u"greg", None))
        self.auth_menu.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u0434\u043b\u044f \u0430\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.params_menu.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0438 \u0431\u0430\u0437\u044b", None))
        self.params_template.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0448\u0430\u0431\u043b\u043e\u043d\u0430 \u0438 \u043e\u0442\u043a\u0440\u044b\u0442\u044b\u0445", None))
        self.links_folder_path.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0441 \u0441\u0441\u044b\u043b\u043a\u0430\u043c\u0438", None))
        self.bt_open_folder.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043f\u043a\u0430 \u043f\u0440\u043e\u0435\u043a\u0442\u0430", None))
        self.cb_my_projects.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0442\u043e\u043b\u044c\u043a\u043e \u043c\u043e\u0438", None))
        self.lb_list_projects.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043f\u0440\u043e\u0435\u043a\u0442\u043e\u0432", None))
        self.bt_load.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.cb_show_only_ip.setText(QCoreApplication.translate("MainWindow", u"\u0425\u043e\u043b\u043b-\u0442\u0435\u0441\u0442\u044b", None))
        self.lb_choise_panel_var.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u0430\u044f \u043f\u0430\u043d\u0435\u043b\u0438:", None))
        self.le_choise_panel_var.setText(QCoreApplication.translate("MainWindow", u"panel", None))
        self.lb_progress.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0413\u043e\u0442\u043e\u0432\u043e</p></body></html>", None))
        self.cb_fin_id.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043d\u0430\u043b\u044c\u043d\u044b\u0435 \u0430\u0439\u0434\u0438", None))
        self.cb_template.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0431\u043b\u043e\u043d", None))
        self.cb_opens.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044b\u0435", None))
        self.cb_dont_load_base.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0437\u0430\u0433\u0440\u0443\u0436\u0430\u0442\u044c \u043d\u043e\u0432\u0443\u044e \u0431\u0430\u0437\u0443", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
    # retranslateUi

