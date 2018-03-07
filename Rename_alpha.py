import.os
def rename_file():
    file_list=os.listdir(r"")
    x=os.getcwd()
    print x
    os.chdir(r"")
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))
rename_file()
