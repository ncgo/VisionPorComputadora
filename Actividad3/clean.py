import os
from random import sample

def deleteExtra(folder, className):
    path = 'data/' + folder + '/' + className
    files = os.listdir(path)
    os.chdir(path)
    print(os.getcwd())
    if folder == 'train':
        size = 140
    elif folder == 'test':
        size = 40
    elif folder == 'validation':
        size = 20
    for file in sample(files,len(files) - size):
        os.remove(file)

def checkCleanUp():
    folders = ['train', 'test', 'validation']
    clases = ['airplane', 'bicycle', 'bus', 'car', 'motorcycle']

    for className in clases:
        print("className")
        for folder in folders:
            path = path = 'data/' + folder + '/' + className
            files = os.listdir(path)
            print(folder + ": " + len(files))

if __name__ == "__main__":
    deleteExtra('test', 'car')
    checkCleanUp()