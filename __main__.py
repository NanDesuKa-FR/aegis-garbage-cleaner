import glob

if __name__ == "__main__":
    for file in glob.glob("*.ass"):
        f_read = open(file, "r")
        content_file = f_read.read()
        f_read.close()
        if content_file.find("[Aegisub Project Garbage]") != -1:
            aegis_garbage = (content_file.split("[Aegisub Project Garbage]")[1]).split("[V4+ Styles]")[0]
            new_content = (content_file.replace(aegis_garbage, "")).replace("[Aegisub Project Garbage]", "")
            file_update = open(file, 'w')
            file_update.write(new_content)
            file_update.close()
        else:
            print(file + " n'a pas de Aegis Garbage")
