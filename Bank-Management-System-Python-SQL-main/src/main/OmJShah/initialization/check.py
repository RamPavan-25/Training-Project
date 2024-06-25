import os
file_path = os.path.join("Bank-Management-System-Python-SQL-main", "src", "main", "OmJShah", "files", "firsttime.txt")
def check():
    try:
        with open(file_path, "r") as a:
            if a.read().strip()=="True":
                return True
            else:
                return False
    except FileNotFoundError:
        with open(file_path, "w") as a:
            a.write("True")
            return True