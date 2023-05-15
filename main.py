import os

# Path where docs will be organized
path = fr"C:\Users\LENOVO\Documents"

# New folders for doc types
jpg = fr"{path}\JPG"
png = fr"{path}\PNG"
pdf = fr"{path}\PDF"
excel = fr"{path}\EXCEL"
powerpoint = fr"{path}\POWERPOINT"
word = fr"{path}\WORD"

# Move or criate the folder
def move_file(file_extension):
    try:
        os.rename(fr"{path}\{name}", fr"{file_extension}\{name}")
    except:
        os.makedirs(file_extension)
        os.rename(fr"{path}\{name}", fr"{file_extension}\{name}")


with os.scandir(path) as files:
    for file in files:
        name = file.name
        if name.endswith(".jpg"):
            move_file(jpg)

        if name.endswith(".png"):
            move_file(png)

        if name.endswith(".xlsx"):
            move_file(excel)
        if name.endswith(".xlsm"):
            move_file(excel)
        if name.endswith(".csv"):
            move_file(excel)
        if name.endswith(".xls"):
            move_file(excel)

        if name.endswith(".pdf"):
            move_file(pdf)

        if name.endswith(".doc"):
            move_file(word)
        if name.endswith(".docx"):
            move_file(word)
        if name.endswith(".txt"):
            move_file(word)


        if name.endswith(".pptx"):
            move_file(powerpoint)
