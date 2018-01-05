#!/usr/bin/python
import random
import os

def createFooFiles(num, path):
    """
    This method is used to create the files with a random string from
    a list in each file for testing.
    """
    file_contents = ['blah', 'stuff', 'foofighters', 'foobar']
    all_files = []
    for i in range(num):
        foo_file = path + '/' + str(i) + '.txt'
        all_files.append(foo_file)

        content_from_list = random.choice(file_contents)
        with open(foo_file, 'w') as file:
            file.write(content_from_list)



def getFileList(path):
    """
    Returns a list of files in a path. Filenames contain full path
    """
    if os.path.exists(path):
        dirlist = []
        for file in os.listdir(path):
            dirlist.append(path + '/' + file)
        return dirlist

    else:
        print("That path does not exist")



def searchForAndReplace(search_str, replacement_str, path):
    """
    This method takes a string to search for in a directory, replaces it with a
    specified string, in a specified path
    """
    list_of_files = getFileList(path)
    for file in list_of_files:
        with open(file, "r") as fin:
            for line in fin:
                if search_str in line:
                    with open(file, "w") as fout:
                        fout.write(line.replace(search_str, replacement_str))


#Run to create files
#createFooFiles(50,'/tmp')
searchForAndReplace('foobar', 'fubar', '/tmp')

