import zipfile
from datetime import datetime
import os
import glob
#
# with open("logs/logs.txt", "a+") as file:
#     file.write("\n" + datetime.now().strftime('%Y-%m-%d %H:%M'))
#     file.write("\n" + "error")
#     file.write("\n" + "------------------------------")

# mail = 'Denis.Reshilov@ipsos.com'
# user_name = mail.split("@")[0]
# print(user_name)
#
# file_name = os.listdir(r'\\10.165.134.71\Qst\dp726\reshilov\3\Programming\data\live')
# if (len(file_name))
# project_number = file_name[0].replace(".csv", "")
# print(project_number)

date_now = datetime.now()
user_name = "Denis.Reshilov"

# list_of_files = glob.glob(
#     f"C:\\Users\\{user_name}\\Downloads\\*.zip")
# latest_file = max(list_of_files, key=os.path.getctime)

# stat = os.stat(latest_file)
# ctime = stat.st_ctime
# date_create_base = datetime.fromtimestamp(ctime)

project_path = r"C:\Users\Denis.Reshilov\Desktop\test\3\Programming\data\live"

list_of_files = glob.glob(f"C:\\Users\\{user_name}\\Downloads\\*.zip")
latest_file = max(list_of_files, key=os.path.getctime)


print(latest_file)
with zipfile.ZipFile(latest_file, "r") as zf:
    for file in zf.namelist():
        if ".csv" in file:
            print(type(file))
            project_number = file.replace(".csv", "")
            print(project_number)


# if latest_file is not None:
#     with zipfile.ZipFile(latest_file, 'r') as base_zip:
#         base_zip.extractall(project_path)



