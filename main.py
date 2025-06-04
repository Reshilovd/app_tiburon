import os
import sys
import json
import traceback
import keyring
import configparser

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl
from datetime import datetime

from cryptography.fernet import Fernet

from py_template.macro_error import Ui_macro_error_form
from py_template.not_found_base import Ui_not_found_base_form
from py_template.permission_error import Ui_permission_error_form
from py_template.ui_dict_not_found import Ui_dict_not_found_form
from py_template.ui_main import Ui_MainWindow
from py_template.ui_auth_form import Ui_auth_form
from py_template.ui_not_found_opens import Ui_not_found_opens_form
from py_template.ui_not_found_template import Ui_not_found_template_form
from py_template.ui_output import Ui_output
from py_template.ui_params import Ui_params_form
from py_template.ui_params_template import Ui_params_template_form
from py_template.ui_template_exists import Ui_template_exists_form
from py_template.info_form import Ui_info_form
from py_template.links_folder_path_form import Ui_links_folder_path_form

from q_threads import StartProcess, GetFinalId, CreateTemplate, CreateOpens, DownloadBaseFromTiburon
from secondary_func import get_shortcut_target_path, error_checker
from selenium_func import init_chrome_driver, auth_tiburon


class MainWindow(QMainWindow):
    projects = {}
    cc_projects = {}
    ip_projects = {}
    project_path = ''
    mail = ''
    folder_is_selected = False
    folder_project = ''
    cc_project_name_list = []
    cc_project_name_only_user_list = []
    ip_projects_name_list = []
    ip_projects_name_only_user_list = []
    driver = None
    status = ""
    project_is_selected = False
    player = QMediaPlayer()
    audio_output = QAudioOutput()
    itab_macro_name = ""
    sheet_name_dict = ""
    itab_path = ""
    template_name = ""
    base_path = ""
    fin_id_path = ""
    opens_path = ""
    opens_syntax_name = ""
    mode_chrome_driver = "hide"
    opens_syntax_path = None
    start_process_list = []
    end_process_list = []

    opens_needs = False
    template_needs = False
    fin_id_needs = False
    new_base_needs = True

    fin_id_needs_fix = False
    template_needs_fix = False
    opens_needs_fix = False
    new_base_needs_fix = True

    base_done = False
    fin_id_done = False
    template_done = False
    opens_done = False

    def __init__(self):
        self.cb_create_client_bases = None
        self.cb_base_with_label = None
        self.cb_time_in_page = None
        self.cb_strip_var = None
        self.cb_binar = None
        self.cb_multi_label = None
        self.cb_utf8 = None
        self.cb_label = None
        self.links_folder = None
        self.project_number = None
        self.tib_id = None
        self.type_tib_id = None
        status = self.status
        super(MainWindow, self).__init__()
        self.ui_window = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # инициализации окон приложения
        self.init_auth_window()
        self.init_output_window()
        self.init_params_window()
        self.init_params_template_window()
        self.init_permission_error_window()
        self.init_not_found_base_window()
        self.init_not_found_template_window()
        self.init_not_found_opens_window()
        self.init_dict_not_found_window()
        self.init_template_exists_window()
        self.init_info_window()
        self.init_macro_error_window()
        self.init_links_folder_path_window()

        # инициализации имени макроса для выгрузки шаблона и имени листа с данными (dict)
        self.itab_macro_name = self.params_template_form.le_template_macro_name.text()
        self.sheet_name_dict = self.params_template_form.le_template_sheet_name.text()

        # инициализация истансов дополнительных потов
        self.StartProcess_instanse = StartProcess(mainwindow=self, status=status)
        self.DownloadBaseFromTiburon_instanse = DownloadBaseFromTiburon(mainwindow=self, status=status)
        self.GetFinalId_instanse = GetFinalId(mainwindow=self, status=status)
        self.CreateTemplate_instanse = CreateTemplate(mainwindow=self, status=status)
        self.CreateOpens_instanse = CreateOpens(mainwindow=self, status=status)

        self.StartProcess_instanse.start_signal.connect(self.start_process)
        self.StartProcess_instanse.progress_signal.connect(self.progress_upgrade)
        self.StartProcess_instanse.open_output_signal.connect(self.open_output)

        self.DownloadBaseFromTiburon_instanse.progress_signal.connect(self.progress_upgrade)
        self.DownloadBaseFromTiburon_instanse.error_signal.connect(self.error_handler)
        self.DownloadBaseFromTiburon_instanse.end_signal.connect(self.end_process)

        self.GetFinalId_instanse.progress_signal.connect(self.progress_upgrade)
        self.GetFinalId_instanse.error_signal.connect(self.error_handler)
        self.GetFinalId_instanse.end_signal.connect(self.end_process)

        self.CreateTemplate_instanse.progress_signal.connect(self.progress_upgrade)
        self.CreateTemplate_instanse.error_signal.connect(self.error_handler)
        self.CreateTemplate_instanse.end_signal.connect(self.end_process)

        self.CreateOpens_instanse.progress_signal.connect(self.progress_upgrade)
        self.CreateOpens_instanse.error_signal.connect(self.error_handler)
        self.CreateOpens_instanse.end_signal.connect(self.end_process)

        self.progress_upgrade(status)

        # инициализация списка проектов (надо бы поменять название)
        # по умолчанию сначала подгружаются сс проекты
        self.get_project_list()
        for p in self.cc_project_name_list:
            self.ui.listWidget.addItem(p)

        # блокируем кнопку выгрузки
        self.ui.bt_load.setEnabled(False)

        # проверяем указана ли почта для фильтрации списка проекта, если нет блокируем кнопку
        if len(self.auth_form.le_mail.text()) == 0:
            self.ui.cb_my_projects.setEnabled(False)

        # дальше идет связка функций с элементами приложения
        # чекбоксы, указывающие что необходимо выгрузить
        self.ui.cb_dont_load_base.clicked.connect(self.click_cb_dont_load_base)
        self.ui.cb_dont_load_base.clicked.connect(self.enable_load_button)
        self.ui.cb_fin_id.clicked.connect(self.click_cb_fin_id)
        self.ui.cb_fin_id.clicked.connect(self.enable_load_button)
        self.ui.cb_template.clicked.connect(self.click_cb_template)
        self.ui.cb_template.clicked.connect(self.enable_load_button)
        self.ui.cb_opens.clicked.connect(self.click_cb_opens)
        self.ui.cb_opens.clicked.connect(self.enable_load_button)

        # чекбоксы, для фильтрации списка проектов
        self.ui.cb_my_projects.clicked.connect(self.show_only_users_projects)
        self.ui.cb_show_only_ip.clicked.connect(self.show_only_users_projects)

        # список проектов
        self.ui.listWidget.clicked.connect(self.project_select)
        self.ui.listWidget.clicked.connect(self.update_project_folder)
        self.ui.listWidget.clicked.connect(self.enable_load_button)

        # пункты меню
        self.ui.auth_menu.triggered.connect(self.open_auth_form)
        self.ui.params_menu.triggered.connect(self.open_params_form)
        self.ui.params_template.triggered.connect(self.open_params_template_form)
        self.ui.links_folder_path.triggered.connect(self.open_links_folder_path_form)

        # кнопки
        self.ui.bt_load.clicked.connect(self.click_load_button)
        self.ui.bt_open_folder.clicked.connect(self.open_file_dialog)
        self.ui.bt_open_folder.clicked.connect(self.enable_load_button)
        self.auth_form.bt_auth_confirm.clicked.connect(self.confirm_login_and_password)
        self.params_template_form.bt_template_params_confirm.clicked.connect(self.confirm_params_template)
        self.links_folder_path_form.bt_links_folder_path.clicked.connect(self.open_file_dialog_for_links_folder)

        self.dict_not_found_form.bt_repeat_template.clicked.connect(self.click_repeat_template_button)
        self.template_exists_form.bt_repeat_template.clicked.connect(self.click_repeat_template_button)
        self.macro_error_form.bt_repeat_template.clicked.connect(self.click_repeat_template_button)
        self.permission_error_form.bt_repeat_template.clicked.connect(self.click_repeat_template_button)

        self.not_found_template_form.bt_set_path_template.clicked.connect(self.click_bt_set_path_template)
        # self.not_found_opens_form.bt_set_path_opens.clicked.connect(self.click_repeat_opens_button)

        self.not_found_opens_form.bt_set_path_opens.clicked.connect(self.click_bt_set_path_opens)
        self.not_found_base_form.bt_set_base_path.clicked.connect(self.click_bt_set_path_base)

        self.params_form.bt_params_confirm.clicked.connect(self.click_bt_params_confirm)

    @error_checker
    def init_login_password(self):
        if self.auth_form.le_login_tib is not None and self.auth_form.le_password_tib is not None:
            login = self.auth_form.le_login_tib.text()
            password = self.auth_form.le_password_tib.text()
            result_auth = auth_tiburon(self.driver, login, password)

            return result_auth

    @error_checker
    def init_auth_window(self):
        self.auth_window = QMainWindow()
        self.auth_form = Ui_auth_form()
        self.auth_form.setupUi(self.auth_window)

        if os.path.isfile('auth_files/login.txt') and os.path.isfile('auth_files/password.txt') and os.path.isfile(
                'auth_files/key.bin') and os.path.isfile("auth_files/mail.txt"):
            with open('auth_files/login.txt', 'r') as file:
                login = file.read()

            with open('auth_files/password.txt', 'rb') as file:
                encrypted_password = file.read()

            with open('auth_files/mail.txt', 'r') as file:
                mail = file.read()

            with open('auth_files/key.bin', 'rb') as file:
                key = file.read()

            f = Fernet(key)
            password = f.decrypt(encrypted_password).decode()

            self.auth_form.le_login_tib.setText(login)
            self.auth_form.le_password_tib.setText(password)
            self.auth_form.le_mail.setText(mail)

    @error_checker
    def init_links_folder_path_window(self):
        self.links_folder_path_window = QMainWindow()
        self.links_folder_path_form = Ui_links_folder_path_form()
        self.links_folder_path_form.setupUi(self.links_folder_path_window)

        if os.path.exists('settings.ini'):
            config = configparser.ConfigParser()
            config.read("settings.ini")
            if config.has_section("Folders"):
                self.links_folder = config["Folders"].get("links_folder")
                self.links_folder_path_form.bt_links_folder_path.setText("Изменить папку")
                self.links_folder_path_form.bt_links_folder_path.setStyleSheet(
                    "background-color: #478ebe; color: rgb(255, 255, 255);")

    def init_output_window(self):
        self.output_window = QMainWindow()
        self.output_form = Ui_output()
        self.output_form.setupUi(self.output_window)

    def init_params_window(self):
        self.params_window = QMainWindow()
        self.params_form = Ui_params_form()
        self.params_form.setupUi(self.params_window)

        if os.path.exists('settings.ini'):
            config = configparser.ConfigParser()
            config.read("settings.ini")
            if config.has_section("Base"):
                self.cb_label = config["Base"].get("cb_label")
                if self.cb_label == "1":
                    self.params_form.cb_label.setChecked(True)
                else:
                    self.params_form.cb_label.setChecked(False)

                self.cb_utf8 = config["Base"].get("cb_utf8")
                if self.cb_utf8 == "1":
                    self.params_form.cb_utf8.setChecked(True)
                else:
                    self.params_form.cb_utf8.setChecked(False)

                self.cb_multi_label = config["Base"].get("cb_multi_label")
                if self.cb_multi_label == "1":
                    self.params_form.cb_multi_label.setChecked(True)
                else:
                    self.params_form.cb_multi_label.setChecked(False)
                self.cb_binar = config["Base"].get("cb_binar")
                if self.cb_binar == "1":
                    self.params_form.cb_binar.setChecked(True)
                else:
                    self.params_form.cb_binar.setChecked(False)
                self.cb_strip_var = config["Base"].get("cb_strip_var")
                if self.cb_strip_var == "1":
                    self.params_form.cb_strip_var.setChecked(True)
                else:
                    self.params_form.cb_strip_var.setChecked(False)
                self.cb_base_with_label = config["Base"].get("cb_base_with_label")
                if self.cb_base_with_label == "1":
                    self.params_form.cb_base_with_label.setChecked(True)
                else:
                    self.params_form.cb_base_with_label.setChecked(False)
                self.cb_time_in_page = config["Base"].get("cb_time_in_page")
                if self.cb_time_in_page == "1":
                    self.params_form.cb_time_in_page.setChecked(True)
                else:
                    self.params_form.cb_time_in_page.setChecked(False)
                self.cb_create_client_bases = config["Base"].get("cb_create_client_bases")
                if self.cb_create_client_bases == "1":
                    self.params_form.cb_create_client_bases.setChecked(True)
                else:
                    self.params_form.cb_create_client_bases.setChecked(False)

    def init_not_found_base_window(self):
        self.not_found_base_window = QMainWindow()
        self.not_found_base_form = Ui_not_found_base_form()
        self.not_found_base_form.setupUi(self.not_found_base_window)

    def init_permission_error_window(self):
        self.permission_error_window = QMainWindow()
        self.permission_error_form = Ui_permission_error_form()
        self.permission_error_form.setupUi(self.permission_error_window)

    def init_macro_error_window(self):
        self.macro_error_window = QMainWindow()
        self.macro_error_form = Ui_macro_error_form()
        self.macro_error_form.setupUi(self.macro_error_window)

    def init_not_found_template_window(self):
        self.not_found_template_window = QMainWindow()
        self.not_found_template_form = Ui_not_found_template_form()
        self.not_found_template_form.setupUi(self.not_found_template_window)

    def init_not_found_opens_window(self):
        self.not_found_opens_window = QMainWindow()
        self.not_found_opens_form = Ui_not_found_opens_form()
        self.not_found_opens_form.setupUi(self.not_found_opens_window)

    def init_dict_not_found_window(self):
        self.dict_not_found_window = QMainWindow()
        self.dict_not_found_form = Ui_dict_not_found_form()
        self.dict_not_found_form.setupUi(self.dict_not_found_window)

    def init_template_exists_window(self):
        self.template_exists_window = QMainWindow()
        self.template_exists_form = Ui_template_exists_form()
        self.template_exists_form.setupUi(self.template_exists_window)

    def init_info_window(self):
        self.info_window = QMainWindow()
        self.info_form = Ui_info_form()
        self.info_form.setupUi(self.info_window)

    @error_checker
    def init_params_template_window(self):
        self.params_template_window = QMainWindow()
        self.params_template_form = Ui_params_template_form()
        self.params_template_form.setupUi(self.params_template_window)

        if os.path.exists('settings.ini'):
            config = configparser.ConfigParser()
            config.read("settings.ini")
            if config.has_section("Template"):
                self.template_name = config["Template"].get("template_name")
                self.sheet_name_dict = config["Template"].get("sheet_name")
                self.itab_macro_name = config["Template"].get("macro_name")

            if config.has_section("Opens"):
                self.opens_syntax_name = config["Opens"].get("syntax_name")

            self.params_template_form.le_template_name.setText(self.template_name)
            self.params_template_form.le_template_macro_name.setText(self.itab_macro_name)
            self.params_template_form.le_template_sheet_name.setText(self.sheet_name_dict)
            self.params_template_form.le_opens_syntax_name.setText(self.opens_syntax_name)

    def open_auth_form(self):
        self.auth_window.show()

    def open_links_folder_path_form(self):
        # self.links_folder_path_window.setWindowFlag(self.windowFlags() | Qt.WindowStaysOnTopHint)
        # self.links_folder_path_window.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.links_folder_path_window.show()

    def open_params_form(self):
        self.params_window.show()

    def open_params_template_form(self):
        self.params_template_window.show()

    def open_not_found_template_form(self):
        self.not_found_template_window.show()
        self.sound_play(filename="error")

    def open_not_found_base_form(self):
        self.not_found_base_window.show()
        self.sound_play(filename="error")

    def open_permission_error_form(self):
        self.permission_error_window.show()
        self.sound_play(filename="error")

    def open_macro_error_form(self):
        self.macro_error_window.show()
        self.sound_play(filename="error")

    def open_not_found_opens_form(self):
        self.not_found_opens_window.show()
        self.sound_play(filename="error")

    def open_dict_not_found_form(self):
        self.dict_not_found_window.show()
        self.sound_play(filename="error")

    def open_template_exists_form(self):
        self.template_exists_window.show()
        self.sound_play(filename="error")

    def open_info_form(self, text):
        self.info_form.label.setText(text)
        self.info_window.show()
        self.sound_play(filename="error")

    def open_output_form(self, text):
        self.output_window.show()
        self.sound_play(filename="sound")
        self.output_form.tb_output.setText(text)

    @error_checker
    def open_file_dialog(self):
        self.folder_project = str(QFileDialog.getExistingDirectory(self, "Выберите папку для выгрузки базы"))
        if self.folder_project != '':
            self.folder_is_selected = True
            self.ui.bt_open_folder.setText("Изменить папку")
            self.ui.bt_open_folder.setStyleSheet("background-color: #478ebe; color: rgb(255, 255, 255);")
            self.folder_project = self.folder_project.replace("/", "\\")

    @error_checker
    def open_file_dialog_for_links_folder(self):
        self.links_folder = str(QFileDialog.getExistingDirectory(self, "Выберите папку где хранятся ссылки на папки с "
                                                                       "данными"))
        if self.links_folder != '':
            self.links_folder = self.links_folder.replace("/", "\\")
            self.links_folder_path_form.bt_links_folder_path.setText("Изменить папку")
            self.links_folder_path_form.bt_links_folder_path.setStyleSheet("background-color: #478ebe; color: rgb("
                                                                           "255, 255, 255);")

            config = configparser.ConfigParser()
            config.read("settings.ini")
            if config.has_section('Folders'):
                config.set("Folders", "links_folder", self.links_folder)
            else:
                config.add_section('Folders')
                config.set("Folders", "links_folder", self.links_folder)

            with open('settings.ini', 'w') as config_file:
                config.write(config_file)

            self.links_folder_path_window.close()

        else:
            self.ui.bt_open_folder.setText("Папка проекта")
            self.ui.bt_open_folder.setStyleSheet("")
            self.folder_project = None
            self.folder_is_selected = False

            self.ui.bt_load.setEnabled(False)
            self.ui.bt_load.setStyleSheet("")

    def closeEvent(self, event):
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()

    def project_select(self):
        self.project_is_selected = True

    def sound_play(self, filename):
        self.player = QMediaPlayer()
        self.player.setAudioOutput(self.audio_output)
        filename = "sounds/" + filename + ".wav"
        self.player.setSource(QUrl.fromLocalFile(filename))
        self.player.play()

    def get_project_list(self):
        self.mail = self.auth_form.le_mail.text()
        self.cc_project_name_list = []
        self.ip_projects_name_list = []
        self.cc_project_name_only_user_list = []
        self.ip_projects_name_only_user_list = []

        with open("projects_tib_cc.json", encoding='utf-8') as json_file:
            self.cc_projects = json.load(json_file)

        for project_number in self.cc_projects.keys():
            self.cc_project_name_list.append(self.cc_projects[project_number]["name"])

        for project_number in self.cc_projects.keys():
            for emp in self.cc_projects[project_number]["processing"]:
                if emp == self.mail:
                    self.cc_project_name_only_user_list.append(self.cc_projects[project_number]["name"])

        self.cc_project_name_list = list(reversed(self.cc_project_name_list))
        self.cc_project_name_only_user_list = list(reversed(self.cc_project_name_only_user_list))

        with open("projects_tib_ip.json", encoding='utf-8') as json_file:
            self.ip_projects = json.load(json_file)

        for project_number in self.ip_projects.keys():
            self.ip_projects_name_list.append(self.ip_projects[project_number]["name"])

        for project_number in self.ip_projects.keys():
            for emp in self.ip_projects[project_number]["processing"]:
                if emp == self.mail:
                    self.ip_projects_name_only_user_list.append(self.ip_projects[project_number]["name"])

        self.ip_projects_name_list = list(reversed(self.ip_projects_name_list))
        self.ip_projects_name_only_user_list = list(reversed(self.ip_projects_name_only_user_list))

        self.projects = self.cc_projects | self.ip_projects

    def progress_upgrade(self, status):
        self.ui.lb_progress.setText(status)

    def error_handler(self, status):
        if status == "Не найден файл айтаба":
            self.open_not_found_template_form()

        if status == "Не найден синтакисис для открытых":
            self.open_not_found_opens_form()

        if status == "Не найдена база":
            self.open_not_found_base_form()

        # нужно сделать одно информационное окно для всех ошибок и просто менять там текст
        if status == "Ошибка во время загрузки базы":
            self.open_info_form(text="Ошибка во время загрузки базы")

        if status == "Ошибка во время конвертации базы":
            self.open_info_form(text="Ошибка во время конвертации базы")

        if status == "Не найдена вкладка dict":
            self.open_dict_not_found_form()

        if status == "Ошибка доступа к файлу":
            self.open_permission_error_form()

        # или как вариант если файл с таким названием есть в папке давать другое имя
        if status == "Айтаб уже существует":
            self.open_template_exists_form()

        if status == "Ошибка макроса":
            self.open_macro_error_form()

    def open_output(self):
        text = ""
        if self.base_done:
            text = "База:\n" + self.base_path + "\n"
        if self.fin_id_done:
            text = text + "Финальные айди:\n" + self.fin_id_path + "\n"
        if self.template_done:
            text = text + "Шаблон:\n" + self.itab_path + "\n"
        if self.opens_done:
            text = text + "Открытые:\n" + self.opens_path + "\n"

        self.clear_var()
        self.open_output_form(text)

    def clear_var(self):
        if self.driver is not None:
            self.driver = None

        self.base_done = False
        self.fin_id_done = False
        self.template_done = False
        self.opens_done = False

        self.base_path = ""
        self.fin_id_path = ""
        self.itab_path = ""
        self.opens_path = ""

        self.start_process_list = []
        self.end_process_list = []

        self.project_number = None
        self.tib_id = None
        self.type_tib_id = None

    def clear_var_short(self):
        if self.driver is not None:
            self.driver = None

        self.base_done = False
        self.fin_id_done = False
        self.template_done = False
        self.opens_done = False

        self.base_path = ""
        self.fin_id_path = ""
        self.itab_path = ""
        self.opens_path = ""

        self.start_process_list = []
        self.end_process_list = []

    def start_process(self, status):
        if status == 1:
            self.DownloadBaseFromTiburon_instanse.start()

        if status == 2:
            self.GetFinalId_instanse.start()

        if status == 3:
            self.CreateTemplate_instanse.start()

        if status == 4:
            self.CreateOpens_instanse.start()

    def end_process(self):
        self.StartProcess_instanse.start()

    @error_checker
    def click_load_button(self):
        self.new_base_needs_fix = self.new_base_needs
        self.fin_id_needs_fix = self.fin_id_needs
        self.template_needs_fix = self.template_needs
        self.opens_needs_fix = self.opens_needs

        p_name = self.ui.listWidget.currentItem().text()
        for p in self.projects.keys():
            if self.projects[p]['name'] == p_name:
                project_id = self.projects[p]['id']
                self.type_tib_id = self.projects[project_id]['type_tib_id']
                self.tib_id = self.projects[project_id]['tib_id']
                self.project_number = self.projects[project_id]['id']

        self.clear_var_short()

        if self.new_base_needs:
            self.driver = init_chrome_driver(mode="show")
            if self.driver is None:
                with open("logs/logs.txt", "a+") as file:
                    traceback_info = traceback.format_exc()
                    file.write("\n" + datetime.now().strftime('%Y-%m-%d %H:%M'))
                    file.write("\n" + traceback_info)
                    file.write("\n" + "init_chrome_driver вернул None")
                    file.write("\n" + "------------------------------")

            result_init_login_password = self.init_login_password()

            if result_init_login_password == "Неверный логин или пароль":
                self.open_info_form(text="Неверный логин или пароль")
            if result_init_login_password == "CAPTСHA":
                self.mode_chrome_driver = "show"
                self.open_info_form(text="Появилась CAPTСHA при авторизации, необходимо снова запуститить "
                                         "выгрузку и пройти ее вручную")

            # там 0 не возвращается
            # elif result_init_login_password == 0:
            #     self.open_info_form(text="Ошибка во время авторизации")
            elif result_init_login_password == 1:
                self.mode_chrome_driver = "hide"
                self.StartProcess_instanse.start()
                self.ui.bt_load.setEnabled(False)
            else:
                with open("logs/logs.txt", "a+") as file:
                    traceback_info = traceback.format_exc()
                    file.write("\n" + datetime.now().strftime('%Y-%m-%d %H:%M'))
                    file.write("\n" + traceback_info)
                    file.write("\n" + f"result_init_login_password={result_init_login_password}")
                    file.write("\n" + "Запуск выгрузки базы не запущен")
                    file.write("\n" + "------------------------------")
        else:
            self.StartProcess_instanse.start()
            self.ui.bt_load.setEnabled(False)

    def click_cb_opens(self):
        if self.ui.cb_opens.isChecked():
            self.opens_needs = True
        else:
            self.opens_needs = False

    def click_cb_template(self):
        if self.ui.cb_template.isChecked():
            self.template_needs = True
        else:
            self.template_needs = False

    def click_cb_fin_id(self):
        if self.ui.cb_fin_id.isChecked():
            self.fin_id_needs = True
        else:
            self.fin_id_needs = False

    def click_cb_dont_load_base(self):
        if self.ui.cb_dont_load_base.isChecked():
            self.new_base_needs = False
        else:
            self.new_base_needs = True

    def enable_load_button(self):
        if self.folder_is_selected and self.project_is_selected:
            if self.new_base_needs or self.fin_id_needs or self.template_needs or self.opens_needs:
                self.ui.bt_load.setEnabled(True)
                self.ui.bt_load.setStyleSheet("background-color: #478ebe; color: rgb(255, 255, 255);")
            else:
                self.ui.bt_load.setEnabled(False)
                self.ui.bt_load.setStyleSheet("")
        else:
            self.ui.bt_load.setEnabled(False)
            self.ui.bt_load.setStyleSheet("")

    def show_only_users_projects(self):
        if not self.ui.cb_my_projects.isChecked() and not self.ui.cb_show_only_ip.isChecked():
            self.ui.listWidget.clear()
            for p in self.cc_project_name_list:
                self.ui.listWidget.addItem(p)

        if not self.ui.cb_my_projects.isChecked() and self.ui.cb_show_only_ip.isChecked():
            self.ui.listWidget.clear()
            for p in self.ip_projects_name_list:
                self.ui.listWidget.addItem(p)

        if self.ui.cb_my_projects.isChecked() and self.ui.cb_show_only_ip.isChecked():
            self.ui.listWidget.clear()
            for p in self.ip_projects_name_only_user_list:
                self.ui.listWidget.addItem(p)

        if self.ui.cb_my_projects.isChecked() and not self.ui.cb_show_only_ip.isChecked():
            self.ui.listWidget.clear()
            for p in self.cc_project_name_only_user_list:
                self.ui.listWidget.addItem(p)

    def show_only_ip_projects(self):
        if self.ui.cb_show_only_ip.isChecked():
            self.ui.listWidget.clear()
            for p in self.ip_projects_name_only_user_list:
                self.ui.listWidget.addItem(p)
        else:
            self.ui.listWidget.clear()
            for p in self.ip_projects_name_list:
                self.ui.listWidget.addItem(p)

    @error_checker
    def confirm_login_and_password(self):
        login = self.auth_form.le_login_tib.text()
        password = self.auth_form.le_password_tib.text()
        self.mail = self.auth_form.le_mail.text()
        mail = self.auth_form.le_mail.text()

        if len(login) > 0 and len(password) > 0 and len(mail) > 0:
            with open("auth_files/login.txt", "w") as file:
                file.write(login)

            keyring.set_password("tib_app", username=login, password=password)
            encryption_key = Fernet.generate_key()

            with open("auth_files/key.bin", "wb") as file:
                file.write(encryption_key)

            f = Fernet(encryption_key)

            encrypted_password = f.encrypt(password.encode())
            with open("auth_files/password.txt", "wb") as file:
                file.write(encrypted_password)

            with open("auth_files/mail.txt", "w") as file:
                file.write(mail)

            self.ui.cb_my_projects.setEnabled(True)
        else:
            if os.path.exists("auth_files/login.txt"):
                os.remove("auth_files/login.txt")
            if os.path.exists("auth_files/password.txt"):
                os.remove("auth_files/password.txt")
            if os.path.exists("auth_files/key.bin"):
                os.remove("auth_files/key.bin")
            if os.path.exists("auth_files/mail.txt"):
                os.remove("auth_files/mail.txt")

        self.get_project_list()

        # if self.driver is not None:
        #     auth_tiburon(self.driver, login, password)
        # else:
        #     self.driver = init_chrome_driver(mode="not_headless")
        #     auth_tiburon(self.driver, login, password)
        self.auth_window.close()

    @error_checker
    def confirm_params_template(self):
        template_name = self.params_template_form.le_template_name.text()
        sheet_name = self.params_template_form.le_template_sheet_name.text()
        macro_name = self.params_template_form.le_template_macro_name.text()
        opens_syntax_name = self.params_template_form.le_opens_syntax_name.text()

        config = configparser.ConfigParser()
        config.read("settings.ini")

        if len(template_name) > 0:
            config.set("Template", "template_name", template_name)

        if len(sheet_name) > 0:
            config.set("Template", "sheet_name", sheet_name)

        if len(macro_name) > 0:
            config.set("Template", "macro_name", macro_name)

        if len(opens_syntax_name) > 0:
            config.set("Opens", "syntax_name", opens_syntax_name)

        with open('settings.ini', 'w') as config_file:
            config.write(config_file)

        self.params_template_window.close()

    def click_repeat_template_button(self):
        self.CreateTemplate_instanse.start()

        self.dict_not_found_window.close()
        self.template_exists_window.close()
        self.macro_error_window.close()
        self.permission_error_window.close()

    def click_repeat_opens_button(self):
        self.CreateOpens_instanse.start()
        self.not_found_opens_window.close()

    @error_checker
    def click_bt_set_path_opens(self):
        self.opens_path = None
        self.opens_path = QFileDialog.getOpenFileName(self, "Выберите пустой синтаксис для открытых")[0]
        if self.opens_path is not None:
            self.opens_path = self.opens_path.replace("/", "\\")
            self.not_found_opens_window.close()
            self.CreateOpens_instanse.start()

    @error_checker
    def click_bt_set_path_template(self):
        self.itab_path = None
        self.itab_path = QFileDialog.getOpenFileName(self, "Выберите пустой шаблон для данного проекта")[0]
        if self.itab_path is not None:
            self.itab_path = self.itab_path.replace("/", "\\")
            self.not_found_template_window.close()
            self.CreateTemplate_instanse.start()

    @error_checker
    def click_bt_set_path_base(self):
        self.base_path = QFileDialog.getOpenFileName(self, "Выберите базу для выгрузки финальных айди")[0]
        if self.base_path is not None:
            self.base_path = self.base_path.replace("/", "\\")
            self.not_found_template_window.close()
            self.GetFinalId_instanse.start()

    @error_checker
    def click_bt_params_confirm(self):
        if os.path.exists('settings.ini'):
            config = configparser.ConfigParser()
            config.read("settings.ini")

            if not config.has_section("Base"):
                config.add_section("Base")

            if self.params_form.cb_label.isChecked():
                config.set("Base", "cb_label", "1")
            else:
                config.set("Base", "cb_label", "0")
            if self.params_form.cb_utf8.isChecked():
                config.set("Base", "cb_utf8", "1")
            else:
                config.set("Base", "cb_utf8", "0")
            if self.params_form.cb_multi_label.isChecked():
                config.set("Base", "cb_multi_label", "1")
            else:
                config.set("Base", "cb_multi_label", "0")
            if self.params_form.cb_binar.isChecked():
                config.set("Base", "cb_binar", "1")
            else:
                config.set("Base", "cb_binar", "0")
            if self.params_form.cb_strip_var.isChecked():
                config.set("Base", "cb_strip_var", "1")
            else:
                config.set("Base", "cb_strip_var", "0")
            if self.params_form.cb_base_with_label.isChecked():
                config.set("Base", "cb_base_with_label", "1")
            else:
                config.set("Base", "cb_base_with_label", "0")
            if self.params_form.cb_time_in_page.isChecked():
                config.set("Base", "cb_time_in_page", "1")
            else:
                config.set("Base", "cb_time_in_page", "0")
            if self.params_form.cb_create_client_bases.isChecked():
                config.set("Base", "cb_create_client_bases", "1")
            else:
                config.set("Base", "cb_create_client_bases", "0")

            with open('settings.ini', 'w') as config_file:
                config.write(config_file)

            self.params_window.close()

    @error_checker
    def update_project_folder(self, *args):
        if self.links_folder is not None and self.links_folder != "":
            links_names_list = os.listdir(self.links_folder)
            self.folder_is_selected = False
            current_project = self.ui.listWidget.currentItem().text()

            for link_name in links_names_list:
                if current_project in link_name.replace("_", " "):
                    # это связано с тем, что тибурон заменяет в названии _ на пробел, при чем если будет несколько __
                    # рядом, всеравно заменит на один пробел (спарсить название из инпута не получается)
                    link_path = get_shortcut_target_path(os.path.join(self.links_folder, link_name))
                    if "data" in link_path and os.path.exists(link_path):
                        self.folder_is_selected = True
                        self.folder_project = link_path
                        self.ui.bt_open_folder.setText("Изменить папку")
                        self.ui.bt_open_folder.setStyleSheet(
                            "background-color: #478ebe; color: rgb(255, 255, 255);")
                        break
            if not self.folder_is_selected:
                self.ui.bt_open_folder.setText("Папка проекта")
                self.ui.bt_open_folder.setStyleSheet("")
                self.folder_project = None
                self.folder_is_selected = False

        if self.links_folder is None or self.links_folder == "":
            self.ui.bt_open_folder.setText("Папка проекта")
            self.ui.bt_open_folder.setStyleSheet("")
            self.folder_project = None
            self.folder_is_selected = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
