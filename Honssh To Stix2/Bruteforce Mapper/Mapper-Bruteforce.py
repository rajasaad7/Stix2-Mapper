import os
import shutil
from os import listdir
from os.path import isfile, join
import time
from subprocess import call


def executeSomething():
    print("Mapping is Started..!!")

    call(["python", "Stix2-bruteforce.py"])

    mypath = str("X:\Cyber Security\Mapper")    #  path to folder where logs are stored
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    totalfiles = len(onlyfiles)

#    print("All files in the folder are : "+str(onlyfiles))

    good = []
    for x in range(0, totalfiles):
        allfilespath = mypath + "/" + onlyfiles[x]
        good.append(allfilespath)


        for filename in os.listdir(mypath):
            filename_without_ext = os.path.splitext(filename)[0]
            extension = os.path.splitext(filename)[1]
            new_file_name = filename_without_ext + "_Mapped"
            changed = new_file_name + extension
            os.rename(os.path.join(mypath, filename), os.path.join(mypath, changed))

            shutil.move(os.path.join(mypath, changed), "X:\Cyber Security\Mapped")  # path where you want to move logs after convertion
    print("System is going for 1 Hour sec sleep..!!")
    time.sleep(3600)


while True:
    executeSomething()
