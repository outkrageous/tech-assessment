#!/usr/bin/python

def createFiles():
    """
    Creates a 100 files named 000.pp through 099.pp with different class names
    iterating in the same way the filenames do. sample_class.txt is used for as
    a template for the class as it's written with a string iteratively replaced
    in each file.
    """
    for i in range(100):
        filename = str(i).zfill(3) + ".pp"
        str_in_file = 'myfile' + str(i).zfill(3)

        with open("sample_class.txt", "rt") as fin:
            with open(filename, "wt") as fout:
                for line in fin:
                    fout.write(line.replace('myfile000', str_in_file))


createFiles()
