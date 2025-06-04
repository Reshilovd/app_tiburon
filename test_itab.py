


def get_itab(project_path, project_number):
    itab_path = get_path_itab_file(project_path)

    if itab_path is None:
        return 0

    syntax_sps_file = open(f"{project_path}\\itab_export.sps", "w")
    syntax_sps = f"""new file.
    set unicode = on.
    get file = "{project_path}\\{project_number}.sav".
    DISPLAY DICTIONARY.
    OUTPUT EXPORT
      /CONTENTS  EXPORT=VISIBLE  LAYERS=PRINTSETTING  MODELVIEWS=PRINTSETTING
      /XLSM  DOCUMENTFILE='{project_path}\\export.xlsm'
         OPERATION=CREATEFILE
         LOCATION=LASTCOLUMN  NOTESCAPTIONS=YES."""

    syntax_sps_file.write(syntax_sps)
    syntax_sps_file.close()

    itab_spj_file = open(f"{project_path}\\itab_task.spj", "w")
    itab_syntax_spj = (f'<?xml version="1.0" encoding="UTF-8"?><job codepageSyntaxFiles="false" print="true" '
                       f'syntaxErrorHandling="continue" syntaxFormat="interactive" unicode="true" '
                       f'xmlns="http://www.ibm.com/software/analytics/spss/xml/production" '
                       f'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
                       f'xsi:schemaLocation="http://www.ibm.com/software/analytics/spss/xml/production '
                       f'http://www.ibm.com/software/analytics/spss/xml/production/production-1.4.xsd"><locale '
                       f'charset="UTF-8" country="RU" language="ru"/><output outputFormat="viewer" '
                       f'outputPath="test.spv"/><syntax syntaxPath="{project_path}\\itab_export.sps"/></job>')
    itab_spj_file.write(itab_syntax_spj)
    itab_spj_file.close()

    itab_run_bat = open(f"{project_path}\\itab_run.bat", "w")
    itab_run_bat.write(
        f'"C:\\Program Files\\IBM\\SPSS\\Statistics\\24\\stats.exe" "{project_path}\\itab_task.spj" -production silent')
    itab_run_bat.close()

    subprocess.run(f'{project_path}\\itab_run.bat', shell=True)

    itab_wb = load_workbook(f"{project_path}\\export.xlsm", keep_vba=True)
    itab_ws = itab_wb.active

    for index, cell in enumerate(itab_ws['A']):
        if cell.value == "Variable Information":
            itab_ws.delete_rows(1, index)
            itab_wb.save(f"{project_path}\\new_export.xlsm")
            itab_wb.close()
            break
    itab_file_wb = load_workbook(itab_path, keep_vba=True)
    itab_file_ws = itab_file_wb.active

    dict_sheet = itab_file_wb["dict"]
    dict_sheet.delete_cols(0, 100)

    for index_row, row in enumerate(itab_ws.iter_rows()):
        for index_column, cell in enumerate(row):
            dict_sheet.cell(row=index_row + 1, column=index_column + 1, value=cell.value)

    itab_file_wb.save(itab_path)
    itab_file_wb.close()

    vba = wx.Book(itab_path)

    if "dict" not in vba.sheet_names:
        os.remove(f"{project_path}\\itab_run.bat")
        os.remove(f"{project_path}\\itab_task.spj")
        os.remove(f"{project_path}\\export.xlsm")
        os.remove(f"{project_path}\\new_export.xlsm")
        os.remove(f"{project_path}\\itab_export.sps")
        vba.save()
        vba.close()
        return 1

    vba_macro = vba.macro("testLoadDic")
    vba_macro()
    vba.save()
    vba.close()

    new_itab_path = "\\".join(itab_path.split("\\")[0:-1]) + f"/itab_v28_{project_number}.xlsm"
    os.rename(itab_path, new_itab_path)

    os.remove(f"{project_path}\\itab_run.bat")
    os.remove(f"{project_path}\\itab_task.spj")
    os.remove(f"{project_path}\\export.xlsm")
    os.remove(f"{project_path}\\new_export.xlsm")
    os.remove(f"{project_path}\\itab_export.sps")

    return new_itab_path