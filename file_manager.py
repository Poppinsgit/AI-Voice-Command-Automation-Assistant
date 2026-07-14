import os


def file_command(command):

    if "create folder" in command:
        folder = command.replace("create folder", "").strip()
        os.makedirs(folder, exist_ok=True)
        return f"Folder {folder} created"


    elif "create file" in command:
        file = command.replace("create file", "").strip()
        with open(file + ".txt", "w") as f:
            f.write("")
        return f"File {file} created"


    elif "delete file" in command:
        file = command.replace("delete file", "").strip()

        if os.path.exists(file):
            os.remove(file)
            return "File deleted"

        else:
            return "File not found"


    elif "open folder" in command:
        folder = command.replace("open folder", "").strip()

        if os.path.exists(folder):
            os.system(f"open {folder}")
            return "Opening folder"

        return "Folder not found"


    return None