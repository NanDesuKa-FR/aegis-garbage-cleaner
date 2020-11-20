from pathlib import Path

if __name__ == "__main__":
    for p in  Path('.').glob('./**/*'):
        name_file = str(p.name)[-4:]
        if p.is_file() and name_file.find(".ass") != -1:
            f_read = open(p, "r", encoding='utf8', errors='ignore')
            content_file = f_read.read()
            f_read.close()
            if content_file.find("[Aegisub Project Garbage]") != -1:
                print("[CLEAR] " + str(p.name))
                aegis_garbage = (content_file.split("[Aegisub Project Garbage]")[1]).split("[V4+ Styles]")[0]
                new_content = (content_file.replace(aegis_garbage, "")).replace("", "")
                file_update = open(p, 'w', encoding='utf8', errors='ignore')
                file_update.write(new_content)
                file_update.close()
            else:
                print(str(p.name) + " n'a pas de Aegis Garbage")