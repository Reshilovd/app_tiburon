import os
import subprocess
import sys
import json
import keyring
import configparser

from datetime import datetime

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
from PyQt6.QtCore import QThread, QMutex
from PyQt6 import QtCore
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl
from cryptography.fernet import Fernet

from py_template.ui_dict_not_found import Ui_dict_not_found_form
from py_template.ui_main import Ui_MainWindow
from py_template.ui_auth_form import Ui_auth_form
from py_template.ui_not_found_template import Ui_not_found_template_form
from py_template.ui_output import Ui_output
from py_template.ui_params import Ui_params_form
from py_template.ui_params_template import Ui_params_template_form
from py_template.ui_template_exists import Ui_template_exists_form

from secondary_func import move_and_unzip, get_itab, get_final_id
from selenium_func import init_chrome_driver, download_base_from_tiburon, auth_tiburon


class CustomTemplateExistsForm(Ui_template_exists_form, QWidget):
    def __init__(self, parent=None):
        super(CustomTemplateExistsForm, self).__init__(parent)
        self.setupUi(self)

    def closeEvent(self, event):
        # Ваш код, который будет выполнен при закрытии виджета
        print("Вызывается при закрытии виджета")
        # Здесь можно вызвать вашу функцию
        self.my_function()

        # Вызов оригинального closeEvent из базового класса
        super(CustomTemplateExistsForm, self).closeEvent(event)

    def my_function(self):
        print("Ваш код после закрытия виджета")


class MainWindow(QMainWindow):
    projects = {}
    cc_projects = {}
    ip_projects = {}
    project_path = ''
    folder_is_selected = False
    folder_project = ''
    cc_project_name_list = []
    cc_project_name_only_user_list = []
    ip_projects_name_list = []
    ip_projects_name_only_user_list = []
    driver = init_chrome_driver()
    status = ""
    project_is_selected = False
    # sound = QtGui.QSound("sound.wav")
    player = QMediaPlayer()
    audio_output = QAudioOutput()
    itab_macro_name = ""
    sheet_name_dict = ""
    itab_path = ""
    template_name = ""
    base_path = ""
    fin_id_path = ""

    def __init__(self):
        status = self.status
        super(MainWindow, self).__init__()
        self.ui_window = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.init_output_window()
        self.init_template_exists_window()

        self.get_project_list()

        for p in self.cc_project_name_list:
            self.ui.listWidget.addItem(p)

        # self.ui.cb_strip_var.click()
        # self.ui.cb_time_in_page.click()
        self.ui.bt_load.setEnabled(False)

        self.ui.listWidget.clicked.connect(self.project_select)

    def project_select(self):
        self.project_is_selected = True
        self.template_exists_window.show()

    def sound_play(self, filename):
        filename = "sounds/" + filename + ".wav"
        self.player.setAudioOutput(self.audio_output)
        self.player.setSource(QUrl.fromLocalFile(filename))
        self.audio_output.setVolume(50)
        self.player.play()

    def init_output_window(self):
        self.output_window = QMainWindow()
        self.output_form = Ui_output()
        self.output_form.setupUi(self.output_window)

    def init_template_exists_window(self):
        self.template_exists_window = QMainWindow()
        self.template_exists_form = CustomTemplateExistsForm()
        self.template_exists_form.setupUi(self.template_exists_window)

    def open_template_exists_form(self):
        self.template_exists_window.show()
        self.sound_play(filename="error")

    def open_file_dialog(self):

        self.folder_project = str(QFileDialog.getExistingDirectory(self, "Выберите папку для выгрузки базы"))

        self.folder_is_selected = True
        if self.folder_project != '':
            self.ui.bt_open_folder.setText("Изменить папку")
            self.ui.bt_open_folder.setStyleSheet("background-color: #478ebe; color: rgb(255, 255, 255);")

    def get_project_list(self):
        with open('C:\\Users\\Denis.Reshilov\\Documents\\projects_tib_cc.json', encoding='utf-8') as json_file:
            self.cc_projects = json.load(json_file)

        for project_number in self.cc_projects.keys():
            self.cc_project_name_list.append(self.cc_projects[project_number]["name"])

        for project_number in self.cc_projects.keys():
            for emp in self.cc_projects[project_number]["processing"]:
                if emp == "denis.reshilov@ipsos.com":
                    self.cc_project_name_only_user_list.append(self.cc_projects[project_number]["name"])

        self.cc_project_name_list = list(reversed(self.cc_project_name_list))
        self.cc_project_name_only_user_list = list(reversed(self.cc_project_name_only_user_list))

        with open('C:\\Users\\Denis.Reshilov\\Documents\\projects_tib_ip.json', encoding='utf-8') as json_file:
            self.ip_projects = json.load(json_file)

        for project_number in self.ip_projects.keys():
            self.ip_projects_name_list.append(self.ip_projects[project_number]["name"])

        for project_number in self.ip_projects.keys():
            for emp in self.ip_projects[project_number]["processing"]:
                if emp == "denis.reshilov@ipsos.com":
                    self.ip_projects_name_only_user_list.append(self.ip_projects[project_number]["name"])

        self.ip_projects_name_list = list(reversed(self.ip_projects_name_list))
        self.ip_projects_name_only_user_list = list(reversed(self.ip_projects_name_only_user_list))

        self.projects = self.cc_projects | self.ip_projects


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
