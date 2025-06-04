import os
from datetime import datetime
from PyQt6.QtCore import QThread, QMutex
from PyQt6 import QtCore
from secondary_func import move_and_unzip, get_itab, get_final_id, get_opens, conversion_base_in_sav
from selenium_func import download_base_from_tiburon


class StartProcess(QThread):
    start_signal = QtCore.pyqtSignal(int)
    progress_signal = QtCore.pyqtSignal(str)
    open_output_signal = QtCore.pyqtSignal(int)

    def __init__(self, mainwindow, status, parent=None):
        super().__init__(parent)
        self.mainwindow = mainwindow
        self.status = status

    def run(self):

        # 1 вариант, когда база нужна:
        if self.mainwindow.new_base_needs_fix:
            # если базы еще нет
            if not self.mainwindow.base_done:
                start_signal = 1
                if start_signal not in self.mainwindow.start_process_list:
                    self.start_signal.emit(start_signal)
                    self.mainwindow.start_process_list.append(start_signal)
            # если база уже есть
            else:
                # айди нужны и еще не готовы?
                if self.mainwindow.fin_id_needs_fix and not self.mainwindow.fin_id_done:
                    start_signal = 2
                    if start_signal not in self.mainwindow.start_process_list:
                        self.start_signal.emit(start_signal)
                        self.mainwindow.start_process_list.append(start_signal)
                if self.mainwindow.template_needs_fix and not self.mainwindow.template_done:
                    start_signal = 3
                    if start_signal not in self.mainwindow.start_process_list:
                        self.start_signal.emit(start_signal)
                        self.mainwindow.start_process_list.append(start_signal)

                # нужно дождаться пока выгрузится шаблон, только потом открытые выгружаем
                if self.mainwindow.template_needs_fix and self.mainwindow.template_done:
                    if self.mainwindow.opens_needs_fix and not self.mainwindow.opens_done:
                        start_signal = 4
                        if start_signal not in self.mainwindow.start_process_list:
                            self.start_signal.emit(start_signal)
                            self.mainwindow.start_process_list.append(start_signal)
                if not self.mainwindow.template_needs_fix:
                    if self.mainwindow.opens_needs_fix and not self.mainwindow.opens_done:
                        start_signal = 4
                        if start_signal not in self.mainwindow.start_process_list:
                            self.start_signal.emit(start_signal)
                            self.mainwindow.start_process_list.append(start_signal)

        # 2 вариант, когда база не нужна:
        if not self.mainwindow.new_base_needs_fix:

            if self.mainwindow.fin_id_needs_fix and not self.mainwindow.fin_id_done:
                start_signal = 2
                if start_signal not in self.mainwindow.start_process_list:
                    self.start_signal.emit(start_signal)
                    self.mainwindow.start_process_list.append(start_signal)
            if self.mainwindow.template_needs_fix and not self.mainwindow.template_done:
                start_signal = 3
                print('3')
                if start_signal not in self.mainwindow.start_process_list:
                    self.start_signal.emit(start_signal)
                    self.mainwindow.start_process_list.append(start_signal)

            # нужно дождаться пока выгрузится шаблон, только потом открытые выгружаем
            if self.mainwindow.template_needs_fix and self.mainwindow.template_done:
                if self.mainwindow.opens_needs_fix and not self.mainwindow.opens_done:
                    start_signal = 4
                    if start_signal not in self.mainwindow.start_process_list:
                        self.start_signal.emit(start_signal)
                        self.mainwindow.start_process_list.append(start_signal)
            if not self.mainwindow.template_needs_fix:
                if self.mainwindow.opens_needs_fix and not self.mainwindow.opens_done:
                    start_signal = 4
                    if start_signal not in self.mainwindow.start_process_list:
                        self.start_signal.emit(start_signal)
                        self.mainwindow.start_process_list.append(start_signal)

        len_start = len(self.mainwindow.start_process_list)
        len_end = len(self.mainwindow.end_process_list)

        if len_start > 0 and len_start == len_end:
            self.open_output_signal.emit(1)
            self.progress_signal.emit("")


class DownloadBaseFromTiburon(QThread):
    progress_signal = QtCore.pyqtSignal(str)
    error_signal = QtCore.pyqtSignal(str)
    end_signal = QtCore.pyqtSignal(int)

    def __init__(self, mainwindow, status, parent=None):
        super().__init__(parent)
        self.mainwindow = mainwindow
        self.status = status
        self._mutex = QMutex()

    def run(self):
        print('1')
        self.progress_signal.emit("Идет загрузка базы...")
        print('2')
        url = f"https://client2.survstat.ru/#/item/{self.mainwindow.type_tib_id}/{self.mainwindow.tib_id}/report"
        print(url)
        date_now = datetime.now()
        params_list = [self.mainwindow.cb_label,
                       self.mainwindow.cb_utf8,
                       self.mainwindow.cb_multi_label,
                       self.mainwindow.cb_binar,
                       self.mainwindow.cb_strip_var,
                       self.mainwindow.cb_base_with_label,
                       self.mainwindow.cb_time_in_page,
                       self.mainwindow.cb_create_client_bases]
        print(params_list)
        result_download = download_base_from_tiburon(driver=self.mainwindow.driver, url=url, params_list=params_list)

        print(result_download)

        if result_download == 0:
            self.error_signal.emit("Ошибка во время загрузки базы")
        else:
            project_path = self.mainwindow.folder_project
            user_name = self.mainwindow.mail.split("@")[0]
            project_number = move_and_unzip(self.mainwindow.folder_project, date_now, user_name)
            self.mainwindow.project_number = project_number
            self.progress_signal.emit("Конвертируем...")
            result_conversion = conversion_base_in_sav(project_number, project_path)
            if result_conversion == 1:
                self.mainwindow.base_path = project_path + f"\\{project_number}.sav"
                self.mainwindow.base_done = True
                self.end_signal.emit(1)
                self.mainwindow.end_process_list.append(1)
            if result_conversion == 0:
                self.error_signal.emit("Ошибка во время конвертации базы")


class GetFinalId(QThread):
    progress_signal = QtCore.pyqtSignal(str)
    error_signal = QtCore.pyqtSignal(str)
    end_signal = QtCore.pyqtSignal(int)

    def __init__(self, mainwindow, status, parent=None):
        super().__init__(parent)
        self.mainwindow = mainwindow
        self.status = status

    def run(self):
        self.progress_signal.emit("Выгружаем финальные айди...")
        result = get_final_id(project_path=self.mainwindow.folder_project,
                              project_number=self.mainwindow.project_number,
                              panel=self.mainwindow.ui.le_choise_panel_var.text())

        if result == 1:
            self.error_signal.emit("Не найдена база")
            self.progress_signal.emit("Не найдена база")
        else:
            self.mainwindow.fin_id_path = self.mainwindow.folder_project + "\\ID.xlsx"
            self.mainwindow.fin_id_done = True
            self.end_signal.emit(2)
            self.mainwindow.end_process_list.append(2)


class CreateTemplate(QThread):
    progress_signal = QtCore.pyqtSignal(str)
    error_signal = QtCore.pyqtSignal(str)
    end_signal = QtCore.pyqtSignal(int)

    def __init__(self, mainwindow, status, parent=None):
        super().__init__(parent)
        self.mainwindow = mainwindow
        self.status = status

    def run(self):
        self.progress_signal.emit("Выгружаем шаблон...")
        itab_path = get_itab(project_path=self.mainwindow.folder_project,
                             project_number=self.mainwindow.project_number,
                             itab_macro_name=self.mainwindow.itab_macro_name,
                             sheet_name_dict=self.mainwindow.sheet_name_dict)

        self.mainwindow.itab_path = itab_path

        if itab_path == 0:
            self.progress_signal.emit("Не найден файл айтаба")
            self.error_signal.emit("Не найден файл айтаба")
        elif itab_path == 1:
            self.progress_signal.emit("Не найдена вкладка dict")
            self.error_signal.emit("Не найдена вкладка dict")
        elif itab_path == 2:
            self.progress_signal.emit("Ошибка доступа к файлу")
            self.error_signal.emit("Ошибка доступа к файлу")
        elif itab_path == 3:
            self.progress_signal.emit("Айтаб уже существует")
            self.error_signal.emit("Айтаб уже существует")
        elif itab_path == 4:
            self.progress_signal.emit("Ошибка макроса")
            self.error_signal.emit("Ошибка макроса")
        elif itab_path == 5:
            self.progress_signal.emit("Не найдена база")
            self.error_signal.emit("Не найдена база")
        elif itab_path:
            self.mainwindow.template_done = True
            self.end_signal.emit(3)
            self.mainwindow.end_process_list.append(3)


class CreateOpens(QThread):
    progress_signal = QtCore.pyqtSignal(str)
    error_signal = QtCore.pyqtSignal(str)
    end_signal = QtCore.pyqtSignal(int)

    def __init__(self, mainwindow, status, parent=None):
        super().__init__(parent)
        self.mainwindow = mainwindow
        self.status = status

    def run(self):
        project_path = self.mainwindow.folder_project
        project_number = self.mainwindow.project_number
        opens_syntax_name = self.mainwindow.opens_syntax_name

        if self.mainwindow.opens_syntax_path is not None:
            opens_syntax_path = self.mainwindow.opens_syntax_path
        else:
            opens_syntax_path = None

        self.progress_signal.emit("Выгружаем открытые...")
        opens_path = get_opens(project_path=project_path,
                               project_number=project_number,
                               opens_syntax_name=opens_syntax_name,
                               opens_syntax_path=opens_syntax_path)

        self.mainwindow.opens_path = opens_path

        if opens_path == 1:
            self.progress_signal.emit("Не найден синтакисис для открытых")
            self.error_signal.emit("Не найден синтакисис для открытых")
        else:
            self.mainwindow.opens_done = True
            self.end_signal.emit(4)
            self.mainwindow.end_process_list.append(4)
