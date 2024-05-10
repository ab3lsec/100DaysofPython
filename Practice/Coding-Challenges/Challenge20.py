import os

def countFiles(path):
    count = 0
    folders = os.listdir(path)

    for folder in folders:
        newpath = os.path.join(path, folder)
        
        if os.path.isfile(newpath):
            count += 1

        elif os.path.isdir(newpath):
            count += countFiles(newpath)

    return count


print(countFiles("/home/kali"))