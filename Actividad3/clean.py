import os
import sys
from random import sample

def deleteExtra(folder, className):
    path = 'data/' + folder + '/' + className
    files = os.listdir(path)
    os.chdir(path)
    if folder == 'train':
        size = 140
    elif folder == 'test':
        size = 40
    elif folder == 'validation':
        size = 20
    for file in sample(files,len(files) - size):
        os.remove(file)
    
    print(folder + ": " + str(len(files)))
    os.chdir('../../..')

def checkCleanUp():
    folders = ['train', 'test', 'validation']
    clases = ['airplane', 'bicycle', 'bus', 'car', 'motorcycle']
    for className in clases:
        print("className: " + className)
        for folder in folders:
            deleteExtra(folder, className)

if __name__ == "__main__":
    checkCleanUp()