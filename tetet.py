import json

with open("\\\\10.165.134.71\\Qst\\dp726\\reshilov\\projects_tib_ip.json", encoding='utf-8') as json_file:
    cc_projects = json.load(json_file)

print(cc_projects)
