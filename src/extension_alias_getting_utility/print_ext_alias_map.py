import os
import json

with open("lang_alias.txt", "r") as f:
    lines = f.readlines()

name_alias_map = {}
for line in lines:
    temp = line.split('\t')
    if '\n' in temp:
            temp.remove('\n')
    for i in range(len(temp)):
        temp[i] = temp[i].replace('\n', '')
    commaSplit = temp[1].split(',')
    for j in range(len(commaSplit)):
        commaSplit[j] = commaSplit[j].replace(' ', '')
    name_alias_map.update({temp[0]: min(commaSplit, key=len)})

with open("lang_ext.json") as jf:
   name_ext_map = json.load(jf)

print("COMMON_EXTS = {")
for lang in name_ext_map:
    try:
        for ext in lang["extensions"]:
            print(f'    "{ext[1:]}"' + f' : "{name_alias_map[lang["name"]]}",')
    except KeyError:
        pass
print('}')
    