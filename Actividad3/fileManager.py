"""
Escrito por Jesús Omar Cuenca Espino 
A01378844@itesm.mx

26/03/2021
"""

import os
from shutil import rmtree

def createFolder(dirName : str):
    try:
        os.mkdir(dirName)
    except FileExistsError:
        print(f"Folder {dirName} already Exists")
    except FileNotFoundError:
        os.makedirs(dirName)

def deleteFolder(dirName : str):
    try:
        os.rmdir(dirName)
    except FileNotFoundError:
        print(f"Folder doesn't exist")
    except Exception as err:
        rmtree(dirName)

def renameToHexAllFiles():
    """
    This function will rename every ".png" file in the CWD
    into a hex-like name such as "motorcycles_ffff.png" if this program is run on .../motorcycles/
    according to its position in the listDir.
    This is meant to be used on a Dataset to rename it fast
    """
    dirName = os.path.abspath(".").split("/")[-1]
    fileNamesTemp = os.listdir(".")
    fileNames = []
    for f in fileNamesTemp:
        if(".png" in f.lower()):
            fileNames.append(f)
    for f in range(len(fileNames)):
        newFileName = dirName+f"_{str(hex(f))[2:]}.png"
        os.rename(fileNames[f],newFileName)
    print(f"{len(fileNames)} where renamed")

def originalTestingFunctionality():
    import time
    TEST_DIR = SINGLE_DIR = "ExampleDir"
    createFolder(TEST_DIR)
    print("Folder Created")
    time.sleep(1)
    deleteFolder(TEST_DIR)
    print("Folder Deleted")

    TEST_DIR = "ExampleDir/InnerDir"
    createFolder(TEST_DIR)
    print("Inner Folder Created")
    time.sleep(1)
    deleteFolder(TEST_DIR)
    print("Inner Folder Deleted")
    deleteFolder(SINGLE_DIR)
    print("Upper Folder Deleted")

if __name__ == "__main__":
    originalTestingFunctionality()
    # This function must be run directly inside the dir with all the .png files to be renamed
    #### renameToHexAllFiles()
