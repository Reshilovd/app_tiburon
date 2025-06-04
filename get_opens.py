import os
import re
import subprocess


def get_opens(project_path, project_number, opens_syntax_name):
    opens_path = project_path.split("Programming")[0] + "DP/Opens/To_coding"
    if not os.path.exists(opens_path + f"\\{opens_syntax_name}"):
        return 1
        # file_list = os.listdir(opens_path)
        # for file in file_list:
        #     if "opens" and ".sps" in file:
        #         open_syntax_file_list.append(file)

    find_text = r"'...\4. DATA (coding, de, dp)\DP\Opens\To_coding\openq1_to_coding_21-000000-01.xlsx'"
    find_text2 = r'"...\4. DATA (coding, de, dp)\DP\Opens\To_coding\openq1_to_coding_21-000000-01.xlsm"'

    find_text_strip = find_text.strip("'")
    find_text2_strip = find_text2.strip('"')

    pattern = r"\d\d-\d\d\d\d\d\d-\d\d"
    result1 = re.sub(pattern, project_number, find_text_strip)
    result2 = re.sub(pattern, project_number, find_text2_strip)

    result1 = result1.replace(r"...\4. DATA (coding, de, dp)\DP\Opens\To_coding", opens_path)
    result2 = result2.replace(r"...\4. DATA (coding, de, dp)\DP\Opens\To_coding", opens_path)

    if "'" in project_path:
        result1 = '"' + result1 + '"'
        result2 = '"' + result2 + '"'
    else:
        result1 = "'" + result1 + "'"
        result2 = "'" + result2 + "'"

    opens_syntax = open(f"{opens_path}/{opens_syntax_name}", "r").read()
    opens_syntax = opens_syntax.replace('get file="...".', f'get file="{project_path}\\{project_number}.sav".')
    opens_syntax = opens_syntax.replace("/keep ID", "/keep InterviewID")
    opens_syntax = opens_syntax.replace(find_text, result1)
    opens_syntax = opens_syntax.replace(find_text2, result2)

    new_opens_syntax = open(f"{opens_path}\\{opens_syntax_name}", "w")
    new_opens_syntax.write(opens_syntax)
    new_opens_syntax.close()

    # unicode = "false" charset="UTF-8" в остальных случаях открытые выгружаются некорректно,
    # либо с битой вкладкой статистики, либо с проблемы с кодировкой
    spj_file = open(f"{project_path}\\opens_task.spj", "w")
    syntax_spj = (f'<?xml version="1.0" encoding="UTF-8"?><job codepageSyntaxFiles="false" print="true" '
                  f'syntaxErrorHandling="continue" syntaxFormat="interactive" unicode="false" '
                  f'xmlns="http://www.ibm.com/software/analytics/spss/xml/production" '
                  f'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
                  f'xsi:schemaLocation="http://www.ibm.com/software/analytics/spss/xml/production '
                  f'http://www.ibm.com/software/analytics/spss/xml/production/production-1.4.xsd"><locale '
                  f'charset="UTF-8" country="RU" language="ru"/><output outputFormat="viewer" '
                  f'outputPath="test.spv"/><syntax syntaxPath="{opens_path}\\{opens_syntax_name}"/></job>')
    spj_file.write(syntax_spj)
    spj_file.close()

    opens_run_bat = open(f"{project_path}\\opens_run.bat", "w")
    opens_run_bat.write(
        f'"C:\\Program Files\\IBM\\SPSS\\Statistics\\24\\stats.exe" "{project_path}\\opens_task.spj" -production silent')
    opens_run_bat.close()

    subprocess.run(f'{project_path}\\opens_run.bat', shell=True)

    opens_file_path = result2.strip("'").strip('"')

    return opens_file_path


project_number = "2303484101"
opens_syntax_name = "opens_v2.2_22-000000-01.sps"
project_path = r"C:\Users\Denis.Reshilov\Desktop\app_tiburon\test\testopens\Programming\data\live"

out = get_opens(project_path, project_number, opens_syntax_name)
print(out)
