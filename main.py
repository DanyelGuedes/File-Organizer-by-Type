import os

# Path where docs will be organazed
path = fr"C:\Users\LENOVO\Documents\- Documentos - Separar"

# New folders for doc types
jpg = fr"{path}\JPG"
png = fr"{path}\PNG"
pdf = fr"{path}\PDF"
excel = fr"{path}\EXCEL"
powerpoint = fr"{path}\POWERPOINT"
word = fr"{path}\WORD"

# Move or criate the folder
def MoveFile(file_extension):
    try:
        os.rename(fr"{path}\{name}", fr"{file_extension}\{name}")
    except:
        os.makedirs(file_extension)
        os.rename(fr"{path}\{name}", fr"{file_extension}\{name}")


with os.scandir(path) as files:
    for file in files:
        name = file.name
        if name.endswith(".jpg"):
            MoveFile(jpg)

        if name.endswith(".png"):
            MoveFile(png)

        if name.endswith(".xlsx"):
            MoveFile(excel)
        if name.endswith(".xlsm"):
            MoveFile(excel)
        if name.endswith(".csv"):
            MoveFile(excel)
        if name.endswith(".xls"):
            MoveFile(excel)

        if name.endswith(".pdf"):
            MoveFile(pdf)

        if name.endswith(".doc"):
            MoveFile(word)
        if name.endswith(".docx"):
            MoveFile(word)
        if name.endswith(".txt"):
            MoveFile(word)


        if name.endswith(".pptx"):
            MoveFile(powerpoint)
