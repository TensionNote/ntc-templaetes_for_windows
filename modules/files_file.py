import os
def files_file(path):
    files = os.listdir(path)
    files_file = [f for f in files if os.path.isfile(os.path.join(path, f))]
    return files_file